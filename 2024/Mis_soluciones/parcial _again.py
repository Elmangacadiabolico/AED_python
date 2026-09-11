def Es_vocales(char):
    if char == char.lower() and char not in 'aeiou' and char not in '0123456789':
        return True
    return False
def Es_numero(char):
    if char in'0123456789':
        return True
    return False

def r2A(palabra,r2):
    if r2 is None:
        r2 = len(palabra)
    else:
        if len(palabra) < r2 :
            r2 = len(palabra)
        return r2
    return r2


def main ():
    r1=r3=r4=0
    r2 = None
    m = open('entrada_1.txt',  'rt')
    texto = m.read()
    E_palabra= E_numeros=E_vocales = False
    Count_palabra=cv= cant_ni= Palabra_total_cv = 0
    palabra = ''


    for char in texto:
        if char not in ' .':
            E_palabra = True
            palabra += char

            if Es_numero(char):
                E_numeros = True

            if Es_vocales(char):
                E_vocales = True
                cv += 1
        else:
            if E_palabra:
                Count_palabra += 1
                #r1
                if E_numeros:
                    if len(palabra) > 2 and Es_vocales(palabra[2]) or len(palabra) > 3 and Es_vocales(palabra[3]):
                        r1 += 1
                #r2
                if palabra[0].lower() in 's':
                    r2 = r2A(palabra,r2)
                #r3
                if Es_vocales:
                    if cv > 2:
                        Palabra_total_cv = len(palabra)
                #r4
                if 'ni' in palabra.lower() and 'NI' in palabra.upper():

                    r4 += 1
            cv = 0
            E_palabra=E_numeros=E_vocales = False
            palabra = ''
            #r3

    if Count_palabra != 0 and Palabra_total_cv:
        r3 = Count_palabra//Palabra_total_cv
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    main()