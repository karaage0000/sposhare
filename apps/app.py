import os
from flask import Flask,render_template, url_for, redirect, flash
from flask_login import LoginManager
from flask_migrate import Migrate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from apps import forms 
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b77d1569d085c8:4a1a8a85@us-cdbr-east-06.cleardb.net/heroku_ba4c1cfdb1ee059' #?reconnect=true
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:pass@localhost/our_users'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://phqt7452addr9x6f:svfeeo43etzu20i2@z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/dt0s92wjtnoovwf5'
db_uri = 'mysql://phqt7452addr9x6f:svfeeo43etzu20i2@z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/dt0s92wjtnoovwf5'

try:
    # SQLAlchemyエンジンを作成し、データベースに接続を試行
    engine = create_engine(db_uri)
    connection = engine.connect()

    # 接続が成功した場合はメッセージを表示
    print("データベースに正常に接続しました。")

    # ここで必要なデータベース操作を実行できます。

    # 接続を閉じる
    connection.close()

except Exception as e:
    print("データベース接続エラー:", str(e))

engine = create_engine(db_uri)
app.config['SECRET_KEY'] = os.urandom(10)
Session = sessionmaker(bind=engine)
#db.init_app(app)
migrate = Migrate(app, engine)

login_manager = LoginManager()
login_manager.login_view = 'index'
login_manager.login_message = ''
login_manager.init_app(app)


from apps.models import User
@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.SignupForm()
    if form.validate_on_submit():
        session = Session()
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        if user.is_duplicate_email():
            flash("登録済みのメールアドレスです")
            return redirect(url_for('index'))
        session.add(user)
        session.commit()
        session.close()
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

from apps.authapp.views import authapp
app.register_blueprint(authapp, url_prefix='/auth')

from apps.pictapp.views import pictapp
app.register_blueprint(pictapp, url_prefix='/picture')



