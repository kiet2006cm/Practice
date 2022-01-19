print("In ra từng ký tự của số N")

print("N = ",end='')
nfake=input()
a=''

try:
	n=int(nfake)
	print('Các ký tự của',n,end=': ')
	while (n != 0):
		a = a + str(n%10)
		n = n//10
	
	a =int(a)

	while (a != 0):
		print(a%10,end=' | ')
		a = a//10
	dung=input("\n Ấn Enter để dừng")
		

	
except ValueError:
	print("Lỗi rồi 😥")
	dung=input("\n Ấn Enter để dừng")