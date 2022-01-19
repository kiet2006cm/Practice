A=[int(x) for x in input().split()]
L=[]
d=0
for i in range(0,10):
	if A[i] == A[10]:
		print(i+1,end=' ')
		d=d+1
if d == 0:
	print('-1')

input()