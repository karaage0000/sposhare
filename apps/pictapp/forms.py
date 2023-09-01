from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# SpotifyのクライアントIDとクライアントシークレットを取得する
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Spotipyクライアントのセットアップ
sp = Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret))


class UploadImageForm(FlaskForm):
    """
    Attributes:
        title: タイトル
        message: メッセージ
        url: spotifyのurl
        submit: 送信ボタン
    """
    title = StringField(
        "タイトル",
        validators=[DataRequired(message="入力が必要です。"),
                    length(max=200, message="200文字以内で入力してください。"),]
    )

    message = TextAreaField(
        "メッセージ",
        validators=[DataRequired(message="入力が必要です。"),])
    
    url = StringField(
        "URL",
        validators=[DataRequired(message="プレイリストのURLを記入してください。"),])
    
    
    # フォームのsubmitボタン
    submit = SubmitField('投稿する')





