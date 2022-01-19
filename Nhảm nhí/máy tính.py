a,b,c=[x for x in input().split()]
cong='+'
tru='-'
nhan='*'
chia='/'
try:
	a= float(a)
	c= float(c)

	if b == cong:
		print(float(a)+float(c))
		input()
		exit()
	if b == tru:
		print(float(a)-float(c))
		input()
		exit()
	if b == nhan:
		print(float(a)*float(c))
		input()
		exit()
	if b == chia:
		if c == 0:
			print("Math Error")
			input()
			exit()
		else:
			print(float(a)/float(c))
			input()
			exit()
except ValueError:
	print("Math Error")
	input()