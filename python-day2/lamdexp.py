print("This is from another module")
def largest(*arg):
    l=[]
    for i in arg:
        l.append(i)
    print("Largest element is:"+str(max(l)))

def sayhello(name):
    print("name is "+str(name))