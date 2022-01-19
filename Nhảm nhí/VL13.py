n=int(input())
a=0
for i in range(1,n):
	if n%i==0:
		a = a + i
if int(a)==n:
	print('YES')
else:
	print('NO')
input()