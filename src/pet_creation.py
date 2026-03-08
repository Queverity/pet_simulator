# CB 1st Pet Creating Functions

import random

# class Pet:
    # create _init_ method
    # define attributes for the pet (happiness, hunger, level, age, stuff like that)
    # create other methods (play, feed, sleep, clean) for pet

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

