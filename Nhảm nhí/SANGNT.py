n=int(input())
if n == 1:
	exit()
if n==2:
	print(2)
if n==3:
	print(2,3)
if n > 3:
	print(2,3,end=' ')
for i in range(5,n+1,2):
	check=0
	for d in range(2,i-1):
		if i%d==0:
			check=1
		if check==1:
			break
	if check ==0:
		print(i,end=' ')
input()