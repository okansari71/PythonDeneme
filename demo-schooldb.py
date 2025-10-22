import mysql.connector

connection = mysql.connector.connect(

    host = "192.168.1.15",
    user = "okans",
    password = "Po19482025"
    database = "scholl"
)

mycursor = connection.cursor()
