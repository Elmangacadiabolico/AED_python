def Not_vocales(i):
    if i.lower() not in 'aeiou'and i == i.lower() and i not in '0123456789':
        return True
    return False
def numeros_e(i):
    if i in '0123456789':
        return True
    return False
def Calcular_menor(palabra,r2):
    if r2 == 0:
        r2 = len(palabra)
    else:
        if r2 > len(palabra):
            r2 = len(palabra)
    return r2
def vocales(i):
    if i in 'aeiou':
        return True
    return False
def main():
    m = open('entrada_1.txt', 'rt')
    texto = m.read()
    r1=r2=r3=r4 = 0
    count_vo= Contador_palabras_vo = Total_Pala_vo = 0
    E_palabra=E_numero = E_vocal  = False
    palabra = ''
    for i in texto:
        if i not in ' .':

            E_palabra = True
            palabra += i
            #r1 SALU4
            if numeros_e(i):
                E_numero = True
               #01234
            #r3
            if vocales(i):
                E_vocal = True
                count_vo += 1
            #r4

        else:
            if E_palabra:
                Total_Pala_vo += 1
                if E_numero:
                    #r1
                    if  len(palabra) > 2 and Not_vocales(palabra[2]) or len(palabra) > 3 and Not_vocales(palabra[3]):
                        r1 += 1
                    #r2
                if palabra[0] in 's':
                        r2 = Calcular_menor(palabra,r2)
                #r3
                if E_vocal:
                    if count_vo >= 2:
                        Contador_palabras_vo +=1
                    #r4
                if 'ni' in palabra.lower():
                    r4 += 1

                E_palabra=E_numero=E_vocal = False
                palabra = ""
                count_vo = 0
                #r3
    if Total_Pala_vo> 0 :
        r3 = (Contador_palabras_vo*100)//Total_Pala_vo
    print(texto)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == '__main__':
    main()