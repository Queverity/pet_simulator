# CB 1st File Managment Functions

import csv
from helper import *
def parse_accounts():
    # open the file so it will close automatically once we are done with it
    with open("Documents/pet_accounts.csv",mode="r",newline="") as pets:
        # used for creating dictionaries
        fieldnames = ['owner','name','species','age','level','xp','hunger','happiness','energy','cleanliness','health','day','time','money','level','xp','agility','obedience','tracking','agility_progress','obedience_progress','tracking_progress','bed','toy','food','brush']


        reader = csv.DictReader(pets,fieldnames)

        pet_accounts = []

        for i in reader:
            # iterate through the csv file, adding pet accounts to list as it goes. if owner is set to 'owner', that means it is the first line and should not be written to active save data
            if i['owner'] == 'owner':
                pass
            else:
                pet_accounts.append(i)

        return pet_accounts


def save_accounts(pet_accounts):
    with open("Documents/pet_accounts.csv",mode="w",newline="") as pets:
        # used for writing dictionaries
        fieldnames = ['owner','name','species','age','level','xp','hunger','happiness','energy','cleanliness','health','day','time','money','level','xp','agility','obedience','tracking','agility_progress','obedience_progress','tracking_progress','bed','toy','food','brush']
        dict_writer = csv.DictWriter(pets,fieldnames)
        writer = csv.writer(pets)


        writer.writerow(fieldnames)

        # iterate through pet accounts and write each dictionary to csv
        for i in pet_accounts:
            dict_writer.writerow(i)

def add_pet(new_pet):
    with open("Documents/pet_accounts.csv",mode="a",newline="") as pets:
        fieldnames = ['owner','name','species','age','level','xp','hunger','happiness','energy','cleanliness','health','day','time','money','level','xp','agility','obedience','tracking','agility_progress','obedience_progress','tracking_progress','bed','toy','food','brush']
        writer = csv.DictWriter(pets,fieldnames)

        # pretty simple here, just write pet object to csv file as a dictionary
        writer.writerow(vars(new_pet))

def remove_pet(pet_accounts,pet_name):
    with open("Documents/pet_accounts.csv",mode="w",newline="") as pets:
        fieldnames = ['owner','name','species','age','level','xp','hunger','happiness','energy','cleanliness','health','day','time','money','level','xp','agility','obedience','tracking','agility_progress','obedience_progress','tracking_progress','bed','toy','food','brush']
        dict_writer = csv.DictWriter(pets,fieldnames)
        writer = csv.writer(pets)
        
        # to remove pet from pet accounts, first see if the names are equal. If they are, find the index of that dictionary in the list, then remove the dictionary from the list using that index.
        for i in pet_accounts:
            if i['name'].title() == pet_name.title():
                dict_index = find_dict_index(pet_accounts,'name',pet_name)
                pet_accounts.pop(dict_index)

        # iterate through pet accounts and write dictionaries
        writer.writerow(fieldnames)
        for i in pet_accounts:
            dict_writer.writerow(i)