a,b=[int(x) for x in input().split()]

# for i in range(a,b+1):
# 	if i%3==0:
# 		print(i,end=' ')

d=[]
for i in range(a+1,b):
	if i%3==0:
		d.append(i)
if len(d)==0:
	print('NOT FOUND')
else:
	i=-1
	while i != (-len(d)-1):
		print(d[i], end=' ')
		i=i-1
input()