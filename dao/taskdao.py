import dbconnect#module import
from service import task#from the package
import time
def run(t):#getting object as para
    print("<<<<<<<<<<<<      WELCOME TO TASK TRACKER      >>>>>>>>>>>>")
    time.sleep(2)#its just to show
    print("connecting to Database........... ")
    time.sleep(2)
    dbconnect.connectdb()#connecting db
    print("Inserting the values.....")
    dbconnect.insert(t.taskid,t.taskname,t.description,t.status,t.priority,t.notes,t.bookmark,t.ownerid,t.creatorid,t.createdon,t.modifiedon)
    time.sleep(2)#task object is created here
    print("Inserted Successfully,getting tables ready with newly inserted values....")
    time.sleep(2)
    dbconnect.showtableval()
    time.sleep(2)
    #dbconnect.deleterow(t.taskid)
    print("All values are commited successfully..")#showing table from dbconnect module
