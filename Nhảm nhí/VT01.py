j=int(input())

# for i in range(0,j):
# 	A.append(input())
A=[x for x in input().split()]
try:
	A[j]
	exit()
except IndexError:
	print(max(A))
input()