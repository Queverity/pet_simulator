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
    # all the variables have to be able to be put in from outside (not defaults) so we can load pets from a CSV file.
    def __init__(self,owner,name,species,age,hunger,happiness,energy,cleanliness,health,day,time,money,level,xp,agility,obedience,tracking,agility_progress,obedience_progress,tracking_progress,bed,toy,food,brush):

        # pet attributes
        self.owner = owner
        self.name = name
        self.species = species
        self.age = age

        # pet stats
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        self.cleanliness = cleanliness
        self.health = health

        # data more prevalent to the owner
        self.day = day
        self.time = time
        self.money = money
        self.level = level
        self.xp = xp

        # skills the pet can have
        self.agility = agility
        self.obedience = obedience
        self.tracking = tracking

        # variables for tracking progress in training a skill
        self.agility_progress = agility_progress
        self.obedience_progress = obedience_progress
        self.tracking_progress = tracking_progress

        # inventory items that give boosts
        self.bed = bed # improves hunger decrease and happiness after sleep
        self.toy = toy # improves happiness gain and maybe xp after play
        self.food = food # improves hunger and happiness gain after eating
        self.brush = brush # improves cleanliness gain after washing

    def evaluate_health(self):
        # Base health is an average of hunger, cleanliness, and happiness. If these stats are below a certain threshold, a certain amount of health will be removed.
        self.health = (self.hunger + self.cleanliness + self.happiness) / 3
        if self.hunger < 25:
            self.health -= 20

        if self.cleanliness < 25:
            self.health - 10

        if self.happiness < 25:
            self.health - 5

    def choose_skill(self):

        # Used to see what pets the user can still obtain, or if they've gained all skills
        available_skills = []

        if self.agility == 0:
            available_skills.append('agility')

        if self.obedience == 0:
            available_skills.append('obedience')

        if self.tracking == 0:
            available_skills.append('tracking')

        # if the user has obtained all skills, allow them to gain one free level in a skill of their choice
        if bool(available_skills) == False:
            while True:
                print("Your pet has gained all skills avaiable. Choose a skill to gain one free level in.")
                skill_choice = input("1. Agility\n2. Obedience\n3. Tracking\nEnter Number:\n").strip()

                match skill_choice:
                    case "1":
                        self.agility += 1
                        print("Your pet has gained a level in Agility.")
                        break
                    case "2":
                        self.obedience += 1
                        print("Your pet has gained a level in Obedience.")
                        break
                    case "3":
                        self.tracking += 1
                        print("Your pet has gained a level in Tracking.")
                        break
                    case _:
                        print("Please enter 1, 2, or 3.")
                        after_action()
                        continue
        else:
            # If the user has not obtained all skills
            while True:
                print("Since your pet has gained a level, they can gain a new skill. Pick which skill you want your pet to gain. If your pet already has a skill, they can't gain it twice.")

                # Show the user what skills they can still grab
                print("Available Skills")
                for i in available_skills:
                    print(i.capitalize())

                # ask user what skill they want
                skill_choice = input("1. Agility\n2. Obedience\n3. Tracking\nEnter Number:\n").strip()


                match skill_choice:
                    # First, check if the skill level is 1 or higher. If it is, then they already have the skill. Continue after that. If the skill level is 0, set the skil level to one and then break out of the loop.
                    case "1":
                        if self.agility >= 1:
                            print("Your pet already has that skill.")
                            continue
                        else:
                            self.agility = 1
                            print("Your pet has gained the Agility skill!")
                            break
                    case "2":
                        if self.obedience >= 1:
                            print("Your pet already has that skill.")
                            continue
                        else:
                            self.obedience = 1
                            print("Your pet has gained the Obedience skill!")
                            break
                    case "3":
                        if self.tracking >= 1:
                            print("Your pet already has that skill.")
                            continue
                        else:
                            self.tracking = 1
                            print("Yor pet has gained the Tracking skill!")
                            break
                    case _:
                        print("Please enter 1, 2, or 3.")
                        continue
            after_action()

    def evaluate_age(self):
        # Since age is calculated in months, just find the age by dividing days by 30. Then, round the number so it isn't ugly.
        age = self.day / 30

        age = round(age,2)

        self.age = age

    def check_level(self):
        # Check if the pet's xp is greater than 100 (level limit). If it is, subtract xp by 100, increment level, and run choose skill function.
        if self.xp > 100:
            self.level += 1
            print(f"{self.name} gained a level! They are now level {self.level}.")
            self.choose_skill()
            self.xp -= 100
            return



    def random_event(self):
        # random events that have a 50% chance to be run than can change attributes of your pet. These will be run anytime time is passed.
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

    def pass_time(self):
        # Increment hour (time) by one, and unless the feed pet event comes before this, decrease hunger by 5. Also, decrease cleanliness by one.
        print("Time passes...")
        
        self.time += 1

        # Hunger goes down by 5 every hour.
        
        
        print("-5 Hunger per hour (Except for Feed Pet action)\n-1 Cleanliness per hour")
        self.hunger -= 5
        self.cleanliness -= 1

        after_action()

        self.random_event()

    def check_time(self):
        # Used before certain actions, just make sure the user isn't going too late in the day (and also make sure it doesn't say it is 2500 hours)
        if self.time >= 22:
            print("It's too late in the day. Have your pet go to sleep to move on to the next day.")
            return False
        else:
            return True



    def shop(self):
        print("Welcome to the pet shop! Here, you can purchase upgrades for specific items your pet uses.")

        while True:
            # This is the pet shop, where users can get items for their pet. Price is calculated for most items by multiplying the current item tier by 50, and multiplying it by 30.
            print(f"You can get upgrades for your pet's bed, toys, food, and brush. Available Purchases:\nTier {self.bed  + 1} Bed, ${(self.bed + 1) * 50}\nTier {self.toy + 1} Toys, ${(self.toy + 1) * 50}\nTier {self.food  + 1} Foods, ${(self.food + 1) * 50}\nTier {self.brush + 1} Brush, ${(self.brush + 1) * 30}\n")

            # see what the user wants to do
            purchase = input("1. Purchase Bed\n2. Purchase Toys\n3. Purchase Foods\n4. Purchase Brush\n5. Explain Boosts\n6. Exit\n").strip()

            clear_screen()

            # First, check if user has enough money. If they don't, send them back to the shop menu. If they do, increment item tier by one, subtract money, and break loop.
            match purchase:
                case "1":
                    if self.money < (self.bed + 1) * 50:
                        print("You don't have enough money for that.")
                        continue

                    print("You have upgraded your pet's bed!")
                    self.bed += 1
                    self.money -= (self.bed + 1) * 50
                    break
                case "2":
                    if self.money < (self.toy + 1) * 50:
                        print("You don't have enough money for that.")
                        continue

                    print("You have upgraded your pet's toys!")
                    self.toy += 1
                    self.money -= (self.toy + 1) * 50
                    break
                case '3':
                    if self.money < (self.food + 1) * 50:
                        print("You don't have enough money for that.")
                        continue

                    print("You have upgraded your pet's foods!")
                    self.food += 1
                    self.money -= (self.food + 1) * 50
                    break
                case '4':
                    if self.money < (self.toy + 1) * 50:
                        print("You don't have enough money for that.")
                        continue

                    print("You have upgraded your pet's brush!")
                    self.brush += 1
                    self.money -= (self.brush + 1) * 50
                    break
                case '5':
                    # explaining what certain items can do
                    print("Beds improve hunger loss and happiness gain after sleeping.\nToys improve happiness and xp gain after play.\nFoods improve hunger and happiness after eating.\nBrushes improve cleanliness gain and happiness loss after washing.\n")
                    continue
                case '6':
                    clear_screen()
                    return
                case _:
                    print("Please enter 1, 2, 3, 4, 5, or 6.")
                    after_action()
                    continue

        after_action()
        return

    def play_with_pet(self):
        # make sure pet isn't out of energy
        if self.energy == 0:
            print("Your pet is out of energy! Have them sleep to reset energy.")
            after_action()
            return
        else:
            # give options for what user can do, each giving different attributes and costing different amounts
            while True:
                print("How would you like to play with your pet?\n1. Go to a park and run around (Free, +10 Happiness, +5 xp, -10 Energy)\n2. Go to a fancy pet park and run around (but fancily) ($10, +20 Happiness, + 10 xp, -15 Energy)\n3. Go to like the fanciest pet park ever ($20, +25 Happiness, + 15 xp, -20 Energy)\n4. Return to Pet Menu")
                choice = input("Enter 1, 2, 3, or 4\n").strip()

                match choice:
                    case "1":
                        print(f"You went to a park and ran around with {self.name}!")
                        self.happiness += 10
                        self.xp += 5
                        self.energy -= 10

                        break
                        
                    case "2":
                        # if option costs money, verify user has enough
                        if self.money < 10:
                            print("You don't have enough money for that.")
                            after_action()
                            continue
                        print(f"You went to a fancy pet park and ran around with {self.name}!")
                        self.happiness += 20
                        self.xp += 10
                        self.money -= 10
                        self.energy -= 15

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

                        break
                    case "4":
                        return
                    case _:
                        print("Please enter 1, 2, 3, or 4.")
                        after_action()
                        continue

            # add item tier boost
            if self.toy > 1:
                self.happiness += self.toy * 3
                self.xp += self.toy * 2

                print(f"Your pet gained +{self.toy * 3} Happiness from their toy upgrade.\nYour pet gained +{self.toy * 2} XP from their toy upgrade.")

            # make sure happiness and energy aren't exceding max or min values
            self.happiness = max_min_checker(self.happiness)
            self.energy = max_min_checker(self.energy)

            self.pass_time()
            
            after_action()

    def clean_pet(self):
        # verify pet has enough energy
        if self.energy == 0:
            print("Your pet is out of energy! Have them sleep to reset energy.")
            after_action()
        else:
            while True:
                # give user multiple options with different attributes
                print("How would you like to clean your pet?\n1. Home Bath (Free, +15 Cleanliness, -5 Energy)\n2. Basic Groomer ($10, +30 Cleanliness, -10 Energy)\n3. Professional Groomer ($20, Cleanliness Max, -15 Energy)\n4. Return to Pet Menu")
                choice = input("Enter 1, 2, or 3:\n").strip()

                match choice:
                    case "1":
                        print("You gave your pet an at-home bath.")
                        self.cleanliness += 15
                        self.energy -= 5

                        

                        break
                    case "2":
                        # if options costs money, verify user has enough
                        if self.money < 10:
                            print("You don't have enough money for this.")
                            after_action()
                            continue
                        print("You went to a basic groomer to get your pet trimmed and cleaned.")
                        self.cleanliness += 30
                        self.energy -= 10
                        self.money -= 10

                        

                        break
                    case "3":
                        if self.money < 20:
                            print("You don't have enough money for this.")
                            after_action()
                            continue
                        print("You went to a professional groomer to get your pet trimmed and cleaned.")
                        self.cleanliness = 100
                        self.energy -= 15
                        self.money -= 20

                        

                        break
                    case "4":
                        return
                    case _:
                        print("Please enter 1, 2, or 3.")
                        after_action()
                        continue

            # give item boosts
            if self.brush > 1:
                self.cleanliness += self.brush * 4
                print(f"Your pet gained +{self.brush*4} Cleanliness from their brush.")

            # make sure cleanliness and energy aren't exceeding max or min values
            self.cleanliness = max_min_checker(self.cleanliness)
            self.energy = max_min_checker(self.energy)

            self.pass_time()

            after_action()

    def feed_pet(self):
        
        while True:
            # give user multiple options for how to feed their pet
            print("How would you like to feed your pet?\n1. Basic Kibble (Free, +10 Hunger, +5 Happiness, -5 Energy)\n2. Treat ($2, +15 Happiness, +5 Hunger, -5 Energy)\n3. Fancy Food ($5, +10 Happiness, +15 Hunger, -5 Energy)\n4. Home Made Meal ($10, +15 Happiness, +20 Hunger, -5 Energy)\n5. Return to Pet Menu")
            choice = input("Please enter 1, 2, 3, 4, or 5:\n").strip()

        
            match choice:
                case "1":
                    print("You fed your pet basic kibble!")
                    self.hunger += 10
                    self.happiness += 5
                    self.energy -= 5
                    break
                case "2":
                    # if option costs money, verify user has enough
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
                case "5":
                    return
                case _:
                    print("Please enter 1, 2, 3, 4, or 5.")
                    continue

        # add item boosts
        if self.food > 1:
            self.happiness += self.food * 3
            self.hunger += self.food * 3
            print(f"Your pet gained +{self.food * 3} Hunger from their food upgrade.\nYour pet gained +{self.food * 3} Happiness from their food upgrade.")

        # verify happiness, hunger, and energy aren't exceeding max or min values
        self.happiness = max_min_checker(self.happiness)
        self.hunger = max_min_checker(self.hunger)
        self.energy = max_min_checker(self.energy)

        self.pass_time()
        # done to have pet not lose hunger right after eating
        hunger += 5

        after_action()
        return

    def train_pet(self):
        while True:
            # make sure pet has enough energy
            if self.energy < 20:
                print("Your pet does not have enough energy to do training! Have them sleep to reset energy.")
                return
            # give user options of how to train pet
            print(f"What skill would would you like to train?\nNote: If a skill is Level 0, your pet has not obtained it yet, and it cannot be trained.\nNote Two: Training your pet takes two hours and twenty energy.\n1. Agility, Level {self.agility}\n2. Obedience, Level {self.obedience}\n3. Tracking, Level {self.tracking}\n4. General Training (Gain 30 xp)\n5. Return to Pet Menu")

            choice = input("Enter number:\n").strip()

            match choice:
                # first, verify pet actually has skill. If they do, add one to training progress. if training progress is equal to three, add 1 level to the skill and reset training progress.
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
                case '4':
                    print("You spent two hours training your pet. Your pet has gained +30 xp.")
                    self.xp += 30
                    break
                case '5':
                    clear_screen()
                    return
                case _:
                    print("Please enter 1, 2, 3, 4, or 5.")
                    after_action()
                    continue

        self.pass_time()
        self.pass_time()
        self.energy -= 20
        after_action()

    def sleep_pet(self):
        # A few checks before the pet sleeps; First, check the time. If it is past 10:00 PM, don't check the next thing, as the user can't do anything past 10:00 PM. If it isn't past 10 PM, check pet energy. If it is above 25, the pet has too much energy to sleep. If both of these are passed, run sleep code.
        if self.time >= 22:
            pass
        else:
            if self.energy >= 25:
                print("Your pet has too much energy to sleep! They can sleep once they have 25 Energy or less.")
                return
            else:
                pass
        print("Your pet has gone to bed.")
        # reset energy, decrease hunger, increase happiness
        self.energy = 100
        self.hunger -= (30 - self.bed * 3)
        self.happiness += (5 + self.bed * 2)

        # reset time to morning, iterate day
        self.time = 8
        self.day += 1

        # check health (if 0 or below, the pet ded)
        self.evaluate_health()
        if self.health <= 0:
            print("Bro. Your pet died in its sleep. Likely, this pet is maybe a few days old. How do you fumble that bad? Like seriously? Either way, it's getting deleted now. Sorry not sorry.")

            return False
        # user gets 50 dollars per day
        self.money += 50
        return True
        # make sure to use pass time after this

    def view_pet(self):
        while True:
            # give user different options on how to view pet
            print("What information about your pet would you like to view?\n1. Basic Info (Name, Age, Species)\n2. Attributes\n3. Save File Attribtues\n4. Skills\n5. Inventory\n6. Exit")

            choice = input("Enter number:\n").strip()

            match choice:
                case '1':
                    print(f"Owner Name: {self.owner}\nName: {self.name}\nAge (months): {self.age}\nSpecies: {self.species}")
                case '2':
                    print(f"Hunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}\nCleanliness: {self.cleanliness}\nHealth: {self.health}")
                case '3':
                    print(f"Money: {self.money}\nPet XP (Progress towards next level): {self.xp}/100\nPet Level: {self.level}")
                case '4':
                    print("Note: If a skill is Level 0, you have not yet obtained it.")
                    print(f"Agility: Level {self.agility}\nObedience: Level {self.obedience}\nTracking: Level {self.tracking}")
                case '5':
                    print(f"Bed: Tier {self.bed}\nToy: Tier {self.toy}\nFoods: Tier {self.food}\nBrush: Tier {self.brush}")
                case '6':
                    return
                case _:
                    print("Please enter 1, 2, 3, 4, 5, or 6.")
                    after_action()

            print("Would you like to continue viewing your pet's statisitics?")
            choice = ("Y/N:\n").strip().capitalize()

            if choice != "Y":
                return
            else:
                continue

            

