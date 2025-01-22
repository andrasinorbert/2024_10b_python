from adatsor import *

def beolvas(filename:str):
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    return sorok

def adat_feldolgozas(sorok:list[str]):
    adatok=AdatLista()
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