""" WollPay Clients Base (Version 01.05 of the clientsbase.py). """

import os
import inputvalid as iv
from phonevalid import empty_phone_number
from datevalid import get_date
from csvwrite import csv_write, file_read
import helpimport as hi

message_cyrillic = 'No cyrillic letters are allowed in this field!'

base_path = './clients_base.csv'  # The relative path to clients_base.csv.
source_path = './source.txt'  # Relative path to pre builded source.txt file.


def clientsbase():
    """Appending of the wollpay clients base' data."""
    # The initialisation of the lists' block:
    source_list = list(file_read(source_path))
    type_1 = [
        'Client',
        'Dealer'
    ]  # 2
    type_2 = [
        'Primary',
        'Dependent'
    ]  # 2
    type_3 = [
        'RENEWABLE',
        'LIMITED',
        'RETAIL',
        'N/A-DEALER'
    ]  # 4
    entity_list = [
        'Natural',
        'Legal'
    ]  # 2

    # The clients' input loop.
    i = 'y'
    while i != 'q':
        os.system('cls')  # Clearing the Screen.
        
        # The Greeting & information.
        print('Hello Host! \nYou run version 01.05 of the \
clientsbase.py program.')
        
        result = hi.help_import()  # The ability to go back in main menu.
        if result == 'Exit': return result
        else: pass

        print('\nInput the Data of the new Client.')
        print('\nFull Path to the clients_base.csv file is: \n'
              + os.path.abspath(base_path)
              + '\n')

        # The Input Data Block with partly Validation.
        cid = input('CID: ')
        cid = iv.cid_checking('CID', cid)

        first_name = input('FirstName: ')
        first_name = iv.remove_cyrillic_and_tabs(first_name,
                                                 message_cyrillic)

        last_name_1 = input('LastName1: ')
        last_name_1 = iv.remove_cyrillic_and_tabs(last_name_1,
                                                  message_cyrillic)

        last_name_2 = input('LastName2: ')
        last_name_2 = iv.remove_cyrillic_and_tabs(last_name_2,
                                                  message_cyrillic)

        middle_names = input('MiddleName: ')
        middle_names = iv.remove_cyrillic_and_tabs(middle_names,
                                                   message_cyrillic)

        source = iv.choose_item('Source', source_list, 1)

        rate_agnostic = input('RateAgnostic: ')
        rate_agnostic = iv.one_or_zero(rate_agnostic)

        phone_number = input('PhoneNumber: ')  # Phone input and validation.
        phone_number = empty_phone_number(phone_number)

        type1 = iv.choose_item('Type1', type_1)
        type2 = iv.choose_item('Type2', type_2)
        type3 = iv.choose_item('Type3', type_3)
        entity = iv.choose_item('Entity', entity_list)

        if type2 == 'Dependent':
            dependent = input('Dependent: ')
            dependent = iv.cid_checking('Dependent', dependent)
        else:
            dependent = ''

        base_currency = input('BaseCurrency: ')
        base_currency = iv.currency_validation(base_currency)

        home_address = input('HomeAddress: ')
        home_address = iv.remove_cyrillic_and_tabs(home_address,
                                                   message_cyrillic)

        telegram_name1 = input('TelegramName1: ')
        telegram_name1 = iv.remove_cyrillic_and_tabs(telegram_name1,
                                                     message_cyrillic)

        telegram_name2 = input('TelegramName2: ')
        telegram_name2 = iv.remove_cyrillic_and_tabs(telegram_name2,
                                                     message_cyrillic)

        facebook_link1 = input('FacebookLink1: ')
        facebook_link1 = iv.remove_cyrillic_and_tabs(facebook_link1,
                                                     message_cyrillic)

        facebook_link2 = input('FacebookLink2: ')
        facebook_link2 = iv.remove_cyrillic_and_tabs(facebook_link2,
                                                     message_cyrillic)

        instagram_link1 = input('InstagramLink1: ')
        instagram_link1 = iv.remove_cyrillic_and_tabs(instagram_link1,
                                                      message_cyrillic)

        instagram_link2 = input('InstagramLink2: ')
        instagram_link2 = iv.remove_cyrillic_and_tabs(instagram_link2,
                                                      message_cyrillic)

        city = input('City: ')
        city = iv.remove_cyrillic_and_tabs(city, message_cyrillic)

        country = input('Country: ')
        country = iv.remove_cyrillic_and_tabs(country, message_cyrillic)

        comments = input('Comments: ')
        comments = iv.remove_cyrillic_and_tabs(comments, message_cyrillic)

        # Input the 'DateAdded' manualy or get from Inet.
        date_added = input('DateAdded: ')
        date_added = get_date(date_added)

        # clients_base.csv file data:
        # Fields' names:
        csv_fields = [
            'CID',
            'FirstName',
            'LastName1',
            'LastName2',
            'MiddleName',
            'Source',
            'RateAgnostic',
            'PhoneNumber',
            'Type1',
            'Type2',
            'Type3',
            'Entity',
            'Dependent',
            'BaseCurrency',
            'HomeAddress',
            'DateAdded',
            'TelegramName1',
            'TelegramName2',
            'FacebookLink1',
            'FacebookLink2',
            'InstagramLink1',
            'InstagramLink2',
            'City',
            'Country',
            'Comments'
        ]

        # Fields' values.
        csv_row = [
            cid,
            first_name,
            last_name_1,
            last_name_2,
            middle_names,
            source,
            rate_agnostic,
            phone_number,
            type1,
            type2,
            type3,
            entity,
            dependent,
            base_currency,
            home_address,
            date_added,
            telegram_name1,
            telegram_name2,
            facebook_link1,
            facebook_link2,
            instagram_link1,
            instagram_link2,
            city,
            country,
            comments
        ]

        # Checking the clients_base.csv file existing
        # and writing to clients_base.csv file.
        csv_write(base_path, csv_fields, csv_row)

        # The end of the loop.
        i = input('\nInput another client data? (Press "q" to exit, \
or "ENTER" to continue): ')
        i = iv.exit_test(i)

    input('Press "ENTER" to exit clientsbase.py: ')  # Exit.
    return result


if __name__ == "__main__":
    clientsbase()
