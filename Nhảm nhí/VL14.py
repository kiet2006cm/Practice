a,b=[int(x) for x in input().split()]

# if a==b:
# 	print(a)
# 	input()
# 	exit()
# if a == 0:
# 	print(b)
# 	input()
# 	exit()
# if b == 0:
# 	print(a)
# 	input()
# 	exit()

if a > b:
	if b < 0:
		d = -b
	else:
		d = b
if a < b:
	if a < 0:
		d = -a
	else:
		d = a


while d != 0:
	if a%d==0:
		if b%d==0:
			cc=d
			input()
			exit()
	d = d - 1