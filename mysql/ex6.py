#insert into table
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
sql='INSERT INTO students (name,address) VALUES(%s,%s)'
val=('hari','bangalore')
mycursor.execute(sql,val)
mydb.commit()
#commit is used when you make any changes to the table.
