#drop schema.
import  mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sneha',
    database='mamatha'
)
mycursor=mydb.cursor()
mycursor.execute('DROP SCHEMA mamatha')
#drop only if exists
mydb.commit()
print('no table found')