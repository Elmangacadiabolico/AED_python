def vocales(u):
    if u in'aeiou' and u == u.lower():
        return True
    return False
def numeros(i):
    if  i in '0123456789':
        return True
    return False

def E_consonantes(u):
    return u.lower() in "bcdfghjklmnñpqrstvwxyz"

def r2A(palabra,r2):
    if 's' in palabra.lower() or 'c' in palabra.lower():
        if r2 is None or len(palabra) < r2:
            r2 = len(palabra)
        return r2

def main():

    m = open('entrada_1.txt','rt')
    texto = m.read()
    texto +=''
    r1=r3=r4=0
    r2 = None
    E_palabra= Hay_vocales= SoC=False
    palabra=''
    count_v=count_n=count_c=count_p=count_p_nn = 0


    for i in texto:
        if i not in ' .':
            E_palabra = True
            palabra += i
            #r1
            if vocales(i):
                Hay_vocales=True
                count_v += 1
            if numeros(i):
                Hay_numero=True
                count_n += 1
            if E_consonantes(i):
                consonantes=True
                count_c += 1
            if 's' in i.lower() or 'c' in i.lower():
                SoC=True
        else:
            if E_palabra:
                count_p += 1
                #1
                if count_n > count_v and count_c == 1:
                    r1 += 1
                #r2
                r2 = r2A(palabra,r2)
                #r3
                if count_n == 0:
                    count_p_nn += 1
                #r4
                if palabra[0:2] in 'vi':
                    r4 += 1

            count_v = count_n = count_c=0
            E_palabra=Hay_vocales=consonantes =Hay_numero=SoC= False
            palabra = ''
    r3 = (count_p_nn * 100) //count_p
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == '__main__':
    main()