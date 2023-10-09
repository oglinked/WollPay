"""receiptoutput.py
The Rceipt output script.
"""


def cli_receipt(items):
    """The current Receipt's printing (the output to console)."""
    [
        input_currency,
        input_summ,
        output_currency,
        output_summ,
        current_date,
        current_time,
        time_zone,
        transaction_ID,
        rate
    ] = list(items)
    print('\n\n----------Welcome to WollPay!----------\n')
    print('Transfer:       ',
          input_currency,
          float_to_int(input_summ, 2),
          '-->',
          output_currency,
          float_to_int(output_summ, 2))
    print('Date:           ', current_date)
    print('Time:           ', current_time, '(' + time_zone + ')')
    print('TransactionID:  ', transaction_ID)
    print('Rate:           ', rate)
    print('\nThank you for being a WollPay customer!')
    print('----------------WollPay----------------\n\n')
    return


def txt_receipt(items):
    """ The current Receipt's appanding in the receipt.txt file. """
    [
        input_currency,
        input_summ,
        output_currency,
        output_summ,
        current_date,
        current_time,
        time_zone,
        transaction_ID,
        rate
    ] = list(items)
    input_summ = float_to_int(input_summ, 2)
    output_summ = float_to_int(output_summ, 2)
    with open('receipt.txt', 'a') as f:
        f.write('\n----------Welcome to WollPay!----------\n')
        f.write('\nTransfer:       '
                + input_currency
                + ' '
                + input_summ 
                + ' --> '
                + output_currency
                + ' '
                + output_summ)
        f.write('\nDate:           ' + current_date)
        f.write('\nTime:           ' + current_time
                + ' ' + '(' + time_zone + ')')
        f.write('\nTransactionID:  ' + transaction_ID)
        f.write('\nRate:           ' + rate)
        f.write('\n\nThank you for being a WollPay customer!\n')
        f.write('----------------WollPay----------------\n\n')
    return


def float_to_int(item, decimal_places=2):
    """This function convert 'float' with .00
    to 'int' and return as 'str'.
    """
    item = float(item)
    item = truncate_float(item, decimal_places)
    item = str(item)
    if item.split('.')[1] in ['0','00','000','0000']:
        return item.split('.')[0]  # <class 'str'>
    else: return item  # <class 'str'>


def truncate_float(float_number, decimal_places=2):
    """"The function that truncate to a specific
    decimal point.
    """
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier  # <class 'float'.
