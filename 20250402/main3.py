filename="input3.txt"

def beolvasas(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

    #print(sorok)

    adatok=[]
    for i in range(len(sorok)):
        elem=sorok[i].strip()
        #print(elem, type(elem))
        lista=elem.split(" ")
        #print(lista)
        szamok=[]
        for j in range(len(lista)):
            szam=int(lista[j])
            szamok.append(szam)
        #print(szamok)
        adatok.append(szamok)
    #print(adatok)
    return adatok

x=beolvasas(filename)
print(x)