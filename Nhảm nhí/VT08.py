s=int(input())
pt=[int(x) for x in input().split()]
for i in range(0,s):
	if pt[i] % 2 != 0:
		try:
			try:
				pt[i] = pt[i] + (pt[i+1]-pt[i-1])
				
			except TypeError:
				try:
					pt= pt[i] + pt[i+1]
				except TypeError:
					pt= pt[i] + pt[i-1]

		except IndexError:
			try:
				pt[i] = pt[i] + pt[i-1]
			except TypeError:
				pt[i]=pt[i]

	if pt[i] < 0:
		pt[i] = -pt[i]
	print(pt[i],end=' ')
input()