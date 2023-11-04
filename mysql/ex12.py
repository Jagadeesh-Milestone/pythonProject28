#select records from table
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM userdetails WHERE name='jagadeesh'")
x=mycursor.fetchall()
for i in x:
    print(i)