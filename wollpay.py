"""wollpay.py (version 00.05) is programmes' Hub.
To run wollpay.py you should run startpay.py program.
"""

import os
import sys
import inputvalid as iv
from receipt import receipt
from clientsbase import clientsbase
from bankaccount import bankaccount
from csvedit import csvedit

menu_list = [
        'To make a receipt for the new transaction?',
        'To append clients base with the new client?',
        'To append banks accounts data of the WollPay clients?',
        'To edit one of your CSV files?',
        'Exit!'
    ]


def wollpay():
    """The programmes' Hub function."""
    # The input loop.
    i = 'y'
    while i != 'q':
        os.system('cls')  # Clearing the Screen.
        # The Greeting & information.
        print('\nHello Host! \
    \nYou run version 00.05 of the program wollpay.py. \
    \nWhat do you prefer to do?')

        item = iv.choose_item('\"What to do\"', menu_list)

        if item == menu_list[0]:
            receipt()
        elif item == menu_list[1]:
            clientsbase()
        elif item == menu_list[2]:
            bankaccount()
        elif item == menu_list[3]:
            csvedit()
        else:
            pass

        # The end of the loop.
        i = input('\nWould you like to continue with wollpay.py?  \
    \n(Press "ENTER" to continue, or "q" to exit): ')
        i = iv.exit_test(i)

    input('Press "ENTER" to exit wollpay.py: ')  # Exit.
    sys.exit(input('Good Job. Well done!! \nPress "ENTER": '))
    return


if __name__ == "__main__":
    wollpay()
