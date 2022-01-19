j=int(input())

A=[x for x in input().split()]
nhi=0
m=int(A[0])
for i in range(1,j):
	hientai=int(A[i])
	if (hientai > m):
		nhi=m
		m = hientai
		continue
	if (hientai > nhi) and (hientai < m):
		nhi= hientai

print(nhi)
input()