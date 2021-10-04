
def is_palindrom(x):
    '''
    problema 5
    verifica daca un numar este palindrom
    :param numarul pe care il verificam daca este plaindrom
    :return bool: true daca e palindrom sau false daca numarul nu este palindrom
    '''


    a=x
    b=0
    while(x):
        b=b*10+x%10
        x=x//10
    if (a==b):
        return True
    else:
        return False


def test_is_palindrom():
    assert(is_palindrom(121))== True
    assert(is_palindrom(24))== False

def is_prim(n):
    '''
    problema 6
    verifica daca un numar este prim sau nu
    :param n: numarul pe care il verificam daca este prim
    :return: bool: True daca este prim sau False daca nu este prim
    '''
    if (n<2):
        return False
    if(n==2):
        return True
    for i in range(3,n//2,2):
        if(n%i==0):
            return False
        else:
            return True

def is_superprime(n):
    '''
    verifica daca un numar este superprim sau nu
    :param n: numarul pe care il verificam daca este sau nu superprim
    :return: bool: True daca este superprim sau False daca nu este superprim
    '''

    cop=n
    while(cop):
        if(is_prim(cop) == False):
            return False
        cop=cop//10
    return True

def test_is_superprime():
    assert(is_superprimee(233))== True
    assert(is_superprime(237))== False


def get_largest_prime_below(n):
    run=False
    '''
    gasim ultimul numaru prim mai mic decat numarul n dat
    :param n: n este numarul de la care pornim sa cautam numarul prim mai mic 
    :return: ultimul numar prim mai mic decat n
    '''
    while run == False :
        for i in range(n-1,1,-1):
            if (is_prim(i) == True):
                run = True
                return i
def test_get_largest_prime_below(n):
    assert(get_largest_prime_below(14))== 13
    assert(get_largest_prime_below(4))==3


def main():
    shouldRun=True
    while shouldRun:
        print("1.un numar este palindrom sau nu")
        print("2.un numar este superprim sau nu")
        print("3.ultimul numar prim mai mic decat un numar dat")
        print("x.Iesire")

        optiune=input("dati optiune:")
        if(optiune=="1"):
            n=int(input("dati nr:"))
            if is_palindrom(n)==True:
                print("numarul n este palindrom")
            else:
                print("numarul n nu este palindrom")
        elif(optiune=="2"):
            n=int(input("dati numarul:"))
            if(is_superprime(n)==True):
                print("numarul n este superprim")
            else:
                print("numarul nu este superprim")
        elif (optiune == "3"):
            n = int(input("dati numarul:"))
            print(get_largest_prime_below(n))

        elif optiune=="x":
            shouldRun=False

if __name__=='__main__':
    main()








