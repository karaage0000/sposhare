from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, DateTime,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

"""Base = declarative_base()
Session = sessionmaker(bind=create_engine('mysql://phqt7452addr9x6f:svfeeo43etzu20i2@z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/dt0s92wjtnoovwf5')) 

class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30), index=True, nullable=False)
    email = Column(String(40), index=True, unique=True, nullable=False)
    password_hash = Column(String(500), nullable=False)
    create_at = Column(DateTime, default=datetime.now)

    
    @property
    def password(self):
        raise AttributeError('password is not readable')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def is_duplicate_email(self):
        session = Session()
        user =  session.query(User).filter_by(email=self.email).first() is not None
        session.close()
        return user is not None
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)"""

"""
from apps.app import login_manager
@login_manager.user_loader
def load_user(user_id):
    from apps.app import Session  # セッションが定義されているモジュールをインポートする
    session = Session()
    try:
        user = session.query(User).get(user_id)
        return user
    except Exception as e:
        print(f"Error loading user: {e}")
        return None
    finally:
        session.close()
"""










