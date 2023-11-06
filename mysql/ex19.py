#delete records:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
mycursor.execute('DELETE FROM userdetails WHERE id="3"')
mydb.commit()
print(mycursor.rowcount,'records got deleted')