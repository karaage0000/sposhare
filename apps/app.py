import os
from flask import Flask,render_template, url_for, redirect, flash
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from apps import models 
from apps import forms 
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b77d1569d085c8:4a1a8a85@us-cdbr-east-06.cleardb.net/heroku_ba4c1cfdb1ee059' #?reconnect=true
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:pass@localhost/our_users'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://phqt7452addr9x6f:svfeeo43etzu20i2@z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/dt0s92wjtnoovwf5'
app.config['SECRET_KEY'] = os.urandom(10)
db = SQLAlchemy(app)
#db.init_app(app)
Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'index'
login_manager.login_message = ''
login_manager.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    form = forms.SignupForm()
    
    if form.validate_on_submit():
        
        user = models.User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        
        if user.is_duplicate_email():
            flash("登録済みのメールアドレスです")
            return redirect(url_for('index'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form)
from apps.authapp.views import authapp
app.register_blueprint(authapp, url_prefix='/auth')

from apps.pictapp.views import pictapp
app.register_blueprint(pictapp, url_prefix='/picture')
