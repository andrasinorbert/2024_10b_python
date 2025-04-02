filename="input4.txt"

def beolvasas(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

    #print(sorok)
    nevek=[]
    adatok=[]
    for i in range(len(sorok)):
        elem=sorok[i].strip()
        #print(elem, type(elem))
        lista=elem.split(" ")
        #print(lista)
        szamok=[]
        for j in range(1,len(lista)):
            szam=int(lista[j])
            szamok.append(szam)
        #print(szamok)
        adatok.append(szamok)
        nevek.append(lista[0])
    #print(adatok)
    return nevek,adatok

x,y=beolvasas(filename)
print(x)
print(y)