from soporte import *
def medio(v):
    x = 0
    for i in range(len(v)):
        x += v[i]
    else:
        x = round(x/len(v), 2)
    return x

def ord(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1,n):
            if v[i] > v[j]:
                v[i],v[j] = v[j],v[i]

def mediano(v):
    n = len(v)
    x = 0
    ord(v)
    if n % 2 != 0:
        c = v[n // 2]
    else:
        c = (v[n//2 -1] + v[n//2]) / 2
    return round(c,2)
def obtener_moda(v):
    n = len(v)
    c = [0] * n
    for i in range(n):
        c[v[i]] += 1
    idm = 0
    cfm = 1
    for j in range(n):
        if c[j] > c[idm]:
            idm = j
            cfm = 1
        elif c[j] == c[idm]:
            cfm += 1
    if cfm == 1:
        return idm
    else:
        return None


def main():
    v = vector_known_range(3000)
    print(medio(v))
    print(mediano(v))
    print(obtener_moda(v))


if __name__ == '__main__':
    main()