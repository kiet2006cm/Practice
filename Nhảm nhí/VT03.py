j=int(input())
A=[x for x in input().split()]
for i in range(0,j):
	if max(A) == A[i]:
		print(i)
		input()
		exit()
