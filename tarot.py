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
    
    
    print(instructions_2)