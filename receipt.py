""" WollPay Receipt (Version 04.06 of receipt.py program). """

import random
import datetime
import os
import inputvalid as iv
import receiptoutput as ro
from calc import rate_calculating
from datevalid import get_date
from csvwrite import csv_write
import helpimport as hi

message_cyrillic = 'No cyrillic letters are allowed in this field!'

log_path = './log.csv'  # The relative path to log.csv file.
txt_path = './receipt.txt'  # The relative path to receipt.txt file.

# Getting current Date, Time and local TimeZone from inet:
local_time_zone = datetime.datetime.now(datetime.UTC) \
.astimezone().strftime("UTC%z")[:-2]
entry_time_zone = local_time_zone
entry_time = datetime.datetime.now(datetime.UTC).astimezone() \
            .strftime('%I:%M %p')
entry_date = datetime.datetime.now(datetime.UTC).astimezone() \
            .strftime("%m/%d/%Y")

# time_zone = 'GMT+2'  # Time zone for Poland.
# entry_time_zone = time_zone
# entry_time = datetime.datetime.now(pytz.timezone('Poland')) \
#             .strftime('%I:%M %p')
# entry_date = datetime.datetime.now(pytz.timezone('Poland')) \
#             .strftime("%m/%d/%Y")


def receipt():
    """The receipt() function."""
    # The transactions loop.
    i = 'y'
    while i != 'q':

        os.system('cls')  # Clearing the Screen.

        # The Greeting & information.
        print('\nHello Host! \
\nYou run version 04.06 of the program receipt.py.') 
               
        result = hi.help_import()  # The ability to go back in main menu.
        if result == 'Exit': return result
        else: pass

        print('\nInput new Transaction Data.')
        print('\nFull Path to log.csv file is: \n'
              + os.path.abspath(log_path))
        print('Full Path to receipt.txt file is: \n'
              + os.path.abspath(txt_path)
              + '\n')

        # The Transaction's random ID calculating.
        # transaction_ID = random.randint(0, 999999999999)
        # transaction_ID = str(transaction_ID).zfill(12)
        transaction_ID = random.randint(100000000000, 999999999999)
        transaction_ID = str(transaction_ID)
        print(f'TID: {transaction_ID}')
        
        # The Input Data Block with partly Validation:
        cid = input('CID: ')
        cid = iv.cid_checking('CID', cid)

        input_currency = input('Currency IN: ')
        input_currency = iv.remove_tabs_and_whitespaces(input_currency)
        input_currency = iv.currency_validation(input_currency)

        input_summ = input('Amount IN: ')
        input_summ = iv.amount_checking(input_summ)

        output_currency = input('Currency OUT: ')
        output_currency = iv.remove_tabs_and_whitespaces(output_currency)
        output_currency = iv.currency_validation(output_currency)

        output_summ = input('Amount OUT: ')
        output_summ = iv.amount_checking(output_summ)
        
        comment = input('Comment: ')
        comment = iv.remove_cyrillic_and_tabs(comment, message_cyrillic)

        cash_in = input('Cash Registrar IN: ')
        cash_in = iv.valid_number(cash_in, 2)
        cash_in = ro.float_to_int(cash_in)

        cash_out = input('Cash Registrar OUT: ')
        cash_out = iv.valid_number(cash_out, 2)
        cash_out = ro.float_to_int(cash_out)

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

        # Current Date & Time getting.
        current_time = datetime.datetime.now(datetime.UTC).astimezone() \
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
            local_time_zone,
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
            'EntryAddedDate',
            'EntryAddedTime',
            'EntryAddedTimeZone',
            'General1',
            'General2'
        ]

        # The Fields values.
        csv_row = [
            transaction_ID,
            current_date,
            current_time,
            local_time_zone,
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
            entry_date,
            entry_time,
            entry_time_zone,
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
    return result


if __name__ == "__main__":
    receipt()
