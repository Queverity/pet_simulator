# CB 1st User Interface Functions

from pet_creation import *
from helper import *
from saving_parsing import *
from competition import competition_menu


# define function pet_interaction(pet_object):
    # give user various options of what to do with their pet
    # actions like feed, play, sleep, clean, train, view status, save, load , and quit
    # After certain actions, use pass_time function. When the pet sleeps, make sure mode is set to False so hunger is not automatically adjusted by the pass time function
    # when user chooses to save their game, go through the pet_accounts, pet_inventory, and pet_skills and make sure to update the values for the changed pet
    # when user chooses to load a different game, remind them that if they don't save their current game, all progress will be lost

# define function display_pets(pet_accounts):
    # use a for loop to iterate through pet accounts and print pet name, level, species, and owner

def pet_interaction(pet_object,pet_accounts):
    # set this at the start so it's easier to call later
    pet = pet_object.name

    while True:
        # display time and day
        print(f"Day {pet_object.day}, {pet_object.time}:00")

        # give user options on what to do
        print(f"What would you like to do with {pet}?\n1. Examine {pet}\n2. Feed {pet}\n3. Play with {pet}\n4. Clean {pet}\n5. Train Pet\n6. Send {pet} to Bed\n7. Save Pet File\n8. Return to Main Menu\n9. Release Pet (CANNOT BE UNDONE)\n10. Go to Pet Item Shop\n11. Compete in Skills")

        choice = input("Enter number:\n").strip()

        clear_screen()

        match choice:
            # If action taken is something that is just viewing the pet or managing save file, only run after_action from helper. If it is actually interaction with the pet, some other actions are taken that are explained in said actions.
            case '1':
                pet_object.view_pet()
                after_action()
                continue
            case '2':
                if pet_object.energy < 5:
                    print("Your pet is too tired to do anything! Have them sleep to reset energy.")
                    continue
                pet_object.feed_pet()
                after_action()
                continue
            case '3':
                if pet_object.energy < 5:
                    print("Your pet is too tired to do anything! Have them sleep to reset energy.")
                    continue
                pet_object.play_with_pet()
                # Pet xp can raise during play, so see if pet has gotten enough xp to level up.
                pet_object.check_level()
                after_action()
                continue
            case '4':
                if pet_object.energy < 5:
                    print("Your pet is too tired to do anything! Have them sleep to reset energy.")
                    continue
                pet_object.clean_pet()
                after_action()
                continue
            case '5':
                if pet_object.energy < 5:
                    print("Your pet is too tired to do anything! Have them sleep to reset energy.")
                    continue
                pet_object.train_pet()
                # Pet can gain xp from training, so see if they have leveled up.
                pet_object.check_level()
                after_action()
                continue
            case '6':
                check_health = pet_object.sleep_pet()
                if check_health == True:
                    after_action()
                    continue
                else:
                    remove_pet(pet_accounts,pet)
                    return
            case '7':
                # iterate through the pet_accounts list, looking for the currently active pet
                # once found, replace that line with the in use dictionary for that pet
                for i in pet_accounts:
                    if i['name'] == pet_object.name:
                        dict_index = find_dict_index(pet_accounts,'name',pet_object.name)
                        pet_accounts.pop(dict_index)
                        pet_accounts.append(vars(pet_object))

                save_accounts(pet_accounts)

                print("Data Saved")

                after_action()
                continue
            case '8':
                print("Reminder, all unsaved information will be lost FOREVER. Make sure you have saved.")

                choice = input("Return to Main Menu Y/N:\n").strip().capitalize()
                if choice != "Y":
                    after_action()
                    continue
                else:
                    return
            case '9':
                print("Are you sure you want to release this pet? This action cannot be undone; they will be lost forever.")

                choice = input("Y/N:\n").strip().capitalize()

                if choice != "Y":
                    continue

                else:
                    print("Pet has been released.")
                    remove_pet(pet_accounts,pet)
                    return
            case '10':
                pet_object.shop()
                after_action()
                continue
            case '11':
                competition_menu(pet_object)
                after_action()
                continue
            case _:
                print("Please enter 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, or 11.")
                after_action()

        

def display_pets(pet_accounts):
    # this is used when having user pick a saved pet. It displays basic information about each pet (name, level, species, and owner) so they are quickly recognizable.
    # the first if statement just sees if there are any saved pets. The return False is there to make sure actions are taken even if there are no pets.
    if bool(pet_accounts) == False:
        print("There are currently no saved pets.")
        return False
    for i in pet_accounts:
        print(f"{i['name']}, Level {i['level']} {i['species']} owned by {i['owner']}")
    
    return True

def main_menu():
    # load all saved pets
    pet_accounts = parse_accounts()

    # explanation of program
    print("This is a pet simulator game! In it, you can take care of a pet by keeping track of their attributes, such as hunger, happiness, and cleanliness. Current work in progress features are pet breeding, if I get the time.")

    while True:
        # give user options of what to do
        print("What would you like to do?\n1. Create New Pet\n2. Load Pet\n3. Exit\n4. Reload Pet Accounts Data")
        choice = input("Enter number:\n").strip()

        clear_screen()

        match choice:
            case "1":
                # make the actual pet_object
                pet_object = create_pet(avaiable_species,pet_accounts)
                # run main game
                pet_interaction(pet_object,pet_accounts)
                # reload pet_accounts, as the file may have been changed
                pet_accounts = parse_accounts()
            case "2":
                has_pets = display_pets(pet_accounts)

                # if there are no saved pets, go back to main menu
                if has_pets == False:
                    continue

                # have user enter name of pet they want to load
                choice = input("Enter the name of the pet you want to select, exactly as seen in the list.").strip()

                # dictionary pet will be loaded into
                pet = {}

                # used to see if user has entered a valid name. This is done because sometimes when user exits the game, "Please enter a valid name" will be printed to the terminal because of how the code is written.

                valid_name = False
                # iterate through pet accounts
                for i in pet_accounts:
                    # if name in dict is equal to given name
                    if i['name'].title() == choice.title():
                        valid_name = True
                        print("Pet found")

                        # set pet dict equal to dict in pet_accounts
                        pet = i
                        after_action()
                        # load pet
                        pet_object = load_pet(pet)
                        # main game
                        pet_interaction(pet_object,pet_accounts)
                        # reload file in case anything has been changed
                        pet_accounts = parse_accounts()

                    else:
                        continue
                    
                    if valid_name != True:
                        print("Please enter a valid name.")
                        continue

                    after_action()
                    continue
        
                
            case "3":
                # exit the main loop
                print("Goodbye!")
                break
            case "4":
                # reload the pet file, this is here for debugging purposes
                pet_accounts = parse_accounts()
                print("Data reloaded.")
                after_action()
                continue
            case _:
                # stupid proofing
                print("Please enter 1, 2, 3, or 4.")
                continue
