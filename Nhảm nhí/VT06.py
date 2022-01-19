j=int(input())
A=[int(x) for x in input().split()]
lan=0
tong=0

for i in range(0,j):
	if A[i] % 2 !=0:
		tong = tong + A[i]
		lan = lan + 1

tbc=float(tong/lan)
print(round(tbc,4))
input()