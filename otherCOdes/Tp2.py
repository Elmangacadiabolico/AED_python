m = open('tratamientos.txt')
line = m.readline()

def Proccess_of_line(a):
    name = line[0:25]
    lcd1O=line[25:30]
    monto=int(line[31:39])
    if len(line)== 40:
        alta_comp=line[39]
    else:
         alta_comp= line  is "N"
    alta_comp=[39]

    return name,lcd1O,monto,alta_comp
def Caracter_especial():
    if int(line[25:30])==0:
        monto_AL,monto_Mz,monto_U = line[2:8],line[8:14],line[14:20]


for line in m:
    if line[-1] in '\n':
        line=line[:-1]
    if line in '#':
        Caracter_especial()
    print(line)