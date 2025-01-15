from fuggvenyek import *

fajlnev="input2.txt"
f=beolvas(fajlnev)
szamok=feldolgoz(f, " ")
print(szamok)
szamlista=[]
for i in range(len(szamok)):
    szamlista.append(szamok[i][0])
print(szamlista)
osszeg=osszegzes(szamlista)
print(osszeg)