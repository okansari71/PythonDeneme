import mysql.connector
mydb = mysql.connector.connect(
    host = "192.168.1.15",
    user = "okans",
    password = "Po19482025"
    database = "node-app"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

