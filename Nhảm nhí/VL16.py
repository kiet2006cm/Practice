a,b= [int(x) for x in input().split()]

def boi(x,y):
	if a<0 and b<0:
		i=-1
		while True:
			if (i%x==0 and i%y==0):
				print(i)
				input()
				break
			i=i-1

	else:
		i=1
		while True:
			if (i%x==0 and i%y==0):
				print(i)
				input()
				break
			i=i+1

if (a==b):
	print(a)
	input()
	exit()

if (a == 1) or (a == -1):
	print(b)
	input()
	exit()
if (b == 1) or (b == -1):
	print(a)
	input()
	exit()

boi(a,b)
