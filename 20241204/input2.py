file=open("input2")
sorok=file.readlines()
file.close()

print(sorok)

sor=sorok[0]
print(sor)
feldarabolt_sor=sor.split(";")
print(feldarabolt_sor)

szamlista=[]
for i in range(len(feldarabolt_sor)):
    szam=int(feldarabolt_sor[i])
    szamlista.append(szam)
print(szamlista)

s=0
for i in range(len(szamlista)):
    s+=szamlista[i]
print(f"összeg: {s}")