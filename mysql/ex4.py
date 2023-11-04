#create a table:
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE employees(name VARCHAR(20),address VARCHAR(30))')
print('one table created successfully')