# ベースイメージを指定
# ベースイメージを指定
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /app

# アプリケーションの依存関係をインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# アプリケーションコードをコピー
COPY apps app.py

# アプリケーションを実行
CMD ["python", "app.py"]
RUN apt-get update && apt-get install -y pkg-config
RUN apt-get update && apt-get install -y default-libmysqlclient-dev