import mysql.connector

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





