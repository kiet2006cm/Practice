import time
print("Nhập số muốn tìm: ", end='')
somuontim = input()
print("Nhập số phần tử của dãy: ", end='')
n= int(input())
bien = []

for hi in range(n):
	bien.append(input())

print(bien)

dem=0

i=0

for i in range(n):
	if bien[i] == somuontim:
		dem = dem + 1

dung=input("Ấn enter để dừng")