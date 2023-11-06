#update records:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
mycursor.execute('UPDATE userdetails SET address="mumbai" WHERE address="chennai"')
mydb.commit()
print(mycursor.rowcount,'records got updated')