# CB 1st Pet Competition

import random
from helper import *

# mild chance part to the competition
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
    # Tiers of the competition are based on skill level, seperated by 3 each.
    if skill_level == 0:
        return "No Skill",0
    elif skill_level <= 3:
        return "Beginner",1
    elif skill_level <= 6:
        return "Intermediate",2
    elif skill_level <= 9:
        return "Pro",3
    else:
        return "Legend",4

def competition(pet_object,skill,skill_level,comp_tier):
    # calculate win chance, then compare it to required win chance to see if pet has won. If they do, give cash prize. If they don't, womp womp.
    win_chance = random.choice(chance_list)
    win_chance *= skill_level

    if comp_tier == "Beginner":
        if win_chance > 0.7:
            print(f"Your pet has won the {comp_tier} {skill} competition! You win $75.")
            pet_object.money += 75
            return 
        else:
            print(f"Unfortunately, your pet lost the {comp_tier} {skill} competition.")
            return 
    elif comp_tier == "Intermediate":
        if win_chance > 2:
            print(f"Your pet has won the {comp_tier} {skill} competition! You win $150.")
            pet_object.money += 150
            return 
        else:
            print(f"Unfortunately, your pet lost the {comp_tier} {skill} competition.")
            return 
    elif comp_tier == "Pro":
        if win_chance > 2.6:
            print(f"Your pet has won the {comp_tier} {skill} competition! You win $225.")
            pet_object.money += 225
            return 
        else:
            print(f"Unfortunately, your pet lost the {comp_tier} {skill} competition.")
            return 
    else:
        if win_chance > 3.3:
            print(f"Your pet has won the {comp_tier} {skill} competition! You win $300.")
            pet_object.money += 300
            return 
        else:
            print(f"Unfortunately, your pet lost the {comp_tier} {skill} competition.")
            return 

def competition_menu(pet_object):
    # check to see if user has enough energy.
    if pet_object.energy < 40:
        print("Your pet does not have enough energy to compete! They need to have at least 40 Energy.")
        return
    print("Welcome to the competition menu! Here, you can participate in competitions for each skill your pet has. Based on your pet's skill level, they will be able to participate in different tiers of comps. If you win the competition, you will get a cash prize equal to three times the entrance fee. Note: All competitions take 4 hours and 40 Energy. This will be taken whether or not you win the competition. Note 2: You can't participate in competitions your pet doesn't have.")

    # calculate tier and multiplier for each competition
    agility_tier,agility_multiplier = calculate_tier(pet_object.agility)

    obedience_tier,obedience_multiplier = calculate_tier(pet_object.obedience)

    tracking_tier,tracking_multiplier = calculate_tier(pet_object.tracking)

    while True:
        # display options for user
        print(f"What would you like to do?\n1. Compete in Agility ({agility_tier} Tier, ${25 * agility_multiplier} Entrance Fee)\n2. Compete in Obedience ({obedience_tier} Tier, ${25 * obedience_multiplier} Entrance Fee)\n3. Compete in Tracking ({tracking_tier} Tier, ${25 * tracking_multiplier} Entrance Fee)\n4. Return to Pet Menu")

        # get user input
        choice = input("Enter number:\n").strip()

        clear_screen()

        match choice:
            case '1':
                # check to make sure user actually has skill, used in all cases for comps
                if pet_object.agility == 0:
                    print("Your pet does not have the agility skill.")
                    continue
                # check to make sure user can pay entrance fee, used in all cases for comps
                if pet_object.money < 25 * agility_multiplier:
                    print("You do not have enough money to participate in this competition.")
                    continue
                
                pet_object.money -= 25 * agility_multiplier
                competition(pet_object,'Agility',pet_object.agility,agility_tier)

                break
            case '2':
                if pet_object.obedience == 0:
                    print("Your pet does not have the obedience skill.")
                    continue
                if pet_object.money < 25 * obedience_multiplier:
                    print("You do not have enough money to participate in this competition.")
                    continue
                
                pet_object.money -= 25 * obedience_multiplier
                competition(pet_object,'Obedience',pet_object.obedience,obedience_tier)

                break
            case '3':
                if pet_object.tracking == 0:
                    print("Your pet does not have the tracking skill.")
                    continue
                if pet_object.money < 25 * tracking_multiplier:
                    print("You do not have enough money to participate in this competition.")
                    continue
                
                pet_object.money -= 25 * tracking_multiplier
                competition(pet_object,'Tracking',pet_object.tracking,tracking_tier)

                break
            case '4':
                return
            case _:
                print("Please enter 1, 2, 3, or 4.")
                continue
    
    # pass time and take energy
    for _ in range (1,4):
        pet_object.pass_time()
        pet_object.energy -= 10

    after_action()
    return

    