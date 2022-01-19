ngay=1
thang=1
nam=1990
while True:
	print(ngay,end='/')
	print(thang,end='/')
	print(nam, end=' ')
	ngay=ngay+1
	if (thang==1) or (thang==3) or (thang==5) or (thang==7) or (thang==8) or (thang==10) or (thang==12):
		if (ngay==32):
			thang = thang + 1
			ngay=1
	if (thang==4) or (thang==6) or (thang==9) or (thang==11):
		if (ngay==31):
			thang=thang+1
			ngay=1
	if (thang==2):
		if (ngay == 29):
			thang=thang+1
			ngay=1
	if (thang == 13):
		ngay = 1
		thang=1 
		nam=nam+1
	if (nam == 2006):
		break
input()