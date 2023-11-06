#limit the result:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
#mycursor.execute('SELECT * FROM userdetails LIMIT 6')
mycursor.execute('SELECT * FROM userdetails LIMIT 4 OFFSET 5')
result=mycursor.fetchall()
for i in result:
    print(i)

