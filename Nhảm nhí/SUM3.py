n=int(input())
tong=0
for i in range(1,n+1):
	tong=tong+(1/(i*(i+1)))
print(round(tong,5))
input()