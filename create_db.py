"""import mysql.connector

mydb = mysql.connector.connect(
    host = "us-cdbr-east-06.cleardb.net",
    user="b77d1569d085c8",
    passwd="4a1a8a85",
    )

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE our_users")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
"""
import mysql.connector

mydb = mysql.connector.connect(
    host = "z3iruaadbwo0iyfp.cbetxkdyhwsb.us-east-1.rds.amazonaws.com",
    user="phqt7452addr9x6f",
    passwd="svfeeo43etzu20i2",
    database = 'dt0s92wjtnoovwf5'
    )

# カーソルを作成
my_cursor = mydb.cursor()

# テーブル一覧を取得
my_cursor.execute("SHOW TABLES")

# 結果を読み込む
tables = my_cursor.fetchall()

# テーブル名を表示
for table in tables:
    print(table[0])




my_cursor = mydb.cursor()


#my_cursor.execute("CREATE DATABASE users")

my_cursor.execute("SHOW DATABASES")
# テーブル一覧を取得
my_cursor.execute("SHOW TABLES")
for db in my_cursor:
    print(db)
    
# SELECTクエリの実行
my_cursor.execute("SELECT * FROM users")


for row in results:
    print(row)
# カーソルを閉じる
my_cursor.close()





