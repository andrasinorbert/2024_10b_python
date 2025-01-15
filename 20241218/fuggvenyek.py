def beolvas(filename:str, elorolkihagy:int=0, vegerolkihagy:int=0):
    f=open(filename)
    sorok=f.readlines()
    f.close()
    return sorok[elorolkihagy:len(sorok)-vegerolkihagy]


def feldolgoz(lista:list[str], elvalasztoChar:str):
    matrix=[]
    for i in range(len(lista)):
        sor=lista[i].strip().split(elvalasztoChar)
        print(sor)
        szamlista=[]
        for j in range(len(sor)):
            szamlista.append(int(sor[j]))
        print(szamlista)
        matrix.append(szamlista)
    return matrix

def osszegzes(lista:list[int]):
    s=0
    for i in range(len(lista)):
        s+=lista[i]
    return s

def matrix_osszegzes(m:list[list[int]]):
    s=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            s+=m[i][j]
    return s