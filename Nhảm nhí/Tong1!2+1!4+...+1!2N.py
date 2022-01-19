import time
print("Tổng 1/2 + 1/4 + ... + 1/2N")
print("N = ",end='')
nfake=input()
tong=0
try:
	n=int(nfake)
	for i in range(1, n+1):
		tong= tong+ (1/(2*i))
	print('Đang tính toán...')
	time.sleep(1)
	print(tong)
	dung=input("\n Ấn Enter để dừng")

except ValueError:
	print("Có lỗi")
	dung=input("\n Ấn Enter để dừng")
