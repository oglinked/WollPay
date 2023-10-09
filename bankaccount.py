""" WollPay Bank Account Details
(Version 01.04 of bankaccount.py).
"""

import os
import inputvalid as iv
from phonevalid import empty_phone_number
from cidvalid import cid_validation
from datevalid import get_date
from csvwrite import csv_write

message_cyrillic = 'No cyrillic letters are allowed in this field!'

# The relative path to the bank_account_details.csv file.
account_details_path = './bank_account_details.csv'
time_zone = 'GMT+2'  # Time zone for Poland.


def account():
    """Wollpay clients' bank accounts details."""
    # The clients' input loop.
    i = 'y'
    while i != 'q':
        os.system('cls')  # Clearing the Screen.
        # The Greeting & information.
        print('Hello Host! \nYou run version 01.04 of the program \
bankaccount.py.')
        print('Enter data for a new client account.')
        print('\nFull Path to bank_account_details.csv file is: \n'
              + os.path.abspath(account_details_path)
              + '\n')

        # The Input Data Block with partly Validation.
        cid = input('CID: ')
        cid = cid_validation(cid)

        bank_name = input('BankName: ')
        bank_name = iv.remove_cyrillic_and_tabs(bank_name, message_cyrillic)

        country = input('Country: ')
        country = iv.remove_cyrillic_and_tabs(country, message_cyrillic)

        bank_home_address = input('BankHomeAddress: ')
        bank_home_address = iv.remove_cyrillic_and_tabs(
            bank_home_address, message_cyrillic)

        currency = input('Currency: ')
        currency = iv.currency_validation(currency)

        account_number = input('AccountNumber: ')
        account_number = iv.remove_cyrillic_and_tabs(account_number,
                                                     message_cyrillic)

        card_number = input('CardNumber: ')
        card_number = iv.valid_decimal(card_number)

        phone_number = input('PhoneNumber: ')  # Phone input and validation.
        phone_number = empty_phone_number(phone_number)

        agreement_number = input('AgreementNumber: ')
        agreement_number = iv.valid_decimal(agreement_number)

        bic = input('BIC: ')
        bic = iv.remove_cyrillic_and_tabs(bic, message_cyrillic)

        routing_number = input('RoutingNumber: ')
        routing_number = iv.remove_cyrillic_and_tabs(routing_number,
                                                     message_cyrillic)

        swift_code = input('SWIFTCODE: ')
        swift_code = iv.remove_cyrillic_and_tabs(swift_code,
                                                 message_cyrillic)

        sort_code = input('SORTCODE: ')
        sort_code = iv.remove_cyrillic_and_tabs(sort_code,
                                                message_cyrillic)

        account_home_address_1 = input('AccountHomeAddress1: ')
        account_home_address_1 = iv.remove_cyrillic_and_tabs(
            account_home_address_1,
            message_cyrillic)

        account_home_address_2 = input('AccountHomeAddress2: ')
        account_home_address_2 = iv.remove_cyrillic_and_tabs(
            account_home_address_2,
            message_cyrillic)

        internal_tag = input('InternalTag: ')
        internal_tag = iv.remove_cyrillic_and_tabs(internal_tag,
                                                   message_cyrillic)

        # Input the 'DateAdded' manualy or get current date.
        date_added = input('DateAdded: ')
        date_added = get_date(date_added)

        # bank_account_details.csv file data:
        # Fields' names:
        csv_fields = [
            'CID',
            'BankName',
            'Country',
            'BankHomeAddress',
            'Currency',
            'AccountNumber',
            'CardNumber',
            'PhoneNumber',
            'AgreementNumber',
            'BIC',
            'RoutingNumber',
            'SWIFTCODE',
            'SORTCODE',
            'AccountHomeAddress1',
            'AccountHomeAddress2',
            'InternalTag',
            'DateAdded'
        ]

        # Fields' values:
        csv_row = [
            cid,
            bank_name,
            country,
            currency,
            bank_home_address,
            account_number,
            card_number,
            phone_number,
            agreement_number,
            bic,
            routing_number,
            swift_code,
            sort_code,
            account_home_address_1,
            account_home_address_2,
            internal_tag,
            date_added
        ]

        # Checking the bank_account_details.csv file existing
        # and writing to bank_account_details.csv file.
        csv_write(account_details_path, csv_fields, csv_row)

        # The end of the loop.
        i = input('\nInput another client account? (Press "q" to exit, \
or "ENTER" to continue): ')
        i = iv.exit_test(i)

    input('Press "ENTER" to exit bankaccount.py: ')  # Exit.
    return


if __name__ == "__main__":
    account()
