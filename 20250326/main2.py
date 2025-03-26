filename="input2.txt"
f=open(filename, encoding="utf-8")
sorok=f.readlines()
f.close()

print(sorok)
"""
szamok=[]
for i in range(len(sorok)):
    listaelem=sorok[i]
    sorvegjelnelkul=listaelem.strip() # \n eltüntetése
    print(sorvegjelnelkul)
    szam=int(sorvegjelnelkul)
    szamok.append(szam)
print(szamok)
"""
"""
# rövidebben
szamok=[]
for i in range(len(sorok)):
    sorvegjelnelkul=sorok[i].strip() # \n eltüntetése
    szam=int(sorvegjelnelkul)
    szamok.append(szam)
print(szamok)
"""
"""
# még rövidebben
szamok=[]
for i in range(len(sorok)):
    szam=int(sorok[i].strip())
    szamok.append(szam)
print(szamok)
"""

# annál is rövidebben
szamok=[]
for i in range(len(sorok)):
    szamok.append(int(sorok[i].strip()))
print(szamok)