class Adat:
    def __init__(self, nev:str, szamok:list[int]):
        self.nev=nev
        self.szamok=szamok
        
    def __str__(self):
        return f"{self.nev} {self.szamok}"
    
    def getName(self)->str:
        return self.nev
    
    def getSzamok(self)->list[int]:
        return self.szamok
    
    def osszeg(self)->int:
        """A számok összegét adja vissza
        """
        return sum(self.szamok)
    
class AdatLista:
    def __init__(self):
        self.lista=[]
        
    def append(self,element:int):
        """Egy elemet hozzáad a listához"""
        self.lista.append(element)
        
    def getNameByIndex(self, index:int)->str:
        """Az indexedik elem nevével tér vissza"""
        return self.lista[index].getName()
        
    def len(self)->int:
        return len(self.lista)
    
    def getElementByIndex(self, index:int)->Adat:
        """Az indexedik elemet adja vissza"""
        return self.lista[index]
    
    def kereses(self,nev:str)->Adat|None:
        """Rákeres a nev paraméterre, és vissza adja az obj-t
            ha megtalálta, különben None
        """
        i=0
        while i<self.len() and self.getNameByIndex(i)!=nev:
            i+=1
        van=i<self.len()
        if van:
            return self.getElementByIndex(i)
        else:
            return None
        
    def getSzamokByName(self, nev:str)->list[int]|None:
        """A nev paraméterre megadott elem számliatáját adja vissza."""
        keresett=self.kereses(nev)
        if keresett == None:
            return None
        else:
            return keresett.getSzamok()
    
    def getObjBySzamokMax(self):
        """A legnagyobb összegű személy nevét adja vissza"""
        max=self.getElementByIndex(0).osszeg()
        obj=self.getElementByIndex(0)
        for i in range(1,self.len()):
            if self.getElementByIndex(i).osszeg()>max:
                max=self.getElementByIndex(i).osszeg()
                obj=self.getElementByIndex(i)
        return obj
        
    def getNameBySzamokMax(self):
        """A legnagyobb összegű személy nevét adja vissza"""
        return self.getObjBySzamokMax().getName()