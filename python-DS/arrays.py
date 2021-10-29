from array import *
a=array('i',[1,2,3,4,5,6,7,8,9])
for i in a:
    print(i,end=" \t")
a.insert(len(a), 10)
a.remove(10)
print(a,len(a))
