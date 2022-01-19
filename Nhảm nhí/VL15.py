a, b=[int(x) for x in input().split()]

if b == 0:
	print('INVALID')
	input()
	exit()

if a == 0:
	print('0')
	input()
	exit()

if int(a) == int(b):
	print('1')
	input()
	exit()
if float(a) == float(-b) or float(-a) == float(b):
	print('-1')
	input()
	exit()

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
cc=1
while d != 0:
	if a%d==0:
		if b%d==0:
			cc=d
			break
	d = d - 1

if b < 0:
	a = -a
	b = -b

kqa=int(a/cc)
kqb=int(b/cc)
if int(kqb) == 1:
	print(kqa)
	input()
	exit()
print(kqa,kqb)
input()