while True:
	n=int(input())
	cuoi=n%10
	while n != 0:
		if n >0:
			dau=n
		n=n//10 
	if int(dau) == int(cuoi):
		print('YES')
	else:
		print('NO')
