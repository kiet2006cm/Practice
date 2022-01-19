n=int(input())
if n < 2 or n > 1e4:
	exit()
A=[int(x) for x in input().split()]
if len(A) > n:
	exit()
a=max(A)
A.remove(max(A))
b=max(A)
A.remove(max(A))
c=max(A)
print(a*b*c)
input()