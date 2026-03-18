# CB 1st Helper Functions

# function clear_screen():
    # print function to clear the screen, take this from another project

# function press_enter():
    # print something like "Press Enter to Continue", put an input() statement after that

# function print_slow():
    # A function to print out characters slowly so it looks like someone is typing them
    # Take this from another project

    
def clear_screen():
    print("\033c", end="")

def continue_screen():
    print("Press Enter to continue.")
    input()

def after_action():
    continue_screen()
    clear_screen()

def max_min_checker(value):
    if value > 100:
        value = 100
    elif value < 0:
        value = 0
    else:
        pass

    return value
