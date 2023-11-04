#select records from table using wildcard characters.
#insert multiple records into table
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM userdetails WHERE address LIKE '%re%'")
x=mycursor.fetchall()
for i in x:
    print(i)