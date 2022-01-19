a=int(input())
u=0
if (a<0):
	a=-a
for i in range(1,a+1):
	if (a % i == 0):
		u=u+1
print(u)
input()