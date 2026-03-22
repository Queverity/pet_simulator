# CB 1st Pet Competition

import random
from helper import *


chance_list = [0.2,0.3,0.4]

# def calculate_tier(skill_level):
    # if skill_level <= 3:
        # return "Beginner"
    # elif skill_level <= 6:
        # return "Intermediate"
    # elif skill_level <= 9:
        # return "Pro"
    # else:
        # return "Legend"

# competition_menu(pet_object):
    # Give user options to compete in skills which their pet has
    # Competitions will have a base entrance fee
    # Maybe make different competition tiers that people can access based on skill level (beginner, intermediate, pro, legend)
    # Entrance fee and prize amount will increase with tier
    # Competition will take a significant amount of energy and time (maybe just skip to next day after comp)

# competition_games(pet_object,skill,tier):
    # win_chance = random.choice(chance_list)
    # win_chance *= pet_object.skill_level

    # if tier == "Beginner":
        # if win_chance > 0.7:
            # pet wins competition, give cash prize, pass time and all that stuff
    # elif tier == "Intermediate"
        # if win_chance > 2:
            # pet wins competition, give cash prize, pass time and all that stuff
    # elif tier == "Pro":
        # if win_chance > 2.6:
            # pet wins competition, give cash prize, pass time and all that stuff
    # else:
        # if win_chance > 3.3:
            # pet wins competition, give cash prize, pass time and all that stuff


def calculate_tier(skill_level):
    if skill_level <= 3:
        return "Beginner",1
    elif skill_level <= 6:
        return "Intermediate",2
    elif skill_level <= 9:
        return "Pro",3
    else:
        return "Legend",4

def competition(pet_object,skill_level,comp_tier):
    win_chance = random.choice(chance_list)
    win_chance *= skill_level

    if comp_tier == "Beginner":
        if win_chance > 0.7:
            # pet wins competition, give cash prize, pass time and all that stuff
            pass
    elif comp_tier == "Intermediate":
        if win_chance > 2:
            # pet wins competition, give cash prize, pass time and all that stuff
            pass
    elif comp_tier == "Pro":
        if win_chance > 2.6:
            # pet wins competition, give cash prize, pass time and all that stuff
            pass
    else:
        if win_chance > 3.3:
            # pet wins competition, give cash prize, pass time and all that stuff
            pass

def competition_menu(pet_object):
    if pet_object.energy < 40:
        print("Your pet does not have enough energy to compete! They need to have at least 40 Energy.")
        return
    print("Welcome to the competition menu! Here, you can participate in competitions for each skill your pet has. Based on your pet's skill level, they will be able to participate in different tiers of comps. Note: All competitions take 4 hours and 40 Energy.")

    agility_tier,agility_multiplier = calculate_tier(pet_object.agility)

    obedience_tier,obedience_multiplier = calculate_tier(pet_object.obedience)

    tracking_tier,tracking_multiplier = calculate_tier(pet_object.tracking)

    while True:
        print(f"What would you like to do?\n1. Compete in Agility ({agility_tier} Tier, ${25 * agility_multiplier} Entrance Fee)\n2. Compete in Obedience ({obedience_tier} Tier, ${25 * obedience_multiplier} Entrance Fee)\n3. Compete in Tracking ({tracking_tier} Tier, ${25 * tracking_multiplier} Entrance Fee)\n4. Return to Pet Menu")

        choice = input("Enter number:\n").strip()

        clear_screen()

        match choice:
            case '1':
                # in these, run compitition, then return
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                return
            case _:
                print("Please enter 1, 2, 3, or 4.")
                continue