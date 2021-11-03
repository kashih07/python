"""
Create a numpy array 4x4 with all TrueReplace all odd numbers from the array with -1

3. Find max and min from a matrix
4. a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
Find the common elements from a and b
5. a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
Remove all values from b if present in a
"""

#ex1
import numpy as np
fourdarray=np.ones((4,4),dtype=bool)
print(fourdarray)

#ex2
b=np.arange(11)
b[b%2!=0]=-1
print(b)

#ex3
mat=np.matrix('1,2,3;5,8,9;12,5,1')
print("max ele is "+str(np.max(mat))+"\nmin element is "+str(np.min(mat)))
x=np.matrix((4,4),dtype=bool)
print(x)