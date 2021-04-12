#在这里学习numpy
import numpy as np

a = np.random.rand(5,5) # [0,1) 5*5 Matrix
# print(a)

b = np.random.rand(5,5) # N(0,1) 
# print(b)

randomInt = np.random.randint(0,100,(5,5)) 
# print(randomInt)

c = np.eye(5)
# print(c)


A = np.matrix(a)
B = np.matrix(b)
# print(A)
# print(B)

C = A.dot(B)
print(C)

b = np.transpose(np.array([1,2,3,4,5]))
x = np.linalg.solve(A,b)
print(x)
print(b)


