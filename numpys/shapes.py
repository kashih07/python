import numpy as np
a=np.arange(10).reshape(5,2)
print(a,end="\n\n")
b=np.arange(0,2)
print(np.multiply(a,b))
c=np.multiply(a,b)
x=np.arange(0,20,2)
for i in x:
    print(i)
y=np.concatenate((a,c))
print(y)
q=np.arange(10)
print(np.split(q,[2,5]))