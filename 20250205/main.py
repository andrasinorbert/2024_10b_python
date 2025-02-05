from ember import *
        
a=Ember("Béla", 12)
print(a.nev)
print(a.getNev())

a.nev="Tóbiás"
print(a.getNev())
print(a.getKor())
a.setKor(15)
print(a.getKor())
a.eszik()

b=Tanulo("Laci", 13, 123)

print(b.getNev())
print(b.getKor())
print(b.getKretaID())
b.setKor(20)
print(b.getKor())
b.iszik()
b.tanul()

m=Munkas("Józsi", 49, 10000)
print(m.getNev())
print(m.getBer())
m.setBer(m.getBer()-1000)
print(m.getBer())
m.eszik()
m.dolgozik()