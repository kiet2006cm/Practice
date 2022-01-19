n= int(input())

# while n != 0:
# 	print(n%10,end='')
# 	n = n // 10
# input()

f=1
a= 0

while n!=0:
	a= a*f + (n%10)
	n=n//10
	if f<10:
		f=f*10
print(a)
input()