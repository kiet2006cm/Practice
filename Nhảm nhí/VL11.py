print('https://luyencode.net/problem/VL11','\nVL11 - Kiểm tra số nguyên tố\n')
print('Đề: Cho số nguyên nn, hãy viết chương trình kiểm tra xem n có phải số nguyên tố hay không?\n')
print('Dữ liệu vào: Số nguyên n cần kiểm tra\n')
print('Giới hạn: |n| <= e12\n')
print('Dữ liệu ra: Nếu n là số nguyên tố, in ra YES, ngược lại in ra NO\n')

n=int(input())
for i in range(2,n):
	if n%i==0:
		print('NO')
		input()
		exit()
print('YES')
input()