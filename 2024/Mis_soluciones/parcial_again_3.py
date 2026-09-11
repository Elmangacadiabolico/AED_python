def Es_mayuscula(x):
    if x == x.upper() and x not in '0123456789':
        return True
    return False
def Es_minuscula(x):
    if x == x.lower() and x not in '0123456789':
        return True
    return False
def Es_numer(x):
    if x in '0123456789':
        return True
    return False
def longitud(palabra,r2):
    if r2 is None:
        r2 = len(palabra)
        print(r2)
        return r2
    else:
        if r2 < len(palabra):
            r2 = len(palabra)
        return r2
def  Es_vocal(x):
    if x in'aeiou'and x == x.lower() or x==x.upper():
        return True
    return False

def main ():
    m = open('entrada_1.txt','rt')
    texto = m.read()
    r1=r2=r3=r4=0
    C_n= C_p_n_V=C_t_P = 0
    palabra =''
    E_palabra=E_p=E_n = E_numero= E_vocal = False
    for i in texto:
        if i not in ' .':
            E_palabra = True
            palabra += i
            if i == 'p':
                E_p = True
            if i == 'n':
                E_n = True
            if Es_numer(i):
                E_numero = True
                C_n += 1
            if Es_vocal(i):
                E_vocal = True
        else:
            if E_palabra:
                C_t_P += 1
                # r1
                #PAJEROLA3
                #01234
                if Es_mayuscula(palabra[0]):
                    if len(palabra) > 3 and  Es_numer(palabra[3]):
                        r1 +=1
                #r2
                if E_p or E_n:
                    r2 = longitud(palabra,r2)
                #r3
                if E_numero:
                    if C_n >= 2 and E_vocal:
                        print(palabra)
                        C_p_n_V += len(palabra)



                E_palabra=E_p=E_n = E_numero= E_vocal = False
                palabra = ''
                C_n = 0

    r3 = (C_t_P // C_p_n_V )
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    main()