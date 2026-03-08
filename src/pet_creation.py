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
        self.owner = owner
        self.name = name
        self.species = species
        self.age = age
        self.hunger = 80
        self.happiness = 80
        self.energy = 80
        self.cleanliness = 80
        self.health = 100
        self.day = 1
        self.time = 8
        self.money = 50
        self.level = 1
        self.xp = 0

    def evaluate_health(self):
        self.health = (self.hunger + self.cleanliness + self.happiness) / 3

    def check_level(self):
        

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

    def pass_time(self,elapsed_time):
        print("Time passes...")
        self.time += elapsed_time
        self.random_event()

    def play_with_pet(self):
        print("How would you like to play with your pet?\n1. Go to a park and run around (Free, +10 Happiness, +5 xp)\n2. ")

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
                    add_pet(pet_object)
                    return pet_object
                
create_pet(avaiable_species)

