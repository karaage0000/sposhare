from flask import Blueprint
from flask import render_template, url_for, redirect, flash
from flask_login import login_user
from sqlalchemy import select
from apps.authapp import forms 
from apps import models 
from apps.app import migrate, Session

authapp = Blueprint(
    'authapp',
    __name__,
    template_folder='templates_auth',
    static_folder='static_auth',
    )


@authapp.route('/', methods=['GET', 'POST'])
def index():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            session = Session()
            stmt = select(models.User).filter_by(email=form.email.data).limit(1)
            user = session.execute(stmt).scalars().first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user)
                session.close()
                return redirect(url_for('pictapp.index'))
            else:
                flash("メールアドレスまたはパスワードが正しくありません")
        except Exception as e:
            flash("ログイン時にエラーが発生しました")
            print(f"Error during login: {e}")
        finally:
            session.close()
    return render_template('login.html', form=form)

