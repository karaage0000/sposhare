from datetime import datetime
from apps.app import db

class UserPicture(db.Model):
    __tablename__ = "pictures"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    username = db.Column(db.String(30),index=True) 
    title = db.Column(db.String(50))
    contents = db.Column(db.Text)
    url = db.Column(db.Text)
    create_at = db.Column(db.DateTime,default=datetime.now) 
    
