###
# Grade: 4/5
#
# Comments:
# - Successfully created an interactive program using classes, properties, and methods
# - A few bugs exist in the submitted version, particularly when using the Help command while picking cards
# - Only one question, but very good replayability due to the various combinations of cards
# - Used docstrings for readability
# - Somewhat clean code, although partly due to having access to an external reference
# - Code can still be improved, but overall, very good work :KyaruCheer:
###

from tarot_detail import *
import textwrap

# Block text
# nice banner
title_banner = """
   /\     ,-----.    ,-----.       ,-----.     ,-----.   ,-----.    /\   
  /  \       |      /       \     |       |   /       \     |      /  \  
 /    \      |     |         |    |       |  |         |    |     /    \ 
/      \     |     |_________|    |------/   |         |    |    /      \              
\      /     |     |         |    |      \   |         |    |    \      /
 \    /      |     |         |    |       |  |         |    |     \    / 
  \  /       |     |         |    |       |   \       /     |      \  /  
   \/        |     |         |    |       |    '-----'      |       \/   
"""

"""Game's parameter"""


def line():
    """Prints a line for seperating menus"""
    print("-" * 66)


# min/max limit a bit unnecessary for this program
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
    """Class for handling menus"""

    def display(self):
        """Prints the main menu and waits for input"""
        print(title_banner)
        # good use of textwrap
        print(textwrap.fill(introduction, 70))
        print(instructions_1)
        print(question_1)
        print(question_2)
        print(question_3)

        return input_int(1, 3)

    def detailed_instructions(self):
        print(textwrap.fill(instructions_2, 70))
        print(" ")
        print(textwrap.fill(instructions_3, 70))

    def display_help(self, type):
        """Prints the help menu"""
        if type == "help_major":
            line()
            print("This will serve as a guide for you to type in your cards:")
            print(major_arcana_to_symbols)
        elif type == "help_wands":
            line()
            print("This will serve as a guide for you to type in your cards:")
            print(wands_to_symbols)
        elif type == "help_cups":
            line()
            print("This will serve as a guide for you to type in your cards:")
            print(cups_to_symbols)
        elif type == "help_swords":
            line()
            print("This will serve as a guide for you to type in your cards:")
            print(swords_to_symbols)
        elif type == "help_symbols":
            line()
            print("This will serve as a guide for you to type in your cards:")
            print(pentacles_to_symbols)
        elif type == "help":
            print(instructions_major)
            print(instructions_wands)
            print(instructions_cups)
            print(instructions_swords)
            print(instructions_pentacles)
        else:
            print("Your input was incorrect, please try again.")
        line()


class GameLoop:
    """Class for handling the flow of the game, such as asking for inputs"""

    def answer(answer, result=0):
        """Converting answer to systematic responses"""
        card = answer + "_" + str(result)
        if result == 0:
            card_0 = cards_positions_to_meaning[card]
            return card_0
        elif result == 1:
            card_1 = cards_positions_to_meaning[card]
            return card_1
        elif result == 2:
            card_2 = cards_positions_to_meaning[card]
            return card_2
        else:
            return ValueError

    def result(list):
        """Prints the results of the reading"""
        print("The result from your tarot reading was:")
        line()
        print("Yourself:")
        print(textwrap.fill(list[0], 70))
        line()
        print("Your partner:")
        print(textwrap.fill(list[1], 70))
        line()
        print("The result:")
        print(textwrap.fill(list[2], 70))

    # No proper error handling for invalid values like "1" or "kyaru"
    def card_error(check):
        """Checking whether two cards are the same or not"""
        if check[0] == check[1]:
            return ValueError
        elif check[1] == check[2]:
            return ValueError
        elif check[0] == check[2]:
            return ValueError

    def card_input(number):
        """Iterating through different questions"""
        if number == 0:
            answer = input(
                'Write your first card with the special syntax. For more information type "help"\n>> ')
        elif number == 1:
            answer = input(
                'Write your second card with the special syntax. For more information type "help"\n>> ')
        elif number == 2:
            answer = input(
                'Write your third card with the special syntax. For more information type "help"\n>> ')
        if answer in ["help", "help_major", "help_wands", "help_cups", "help_swords", "help_pentacles"]:
            menu.display_help(answer)
        elif answer in possible_answers:
            card_answer_position_regard.append(answer)
            card_answer.append(GameLoop.answer(answer, i))
            line()


menu = GameManager()

while True:
    line()
    option = menu.display()
    line()

    if option == 1:
        i = 0
        card_answer = []
        card_answer_position_regard = []
        menu.detailed_instructions
        while i < 3:
            # BUG: if the user uses the help command, it is still considered as though a valid card has been inputted
            GameLoop.card_input(i)
            i += 1
        # could be improved by validating the input immediately upon user entry (during the loop, not after)
        validation = GameLoop.card_error(card_answer_position_regard)
        if validation == ValueError:
            print(textwrap.fill(
                "Two identical cards detected. Please input your cards all over again. The system will now restart.", 70))
            continue
        else:
            GameLoop.result(card_answer)
            line()
            restart = input('Type "restart" to restart the program\n>> ')
            if restart == "restart":
                continue

    # hopefully you finish these other two one day...
    elif option == 2:
        print("This is still a work in progress, please choose another question.")
        continue

    elif option == 3:
        print("This is still a work in progress, please choose another question.")
        continue
    break
