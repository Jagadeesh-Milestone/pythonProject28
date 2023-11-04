#selecting columns
#insert into table
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
mycursor.execute('SELECT name FROM students')
x=mycursor.fetchall()
for i in x:
    print(i)