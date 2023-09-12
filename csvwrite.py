"""csvwrite.py"""

import csv
from pathlib import Path


def csv_write(file_path, fields, row):
    """Checking the csv file existing and writing to csv file."""
    path = Path(file_path)
    result = path.is_file()

    if result == True:
        with open(file_path, 'a', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(row)
    else:
        with open(file_path, 'w', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(fields)  # Writing the fields.
            csvwriter.writerow(row)
    return


def file_read(file_path):
    """Testing if the source.txt file exist,
    and appending to source_list from source.txt.
    """
    path = Path(file_path)
    result = path.is_file()
    if result == True:
        # Appending to item_list from file_path.
        item_list = []
        with open(file_path, 'r') as f:
            for x in f:
                item_list.append(x)
    else:
        input('Error: The source.txt file is missing!\n\
Upload source.txt file in current folder and press "Enter" \
to continue: ')
        item_list = file_read(file_path)  # Recursion.
    return item_list
