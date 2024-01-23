"""wollpay.py (version 00.07 without balance.py) is programmes' Hub.
To run wollpay.py you should run startpay.py program.

The Project wollpay.py is a CLI version of programmes' Hub for bank transactions' 
small startup, written fully with Python programming language.

WARNING: 
If you going to run exactly wollpay.py in python environment, you should run 
startpay.py program. It's importent tricky moment to avoid 
"ImportError:(most likely due to a circular import)".
If you gonna run wollpay.exe instead, than simply run it!

The functional inside wollpay.py is:
1. To make a receipt for the new transaction;
2. To append clients base with the new client;
3. To append banks accounts data of the WollPay clients;
4. To edit CSV files' database contents.

After programm starts you choose the item from menu "What to do" and 
run one of programmes:
1. receipt.py
2. clientsbase.py
3. bankaccount.py
4. csvedit.py
You can always return to the main menu or EXIT the program.
"""

import os
import sys
import inputvalid as iv
from receipt import receipt
from clientsbase import clientsbase
from bankaccount import bankaccount
from csvedit import csvedit
# from balance import balance

menu_list = [
        'To make a receipt for the new transaction?',
        'To append clients base with the new client?',
        'To append banks accounts data of the WollPay clients?',
        'To edit one of your CSV files?',
        # 'To calculate intermediate balance?',
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
    \nYou run version 00.07 of the program wollpay.py without balance.py. \
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
        # elif item == menu_list[4]:
        #     balance()
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
