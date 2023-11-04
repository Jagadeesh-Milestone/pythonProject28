#create a new database:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE DATABASE mamatha')
print('one database created successfully')