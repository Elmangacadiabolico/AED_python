def main():
    m=open('entrada_1.txt', 'rt')
    texto = m.read()
    r1=r2=r3=r4=0
    Cont_numero = Cont_palab_numer=0
    palabra = ""
    E_palabra= E_ex = Hay_numero= E_te=False

    for i in texto:
        if i not in ' .':
            E_palabra = True
            palabra += i
            #r1
            if not E_ex:
                E_ex = True
            #3
            if not Hay_numero:
                if numeros_e(i):
                    Hay_numero = True
            #r4 necesito que exista el "te"


        else:
            if E_palabra:
                #r1
                if E_ex:
                    if len(palabra)>2:
                        if palabra[1] in 'x':
                            r1 +=1
                            print(palabra)
                #r2
                if len(palabra)> r2:
                    r2 = len(palabra)
                #r3
                if Hay_numero:
                    Cont_palab_numer +=1
                    Cont_numero +=len(palabra)
                #r4
                if 'te' in palabra.lower():
                    r4+=1
            palabra=""
            E_te =Hay_numero=E_ex = E_palabra = False

    if Cont_palab_numer > 0:
        r3 = Cont_numero // Cont_palab_numer
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
def numeros_e(i):
    if i in '0123456789':
        return True
    return False


if __name__== '__main__':
    main()