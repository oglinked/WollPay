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
          input_summ,
          '--> ',
          output_currency,
          output_summ)
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
