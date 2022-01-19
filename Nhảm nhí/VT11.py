n = int(input())
if n < 3:
	exit()
A=[int(x) for x in input().split()]
if len(A) > n:
	exit()
print(A[0],end=' ')
A.remove(A[0])

bruh=A[n-2]
A.remove(A[n-2])
for i in range(0,n-2):
	print(min(A),end=' ')
	A.remove(min(A))
print(bruh)

input()