import math

def Bac2MotAn():
    print("Giải phương trình bậc hai 1 ẩn")
    print("ax^2 + bx + c = 0")
    print('a = ',end='')
    afake = input()
    print('b = ',end='')
    bfake = input()
    print('c = ',end='')
    cfake = input()
    try:
        a = float(afake)
        b = float(bfake)
        c = float(cfake)

        delta = b**2 - (4 * a * c)

        if delta == 0:
            x = (-b)/(2*a)
            print("Phương trình có nghiệm kép là: x1 = x2 =",x)
        if delta < 0:
            print("Phương trình vô nghiệm")
        if delta > 0:
            x1 = ((-b) + math.sqrt(delta))/(2*a)
            x2 = ((-b) - math.sqrt(delta))/(2*a)
            print("Phương trình có 2 nghiệm phân biệt:")
            print("x1 =",x1, end=' | ')
            print("x2 =",x2)
    except ValueError:
        print("Error! ⁌Try again⁍")
def Bac1MotAn():
    print("Tìm x phương trình bậc nhất 1 ẩn")
    print("ax + b = 0")
    print("A = ",end='')
    afake = input()
    print("B = ",end='')
    bfake = input()
    try:
        a=float(afake)
        b=float(bfake)
        if b == 0 and a == 0:
            print("Phương trình vô số nghiệm")
        if a == 0 and b != 0:
            print("Phương trình vô nghiệm")
        x = ((-b)/a)
        print("Nghiệm của phương trình là: x =",x)
    except ValueError:
	    print("Error")
def GiaiThua():
    print("Số cần tính giai thừa: ",end='')
    so=input()
    def giaithua(x):
        if x == 1:
            return 1
        else:
            return (x * giaithua(x-1))
    try:
        so=int(so)
        print("Giai thừa của",so,'là:',giaithua(so))
    except ValueError:
        print('Lỗi')
def HePhuongTrinhBac1MotAn():
    print("Hệ phương trình bậc nhất 1 ẩn")
    a1fake = input("a = ")
    b1fake = input("b = ")
    c1fake = input("c = ")
    a2fake = input("a' = ")
    b2fake = input("b' = ") 
    c2fake = input("c' = ")
    try:
        a1 = float(a1fake)
        b1 = float(b1fake)
        c1 = float(c1fake)
        a2 = float(a2fake)
        b2 = float(b2fake)
        c2 = float(c2fake)
        print("\n")
        print('|',a1,'x + ',b1,'y =',c1)
        print('|',a2,'x + ',b2,'y =',c2)
        if a1/a2 == b1/b2 and a1/a2 != c1/c2:
            print("\t\t => Vô nghiệm")
        if a1/a2 == c1/c2 and a1/a2 == c1/c2:
            print("\t\t => Vô số nghiệm")
        if a1/a2 != b1/b2:
            if a1 == a2:
                bnew = b1 - b2
                cnew = c1 - c2
                y = cnew/bnew
                x = (c1-(b1*y))/a1 
                print("\t [ x = ",x,']')
                print("\t [ y = ",y,']')
            if a1 > a2:
                nhan = (a1/a2)
                b2 = b2 * nhan
                c2 = c2 * nhan
                bnew= b1 - b2
                cnew= c1 - c2
                y = cnew/bnew
                x = (c1-(b1*y))/a1 
                print("\t [ x = ",x,']')
                print("\t [ y = ",y,']')
            if a1 < a2:
                nhan = (a2/a1)
                b1 = b1 * nhan
                c1 = c1 * nhan
                bnew= b2 - b1
                cnew= c2 - c1
                y = cnew/bnew
                x = (c2-(b2*y))/a2
                print("\t [ x = ",x,']')
                print("\t [ y = ",y,']')            
    except ValueError:
        print("Nhập nhầm rồi")	
def KiemTraSo9Phuong():
    print("Kiểm tra N có phải số chính phương không")
    print("N = ",end='')
    nfake=input()
    a=0
    try:
        n = int(nfake)
        if n == 1:
            print("1 là số chính phương")
        for i in range(1,n):
            if i**2 == n:
                a = 1
                break
        if a == 0:
            print(n,'không là số chính phương')
        else:
            print(n,"là số chính phương")		
    except ValueError:
        print("Có lỗi!")
def KiemSoNguyenTo():
    print("Kiểm tra N có phải số nguyên tố không")
    print("N = ",end='')
    nfake=input()
    try:
        n=int(nfake)
        if n == 1 or n == 2 or n == 3:
            print(n,"là số nguyên tố")
        for i in range(3,n,2):
            if n%i != 0:
                print(n,'là số nguyên tố')
                break
            if n%i==0:
                print(n,"không là số nguyên tố")
                break
    except ValueError:
        print("Lỗi!")
