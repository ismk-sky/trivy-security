import pyodbc

instance = "<接続先のサーバー名>"
user = "<ユーザー>"
password = "<パスワード>"
db = "<データベース名>"

#接続文字列の組み立て
conn_str = "DRIVER={SQL Server};SERVER=" + instance + \
     ";uid=" + user + \
     ";pwd=" + password + \
     ";DATABASE=" + db

#データベースへ接続
conn = pyodbc.connect(conn_str)

name="\" OR \"\"=\"\""
pass="1234"
sql = 'SELECT * FROM Users WHERE Name ="' + name + '" AND Pass ="' + pass + '"'

cursor = conn.cursor()
cursor.execute(sql)
rows = cursor.fetchall()
cursor.close()

