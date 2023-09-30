"""CSV file's field edit programm.
(csvedit.py Version.00.02).
"""

import csv
import os
import inputvalid as iv

message_cyrillic = 'No cyrillic letters are allowed in this field!'


def valid_item_in_decimals_list(index, decimals_list):
    """Validation presence of index (type string) in list decimals'."""
    list_string = map(str, decimals_list)  # int --> str
    if index in list_string:
        pass
    else:
        index = input(f'Error: Index should \
be in {decimals_list}. \nPlease input the right index: ')
        # Recursion.
        index = valid_item_in_decimals_list(index, decimals_list)
    return index
            

def replacement(file_path, item_list, target_item):
    """Replacement of one item."""
    # Calculating target item occurrences in item_list.
    namber_occurrences = item_list.count(target_item)

    # Getting occurrences' list (index_list).
    item = target_item
    index_list = [i for i in range(len(item_list)) 
                     if item_list[i] == item]
    
    if namber_occurrences == 1:
        target_row_index = index_list[0]
    elif namber_occurrences > 1:
        print(f'\nWarning: The number of occurrences \
"{target_item}" in list is "{namber_occurrences}".')
        print('\nOccurrences\' row indices are:', index_list)

        for i in index_list:
            print('\n', read_row(file_path, i))
            # read_row(file_path, i, 2)
        # Getting the target row. The row for further editing.
        target_row_index = input('\nInput the index of the row you prefer: ')

        # Validation block.
        target_row_index = valid_item_in_decimals_list(target_row_index, index_list)

    else:
        print(f'\nWarning: No occurrences "{target_item}" in list.')
        input('Press to EXIT!')  # Should be corrected!

    # Getting the target row. The row for further editing.
    target_row_index = int(target_row_index)
    target_row = read_row(file_path, target_row_index)  # <-- This row.

    print('Target row\'s (row\'s to edit) Table::\n')
    list_print_in_column(target_row)
    index = input('\nInput index of item you are going to edit: ')
    index = valid_index_input(index, len(target_row)-1, 0)  # Validation
    # index <class int>

    # The replacement.
    new_value = input('Input new value for target item: ')
    new_value = iv.remove_cyrillic_and_tabs(new_value)  # Validation.
    replace_value(file_path, target_row_index , index, new_value)
    print(f'\nWell done! "{target_row[index]}" was replaced \
to "{new_value}".')
    return


def check_presence(item, item_list):
    """Checking presence item in list."""
    if item in item_list:
            pass
    else:
        item = input(f'Error: There is no such item in iterator! \
                     \nInput another item: ')
        item = iv.remove_cyrillic_and_tabs(item, message_cyrillic)
        item = check_presence(item, item_list)  # Recursion.
    return item


def valid_index_input(number, max_number, min_number=1):
    """Index input validation."""
    number = iv.cyrillic_presence_test(number, message_cyrillic)
    number = iv.remove_tabs_and_whitespaces(number)
    number = iv.number_validation(number, max_number, min_number)  # Validation.
    number = int(number)
    return number  


def choose_path():
    """Choosing (CSV) file in current directory
    and getting relative path to it.
    """
    files_number = len(list_files())
    if files_number >= 2:
        print(f'\nThere are {files_number} CSV files in \
current directory.\n')
        for i, file in enumerate(list_files(), start=1):
            print(i, '\t', file)
        k = input(f'\nInput the file serial number you are going to edit. \
                    \nPlease get the number in [1, {files_number}]: ')
        k = valid_index_input(k, files_number)  # Validation.
        # k  <class int>
        file_path = './' + list_files()[k-1]
    elif files_number == 1:
        file_path = './' + list_files()[0]
    else:
        input('\nError: No CSV files in current directory! \
              \nPlease upload CSV file you going to edit \
in current directory. \nPress "ENTER" to continue: ')
        file_path = choose_path()  # Recursion.
    return file_path


def list_files(file_extension=".csv"):
    """Returns all files with specific extension
    in current directory as a list.
    """
    list_f = []
    for file in os.listdir(r'./'):
        # Checking the files with specific extension.
        if file.endswith(file_extension):
            list_f.append(file)
    return list_f


def read_row(file_path, row_number, print_control=0):
    """Read a specific Row"""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            if index == row_number:
                if print_control == 1:  # Printing in column.
                    for i, item in enumerate(row, start=1):
                        print(i, '\t', item)
                    print('')
                    break
                elif print_control == 2:  # Printing in line.
                    print(row, '\n', end='')
                    break
                else:
                    # row = row
                    break
    return row


def read_column(file_path, column_number, print_control=0 ):
    """Read a Specific Column."""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        column = []
        for i, row in enumerate(reader):
            column.append(row[column_number])
        if print_control == 0:
            pass
        else:  # Printing in column.
            list_print_in_column(column)
    return column


def list_print_in_column(list_name, s=0):
    """Printing list in column."""
    for i, item in enumerate(list_name, start=s):
        print(i, '\t', item)
    return    


def replace_value(file_path, i, j, new_value):
    """The replacing old value with new one in the table
    (where table is a file).
    Parameters:
    file_path   - the path to the file;
    i           - the index of row;
    j           - the index of replaceble value in row (column index);
    new_value   - the new value of the replaceble value.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)  # Full table.
    # Replacing the old value with new_value.
    rows[i][j] = new_value
    # Writing the data back to the file.
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return


def csvedit():
    """CSV file edit program."""
    # The replacements main loop.
    n = 'y'
    while n != 'q':
        os.system('cls')  # Clearing the Screen.

        # The Greeting & information.
        print('\nHello Host! \
              \nYou run version 00.02 of the program csvedit.py.')

        file_path = choose_path()

        print('\nFull Path to file you edit is: \n'
                + os.path.abspath(file_path)
                + '\n')

        print('The Table of CSV file headers:\n')
        headers_row = read_row(file_path, 0, 1)
        j = input(f'Choose the header you interesting with. \
                  \nPlease get the number in [1, {len(headers_row)}]: ')
        j = valid_index_input(j, len(headers_row))  # Validation.
        # j = int(j)

        column = read_column(file_path, j-1)  

        # Choosing target item in column.
        target_item = input(f'Input target item for CSV file\'s column \
"{column[0]}": ')
        # Validation block.
        target_item = iv.remove_cyrillic_and_tabs(target_item, message_cyrillic)
        # Validation and deprecting column[0] item.
        target_item = check_presence(target_item, column[1:])

        # The loop for row we edit.
        m = 'y'
        while m != 'q':
            replacement(file_path, column, target_item)
            m = input(f'\nWould you like to make another replacement \
in "{target_item}" row? \n(Press "q" to exit, or "ENTER" to continue): ')
            m = iv.exit_test(m)  # Validation.

        # The end of the replacements main loop.
        n = input('\nWould you like to make another replacement \
in CSV file? \n(Press "q" to exit, or "ENTER" to continue): ')
        n = iv.exit_test(n)  # Validation.

    input('Press "ENTER" to exit csvedit.py: ')  # Exit.
    return

if __name__ == "__main__":
    csvedit()
