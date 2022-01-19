n = int(input())

A=[int(x) for x in input().split()]
B=[]
for i in range(0,n):
	B.append(A[i])

for i in range(0,n):
	print(max(B),end=' ')
	B.remove(max(B))


input()