T=int(input())

for i in range(1,T+1):
	n=int(input())
	ketquanguoc=[]
	while n-1>=0:
		ketquanguoc.append(n%2)
		n=n//2
	dem=len(ketquanguoc)-1
	while dem>=0:
		print(ketquanguoc[dem],end='')
		dem=dem-1
	print('')

