from flask import Blueprint, request,render_template, url_for, redirect, session
from flask_login import login_required,logout_user
from sqlalchemy import select 
from flask import request 
from flask_paginate import Pagination, get_page_parameter
from flask import send_from_directory # send_from_directory

pictapp = Blueprint(
    'pictapp',
    __name__,
    template_folder='templates_pict',
    static_folder='static_pict',
    )

@pictapp.route('/', methods=['GET', 'POST'])
def index():
    stmt = select(
        modelpict.UserPicture).order_by(modelpict.UserPicture.create_at.desc())
    entries = db.session.execute(stmt).scalars().all()
    page = request.args.get(
        get_page_parameter(), type=int, default=1)
    res = entries[(page - 1)*6: page*6]
    pagination = Pagination(page=page,total=len(entries), per_page=6)
    return render_template('top.html', user_picts=res, pagination=pagination)

@pictapp.route('/logout')
def logout():
    session['logged_in'] = False
    logout_user()
    return redirect(url_for('authapp.index'))


import uuid 
from pathlib import Path 
from flask_login import current_user 
from flask import current_app 

from apps.app import db 
from apps.pictapp import forms 
from apps.pictapp import models as modelpict

@pictapp.route('/upload', methods=['GET', 'POST'])
def upload():
    form = forms.UploadImageForm()
    if form.validate_on_submit():
        upload_data = modelpict.UserPicture(
            user_id=current_user.id,
            username = current_user.username,
            title=form.title.data,
            contents=form.message.data,
            url=form.url.data,
        )
        
        db.session.add(upload_data)
        db.session.commit()
        return redirect(url_for('pictapp.index'))
    
    return render_template('upload.html', form=form)

@pictapp.route('/detail/<int:id>')
def show_detail(id):
    detail = db.session.get(modelpict.UserPicture, id)
    playlist_url = None
    if request.method == 'POST':
        playlist_url = request.detail.url
        if playlist_url:
            playlist_id = playlist_url.split('/')[-1]
            playlist_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"
    return render_template('detail.html', detail=detail)

@pictapp.route('/user-list/<int:user_id>')
def user_list(user_id):
    stmt = select(
        modelpict.UserPicture).filter_by(user_id=user_id).order_by(
            modelpict.UserPicture.create_at.desc())
    userlist = db.session.execute(stmt).scalars().all()
    return render_template('userlist.html', userlist=userlist)


@pictapp.route('/mypage/<int:user_id>')
def mypage(user_id):
    stmt = select(
        modelpict.UserPicture).filter_by(user_id=user_id).order_by(
            modelpict.UserPicture.create_at.desc())
    mylist = db.session.execute(stmt).scalars().all()
    return render_template('mypage.html', mylist=mylist)


@pictapp.route('/delete/<int:id>')
def delete(id):
    entry = db.session.get(modelpict.UserPicture, id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('pictapp.index'))


@pictapp.route('/playlist', methods=['GET', 'POST'])
def show_embedded_playlist():
    form = forms.UploadImageForm()
    playlist_url = None
    if form.validate_on_submit():
        url = form.url.data
        playlist_id = url.split('/')[-1]
        playlist_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"
    
    return render_template('index.html', form=form, playlist_url=playlist_url)