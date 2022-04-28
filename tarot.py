from tarot_detail import *

# Block text
title_banner = """

"""

def line():
    """Prints a line for seperating menus"""
    print("-" * 66)
    
def input_int(min_num: int = -9999999, max_num: int = 9999999):
    """Returns the first integer user input between min_num and max_num"""
    while True:
        try:
            num = int(input(">> "))
            if (num < min_num) or (num > max_num):
                print("Error! Please enter a valid number.")
                continue
            return num
        except ValueError:
            print("Error! Please enter a valid number.")

class GameManager:
    """Class for handling menus(for now)"""
    def display(self):
        """Prints the main menu and waits for input"""
        print(title_banner)
        print(introduction)
        print(instructions_1)
        print(question_1)
        print(question_2)
        print(question_3)
        
        return input_int(1, 3)
    
    def display_help(self, type):
        if type == "help_major":
            line()
            print("This will serve as a guide for you to type in your cards")
            print(major_arcana_to_symbols)
        elif type == "help_wands":
            line()
            print("This will serve as a guide for you to type in your cards")
            print(wands_to_symbols)
        elif type == "help_cups":
            line()
            print("This will serve as a guide for you to type in your cards")
            print(cups_to_symbols)
        elif type == "help_swords":
            line()
            print("This will serve as a guide for you to type in your cards")
            print(swords_to_symbols)
        elif type == "help_symbols":
            line()
            print("This will serve as a guide for you to type in your cards")
            print(pentacles_to_symbols)
        elif type == "help":
            print(instructions_major)
            print(instructions_wands)
            print(instructions_cups)
            print(instructions_swords)
            print(instructions_pentacles)
        else: print("Your input was incorrect, please try again.")
        line()

class GameLoop:
    """Class for handling the flow of the game, such as asking for inputs"""
    
    def __init__(self, question_chose):
        if question_chose == 1:
            pass
menu = GameManager()

while True:
    line()
    option = menu.display()
    line()
    
    if option == 1:
        print(instructions_2)
        while True:
            answer = input('Write your first card with the special syntax. For more information type "help"\n')
            if answer in ["help", "help_major", "help_wands", "help_cups", "help_swords", "help_pentacles"]:
                menu.display_help(answer)
    elif option == 2:
        print("This is still a work in progress, please choose another question.")