# CB 1st Pet Creating Functions

import random
from helper import *
from saving_parsing import add_pet

# class Pet:
    # create _init_ method
    # define attributes for the pet (happiness, hunger, level, age, stuff like that)
    # create other methods (play, feed, sleep, clean) for pet

    # define function evaluate_health():
        # health will be an average of hunger, happiness, and cleanliness
        # health = (hunger + happiness + cleanliness) / 3
        # return health

    # define function random_event():
        # generate a random number between 1 - 20
        # on odd numbers nothing will happen
        # designate specific events to happen on each even number
        # to be called when time passes


    # define function pass_time(current_time,elapsed_time):
        # to be called after any other function
        # takes the current time variable, adds elapsed time to it (we'll be using military time for this)
        # call random_event() function 
        

    # define function play_with_pet(money,time,energy,happiness,cleanliness):
        # ask user what they would like to do with pet (give a few options, ranging from basic to high-end)
        # make each different hoice take a different amount of time, energy, and money in some cases
        # make each different choice affect happiness and energy of pet in different ways, possible training in some cases

    # define function feed_pet(money,hunger,happiness,energy):
        # ask user what they would like to feed the pet (give a few options, low to high quality)
        # make each different option give a different amount of hunger and happiness, and cost a different amount of money

    # define function sleep_pet(bed_quality,hunger,energy,happiness):
        # function that puts the pet to sleep (not killing it you sicko)
        # run evaluate health function
        # pet sleeping will pass the day, reset energy to normal max, decrease hunger
        # different bed quality will give better stat resets, such as higher energy and better happiness

    # define function clean_pet(money,cleanliness,happiness,energy)
        # ask user what they would like to do for cleaning their pet (there will be a few options low to high quality, ranging from basically a spray down with a hose to a deep cleaning by a professional)
        # have each different option affect pet cleanliness, happiness, and energy in different ways
        # have each option cost different amounts of money

    # define function train_pet(money,energy,level):
        # two ideas for this one

        # one:
        # have training be a way to get xp for your pet so they can level up
        # different forms of training, costing different amounts of money but giving different amounts of xp

        # two:
        # look at current pet level (play will gain them xp), see what skills they have unlocked
        # allow user to train different skills 
        # different training will cost different amounts of money, take different amounts of time, take different amounts of energy from pet

# define function create_pet(pet_accounts):
    # get pet name from user
    # check if that name already exists in the pet accounts file
    # if it does, get new name
    # get species of pet from user (show list of available species)
    # get age of pet from user (keep in months)
    # make object of Pet using given values, set baselines for hunger, energy, and happiness
    # use vars() method to save the pet to the pet_accounts csv

avaiable_species = ['Cat','Dog','Crocodile','Snek']



