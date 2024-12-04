file=open("input1")
sorok=file.readlines()
file.close()

print(sorok)

szamlista=[]

for i in range(len(sorok)):
    sor=sorok[i]
    felesleg_nelkuli_sor=sor.strip()
    print(felesleg_nelkuli_sor)
    szam=int(felesleg_nelkuli_sor)
    szamlista.append(szam)
print(szamlista)

s=0
for i in range(len(szamlista)):
    s+=szamlista[i]
print(f"összeg: {s}")