import time
print("Tổng 1 + 1/3 + 1/5 + ... + 1/(2N+1)")
print("N = ",end='')
nfake=input()
tong=0
try:
	n=int(nfake)
	for i in range(1, n+1):
		tong= tong+ (1/(2*i +1))
	tong=tong+1
	print('Đang tính toán...')
	time.sleep(1)
	print(tong)
	dung=input("\n Ấn Enter để dừng")

except ValueError:
	print("Có lỗi")
	dung=input("\n Ấn Enter để dừng")

