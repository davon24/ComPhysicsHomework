from numpy import *

A = array([[2,4],[8,1],[0,7]])
B = array([[7,3,7],[2,8,0]])

m = A.shape[0] #A row
n = A.shape[1] #A column
l = B.shape[1]

C = zeros((m,l))
for i in range(m):
	for j in range(l):
		rowsum = 0
		for k in range(n):
			rowsum += A[i,k]*B[k,j]
		C[i,j] = rowsum

print C