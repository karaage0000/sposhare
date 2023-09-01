import os

#MySQLでのデータベース
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@localhost/our_users'


# シークレットキーの値として10バイトの文字列をランダムに生成
SECRET_KEY = os.urandom(10)

# 画像のアップロード先のフォルダーを登録
#from pathlib import Path
# basedirにapps、imagesを連結してPathオブジェクトを生成し、
# str()で文字列に変換
#UPLOAD_FOLDER = str(Path(basedir, 'apps', 'images'))
