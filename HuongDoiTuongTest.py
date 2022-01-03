from time import sleep as t
class Car:
    _loaixe="Oto"
    def __init__(self,soghe=4,hieu="Unknow",sobanh=4,bienso="Unknow",dongxe="Unknow",
                gia="Unknow",maluc="Unknow",phanloai="Unknow",chuxe="Kiệt"):
        self.sobanh = sobanh
        self.soghe = soghe
        self.bienso= bienso
        self.dongxe = dongxe
        self.gia = gia
        self.maluc= maluc
        self.phanloai = phanloai
        self.chuxe = chuxe
        self.hieu=hieu
    def Info(self):
        thuonghieu=f"Thương hiệu: {self.hieu}"
        dongxe=f"Dòng xe: {self.dongxe}"
        phanloai=f"Phân loại: {self.phanloai}"
        gia=f'Giá: {self.gia}'
        sobanh=f"Số bánh: {self.sobanh}"
        soghe=f"Số ghế: {self.soghe}"
        maluc=f"Mã lực: {self.maluc}"
        bienso=f"Biển số: {self.bienso}"
        chuxe=f"Chủ xe: {self.chuxe}"
        print(" ".ljust(50,"-")+'\n'+
        "|",thuonghieu.ljust(48," ")+"|"+"\n"+
        "|",dongxe.ljust(48," ")+"|"+"\n"+
        "|",phanloai.ljust(48," ")+"|"+"\n"+
        "|",gia.ljust(48," ")+"|"+"\n"+
        "|",(sobanh+"      "+soghe).ljust(48," ")+"|"+"\n"+
        "|",maluc.ljust(48," ")+"|"+"\n"+
        "|",bienso.ljust(48," ")+"|"+"\n"+
        "|",chuxe.ljust(48," ")+"|"+"\n"+
        " ".ljust(50,"-"))
class Motorcycle:
    __loaixe="Xe máy"
    def __init__(self,hieu="Unknow",sobanh=2,bienso="Unknow",dongxe="Unknow",
            gia="Unknow",maluc="Unknow",phanloai="Unknow",chuxe="Kiệt"):
        self.sobanh = sobanh
        self.bienso= bienso
        self.dongxe = dongxe
        self.gia = gia
        self.maluc= maluc
        self.phanloai = phanloai
        self.chuxe = chuxe
        self.hieu=hieu
    def Info(self):
        thuonghieu=f"Thương hiệu: {self.hieu}"
        dongxe=f"Dòng xe: {self.dongxe}"
        phanloai=f"Phân loại: {self.phanloai}"
        gia=f'Giá: {self.gia}'
        sobanh=f"Số bánh: {self.sobanh}"
        maluc=f"Mã lực: {self.maluc}"
        bienso=f"Biển số: {self.bienso}"
        chuxe=f"Chủ xe: {self.chuxe}"
        print(" ".ljust(50,"-")+'\n'+
        "|",thuonghieu.ljust(48," ")+"|"+"\n"+
        "|",dongxe.ljust(48," ")+"|"+"\n"+
        "|",phanloai.ljust(48," ")+"|"+"\n"+
        "|",gia.ljust(48," ")+"|"+"\n"+
        "|",sobanh.ljust(48," ")+"|"+"\n"+
        "|",maluc.ljust(48," ")+"|"+"\n"+
        "|",bienso.ljust(48," ")+"|"+"\n"+
        "|",chuxe.ljust(48," ")+"|"+"\n"+
        " ".ljust(50,"-"))

def phuongtien():
    print("(1) Ôtô\n"+
        "(2) Xe máy")
    idpt=input("Id loại phương tiện: ")
    print()
    return int(idpt)

def xemay():
    listxe=("(1) Honda AirBlade",
            "(2) ...")

    print("Danh sách xe máy:")
    for i in listxe:
        print(i)

    idxm=int(input('\nId xe muốn xem thông tin: '))
    if idxm == 1:
        Honda_AirBlade = Motorcycle(dongxe="AirBlade",
                hieu="Honda", phanloai="Xe tay ga",
                bienso="69A 333.33", maluc=150,
                gia="$2000")            
        Honda_AirBlade.Info()
    else:
        print("NOT FOUND")
def oto():
    listxe=("(1) RollsRoyce Phantom",
                "(2) ...")

    print("Danh sách oto:")
    for i in listxe:
        print(i)

    idxm=int(input('\nId xe muốn xem thông tin: '))
    if idxm == 1:
        RollsRoyce_Phantom = Car(dongxe="Phantom",
                    hieu="RollsRoyce", phanloai="SUV",
                    bienso="69A 222.22", maluc=563,
                    gia="$2.3M")          
        RollsRoyce_Phantom.Info()
    else:
        print("NOT FOUND")

if __name__ == "__main__":
    idpt=phuongtien()
    if idpt==1:
        oto()

    if idpt==2:
        xemay()

    if idpt >2 :
        print("NOT FOUND")
