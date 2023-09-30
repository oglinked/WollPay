"""inputvalid.py
The validating inputed values.
"""

import re

message_latin = 'Only Latin letters are allowed in this field!'
message_cyrillic = 'No cyrillic letters are allowed in this field!'


def cyrillic_presence_test(string, message=message_latin):
    """No cyrillic letters please."""
    result = re.findall("[а-яА-Я]", string)
    if not bool(result):
        pass
    else:
        print(f'Error: {message}')
        string = input('Repeat input: ')
        string = cyrillic_presence_test(string, message)
        # It was Recursion.
    return string


def remove_tabs(string):
    """Code to remove tabulation."""
    if '\t' in string:
        print('Warning: Inputted Tabs characters were removed!')
    return string.replace('\t', '')


def check_letters(string):
    """Checking for absence of letters in given string."""
    string = cyrillic_presence_test(string)
    string = remove_tabs(string)
    result = True  # Initializing result variable.
    for i in string:
        if i.isalpha():  # If string has letter:
            result = False
    return result


def remove_cyrillic_and_tabs(string, message=message_latin):
    """Cyrillic + Tabs removing."""
    string = cyrillic_presence_test(string, message)
    string = remove_tabs(string)
    return string


def remove_whitespaces(string):
    """Code to remove whitespaces."""
    if ' ' in string:
        print('Warning: Inputted whitespaces were removed!')
    return string.replace(" ", "")


def remove_tabs_and_whitespaces(string):
    """Code to remove tabulation and whitespaces."""
    string = remove_tabs(string)
    string = remove_whitespaces(string)
    return string


def str_valid_to_upper(string):
    """ String validation.
    Capital letters only. No numbers.
    string - parameter (Input string to validation).
    """
    string = cyrillic_presence_test(string)
    string = remove_tabs(string)
    if string.isalpha():
        pass
    else:
        print('Error: Only Latin letters are allowed in this field!')
        string = input('Repeat input: ')
        string = cyrillic_presence_test(string)
        string = remove_tabs(string)
        string = str_valid_to_upper(string)  # Recursion.
    string = string.upper()
    return string


def valid_decimal(number, sign_control=0):  # Now sign control is "off".
    """ Number validation.
    Decimal digits ( > 0 ) are allowed only.
    number - parameter (Input string to validation).
    """
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)

    if number.isdecimal():
        pass
    else:
        print('Error: Only decimal digits are allowed in this field!')
        number = input('Repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = valid_decimal(number, sign_control)  # Recursion.

    if sign_control == 1:
        number = int(number)  # str --> int
        if number > 0: pass  # Only decimal digits > 0 are allowed.
        else:
            print('Error: Only decimal digits > 0 are allowed \
in this field!')
            number = input('Repeat input: ')
            number = valid_decimal(number, sign_control)  # Recursion.
    else: pass

    return str(number)  # Back int --> str


def isfloat(number):
    """Python Program to Check If a String Is a Number (Float)"""
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)
    try:
        float(number)
        return True
    except ValueError:
        return False


