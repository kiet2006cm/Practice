import string
import random

def randompassword(chu=string.ascii_letters,
            so=string.digits,
            ktdb=string.punctuation,
            length=random.randint(8,16),
            daokitu=random.randint(5,20)):
    """Return Random Password"""
    kitu = f'{chu}{so}{ktdb}'
    kitu =list(kitu)
    for i in range(daokitu):
        random.shuffle(kitu)
    pw = random.choices(kitu, k=length)
    pw = ''.join(pw)
    return pw

def main():
    print(randompassword())

if __name__=='__main__':
    main()
