from adatsor import *
from file_feldolgozas import *

sorok=beolvas("input")
adatok=adat_feldolgozas(sorok)

for adat in adatok.lista:
    print(adat)

print(f"Eszter összesen {adatok.kereses("Eszter").osszeg()} kókuszgolyót készített")

print(f"Aki a legtöbb kókuszgolyót gyártotta a héten: {adatok.getNameBySzamokMax()}")