print("szoveg")
print("a", "b", "c")

print("a", "b", "c", sep="; ")
print("a", "b", "c", sep="HAHO")
print("a", "b", "c", sep="\n")

print("Szia", end=" ")
print("Zoli")

for i in range(5): # end 
    print(i, end=" ") # 0 1 2 3 4
print()
for i in range(2,5): # start end 
    print(i, end=" ") # 2 3 4
print()
for i in range(2,15,2): # start end step
    print(i, end=" ") # 2 4 6 8 10 12 14
print()

l=[1,2,3,4,5]
s=0
for i in range(len(l)): # len: l-nek hány eleme van
    s+=l[i]
print(s)

def osszeg(lista):
    s=0
    for i in range(len(lista)):
        s+=lista[i]
    return s
l2=[3,4,5]
listaosszeg=osszeg(l2)
print(listaosszeg)

listaosszeg=osszeg([4,5,6])
print(listaosszeg)

print(osszeg([5,6,7]))

l3=[2,7,6,4,5]
maxertek=l3[0]
maxindex=0
for i in range(1,len(l3)):
    if maxertek<l3[i]:
        maxertek=l3[i]
        maxindex=i
print(f"érték: {maxertek}; index: {maxindex}")

def maxkiv(lista):
    maxertek=lista[0]
    maxindex=0
    for i in range(1,len(lista)):
        if maxertek<lista[i]:
            maxertek=lista[i]
            maxindex=i
    return (maxertek, maxindex)

print(maxkiv(l3))

"""
def osszeg(lista):
    s=0
    for i in range(len(lista)):
        s+=lista[i]
    return s
"""

def szorzat(lista):
    s=1
    for i in range(len(lista)):
        s*=lista[i]
    return s
print(szorzat([1,2,3,4,5]))
