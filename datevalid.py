"""datevalid.py"""

import datetime
from inputvalid import test_cyr_tabs_whitespaces, check_letters

message_cyrillic = 'No cyrillic letters are allowed in this field!'


def empty_date(date):
    """"Please repeat input": if field is empty and I press
    "Enter", make the program ask me if I really want
    to leave this field empty y/n?.
    """
    date = test_cyr_tabs_whitespaces(date, message_cyrillic)
    if date in ['']:
        date = force_empty_date(date)
    else:
        date = date_validation(date)
    return date


def force_empty_date(date):
    """Empty (or current) date."""
    # result = input('Do you really want to leave this field empty (y/n)?: ')
    result = input('Do you want to get current date to this field (y/n)?: ')
    result = test_cyr_tabs_whitespaces(result, message_cyrillic)
    if result in ['y', 'Y', '']:
        # date = '' # Empty field.
        date = datetime.datetime.now(datetime.UTC).astimezone() \
            .strftime("%m/%d/%Y")  # Getting current date.
    else:
        date = date_validation(date)
    return date


def date_validation(date):
    """ Date validation.
    date - parameter (Inputed date to validation).
    """
    date = test_cyr_tabs_whitespaces(date, message_cyrillic)
    # Testing the length of the field.
    if len(date) == 10:
        pass
    else:
        print('Error: In this field should be 10 characters.')
        date = input('Repeat date input in mm/dd/yyyy mode: ')
        date = empty_date(date)
        if date == datetime.datetime.now(datetime.UTC).astimezone() \
            .strftime("%m/%d/%Y"):  # Getting current date.
            return date
    # Testing the absence of alphabetical letters.
    if check_letters(date):
        pass
    else:
        print('Error: No letters are allowed in this field!')
        date = input('Repeat input: ')
        date = empty_date(date)
        if date == datetime.datetime.now(datetime.UTC).astimezone() \
            .strftime("%m/%d/%Y"):  # Getting current date.
            return date
    # Testing the presence of two "/" characters.
    if date[2] == date[5] == '/':
        pass
    else:
        print('Error: Check the presence of "/" characters in right places!')
        date = input('Repeat input: ')
        date = empty_date(date)
        if date == datetime.datetime.now(datetime.UTC).astimezone() \
            .strftime("%m/%d/%Y"):  # Getting current date.
            return date
    # Testing "mm" in mm/dd/yyyy
    mm = ['01', '02', '03', '04', '05', '06',
          '07', '08', '09', '10', '11', '12']
    month = date[0] + date[1]
    if month in mm:
        pass
    else:
        print('Error: The Month value should be in [01,...,12].')
        date = input('Repeat input: ')
        date = empty_date(date)
        if date == datetime.datetime.now(datetime.UTC).astimezone() \
            .strftime("%m/%d/%Y"):  # Getting current date.
            return date
    # Testing "dd" in mm/dd/yyyy
    dd = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
          '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
          '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
          '31']
    day = date[3] + date[4]
    if day in dd:
        pass
    else:
        print('Error: The Day value should be in [01,...,31].')
        date = input('Repeat input: ')
        date = empty_date(date)
        if date == datetime.datetime.now(datetime.UTC).astimezone() \
            .strftime("%m/%d/%Y"):  # Getting current date.
            return date
    # Testing "yyyy" in mm/dd/yyyy
    yyyy = ['2022', '2023', '2024', '2025', '2026', '2027', '2028',
            '2029', '2030', '2031', '2032', '2033', '2034', '2035']
    year = date[6] + date[7] + date[8] + date[9]
    if year in yyyy:
        pass
    else:
        print('Error: The Year value should be in [2022,...,2035].')
        date = input('Repeat input: ')
        date = empty_date(date)
        if date == datetime.datetime.now(datetime.UTC).astimezone() \
            .strftime("%m/%d/%Y"):  # Getting current date.
            return date
    return date


def get_date(date):
    """Current date for Poland if argument == ''."""
    if date in ['']:
        date = datetime.datetime.now(datetime.UTC).astimezone() \
            .strftime("%m/%d/%Y")  # Getting current date.
    else:
        date = date_validation(date)  # Validation
    return date
