import os
from flask import Flask,render_template, url_for, redirect, flash,request, jsonify
import firebase_admin
from firebase_admin import credentials,auth

app = Flask(__name__)
cred = credentials.Certificate("apps/sposhare-64506-firebase-adminsdk-jucj1-d05bc5db1d.json")
firebase_admin.initialize_app(cred)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://b77d1569d085c8:4a1a8a85@us-cdbr-east-06.cleardb.net/heroku_ba4c1cfdb1ee059' #?reconnect=true
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:pass@localhost/our_users'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://phqt7452addr9x6f:svfeeo43etzu20i2@z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/dt0s92wjtnoovwf5'
#db_uri = 'mysql://phqt7452addr9x6f:svfeeo43etzu20i2@z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/dt0s92wjtnoovwf5'
# ユーザーを作成
def create_user(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        return user
    except auth.AuthError as e:
        # エラーハンドリング
        print(f"Error creating user: {e}")
        return None


# ユーザーを作成
def create_user(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        return user
    except auth.AuthError as e:
        # エラーハンドリング
        print(f"Error creating user: {e}")
        return None

# ユーザーの認証
def authenticate_user(email, password):
    try:
        user = auth.get_user_by_email(email)
        return user
    except auth.AuthError as e:
        # 認証エラーハンドリング
        print(f"Error authenticating user: {e}")
        return None
    
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # ユーザーを作成
    user = create_user(email, password)

    if user:
        return jsonify({'message': 'ユーザーの登録が完了しました。'}), 200
    else:
        return jsonify({'message': 'ユーザーの登録が失敗しました。'}), 400

#------------------------------------------------------------------#


"""from apps.authapp.views import authapp
app.register_blueprint(authapp, url_prefix='/auth')

from apps.pictapp.views import pictapp
app.register_blueprint(pictapp, url_prefix='/picture')"""

if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)



