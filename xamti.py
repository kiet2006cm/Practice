import random as r
import string as s

def chonveso(so=s.digits,dodai=6):
    """Return 1 Tờ Vé Số Ngẫu Nhiên"""
    a=f'{so*6}'
    a=list(a)
    for i in range(1,r.randint(2,21)):
        r.shuffle(a)
    a= r.choices(a,k=dodai)
    a=''.join(a)
    return a

def inveso(sove):
    """Return Mấy Tờ Vé Số"""
    veso=[]
    for i in range(1,int(sove)+1):
        veso.append(chonveso())
    veso = list(set(veso))
    r.shuffle(veso)
    while int(len(veso)) < int(sove):
        veso.append(chonveso())
        veso=list(set(veso))
        r.shuffle(veso)
    for i in veso:
        print(i)

def main():
    print('Xin chào tôi là lính thủy đánh bạc')
    print('Đây là trình random vé số')
    sove=input('Số tờ vé số muốn in: ')
    inveso(sove)

if __name__ == '__main__':
    main()

        
