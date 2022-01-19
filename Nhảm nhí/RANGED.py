A=[int(x) for x in input().split()]
a,b,c,d=A[0],A[1],A[2],A[3]
if c <= a and d >= a:
	print('YES')
	exit()
if b >= c:
	print('YES')
	exit()
print('NO')
