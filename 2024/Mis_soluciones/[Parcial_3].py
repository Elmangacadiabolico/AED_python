def mayuscula(i):
    return 'A' <= i <= 'Z'
def longitud(palabra,r2):
    if 'p' in palabra.lower() or 'n'in palabra.lower():
        if len(palabra) > r2:
            r2 = len(palabra)
    return r2

def Es_vocal (i):
    if i == i.lower() and i in 'aeiou':
        return True
    return False
def Es_numero(i):
    if  i in'0123456789':
        return True
    return False
def main ():
    m = open('entrada_1.txt', 'rt')
    texto = m.read()
    m.close()
    r1=r2=r3=r4=0
    cout_palabra_numero= total_pala_num=count_palabras = 0
    Palabra = ''
    E_palabra=Letra_vocal= letra_con_num = False
    texto +=''
    for i in texto:
        if i not in ' .':
            E_palabra = True
            Palabra += i


            #r3
            if Es_vocal(i):
                Letra_vocal = True
            if Es_numero (i):
                letra_con_num = True
                cout_palabra_numero += 1
        else:
            #r1
            #PES24" Civ5
            #01234  0123
            if E_palabra:
                count_palabras += 1
                #r1
                if mayuscula(Palabra[0]):
                    if len(Palabra) > 3 and Es_numero(Palabra[3]):
                        r1 += 1
                #r2
                r2 = longitud(Palabra,r2)
                #r3
                if letra_con_num and Letra_vocal and cout_palabra_numero > 2:
                    total_pala_num += len(Palabra)
                    print(total_pala_num)
                #r4
                if Palabra[0] in 'aeiouAEIOU':
                    if 'fa' in Palabra:
                        r4 += 1
            Palabra = ''
            E_palabra =letra_con_num=Letra_vocal= False
            cout_palabra_numero = 0

    r3 = total_pala_num//count_palabras
    print(texto)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    main()