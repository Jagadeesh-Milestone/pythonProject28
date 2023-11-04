#check for the databases
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha'
)
mycursor=mydb.cursor()
mycursor.execute('SHOW DATABASES')
for i in mycursor:
    print(i)