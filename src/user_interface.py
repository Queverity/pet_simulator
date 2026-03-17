# CB 1st User Interface Functions

from pet_creation import *
from helper import *
from saving_parsing import *


# define function pet_interaction(pet_object):
    # give user various options of what to do with their pet
    # actions like feed, play, sleep, clean, train, view status, save, load , and quit
    # After certain actions, use pass_time function. When the pet sleeps, make sure mode is set to False so hunger is not automatically adjusted by the pass time function
    # when user chooses to save their game, go through the pet_accounts, pet_inventory, and pet_skills and make sure to update the values for the changed pet
    # when user chooses to load a different game, remind them that if they don't save their current game, all progress will be lost

def pet_interaction(pet_object):
    pass

def main_menu():


    print("This is a pet simulator game! In it, you can take care of a pet by keeping track of their attributes, such as hunger, happiness, and cleanliness. Current work in progress features are a shop, skill competitions, and possibly pet breeding.")

    while True:
        print("What would you like to do?\n1. Create New Pet\n2. Load Pet\n3. Exit")
        choice = input("Enter number:\n").strip()

        match choice:
            case "1":
                pet_object = create_pet(avaiable_species)
                pet_interaction()
            case "2":
                # make something to read the pet_accounts file and list all of the pet names with basic details on each pet
                pass
            case "3":
                print("Goodbye!")
                break
