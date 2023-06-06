import mysql.connector

dataBase = mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="coolproject123",
    auth_plugin="mysql_native_password",
)

# prepare cursor object
cursorObject = dataBase.cursor()

# Make database
cursorObject.execute("CREATE DATABASE studentsdb")

print("Done!")