def valid_number(number, sign_control=1):
    """ Number validation.
    Numbers only. Dots are allowed to float numbers.
    number - parameter (Input string to validation).
    """
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)

    if number.isdecimal():
        pass
    elif isfloat(number):
        pass
    else:
        print('Error: Only decimal digits (and one dot) \
are allowed in this field!')
        number = input('Repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = valid_number(number, sign_control)  # Recursion.

    if sign_control == 1:
        number = float(number)  # str --> float
        if number > 0: pass  # Only numbers >= 0 are allowed.
        else:
            print('Error: Only numbers > 0 are allowed \
in this field!')
            number = input('Repeat input: ')
            number = valid_number(number, sign_control)  # Recursion.
    else: pass

    return str(number)  # Back float --> str


def yes_or_no(string):
    """Only "y","Y" or "n","N" are allowed."""
    # Removing "\t" and " ".
    string = remove_tabs_and_whitespaces(string)
    if string in ['y', 'Y']:
        string = 'Y'
    elif string in ['n', 'N']:
        string = 'N'
    else:
        print('Error: Only "Y" or "N" are allowed in this field!')
        string = input('Repeat input: ')
        string = cyrillic_presence_test(string,
                                        message_cyrillic)
        # Removing "\t" and " ".
        string = remove_tabs_and_whitespaces(string)
        string = yes_or_no(string)  # Recursion.
    return string


def currency_validation(currency):
    """Checks if the currency's input was right."""
    currency = cyrillic_presence_test(currency)
    currency = remove_tabs(currency)
    if len(currency) < 1:  # Minimum 1 character should be present.
        print('Error: Too few characters were inputted!')
        currency = input('Repeat Input: ')
        currency = currency_validation(currency)  # Recursion.
    currency = str_valid_to_upper(currency)
    return currency


def amount_validation(amount):
    """Amount validation."""
    amount = cyrillic_presence_test(amount, message_cyrillic)
    amount = remove_tabs(amount)
    if len(amount) < 1:  # Minimum 1 character should be present.
        print('Error: Too few characters were inputted.')
        amount = input('Repeat Input: ')
        amount = amount_validation(amount)  # Recursion.
    amount = valid_number(amount)
    return amount


def exit_test(i):
    """Exit or continue validation test."""
    i = cyrillic_presence_test(i, message_cyrillic)
    i = remove_tabs_and_whitespaces(i)
    if i in ['q', '']:
        pass
    else:
        print('Error: only "q" or "ENTER" are allowed!')
        i = input('Press "q" to exit, or "ENTER" to continue): ')
        i = exit_test(i)  # Recursion.
    return i


def one_or_zero(string):
    """Only "1" or "0" are valid values to input parameter."""
    string = cyrillic_presence_test(string,
                                    message_cyrillic)
    string = remove_tabs_and_whitespaces(string)
    if string in ["1", "0"]:
        pass
    else:
        print('Error: Only "1" or "0" without spaces \
are allowed in this field!')
        string = input('Repeat input: ')
        string = cyrillic_presence_test(string,
                                        message_cyrillic)
        string = remove_tabs_and_whitespaces(string)
        string = one_or_zero(string)  # Recursion.
    return string


def number_validation(number, max_number, min_number=1):
    """Number validation integer 
    in interval [min_number, max_number].
    """
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)

    if number.isdigit():  # Only decimal digits.
        number = int(number)
    else:
        print(
            f'Error: The item number shold be decimal digit \
in [{min_number}, {max_number}].')
        number = input('Repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        # Recursion.
        number = number_validation(number, max_number, min_number)

    if number in range(min_number, max_number+1):
        # Only in range [min_number, max_number].
        pass
    else:
        print(
            f'Error: The item number shold be decimal digit \
in [{min_number}, {max_number}].')
        number = input('Repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        # Recursion.
        number = number_validation(number, max_number, min_number)
    return number


def choose_item(item_name, item_menu):
    """Drop-down menu analog."""
    print(f'\nThe {item_name} menu Table: \n')  # Table's title.
    if item_name == 'Source':
        for i, item in enumerate(item_menu, start=1):
            print(i, item, end='')
        number = input('\n\nChoose and input the number: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        # Validation.
        number = number_validation(number, len(item_menu))
        number = int(number)
        return number  # Output for 'Source'.
    else:
        for i, item in enumerate(item_menu, start=1):
            print(i, item)
        number = input('\nChoose and Input the number: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = number_validation(number, len(item_menu))  # Validation.
        number = int(number)
        return item_menu[number - 1]  # If not 'Source'.


def empty_field(field):
    """"Please repeat input": if field is empty and I press
    "Enter", make the program ask me if I really want
    to leave this field empty y/n?.
    """
    field = cyrillic_presence_test(field, message_cyrillic)
    field = remove_tabs_and_whitespaces(field)  # Remove "\t" and " ".
    if field == '':
        field = force_empty_field(field)
    else:
        field = valid_decimal(field, 0)
    return field


def force_empty_field(field):
    """Empty (or ...) field's value."""
    result = False
    result = input('Do you really want to leave this field empty (y/n)?: ')
    result = cyrillic_presence_test(result, message_cyrillic)
    result = remove_tabs(result)
    if result in ['y', 'Y']:
        field = ''
    else:
        field = valid_decimal(field, 0)  # Go to
    return field
