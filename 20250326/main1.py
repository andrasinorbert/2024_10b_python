filename="input1.txt"

f=open(filename, encoding="utf-8")
sorok=f.readlines()
f.close()

print(sorok)
adat=sorok[0]
print(f"({adat})")
# adat tisztítás
"s z i a"
lista=adat.split(" ") # szóközönkénti felbontás
print(lista)
"""
szamok=[]
for i in range(len(lista)):
    listaelem=lista[i]
    szam=int(listaelem)
    szamok.append(szam)
print(szamok)
"""
"""
# rövidebben
szamok=[]
for i in range(len(lista)):
    szam=int(lista[i])
    szamok.append(szam)
print(szamok)
"""
# még rövidebben
szamok=[]
for i in range(len(lista)):
    szamok.append(int(lista[i]))
print(szamok)