#import mysql.connector

#mydb = mysql.connector.connect(
#    host = "127.0.0.1",
#    user="root",
#    passwd="pass",
#    )

#my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE our_users")

#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)

from apps.app import create_app, db

app = create_app()

if __name__ == '__main__':
    # アプリケーションコンテキストを設定してデータベースを初期化
    with app.app_context():
        db.create_all()

    # アプリケーションを実行
    app.run()