def create_pet(avaiable_species,pet_accounts):
    # owner name, not technically neccesary
    owner = input("What is your name?").strip()
    

    # loop used for stupid proofing
    while True:
        # get name of pet
        pet = input("What is the name of your pet?").strip()

        # show what species user can make their pet
        print("Avaiable Species")
        for i in avaiable_species:
            print(i)
        # take in user input for species, then validate it is an accepted species
        species = input("What species is your pet?").strip().capitalize()
        if species not in avaiable_species:
            print("Please enter a valid answer.")
            continue_screen()
        else:   
            # create pet object, have all defualt values preset
            try:
                # pet age, because setting day equal to age and figuring that out sounds annoying
                age = 0
                # pet stats
                hunger = 80
                happiness = 80
                energy = 80
                cleanliness = 80
                health = 100

                # data more prevalent to the owner
                day = 1
                time = 8
                money = 500
                level = 1
                xp = 0

                # skills the pet can have
                agility = 0
                obedience = 0
                tracking = 0

                # variables for tracking progress in training a skill
                agility_progress = 0
                obedience_progress = 0
                tracking_progress = 0

                # inventory items that give boosts
                bed = 1 # improves hunger decrease and happiness after sleep
                toy = 1 # improves happiness gain and maybe xp after play
                food = 1 # improves hunger and happiness gain after eating
                brush = 1 # improves cleanliness gain after washing
                pet_object = Pet(owner,pet,species,age,hunger,happiness,energy,cleanliness,health,day,time,money,level,xp,agility,obedience,tracking,agility_progress,obedience_progress,tracking_progress,bed,toy,food,brush)
            except:
                print("Failed to create pet object")
                return
            else:
                # if pet is created succesfully, tell user that, than run game
                print("Pet created succesfully!")
                after_action()
                add_pet(pet_object)
                pet_accounts.append(vars(pet_object))
                return pet_object