class Pet:
    def __init__(self,owner,name,species,age):

        # pet attributes
        self.owner = owner
        self.name = name
        self.species = species
        self.age = age

        # pet stats
        self.hunger = 80
        self.happiness = 80
        self.energy = 80
        self.cleanliness = 80
        self.health = 100

        # data more prevalent to the owner
        self.day = 1
        self.time = 8
        self.money = 500
        self.level = 1
        self.xp = 0

        # skills the pet can have
        self.agility = 0
        self.obedience = 0
        self.tracking = 0

        # variables for tracking progress in training a skill
        self.agility_progress = 0
        self.obedience_progress = 0
        self.tracking_progress = 0

    def evaluate_health(self):
        self.health = (self.hunger + self.cleanliness + self.happiness) / 3
        if self.hunger < 25:
            self.health -= 20

        if self.cleanliness < 25:
            self.health - 10

        if self.happiness < 25:
            self.health - 5
            
        print(f"Pet Health: {self.health}")
        after_action()

    def choose_skill(self):

        available_skills = []

        if self.agility == 0:
            available_skills.append('agility')

        if self.obedience == 0:
            available_skills.append('obedience')

        if self.tracking == 0:
            available_skills.append('tracking')

        if bool(available_skills) == False:
            while True:
                print("Your pet has gained all skills avaiable. Choose a skill to gain one free level in.")
                skill_choice = input("1. Agility\n2. Obedience\n3. Tracking\nEnter Number:\n").strip()

                match skill_choice:
                    case "1":
                        self.agility += 1
                        break
                    case "2":
                        self.obedience += 1
                        break
                    case "3":
                        self.tracking += 1
                        break
                    case _:
                        print("Please enter 1, 2, or 3.")
                        after_action()
                        continue
        else:
            while True:
                print("Since your pet has gained a level, they can gain a new skill. Pick which skill you want your pet to gain.")

                skill_choice = input("1. Agility\n2. Obedience\n3. Tracking\nEnter Number:\n").strip()

                match skill_choice:
                    case "1":
                        if self.agilty >= 1:
                            print("Your pet already has that skill.")
                            continue
                        else:
                            self.agility = 1
                            break
                    case "2":
                        if self.obedience >= 1:
                            print("Your pet already has that skill.")
                            continue
                        else:
                            self.obedience = 1
                            break
                    case "3":
                        if self.tracking >= 1:
                            print("Your pet already has that skill.")
                            continue
                        else:
                            self.tracking = 1
                            break
                    case _:
                        print("Please enter 1, 2, or 3.")
                        continue
            after_action()

    def evaluate_age(self):
        age = self.day / 30

        age = round(age,2)

        self.age = age

    def check_level(self):

        current_level = self.level

        if self.xp % 100 == 0:
            self.level = (self.xp / 100) + 1
            if self.level > current_level:
                while self.level != current_level:
                    print(f"{self.name} gained a level! They are now level {self.level}.")
                    current_level += 1
                    self.choose_skill



        else:
            level = 1
            while True:
                xp = self.xp
                if xp > 100:
                    xp - 100
                    level += 1
                else:
                    break
            
            self.level = level

    def random_event(self):
        event = random.randint(1,15)
        if event % 2 != 0:
            pass
        else:
            match event:
                case 2:
                    print(f"{self.name} found a stick! +10 happiness!")
                    self.happiness += 10
                case 4:
                    print(f"{self.name} lost one of their toys. -10 happiness.")
                    self.happiness -= 10
                case 6:
                    print(f"{self.name} has the zoomies! +10 energy!")
                    self.energy += 10
                case 8:
                    print(f"{self.name} is unexpectedly tired. -10 energy.")
                    self.energy -= 10
                case 10:
                    print(f"{self.name} somehow cleaned themselves. +10 cleanliness.")
                    self.cleanliness += 10
                case 12:
                    print(f"{self.name} rolled around in a bunch of mud! -10 cleanliness.")

            after_action()

    def pass_time(self,elapsed_time,mode):
        print("Time passes...")
        
        self.time += elapsed_time

        # Hunger goes down by 5 every hour.
        if mode == True:
            while elapsed_time > 0:
                print("-5 Hunger per hour")
                hunger -= 5
                elapsed_time -= 1

        after_action()

        self.random_event()

    def check_time(self):
        if self.time >= 22:
            print("It's too late in the day. Have your pet go to sleep to move on to the next day.")
            return False
        else:
            return True

    def play_with_pet(self):
        if self.energy == 0:
            print("Your pet is out of energy! Have them sleep to reset energy.")
            after_action()
            return
        else:
            while True:
                print("How would you like to play with your pet?\n1. Go to a park and run around (Free, +10 Happiness, +5 xp, -10 Energy)\n2. Go to a fancy pet park and run around (but fancily) ($10, +20 Happiness, + 10 xp, -15 Energy)\n3. Go to like the fanciest pet park ever ($20, +25 Happiness, + 15 xp, -20 Energy)")
                choice = input("Enter 1, 2, or 3:\n").strip()

                match choice:
                    case "1":
                        print(f"You went to a park and ran around with {self.name}!")
                        self.happiness += 10
                        self.xp += 5
                        self.energy -= 10

                        self.happiness = max_min_checker(self.happiness)
                        self.energy = max_min_checker(self.energy)
                        break
                        
                    case "2":
                        if self.money < 10:
                            print("You don't have enough money for that.")
                            after_action()
                            continue
                        print(f"You went to a fancy pet park and ran around with {self.name}!")
                        self.happiness += 20
                        self.xp += 10
                        self.money -= 10
                        self.energy -= 15

                        self.happiness = max_min_checker(self.happiness)
                        self.energy = max_min_checker(self.energy)
                        break
                        
                    case "3":
                        if self.money < 20:
                            print("You don't have enough money for that.")
                            after_action()
                        print(f"You went to the fanciest pet park and ran around with {self.name}!")
                        self.happiness += 25
                        self.xp += 15
                        self.money -= 20
                        self.energy -= 20

                        self.happiness = max_min_checker(self.happiness)
                        self.energy = max_min_checker(self.energy)
                        break
                       
                    case _:
                        print("Please enter 1, 2, or 3.")
                        after_action()
                        continue
            
            after_action()

    def clean_pet(self):
        if self.energy == 0:
            print("Your pet is out of energy! Have them sleep to reset energy.")
            after_action()
        else:
            while True:
                print("How would you like to clean your pet?\n1. Home Bath (Free, +15 Cleanliness, -10 Energy)\n2. Basic Groomer ($10, +30 Cleanliness, -15 Energy)\n3. Professional Groomer ($20, Cleanliness Max, -20 Energy)")
                choice = input("Enter 1, 2, or 3:\n").strip()

                match choice:
                    case "1":
                        print("You gave your pet an at-home bath.")
                        self.cleanliness += 15
                        self.energy -= 10

                        self.cleanliness = max_min_checker(self.cleanliness)
                        self.energy = max_min_checker(self.energy)

                        break
                    case "2":
                        if self.money < 10:
                            print("You don't have enough money for this.")
                            after_action()
                            continue
                        print("You went to a basic groomer to get your pet trimmed and cleaned.")
                        self.cleanliness += 30
                        self.energy -= 15
                        self.money -= 10

                        self.cleanliness = max_min_checker(self.cleanliness)
                        self.energy = max_min_checker(self.energy)

                        break
                    case "3":
                        if self.money < 20:
                            print("You don't have enough money for this.")
                            after_action()
                            continue
                        print("You went to a professional groomer to get your pet trimmed and cleaned.")
                        self.cleanliness = 100
                        self.energy -= 20
                        self.money -= 20

                        self.cleanliness = max_min_checker(self.cleanliness)
                        self.energy = max_min_checker(self.energy)

                        break
                    case _:
                        print("Please enter 1, 2, or 3.")
                        after_action()
                        continue

            after_action()

    def feed_pet(self):
        print("How would you like to feed your pet?\n1. Basic Kibble (Free, +10 Hunger, +5 Happiness, -5 Energy)\n2. Treat ($2, +15 Happiness, +5 Hunger, -5 Energy)\n3. Fancy Food ($5, +10 Happiness, +15 Hunger, -5 Energy)\n4. Home Made Meal ($10, +15 Happiness, +20 Hunger, -5 Energy)")
        while True:
            choice = input("Please enter 1, 2, 3, or 4:\n").strip()

        
            match choice:
                case "1":
                    print("You fed your pet basic kibble!")
                    self.hunger += 10
                    self.happiness += 5
                    self.energy -= 5
                    break
                case "2":
                    if self.money < 2:
                        print("You don't have enough money for that.")
                        after_action()
                        continue
                    
                    print("You gave your pet a treat!")
                    self.happiness += 15
                    self.hunger += 5
                    self.energy -= 5
                    break

                case "3":
                    if self.money < 5:
                        print("You don't have enough money for that.")
                        after_action()
                        continue
                    
                    print("You fed your pet fancy kibble!")
                    self.happiness += 10
                    self.hunger += 15
                    self.energy -= 5
                    break

                case "4":
                    if self.money < 10:
                        print("You don't have enough money for that.")
                        after_action()
                        continue
                        
                    print("You fed your pet a home made meal!")
                    self.happiness += 15
                    self.hunger += 20
                    self.energy -= 5
                    break
        after_action()
        return

    def train_pet(self):
        while True:
            print(f"What skill would would you like to train?\nNote: If a skill is Level 0, your pet has not obtained it yet, and it cannot be trained.\nNote Two: Training your pet takes two hours and twenty energy.\n1. Agility, Level {self.agility}\n2. Obedience, Level {self.obedience}\n3. Tracking, Level {self.tracking}")

            choice = input("Enter number:\n").strip()

            match choice:
                case '1':
                    if self.agility == 0:
                        print("You have not yet obtained that skill.")
                        after_action()
                        continue

                    print("You spent two hours training your pet in agility. You have gained progress towards the next level.")

                    self.agility_progress += 1

                    if self.agility_progress == 3:
                        print("Your pet gained a level in Agility!")
                        self.agility += 1
                        self.agility_progress == 0

                    break
                case '2':
                    if self.obedience == 0:
                        print("You have not yet obtained that skill.")
                        after_action()
                        continue
                    
                    print("You spent two hours training your pet in obedience. You have gained progress towards the next level.")

                    self.obedience_progress += 1

                    if self.obedience_progress == 3:
                        print("Your pet gained a level in Obedience!")
                        self.obedience += 1
                        self.obedience_progress == 0

                    break
                case '3':
                    if self.tracking == 0:
                        print("You have not yet obtained that skill.")
                        after_action()
                        continue
                    
                    print("You spent two hours training your pet in tracking. You have gained progress towards the next level.")

                    self.tracking_progress += 1

                    if self.tracking_progress == 3:
                        print("Your pet gained a level in Tracking!")
                        self.tracking += 1
                        self.tracking_progress == 0

                    break
                case _:
                    print("Please enter 1, 2, or 3.")
                    after_action()
                    continue

        after_action()

    def sleep_pet(self):
        print("Your pet has gone to bed.")
        self.energy = 100
        self.hunger -= 30
        self.happiness += 5
        # make sure to use pass time after this

    def view_pet(self):
        while True:
            print("What information about your pet would you like to view?\n1. Basic Info (Name, Age, Species)\n2. Attributes\n3. Save File Attribtues\n4. Skills")

            choice = input("Enter number:\n").strip()

            match choice:
                case '1':
                    print(f"Owner Name: {self.owner}\nName: {self.name}\nAge (months): {self.age}\nSpecies: {self.species}")
                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    pass
                case _:
                    print("Please enter 1, 2, 3, or 4.")
        



def create_pet(avaiable_species):
    owner = input("What is your name?").strip()
    pet = input("What is the name of your pet?").strip()

    print("Avaiable Species")
    for i in avaiable_species:
        print(i)

    while True:
        species = input("What species is your pet?").strip().capitalize()
        if species not in avaiable_species:
            print("Please enter a valid answer.")
            continue_screen()
        else:
            try:
                age = input("What is the age of your pet (in months)?").strip()
                age = int(age)
            except:
                print("Please enter a numerical value.")
                continue_screen()
            else:
                try:
                    pet_object = Pet(owner,pet,species,age)
                except:
                    print("Failed to create pet object")
                else:
                    print("Pet created succesfully!")
                    after_action()
                    add_pet(pet_object)
                    return pet_object
                
create_pet(avaiable_species)

