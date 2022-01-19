a,b=[x for x in input().split()]
bcc=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i' , 'j', 'k' , 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
bcch=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' , 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
c,d=a,b

for i in range(0,len(bcc)):
	if (a == bcc[i]):
		a = bcch[i]
		e=int(i)
	if (b == bcc[i]):
		b = bcch[i]
		f=int(i)+1
	if (a != c and b != d):
		break

for i in range(e,f):
	print(bcch[i],end=' ')

input()