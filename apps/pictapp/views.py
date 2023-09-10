from flask import Blueprint, request,render_template, url_for, redirect,flash
from flask_login import login_required,logout_user
from sqlalchemy import select,desc
from flask import request
from apps.app import Session
from apps.pictapp.models import UserPicture

pictapp = Blueprint(
    'pictapp',
    __name__,
    template_folder='templates_pict',
    static_folder='static_pict',
    )

@pictapp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    session = Session()
    page = request.args.get('page', type=int, default=1)
    per_page = 6
    user_picts = (
        session.query(UserPicture)
        .filter_by(user_id=current_user.id)
        .order_by(desc(UserPicture.create_at))
        .limit(per_page)
        .offset((page - 1) * per_page)
        .all()
    )
    session.close()
    return render_template('top.html', user_picts=user_picts, pagination=None)  # pagination=None を追加


@pictapp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('authapp.index'))


import uuid 
from pathlib import Path 
from flask_login import current_user 
from flask import current_app 
from apps.app import migrate
from apps.pictapp import forms 
from apps.pictapp import models as modelpict

@pictapp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = forms.UploadImageForm()
    if form.validate_on_submit():
        try:
            session = Session()
            upload_data = modelpict.UserPicture(
                user_id=current_user.id,
                username = current_user.username,
                title=form.title.data,
                contents=form.message.data,
                url=form.url.data,
            )
        except Exception as e:
            flash('正しく送信されませんでした。')
            print(f"Error during login: {e}")
        finally:
            session.add(upload_data)
            session.commit()
            session.close()
        return redirect(url_for('pictapp.index'))
    return render_template('upload.html', form=form)

@pictapp.route('/detail/<int:id>')
@login_required
def show_detail(id):
    session = Session()
    detail = session.get(modelpict.UserPicture, id)
    playlist_url = None
    if request.method == 'POST':
        playlist_url = request.detail.url
        if playlist_url:
            playlist_id = playlist_url.split('/')[-1]
            playlist_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"
    return render_template('detail.html', detail=detail)

@pictapp.route('/user-list/<int:user_id>')
@login_required
def user_list(user_id):
    session = Session()
    stmt = select(
        modelpict.UserPicture).filter_by(user_id=user_id).order_by(
            modelpict.UserPicture.create_at.desc())
    userlist = session.execute(stmt).scalars().all()
    return render_template('userlist.html', userlist=userlist)


@pictapp.route('/mypage/<int:user_id>')
@login_required
def mypage(user_id):
    session = Session()
    stmt = select(
        modelpict.UserPicture).filter_by(user_id=user_id).order_by(
            modelpict.UserPicture.create_at.desc())
    mylist = session.execute(stmt).scalars().all()
    session.close()
    return render_template('mypage.html', mylist=mylist)


@pictapp.route('/delete/<int:id>')
@login_required
def delete(id):
    session = Session()
    entry = session.get(modelpict.UserPicture, id)
    session.delete(entry)
    session.commit()
    session.close()
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