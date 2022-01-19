n=int(input())
t=0
for x in range(1,n):
	if (t<n):
		t=x+t
	if (t+x > n):
		break
print(x)
input()
