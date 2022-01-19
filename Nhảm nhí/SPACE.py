T=int(input())
A=[]
for i in range(0,T):
	space=0
	A.clear()
	A=[x for x in input()]
	for d in range(0,len(A)):
		if d == len(A)-1 and A[d] == ' ':
			break
		if A[d] != ' ' and A[d-1] == ' ':
			space=space+1

	print(space)