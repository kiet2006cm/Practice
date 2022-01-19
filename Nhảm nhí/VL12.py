print('https://luyencode.net/problem/VL12','\nVL12 - Liệt kê các ước số\n')
print('Đề: Viết chương trình liệt kê các ước nguyên dương của số nguyên n nhập từ bàn phím theo thứ tự giảm dần.\n')
print("Dữ liệu vào: Số nguyên n, |n| <= e4\n")
print('Dữ liệu ra:\n  - Danh sách các ước số nguyên dương của số n theo thứ tự giảm dần, các số cách nhau bởi 1 dấu cách')
print('  - Nếu số n có vô số ước nguyên dương, in ra INF\n')

n=int(input())
if n > int(1e4):
	print('INF')
	input()
	exit()

else:
	i=n
	while i!=0:
		if n%i==0:
			print(i,end=' ')
		i = i-1
input()