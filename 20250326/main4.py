
def beolvas(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    matrix=[]
    nevek=[]
    for i in range(len(sorok)):
        szokozonkentifelbontas=sorok[i].strip().split(" ")
        nev=szokozonkentifelbontas[0]
        szamlista=szokozonkentifelbontas[1:]
        szamok=[]
        for j in range(len(szamlista)):
            szamok.append(int(szamlista[j]))
        matrix.append(szamok)
        nevek.append(nev)
    return nevek,matrix

filename="input4.txt"
nevek,szamok=beolvas(filename)
print(nevek)
print(szamok)