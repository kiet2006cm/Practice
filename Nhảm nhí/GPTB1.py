A=[int(x) for x in input().split()]
if len(A) > 6:
	exit()
a=A[0]
b=A[1]
c=A[2]
af=A[3]
bf=A[4]
cf=A[5]
if (float(a/af) == float(b/bf)) and float((a/af) != float(c/cf)):
	print('VONGHIEM')
	input()
	exit()
if (float(a/af) == float(b/bf)) and float((a/af) == float(c/cf)):
	print('VOSONGHIEM')
	input()
	exit()
if a / af != b / bf:
	if a == af:
		bn=b-bf
		cn=c-cf
		y=round(cn/bn,2)
		x=round((c-(y*b))/a)
		print(round(x,2),round(y,2))
		input()
		exit()

	if a >  af:
		gap= a / af
		bf=bf*gap
		cf=cf*gap
		bn=b-bf
		cn=c-cf
		y=round(cn/bn,2)
		x=round((c-(y*b))/a)
		print(round(x,2),round(y,2))
		input()
		exit()
	if a < af:
		gap = af/a
		b=b*gap
		c=c*gap
		bn=bf-b
		cn=cf-c
		y=cn/bn
		x=((cf-(bf*y))/af)
		print(round(x,2),round(y,2))
		input()
		exit()
