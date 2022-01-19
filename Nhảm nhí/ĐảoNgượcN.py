print("Đảo ngược số N")

print("N = ",end='')
nfake=input()

# try:
# 	n=int(nfake)
# 	while (n != 0):
# 		print(n%10,end='')
# 		n = n//10
# 	print('')
# except ValueError:
# 	print("Lỗi")

daonguoc=''
try:
	n=int(nfake)
	print('Đảo ngược của',n,end=' ')
	while (n != 0):
		daonguoc = daonguoc + str(n%10)
		n = n//10
	print('là:',daonguoc)
	input("\n Ấn Enter để tắt")
except ValueError:
	print("Lỗi")
	input("\n Ấn Enter để tắt")

