#ex7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,2,3]
def fun(a):
    r = []
    for i in a:
        if i in r:
            pass
        else:
            r.append(i)
    return r
print(fun(a))