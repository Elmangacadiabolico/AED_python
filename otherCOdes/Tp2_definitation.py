m = open('tratamientos.txt')
r1 = r2 = r3 = r4 = r5 = r6 = 0

suma_st = 0
st_pacientes = 0
monto_total = 0
r8 = ""
r9 = None
tratamiento_X = 0
Xmayor_promedio = 0
def Process_of_line(line):
    nombre = line[0:25].strip()
    codigo = line[25:31].strip()
    monto_base = int(line[31:39])
    if len(line) > 39:
        alta_comp = line[39]
    else:
        alta_comp = "N"

    return nombre, codigo, monto_base, alta_comp
def Caracter_especial(line):
    monto_AL = int(line[2:8])
    monto_MZ = int(line[8:14])
    monto_U = int(line[14:20])

    return monto_AL, monto_MZ, monto_U


def Calcular_monto(letra, porcentaje,
    monto_base,monto_AL,monto_MZ,monto_U):
    if letra in "ABCDEFGHIJKL":
        monto = monto_base + monto_AL
    elif letra in "MNOPQRSTVWXYZ":
        monto = monto_base + monto_MZ
    else:
        monto = monto_base + monto_U
    porcentaje = int(porcentaje)
    monto = monto + (monto * porcentaje / 100)

    return monto


for line in m:
    if line[-1] == '\n':
        line = line[:-1]
    if line[0] == "#":

        monto_AL, monto_MZ, monto_U = Caracter_especial(line)
    else:
        nombre, codigo, monto_base, alta_comp = Process_of_line(line)
        letra = codigo[0]
        porcentaje = codigo[4:6]
        monto_final = Calcular_monto(
        letra,porcentaje,monto_base,monto_AL,monto_MZ,monto_U)
        r1 += 1
        monto_total += monto_final
        if letra == "A":
            r2 += 1
        elif letra == "B":
            r3 += 1
        elif letra == "C":
            r4 += 1
        elif letra == "E":
            r5 += 1
        elif letra == "P":
            r6 += 1
        if letra == "S" or letra == "T":
            suma_st += monto_final
            st_pacientes += 1
        if (r9 is None or monto_final > r9) and letra != "U":
            r9 = monto_final
            r8 = nombre
        if alta_comp == "X":
            tratamiento_X += 1
promedio_total = monto_total / r1
#m.close()
m = open('tratamientos.txt')
for line in m:
    if line[-1] == '\n':
        line = line[:-1]
    if line[0] == "#":
        monto_AL, monto_MZ, monto_U = Caracter_especial(line)
    else:
        nombre, codigo, monto_base, alta_comp = Process_of_line(line)
        if alta_comp == "X":
            letra = codigo[0]
            porcentaje = codigo[4:6]
            monto_final = Calcular_monto(
                letra,porcentaje,monto_base,monto_AL,monto_MZ,monto_U)
            if monto_final > promedio_total:
                Xmayor_promedio += 1


if st_pacientes > 0:
    r7 = round(suma_st / st_pacientes, 2)
else:
    r7 = 0
if tratamiento_X > 0:
    r10 = round((Xmayor_promedio * 100) / tratamiento_X, 2)
else:
    r10 = 0


print("(r1) Cantidad de tratamientos cargados:", r1)
print("(r2) Cantidad de tratamientos A:", r2)
print("(r3) Cantidad de tratamientos B:", r3)
print("(r4) Cantidad de tratamientos C:", r4)
print("(r5) Cantidad de tratamientos E:", r5)
print("(r6) Cantidad de tratamientos P:", r6)
print("(r7) Importe final promedio (S y T):", r7)
print("(r8) Paciente que más pagó (no U):", r8)
print("(r9) Mayor importe pagado:", round(r9, 2))
print("(r10) Porcentaje de tratamientos X sobre promedio:", r10)

m.close()