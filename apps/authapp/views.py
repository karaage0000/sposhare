from flask import Blueprint

""" 識別名をauthappにしてBlueprintオブジェクトを生成

    テンプレートフォルダーは'templates_auth'
    staticフォルダーは'static_auth'
"""
authapp = Blueprint(
    'authapp',
    __name__,
    template_folder='templates_auth',
    static_folder='static_auth',
    )

"""authappのログインページのルーティングとビューの定義

    ユーザー認証を行う
"""
from flask import render_template, url_for, redirect, flash
from flask_login import login_user
from sqlalchemy import select
from apps.authapp import forms 
from apps import models 
from apps.app import db 

@authapp.route('/', methods=['GET', 'POST'])
def index():
    
    form = forms.LoginForm()
    
    if form.validate_on_submit():

        stmt = (
            select(models.User).filter_by(email=form.email.data).limit(1))
        
        user = db.session.execute(stmt).scalars().first()

        if user is not None and user.verify_password(form.password.data):

            login_user(user)

            return redirect(url_for('pictapp.index'))

        flash("認証に失敗しました")

    return render_template('login.html', form=form)

