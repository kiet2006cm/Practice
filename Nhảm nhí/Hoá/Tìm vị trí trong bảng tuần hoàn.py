print('Tìm vị trí trong bảng tuần hoàn và cho biết số Z, e, p')
print('Khi cho biết cấu hình e phân lớp ngoài cùng\n')
print('Ví dụ: 3 s 2')
print('Chu kì 3 | Nhóm IIA | Z, e, p = 12 |\n')

print('(#) Chỉ đúng với nguyên tố dưới chu kì 5\n')

while True:	
	p,t,s=[x for x in input().split()]
	if [p,t,s] == ['1','s','1']:
		print('Chu kì 1 | Nhóm IA \nZ,p,e = 1\nLà phi kim\n')
		continue
	if [p,t,s] == ['1','s','2']:
		print('Chu kì 1 | Nhóm VIIIA \nZ,p,e = 2\nLà phi kim\n')
		continue
	if [p,t,s] == ['2','p','1']:
		print('Chu kì 2 | Nhóm IIIA \nZ,p,e = 5\nLà phi kim\n')
		continue


	chuki = int(p)
	ab= int(p)
	electron=0

	for i in range(1,chuki):
		if i == 1:
			electron=electron+2
		if i == 2:
			electron=electron+8
		if i == 3:
			electron=electron+18
		if i == 4:
			electron=electron+32
	if str(t) == 's':
		electron = electron + int(s)
	if str(t) == 'p':
		electron = electron + 2 + int(s)
	if str(t) == 'd':
		electron = electron + 8 + int(s)
	if str(t) == 'f':
		electron = electron + 18 + int(s)

	if int(s)==1:
		if str(t)=='p':
			nhom='III'
		else:
			nhom='I'
	if int(s)==2:
		if str(t)=='p':
			nhom='IV'
		else:
			nhom='II'
	if int(s)==3:
		if str(t)=='p':
			nhom='V'
		else:
			nhom='III'
	if int(s)==4:
		if str(t)=='p':
			nhom='VI'
		else:
			nhom='IV'
	if int(s)==5:
		if str(t)=='p':
			nhom='VII'
		else:
			nhom='V'
	if int(s)==6:
		if str(t)=='p':
			nhom='VIII'
		else:
			nhom='VI'
	if int(s)==7:
		nhom='VII'
	if int(s)==8:
		nhom='VIII'
	if int(s) > 8:
		nhom='?'
	if ab < 4:
		nhom=nhom+'A'
	if ab==4:
		nhom=nhom+'B'


	if int(s)==1 or int(s)==2 or int(s)==3:
		nguyento='Kim Loại'
	if int(s)==5 or int(s)==6 or int(s)==7:
		nguyento='Phi Kim' 
	if int(s)==8:
		nguyento='Khí Hiếm'
	if int(s) == 4:
		if chuki==2 or chuki==3:
			nguyento='Phi Kim'
		else:
			nguyento='Kim Loai'

	print('Chu kì',chuki,'| Nhóm',nhom,'\nZ, e, p =',electron)
	print('Là',nguyento,'\n')