def kiemsohoanhao():
    print("Kiểm tra N có phải số hoàn hảo không")
    print("N = ",end='')
    nfake=input()
    tong=0
    try:
        n=int(nfake)
        for i in range(1, n):
            if n%i == 0:
                tong= tong + i
        if tong == n:
            print(n,'Là số hoàn hảo')
        else:
            print(n,'Không phải là số hoàn hảo')
    except ValueError:
        print("Có lỗi!")
def sohoanhaotu1toin():
    print("Các số hoàn hảo từ 1 tới N")
    print("N = ",end='')
    toi=int(input())
    shh=[]
    def check(n):
        tong=0
        for i in range(1, n):
            if n%i == 0:
                tong= tong + i
        if tong == n:
            shh.append(n)
    for n in range(1,toi+1):
        check(n)
    print("Các số hoàn hảo từ 1 tới ",toi," là: ",shh)
def tatcauocso():
    print("Liệt kê tất cả các ước số của số nguyên dương N")
    print("N = ",end='')
    nfake=input()
    print("Ước của N: ",end='')
    try:
        n=int(nfake)
        for i in range(1, n+1):
            if n%i == 0:
                print(i,end=' | ')
    except ValueError:
        print("Có lỗi!")
def tohopchapk():
    n,k=[int(x) for x in input().split()]
    gn=1
    gk=1
    gnk=1
    for i in range(2,n+1):
        gn= gn*i
        if k >= i:
            gk=gk*i
        if (n-k) >= i:
            gnk= gnk*i
    kq=gn//(gk*gnk)
    print(kq)
def tong1binhtoinbinh():
    import time
    print("Tính tổng từ 1^2 tới N^2")
    time.sleep(2)
    print("Nhập N: ", end='')
    n=input()
    i=0
    a=1
    try:
        hi = int(n)
        for i in range(hi+1):
            a= a + a^2
        print(a)
    except ValueError:
        print("Thứ bạn nhập vào không phải số nguyên")
def tongtu1toin():
    try:
        n=int(input())
        tong=0
        for i in range(1,n):
            tong=tong+i
        print(tong)
    except ValueError:
        print('Error')
def uoclelonnhat():
    print("Ước lẻ lớn nhất của N")
    print("N = ",end='')
    nfake=input()
    uoclelonnhat=0
    try:
        n=int(nfake)
        for i in range(1, n+1):
            if (n % i == 0 and i % 2 == 1):
                uoclelonnhat = i
        print(uoclelonnhat)
    except ValueError:
        print("Có lỗi!")
if __name__=="__main__":
    while True:
        try:
            print('\nNhập id phép tính')
            yn=input('Bạn có muốn in list id ra không? (y/n)')
            if yn=='y':
                print(
                    '0: Thoát'
                    '1: Phương trình bậc hai 1 ẩn\n'
                    '2: Phương trình bậc nhất 1 ẩn\n'
                    '3: Giai thừa\n'
                    '4: Hệ phương trình bậc nhất 1 ẩn\n'
                    '5: Kiểm tra số chính phương\n'
                    '6: Kiểm tra số nguyên tố\n'
                    '7: Kiểm tra số hoàn hảo\n'
                    '8: Kiểm tra số hoàn hảo từ 1 tới n\n'
                    '9: Tất cả ước số của n\n'
                    '10: Tổ hợp chập k của n\n'
                    '11: Tổng từ 1 bình phương tới n bình phương\n'
                    '12: Tổng từ 1 tới n\n'
                    '13: Ước lẻ lớn nhất của n\n'
                )
            pheptoan=int(input())
            if pheptoan==0:break
            if pheptoan==1:Bac2MotAn()
            if pheptoan==2:HePhuongTrinhBac1MotAn()
            if pheptoan==3:GiaiThua()
            if pheptoan==4:HePhuongTrinhBac1MotAn()
            if pheptoan==5:KiemTraSo9Phuong()
            if pheptoan==6:KiemSoNguyenTo()
            if pheptoan==7:kiemsohoanhao()
            if pheptoan==8:sohoanhaotu1toin()
            if pheptoan==9:tatcauocso()
            if pheptoan==10:tohopchapk()
            if pheptoan==11:tong1binhtoinbinh()
            if pheptoan==12:tongtu1toin()
            if pheptoan==13:uoclelonnhat()
            if pheptoan>13:print('Hiện tại chưa có')
        except ValueError:
            print('Bạn nhập sai giá trị')
        