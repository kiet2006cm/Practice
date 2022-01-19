n=int(input())
A=[int(x) for x in input().split()]
if len(A) > n:
	exit()
D=[]
for i in range(0,n-1):
	if A[i] > A[i+1]:
		D.append(A[i]-A[i+1])
	if A[i] < A[i+1]:
		D.append(A[i+1]-A[i])
print(max(D))
input()
