def numb(i):
    if i.lower() in '0123456789':
        return True
    return False
def num_impar(i):
    if i in '13579':
        return True
    return False

def Mayuscula(i):
    if i ==  i.upper() and i not in '0123456789':
        return True
    return False
def logitud (i,r2):

    if r2 is None or len(i)> r2:
            print(r2)
            r2 = len(i)
    return r2

def vocal(i):
    if i == i.lower() and i in'aeiou':
        return True
    return False
def consotante(i):
    if i.lower() in 'bcdfghjklmnñpqrstvwxyz':
        return True
    return False


def main():
    m = open('entrada_1.txt','rt')
    txt = m.read()
    r1=r3=r4 = 0
    r2 = None
    count_letra = cc = cv = count_r3 = Count_pp = sum_char = 0
    palabra = ''
    E_palabra= E_Mayuscula = E_numero = E_numbers_im = False
    m.close()
    for i in txt:
        if i not in ' .':
            E_palabra = True
            palabra += i
            count_letra += 1

            if Mayuscula(i):
                E_Mayuscula = True
            if numb(i):
                E_numero = True
            if num_impar:
                E_impar = True
            if vocal(i):
                E_vocal = True
                cv +=1
            if consotante(i):
                cc += 1
        else:
            if E_palabra:
                Count_pp += 1
                #r1
                if E_numero:
                    if  numb(palabra[-1]) and not E_Mayuscula:
                        r1+=1
                #r2
                if E_numbers_im:
                    r2 = logitud(i,r2)
                    print(r2)
                #r3
                if vocal(palabra[0]) and cc >= 3:
                        sum_char = len(palabra)
                        count_r3 += 1


            E_palabra = E_Mayuscula = E_numero = E_numbers_im = False
            palabra =''
            count_letra = cc = cv = 0
    if count_r3 > 0:
        r3 = (sum_char//count_r3)
    else:
        r3 = 0
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == '__main__':
    main()
