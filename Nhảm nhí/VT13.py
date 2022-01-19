n=int(input())
if n < 2 or n > 1e4:
	exit()
A=[int(x) for x in input().split()]
if len(A) > n:
	exit()
B=[]

for i in range(0,n-1):
	B.append(A[i]+ A[i+1])

for i in range(0,len(B)):
	if max(B) == B[i]:
		d = i
		break
print(A[d],A[d+1])
input()



