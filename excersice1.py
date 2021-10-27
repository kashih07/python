""" Create a program to compare three numbers and find the bigger numbers. [topics covered:
identified, variable, types, operator, if statement]"""
l=[]#empty list
for i in range(3):
    x=input("enter no")
    l.append(x)
l.sort()
print("largest no. is "+str(l[-1]))