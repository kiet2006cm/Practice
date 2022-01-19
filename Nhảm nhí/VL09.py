print('Luyencode.net/problem/VL09\n')
x,n=[int(x) for x in input().split()]
s=0

def giaithua(x):
	if x==1:
		return 1
	else:
		return (x * giaithua(x-1))

for i in range(1,n+1):
	s= ((x**i)/giaithua(i)) + s

print(s)
input()