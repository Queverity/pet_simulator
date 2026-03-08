import csv

class Pet:
    def __init__(self,owner,name,species,age,hunger,energy,cleanliness,health):
        self.owner = owner
        self.name = name
        self.species = species
        self.age = age
        self.hunger = hunger
        self.energy = energy
        self.cleanliness = cleanliness
        self.health = health

    
pet = Pet("Dave","Buddy","Dog",0,80,80,80,100)

for k,v in vars(pet).items():
    print(f"{k.capitalize()}: {v}")

with open("Documents//pet_accounts.csv",mode="a",newline="") as pets:
    fieldnames = ['owner','name','species','age','hunger','energy','cleanliness','health']

    writer = csv.DictWriter(pets,fieldnames)

    writer.writerow(vars(pet))
