"""phonevalid.py"""

from inputvalid import cyrillic_presence_test, remove_tabs_and_whitespaces

message_cyrillic = 'No cyrillic letters are allowed in this field!'


def force_empty_phone_number(phone_number):
    """Empty phone_number ability to input."""
    result = False
    result = input('Do you really want to leave "PhoneNumber" \
field empty (y/n)?: ')
    result = cyrillic_presence_test(result, message_cyrillic)
    result = remove_tabs_and_whitespaces(result)
    if result == 'y' or result == 'Y':
        phone_number = ''
    else:
        phone_number = phone_number_validation(phone_number)  # Validation.
    return phone_number


def empty_phone_number(phone_number):
    """Testing phone number input."""
    phone_number = cyrillic_presence_test(phone_number, message_cyrillic)
    phone_number = remove_tabs_and_whitespaces(phone_number)
    if phone_number == '':
        phone_number = force_empty_phone_number(phone_number)
    else:
        phone_number = phone_number_validation(phone_number)  # Validation.
    return phone_number


def phone_number_validation(number):
    """Phone number validation.
    Sign '+' allowed on the first position.
    """
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)
    # Empty phone number is not allowed.
    if number != '':
        pass
    else:
        print('Error: More digits should be in "PhoneNumber" field!')
        number = input('Repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = empty_phone_number(number)
        if number == '':
            return number
    # Here 6 is minimum digits in phone number.
    if len(number) >= 6:
        pass
    else:
        print('Error: More digits should be in "PhoneNumber" field!')
        number = input('Repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = empty_phone_number(number)
        if number == '':
            return number
    first_sign = ['+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if number[0] in first_sign:
        pass
    else:
        print('Error: Only decimal digits and "+" sign \
on first position are allowed in "PhoneNumber" field!')
        number = input('Repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = empty_phone_number(number)
        if number == '':
            return number
    sub_number = number[1:]  # Validating the string after first sign.
    if sub_number.isdecimal():
        pass
    else:
        print('Error: Only decimal digits and "+" sign \
on first position are allowed in "PhoneNumber" field!')
        number = input('Repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = empty_phone_number(number)
        if number == '':
            return number
    return number
