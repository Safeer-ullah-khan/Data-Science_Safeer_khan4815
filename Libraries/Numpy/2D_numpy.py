import numpy as np
# a=np.array([[1,0],[0,1]])
# b=np.array([[2,1],[1,2]])
# c=np.add(a,b)
# d=np.subtract(a,b)
# e=np.multiply(2,b)
# print(c)
# print(d)
# print(e)
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
c=np.dot(A,B)
print(c)