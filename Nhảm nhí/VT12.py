n=int(input())
A= [int(x) for x in input().split()]
if len(A) > n:
	exit()
print(max(A)-min(A))
input()