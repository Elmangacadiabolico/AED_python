def main():
    m = open('entrada.txt', 'rt')
    texto = m.read()
    r1=r2=r3=r4=0
    Contador_palabras=long_par =cant_vocale=cant_consonant= count_Ra= couT_r3= count_r3=0
    palabra= ""
    E_vocal =E_palabra=Ex_Numer= E_palabla_S =False
    Not_Exi_pP = True
    for i in texto:
        if i not in ' .':
            #r1
            E_palabra = True
            palabra += i

            if Es_vocal(i):
                E_vocal = True
                cant_vocale +=1
            else:
                cant_consonant +=1
            #r2
            if i  in 'pP':
                Not_Exi_pP = False
            if i in '0123456789':
                Ex_Numer = True
            #r3
            if i.lower() in 's':
                E_palabla_S = True
           #r4
            if palabra.lower() in 'ra' :
                if Es_vocal(palabra[0:0]) or Es_vocal(palabra[0:1]):
                    r4+=1

        else:
            #r1
            if E_palabra:
                if len(palabra) % 2 == 0 :
                    if cant_vocale == cant_consonant:
                        r1 += 1
                #r2
                if  Not_Exi_pP and Ex_Numer:
                    if len(palabra) > r2:
                        r2 = len(palabra)
                #r3
                if len(palabra) > 2 and E_palabla_S:
                    count_r3 += 1
                    couT_r3 += len(palabra)

            Contador_palabras =  0
            palabra = ""
            cant_vocale = 0
            cant_consonant = 0
            E_palabra=Ex_Numer =E_palabla_S= False
            Not_Exi_pP = True


    r3 = (couT_r3//count_r3)
    print(texto)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
def Es_vocal(i):
    if i.lower() in 'aeiou':
        return True
    return False

if __name__ == '__main__':
   main()