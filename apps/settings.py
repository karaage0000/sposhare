import os

#MySQLでのデータベース
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pass@localhost/our_users'

SECRET_KEY = os.urandom(10)


#from pathlib import Path
#UPLOAD_FOLDER = str(Path(basedir, 'apps', 'images'))
