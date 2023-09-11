from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship
# データベースの接続情報
db_uri = 'mysql://phqt7452addr9x6f:svfeeo43etzu20i2@z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/dt0s92wjtnoovwf5'

# SQLAlchemy エンジンを作成
engine = create_engine(db_uri)
# セッションを作成
Session = sessionmaker(bind=engine)
session = Session()
# SQLAlchemy モデルのベースクラスを作成
Base = declarative_base()


# モデルの定義
class UserPicture(Base):
    __tablename__ = "pictures"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    username = Column(String(30), index=True)
    title = Column(String(50))
    contents = Column(Text)
    url = Column(Text)
    create_at = Column(DateTime, default=datetime.now)

# クエリ実行例
user_id = 1  # 例: ユーザーID を指定
user_pictures = session.query(UserPicture).filter_by(user_id=user_id).order_by(desc(UserPicture.create_at)).all()

# クエリ結果の処理
for picture in user_pictures:
    print(f"ID: {picture.id}, Title: {picture.title}, Created At: {picture.create_at}")
# セッションをクローズ
session.close()


