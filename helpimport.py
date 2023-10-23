"""The ability to go back to main menu."""

from wollpay import wollpay
from inputvalid import exit_test


def help_import():
    """Function give the ability to go back 
    into the main menu.
    """
    result = ''
    print('\nWould you like to continue or prefer to go back in main menu?')
    k = input('To continue press "ENTER", to go back in main menu press "q": ')
    k = exit_test(k)
    if k in ['q']:
        result = str(wollpay())
    else: pass
    return result


def help_start():
    """Function give the ability to start the main menu
    in wollpay.py.
    """
    return str(wollpay())
