#primary key.
#it is used to define a unique name for all the records in a table.
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
mycursor.execute('CREATE TABLE userdetails(id INT AUTO_INCREMENT PRIMARY KEY ,name VARCHAR(20), address VARCHAR(30))')
