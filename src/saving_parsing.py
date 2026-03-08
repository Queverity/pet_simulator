# CB 1st File Managment Functions

import csv

def parse_accounts():
    with open("Documents//pet_accounts.csv",mode="r",newline="") as pets:
        fieldnames = ['owner','name','species','age','hunger','energy','cleanliness','health','day','time','money']
        reader = csv.DictReader(pets,fieldnames)

        pet_accounts = []

        for i in reader:
            pet_accounts.append(i)

        return pet_accounts

def parse_skills():
    with open("Documents//pet_skills.csv",mode="r",newline="") as skills:
        fieldnames = ['name','running','jumping','swimming']
        reader = csv.DictReader(skills,fieldnames)

        pet_skills = []

        for i in reader:
            pet_skills.append(i)

        return pet_skills

def parse_inventories():
    with open("Documents//pet_inventories.csv",mode="r",newline="") as skills:
        fieldnames = ['name','toy','bed']
        reader = csv.DictReader(skills,fieldnames)

        pet_inventories = []

        for i in reader:
            pet_inventories.append(i)

        return pet_inventories







def save_accounts(pet_accounts):
    with open("Documents//pet_accounts.csv",mode="w",newline="") as pets:
        fieldnames = ['owner','name','species','age','hunger','energy','cleanliness','health','day','time','money']
        writer = csv.DictWriter(pets,fieldnames)

        writer.writerow(fieldnames)

        for i in pet_accounts:
            writer.writerow(i)

def save_skills(pet_skills):
    with open("Documents//pet_skills.csv",mode="w",newline="") as skills:
        fieldnames = ['name','running','jumping','swimming']
        writer = csv.DictWriter(skills,fieldnames)

        writer.writerow(fieldnames)

        for i in pet_skills:
            writer.writerow(i)

def save_inventories(pet_inventories):
    with open("Documents//pet_inventories.csv",mode="w",newline="") as inventories:
        fieldnames = ['name','toy','bed']
        writer = csv.DictWriter(inventories,fieldnames)

        writer.writerow(fieldnames)

        for i in pet_inventories:
            writer.writerow(i)

def add_pet(new_pet):
    with open("Documents//pet_accounts.csv",mode="a",newline="") as pets:
        fieldnames = ['owner','name','species','age','hunger','happiness','energy','cleanliness','health','day','time','money']
        writer = csv.DictWriter(pets,fieldnames)

        writer.writerow(vars(new_pet))