def load_pet(pet_account):
    # set all values to something in the csv
    
    # save file info
    owner = pet_account['owner']
    pet = pet_account['name']
    species = pet_account['species']
    age = int(pet_account['age'])

    # pet stats
    hunger = int(pet_account['hunger'])
    happiness = int(pet_account['happiness'])
    energy = int(pet_account['energy'])
    cleanliness = int(pet_account['cleanliness'])
    health = float(pet_account['health'])

    # data more prevalent to the owner
    day = int(pet_account['day'])
    time = int(pet_account['time'])
    money = int(pet_account['money'])
    level = int(pet_account['level'])
    xp = int(pet_account['xp'])

    # skills the pet can have
    agility = int(pet_account['agility'])
    obedience = int(pet_account['obedience'])
    tracking = int(pet_account['tracking'])

    # variables for tracking progress in training a skill
    agility_progress = int(pet_account['agility_progress'])
    obedience_progress = int(pet_account['obedience_progress'])
    tracking_progress = int(pet_account['tracking_progress'])

    # inventory items that give boosts
    bed = int(pet_account['bed']) # improves hunger decrease and happiness after sleep
    toy = int(pet_account['toy']) # improves happiness gain and maybe xp after play
    food = int(pet_account['food']) # improves hunger and happiness gain after eating
    brush = int(pet_account['brush']) # improves cleanliness gain after washing

    pet_object = Pet(owner,pet,species,age,hunger,happiness,energy,cleanliness,health,day,time,money,level,xp,agility,obedience,tracking,agility_progress,obedience_progress,tracking_progress,bed,toy,food,brush)
    
    return pet_object