A=[int(x) for x in input().split()]
B=[]
for i in range(0,len(A)):
	if A[i] < 0:
		B.append(A[i])
if len(B) == 0:
	input('NOT FOUND')
	exit()
else:
	for i in range(0,len(B)):
		print(B[i],end=' ')
	input()
