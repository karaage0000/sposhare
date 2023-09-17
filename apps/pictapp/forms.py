from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length
from flask_wtf.file import FileField, FileRequired, FileAllowed
#from spotipy import Spotify
#from spotipy.oauth2 import SpotifyClientCredentials
import os
#from dotenv import load_dotenv


#load_dotenv()


#spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
#spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

#sp = Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret))


class UploadImageForm(FlaskForm):
    title = StringField(
        "",
        validators=[DataRequired(message="入力が必要です。"),length(max=200, message="200文字以内で入力してください。"),]
    )
    message = TextAreaField(
        "",render_kw={'style': 'height: 200px;' 'width:183px;' ' resize: none;'},
        validators=[DataRequired(message="入力が必要です。"),])
    url = StringField(
        "",render_kw={'style':'width:183px'},
        validators=[DataRequired(message="プレイリストのURLを記入してください。"),])
    submit = SubmitField(
        '投稿する'
        )





