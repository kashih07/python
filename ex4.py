#ex 4
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
l=[]
for i in a:
    for j in b:
        if i==j:
            l.append(i)
r=[]
for i in l:
    if i in r:
        pass
    else:
        r.append(i)
print(r)