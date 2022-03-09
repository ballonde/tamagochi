from unicodedata import name
import random

class Tamagochi:
    def __init__(self,name,pv,humeur):
        self.nom=name
        self.vie=pv
        self.humeur=humeur
    
    def getName(self):
        return self.nom
    
    def getVie(self):
        return self.vie
    
    def getHumeur(self):
        return self.humeur

class Chat(Tamagochi):
    def __init__(self,name,pv,humeur):
        Tamagochi.__init__(self,name,pv,humeur)
        self.espece="chat"
        
    def griffe(self):
        print(self.nom+" vous a griffé!")
    
    def getEspece(self):
        return self.espece


class Poulet(Tamagochi):
    def __init__(self,name,pv,humeur):
        Tamagochi.__init__(self,name,pv,humeur)
        self.espece="poulet"
        
    def ultralaser(self):
        print(self.nom+" lance un ultralaser!")

    def getEspece(self):
        return self.espece

class OrangOutan(Tamagochi):
    def __init__(self,name,pv,humeur):
        Tamagochi.__init__(self,name,pv,humeur)
        self.espece="OrangOutan"
        
    def Hadoken(self):
        print(self.nom+" concentre son énergie et lance un Hadoken!")
    
    def Danse(self):
        print(self.nom+" danse la Salsa!")
    
    def getEspece(self):
        return self.espece

tabEspece=["Chat","Poulet","OrangOutan"]
print("Vous allez recevoir aléatoirement un animal!")
espece=tabEspece[random.randint(0,3)]

print("Vous avez obtenue un ",espece,"! Quel est son nom?")
nom=input()
if (espece=="Chat"):
    animal=Chat(nom,100,100)
if (espece=="Poulet"):
    animal=Poulet(nom,100,100)
if (espece=="OrangOutan"):
    animal=OrangOutan(nom,100,100)

print("Vous avez",animal.getName(),"un",animal.getEspece(),".")

while(animal.getVie>0):
    if (animal.getEspece()==Chat):
        print("Les action disponible pour votre animal: 1-Griffer")

