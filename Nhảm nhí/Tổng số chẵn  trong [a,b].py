a,b=[int(x) for x in input().split()]
c=0
if a % 2 ==0:
	for i in range(a,b+1,2):
		c=c+i
else:
	for i in range(a+1,b+1,2):
		c=c+i        
print(c)
input()