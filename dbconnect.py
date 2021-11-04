#this is db file
import mysql.connector

def connectdb():
    db = mysql.connector.connect(host="localhost", user="root", password="asus", database="python")
    curzor = db.cursor()
    print("""
         +------------------------------------+
         |Database Connection Status:Connected|
         +------------------------------------+
         |USER==root          DATABASE==python|
         +------------------------------------+
         """)
    return db

def showtableval():
    db = connectdb()
    curzor = db.cursor()
    y=curzor.execute("select * from task")
    x=curzor.fetchall()
    for i in x:
        print(i)
    print("No. of rows are: ")
    curzor.execute("select Count(*) from task")
    print(curzor.fetchall())

def insert(taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon, modifiedon):
    db = connectdb()
    curzor = db.cursor()
    command = ("insert into task(taskid,taskname,descript,stats,priority,notes,bookmark,ownerid,creatorid,createdon,modifiedon)""values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    data = (taskid, taskname, description, status, priority, notes, bookmark, ownerid, creatorid, createdon, modifiedon)
    curzor.execute(command, data)
    db.commit()

def deleterow(taskid):
    db=connectdb()
    curzor=db.cursor()
    command=("delete from task where taskid=%s"%(taskid))
    data=(taskid)
    curzor.execute(command,data)
    db.commit()
    showtableval();