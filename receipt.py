""" WollPay Receipt (Version 04.04 of receipt.py program). """

import random
import datetime
import pytz
import os
import inputvalid as iv
import receiptoutput as ro
from calc import rate_calculating
from cidvalid import cid_validation
from datevalid import get_date
from csvwrite import csv_write

message_cyrillic = 'No cyrillic letters are allowed in this field!'

log_path = './log.csv'  # The relative path to log.csv file.
txt_path = './receipt.txt'  # The relative path to receipt.txt file.
time_zone = 'GMT+2'  # Time zone for Poland.


def receipt():
    """The receipt() function."""
    # The transactions loop.
    i = 'y'
    while i != 'q':
        os.system('cls')  # Clearing the Screen.

        # The Greeting & information.
        print('\nHello Host! \
\nYou run version 04.04 of the program receipt.py.')
        print('Please input the Data of the new Transaction.')
        print('\nFull Path to log.csv file is: \n'
              + os.path.abspath(log_path)
              + '\n')
        print('Full Path to receipt.txt file is: \n'
              + os.path.abspath(txt_path)
              + '\n')

        # The Input Data Block with partly Validation.
        cid = input('CID: ')
        cid = cid_validation(cid)

        input_currency = input('Currency IN: ')
        input_currency = iv.remove_tabs_and_whitespaces(input_currency)
        input_currency = iv.currency_validation(input_currency)

        input_summ = input('Amount IN: ')
        input_summ = iv.valid_number(input_summ, 1)

        output_currency = input('Currency OUT: ')
        output_currency = iv.remove_tabs_and_whitespaces(output_currency)
        output_currency = iv.currency_validation(output_currency)

        output_summ = input('Amount OUT: ')
        output_summ = iv.valid_number(output_summ, 1)

        comment = input('Comment: ')
        comment = iv.remove_cyrillic_and_tabs(comment, message_cyrillic)

        cash_in = input('Cash Registrar IN: ')
        cash_in = iv.valid_number(cash_in, 2)

        cash_out = input('Cash Registrar OUT: ')
        cash_out = iv.valid_number(cash_out, 2)

        new_client_data = input('New data about client: ')
        new_client_data = iv.remove_cyrillic_and_tabs(new_client_data,
                                                      message_cyrillic)

        covered = input('Covered: ')
        covered = iv.remove_cyrillic_and_tabs(covered)
        covered = iv.yes_or_no(covered)

        general1 = input('General1: ')
        general1 = iv.remove_cyrillic_and_tabs(general1, message_cyrillic)

        general2 = input('General2: ')
        general2 = iv.remove_cyrillic_and_tabs(general2, message_cyrillic)

        # The calculating of the rate.
        rate = rate_calculating(input_summ, output_summ)

        # The Transaction's random ID calculating.
        transaction_ID = random.randint(0, 999999999999)
        transaction_ID = str(transaction_ID).zfill(12)

        # Current Date & Time getting (for Poland).
        current_time = datetime.datetime.now(pytz.timezone('Poland')) \
            .strftime('%I:%M %p')

        # Input the current date manualy or get from Inet.
        current_date = input('Date: ')
        current_date = get_date(current_date)

        # The Receipt items' values.
        receipt_items = [
            input_currency,
            input_summ,
            output_currency,
            output_summ,
            current_date,
            current_time,
            time_zone,
            transaction_ID,
            rate
        ]

        # The current Receipt's printing (the output to console).
        ro.cli_receipt(receipt_items)

        # The current Receipt's appanding in the receipt.txt file.
        ro.txt_receipt(receipt_items)

        # log.csv file data:
        # The Fields names:
        csv_fields = [
            'TID',  # TransactionID
            'Date',
            'Time',
            'TZ',  # TimeZone
            'CID',
            'Currency1',
            'Amount1',
            'Currency2',
            'Amount2',
            'Rate',
            'Comment',
            'CashRegistrarIN',
            'CashRegistrarOUT',
            'NewData',
            'Covered',
            'General1',
            'General2'
        ]

        # The Fields values.
        csv_row = [
            transaction_ID,
            current_date,
            current_time,
            time_zone,
            cid,
            input_currency,
            # input_summ,
            ro.float_to_int(input_summ, 2),
            output_currency,
            # output_summ,
            ro.float_to_int(output_summ, 2),
            rate,
            comment,
            cash_in,
            cash_out,
            new_client_data,
            covered,
            general1,
            general2
        ]

        # Checking the log.csv file existing and writing to log.csv.
        csv_write(log_path, csv_fields, csv_row)

        # The end of the loop.
        i = input('\nAnother Transaction? (Press "q" to exit, \
or "ENTER" to continue): ')
        i = iv.exit_test(i)

    input('Press "ENTER" to exit receipt.py: ')  # Exit.
    return


if __name__ == "__main__":
    receipt()
