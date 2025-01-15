def beolvas(filename:str):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    return sorok

def adat_feldolgozas(sorok:list[str]):
    adatok=[]
    for sor in sorok:
        sor=sor.strip()
        sor_lista=sor.split(" ")
        nev=sor_lista[0]
        szamok=[]
        for i in range(1,len(sor_lista)):
            szamok.append(int(sor_lista[i]))
        obj=Adat(nev,szamok)
        adatok.append(obj)
    return adatok

class Adat:
    def __init__(self, nev, szamok):
        self.nev=nev
        self.szamok=szamok
        
    def __str__(self):
        return f"{self.nev} {self.szamok}"
    
    def osszeg(self):
        return sum(self.szamok)
    
class AdatLista:
    def __init__(self):
        self.lista=[]
    
    def kereses(self, nev):
        i=0
        while i<len(self.lista) and self.lista[i].nev!=nev:
            i+=1
        van=i<len(self.lista)
        if van:
            return self.lista[i]
        else:
            return None
        
sorok=beolvas("input")
adatok=adat_feldolgozas(sorok)
# print(adatok) memóriacímet ír ki

for adat in adatok:
    print(adat.nev, adat.szamok)
for adat in adatok:
    print(adat)

for adat in adatok:
    if adat.nev=="Eszter":
        print(adat.osszeg())