# CB 1st File Managment Functions

import csv

def parse_accounts():
    with open("Documents//pet_accounts.csv",mode="r",newline="") as pets:
        fieldnames = ['owner','name','species','age','hunger','energy','cleanliness','health','day','time','money','agility','obedience','tracking','agility_progress','obedience_progress','tracking_progress','bed','toy','food','brush']
        reader = csv.DictReader(pets,fieldnames)

        pet_accounts = []

        for i in reader:
            pet_accounts.append(i)

        return pet_accounts


def save_accounts(pet_accounts):
    with open("Documents//pet_accounts.csv",mode="w",newline="") as pets:
        fieldnames = ['owner','name','species','age','hunger','energy','cleanliness','health','day','time','money','agility','obedience','tracking']
        writer = csv.DictWriter(pets,fieldnames)

        writer.writerow(fieldnames)

        for i in pet_accounts:
            writer.writerow(i)

def add_pet(new_pet):
    with open("Documents//pet_accounts.csv",mode="a",newline="") as pets:
        fieldnames = ['owner','name','species','age','hunger','happiness','energy','cleanliness','health','day','time','money']
        writer = csv.DictWriter(pets,fieldnames)

        writer.writerow(vars(new_pet))

def remove_pet(pet_name):
    pass

