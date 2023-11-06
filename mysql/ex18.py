#alter the existing table:
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
mycursor.execute('ALTER TABLE employees ADD COLUMN company VARCHAR(20)')
