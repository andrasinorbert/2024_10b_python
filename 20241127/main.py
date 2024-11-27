def osszeg(lista):
    s=lista[0]
    for i in range(1,len(lista)):
        s=s+lista[i]
    return s

def szorzat(lista):
    s=lista[0]
    for i in range(1,len(lista)):
        s=s*lista[i]
    return s

print(osszeg([1,2,3,4,5]))
print(szorzat([1,2,3,4,5]))

def osszegzes(lista,f):
    s=lista[0]
    for i in range(1,len(lista)):
        s=f(s,lista[i])
    return s

def osszead(num1, num2):
    return num1+num2

def szorzas(num1, num2):
    return num1*num2

print(osszegzes([1,2,3,4,5], osszead))
print(osszegzes([1,2,3,4,5], szorzas))

szorzat=lambda num1, num2: num1*num2

print(szorzat(3,4))
print((lambda num1, num2: num1*num2)(3,4))
print(osszegzes([1,2,3,4,5], lambda num1, num2: num1*num2))

lista=[]
for i in range(10):
    lista.append(i)
print(lista)

# list comprehension
lista=[]
[lista.append(i) for i in range(10)]
print(lista)

x=10
if x>5:
    y=1
else:
    y=0
y=1 if x>5 else 0
print(y)