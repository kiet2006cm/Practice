import time
print("Tổng từ 1 + 1/2 + 1/3 + ... + 1/N")
# time.sleep(2)
bd= time.time()
print("Nhập N: ", end='')
nfake = input()
tong=0

try:
	n=int(nfake)
	for i in range(1, n+1):
		tong= tong + 1/i
	print(tong) 


except ValueError:
	print("Số bạn nhập không thuộc tập số N")
kt=time.time()

tongtime = kt-bd
print("Số thời gian để thực hiện phép tính: ",tongtime,'giây')
dung=input("\n Ấn Enter để dừng")