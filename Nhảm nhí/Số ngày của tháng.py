m,y=[int(x) for x in input().split()]
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
	print("31")
	input()
if m==4 or m==6 or m==9 or m==11:
	print('30')
	input()
if m==2:
	if y%400==0 or y%4==0 and y%100!=0:
		print('29')
		input()
	else:
		print('28')
		input()