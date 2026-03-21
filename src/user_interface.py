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

# define function display_pets(pet_accounts):
    # use a for loop to iterate through pet accounts and print pet name, level, species, and owner

def pet_interaction(pet_object,pet_accounts):
    pet = pet_object.name

    while True:
        print(f"Day {pet_object.day}, {pet_object.time}:00")

        print(f"What would you like to do with {pet}?\n1. Examine {pet}\n2. Feed {pet}\n3. Play with {pet}\n4. Clean {pet}\n5. Train Pet\n6. Send {pet} to Bed\n7. Save Pet File\n8. Return to Main Menu\n9. Release Pet (CANNOT BE UNDONE)\n10. Go to Pet Item Shop")

        choice = input("Enter number:\n").strip()

        clear_screen()

        match choice:
            case '1':
                pet_object.view_pet()
                after_action()
                continue
            case '2':
                if pet_object.energy < 5:
                    print("Your pet is too tired to do anything! Have them sleep to reset energy.")
                    continue
                pet_object.feed_pet()
                pet_object.hunger += 5
                after_action()
                continue
            case '3':
                if pet_object.energy < 5:
                    print("Your pet is too tired to do anything! Have them sleep to reset energy.")
                    continue
                pet_object.play_with_pet()
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
                pet_object.check_level()
                after_action()
                continue
            case '6':
                pet_object.sleep_pet()
                after_action()
                continue
            case '7':
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
                continue
            case _:
                print("Please enter 1, 2, 3, 4, 5, 6, 7, or 8.")
                after_action()

        

def display_pets(pet_accounts):
    if bool(pet_accounts) == False:
        print("There are currently no saved pets.")
        return False
    for i in pet_accounts:
        print(f"{i['name']}, Level {i['level']} {i['species']} owned by {i['owner']}")
    
    return True

def main_menu():
    pet_accounts = parse_accounts()

    print("This is a pet simulator game! In it, you can take care of a pet by keeping track of their attributes, such as hunger, happiness, and cleanliness. Current work in progress features are a shop, skill competitions, and possibly pet breeding.")

    while True:
        print("What would you like to do?\n1. Create New Pet\n2. Load Pet\n3. Exit\n4. Reload Pet Accounts Data")
        choice = input("Enter number:\n").strip()

        clear_screen()

        match choice:
            case "1":
                pet_object = create_pet(avaiable_species)
                pet_interaction(pet_object,pet_accounts)
                pet_accounts = parse_accounts()
            case "2":
                has_pets = display_pets(pet_accounts)

                if has_pets == False:
                    continue
                choice = input("Enter the name of the pet you want to select, exactly as seen in the list.").strip()

                pet = {}
                try:
                    for i in pet_accounts:
                        if i['name'].title() == choice.title():
                            print("Pet found")
                            pet = i
                            after_action()
                        else:
                            continue
                except:
                    print("Please enter a valid name.")
                    after_action()
                    continue
                else:
                    pet_object = load_pet(pet)
                    pet_interaction(pet_object,pet_accounts)
                    pet_accounts = parse_accounts()
                    continue
                
            case "3":
                print("Goodbye!")
                break
            case "4":
                pet_accounts = parse_accounts()
                print("Data reloaded.")
                after_action()
                continue
            case _:
                print("Please enter 1, 2, 3, or 4.")
                continue
