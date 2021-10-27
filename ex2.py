"""excersice 2"""
a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
def fun(a,b,c):
    l=[a,b,c]
    l.sort()
    return l[-1];
print("Largest no."+str(fun(a,b,c)))

