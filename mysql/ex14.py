#sort the records.
import  mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM userdetails ORDER BY address')
result=mycursor.fetchall()
for i in result:
    print(i)