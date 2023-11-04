#insert multiple records into table
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
sql='INSERT INTO students (name,address) VALUES(%s,%s)'
val=[('hari','bangalore'),('suresh','hyderabad'),
     ('manoj','chennai'),('naresh kumar','hyderabad'),
     ('manoj kumar','chennai')]
mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcount,'records got inserted into a table')