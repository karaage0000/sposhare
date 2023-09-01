import os

# モジュールの親ディレクトリのフルパスを取得
#basedir = os.path.dirname(os.path.dirname(__file__))
# 親ディレクトリのpict.sqliteをデータベースに設定
#SQLite3でのURI
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
#                              basedir, 'app.sqlite')
#MySQLでのデータベース
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@localhost/our_users'

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://kara:9Lakkdplz2z@@@localhost/database_name'

# シークレットキーの値として10バイトの文字列をランダムに生成
SECRET_KEY = os.urandom(10)

# 画像のアップロード先のフォルダーを登録
#from pathlib import Path
# basedirにapps、imagesを連結してPathオブジェクトを生成し、
# str()で文字列に変換
#UPLOAD_FOLDER = str(Path(basedir, 'apps', 'images'))
