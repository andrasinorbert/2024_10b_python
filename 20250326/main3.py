filename="input3.txt"

f=open(filename, encoding="utf-8")
sorok=f.readlines()
f.close()

print(sorok)
"""
matrix=[]
for i in range(len(sorok)):
    lista=sorok[i].strip()
    print(lista)
    szokozonkentifelbontas=lista.split(" ")
    print(szokozonkentifelbontas)
    szamok=[]
    for j in range(len(szokozonkentifelbontas)):
        szam=int(szokozonkentifelbontas[j])
        szamok.append(szam)
    print(szamok)
    matrix.append(szamok)
print(matrix)
"""

# rövidebben
matrix=[]
for i in range(len(sorok)):
    szokozonkentifelbontas=sorok[i].strip().split(" ")
    szamok=[]
    for j in range(len(szokozonkentifelbontas)):
        szamok.append(int(szokozonkentifelbontas[j]))
    matrix.append(szamok)
print(matrix)

def beolvas(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    matrix=[]
    for i in range(len(sorok)):
        szokozonkentifelbontas=sorok[i].strip().split(" ")
        szamok=[]
        for j in range(len(szokozonkentifelbontas)):
            szamok.append(int(szokozonkentifelbontas[j]))
        matrix.append(szamok)
    return matrix

filename="input3.txt"
x=beolvas(filename)
print(x)


def beolvas_rovidebben(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    matrix=[]
    for i in range(len(sorok)):
        szokozonkentifelbontas=sorok[i].strip().split(" ")
        szamok=[int(szokozonkentifelbontas[j]) for j in range(len(szokozonkentifelbontas))]
        matrix.append(szamok)
    return matrix

filename="input3.txt"
y=beolvas_rovidebben(filename)
print(y)