import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="asus",database="python")
curzor=db.cursor()
curzor.execute("delete from table1 where name='Brundha M'")
db.commit()
x=curzor.execute("select * from table1");

y=curzor.fetchall()
print(y)