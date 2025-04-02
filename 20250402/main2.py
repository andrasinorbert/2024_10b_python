filename="input2.txt"

def beolvasas(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

    #print(sorok)

    szamok=[]
    for i in range(len(sorok)):
        elem=sorok[i].strip()
        #print(elem, type(elem))
        szam=int(elem)
        #print(szam, type(szam))
        szamok.append(szam)
    #print(szamok)
    return szamok

x=beolvasas(filename)
print(x)