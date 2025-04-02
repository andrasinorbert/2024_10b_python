filename="input1.txt"

def adatbeolvasas(filename):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    
    elem=sorok[0].split(" ")
    #print(elem)
    szamok=[]
    for i in range(len(elem)):
        szam=int(elem[i])
        szamok.append(szam)
    #print(szamok)
    return szamok

x=adatbeolvasas(filename)
print(x)