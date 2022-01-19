n,x= [int(x) for x in input().split()]
A=[int(x) for x in input().split()]

for i in range(0,n):
	if A[i] == x:
		print('Yes')
		input()
		exit()
print('NO')
input()

