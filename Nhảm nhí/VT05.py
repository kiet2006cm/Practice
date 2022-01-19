n,x= [int(x) for x in input().split()]
A=[int(x) for x in input().split()]
d=0
for i in range(0,n):
	if A[i] == x:
		d=d+1
print(d)
input()
