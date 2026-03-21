# CB 1st File Managment Functions

import csv
from helper import *
def parse_accounts():
    with open("Documents/pet_accounts.csv",mode="r",newline="") as pets:
        fieldnames = ['owner','name','species','age','level','xp','hunger','happiness','energy','cleanliness','health','day','time','money','level','xp','agility','obedience','tracking','agility_progress','obedience_progress','tracking_progress','bed','toy','food','brush']
        reader = csv.DictReader(pets,fieldnames)

        pet_accounts = []

        for i in reader:
            if i['owner'] == 'owner':
                pass
            else:
                pet_accounts.append(i)

        return pet_accounts


def save_accounts(pet_accounts):
    with open("Documents/pet_accounts.csv",mode="w",newline="") as pets:
        fieldnames = ['owner','name','species','age','level','xp','hunger','happiness','energy','cleanliness','health','day','time','money','level','xp','agility','obedience','tracking','agility_progress','obedience_progress','tracking_progress','bed','toy','food','brush']
        dict_writer = csv.DictWriter(pets,fieldnames)
        writer = csv.writer(pets)


        writer.writerow(fieldnames)

        for i in pet_accounts:
            dict_writer.writerow(i)

def add_pet(new_pet):
    with open("Documents/pet_accounts.csv",mode="a",newline="") as pets:
        fieldnames = ['owner','name','species','age','level','xp','hunger','happiness','energy','cleanliness','health','day','time','money','level','xp','agility','obedience','tracking','agility_progress','obedience_progress','tracking_progress','bed','toy','food','brush']
        writer = csv.DictWriter(pets,fieldnames)

        writer.writerow(vars(new_pet))

def remove_pet(pet_accounts,pet_name):
    with open("Documents/pet_accounts.csv",mode="w",newline="") as pets:
        fieldnames = ['owner','name','species','age','level','xp','hunger','happiness','energy','cleanliness','health','day','time','money','level','xp','agility','obedience','tracking','agility_progress','obedience_progress','tracking_progress','bed','toy','food','brush']
        dict_writer = csv.DictWriter(pets,fieldnames)
        writer = csv.writer(pets)
        
        for i in pet_accounts:
            if i['name'].title() == pet_name.title():
                dict_index = find_dict_index(pet_accounts,'name',pet_name)
                pet_accounts.pop(dict_index)

        writer.writerow(fieldnames)
        for i in pet_accounts:
            dict_writer.writerow(i)