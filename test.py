
import mysql.connector
cnx = mysql.connector.connect(user='root', password='Radin*tara92', host='127.0.0.1', database='shop')
cursor = cnx.cursor()

cursor.execute('insert into customers values(8, \'aa\', \'aaa\', \'aaaa\')')
cnx.commit()

id = 11
name = 'marjan'
lname = 'saedi'
email = 'mm@aa'
cursor.execute('insert into customers values(%i, \'%s\', \'%s\', \'%s\')' % (id, name, lname, email))
cnx.commit()

cursor.close()
cnx.close()
