def Letras_minusculas(i):
    if i  == i.lower() and i not in '0123456789':
        return True
    return False
def Es_impar(i):
    if i in '13579':
        return True
    return False


def main():
    m = open('entrada (3).txt', 'rt')
    texto = m.read()
    r1=r2=r3=r4 = 0
    contador_letras= count_im = position= 0
    palabra= ""
    E_palabra= Hay_numero_im = letras_min = False
    valid = True
    for i in texto:
        if i not in ' .':
            if not E_palabra:
                E_palabra = True
                #empieza una palabra
                palabra += i
            if not Hay_numero_im:
                if Es_impar(i):
                    Hay_numero_im = True
            if not letras_min:
                if Letras_minusculas(i):
                    letras_min = True



        else:
            if E_palabra:
                pass

            E_palabra= Hay_numero_im=letras_min = False





    print(texto)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == '__main__':
    main()