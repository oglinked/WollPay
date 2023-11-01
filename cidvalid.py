"""cidvalid.py
CID validation.
"""

import inputvalid as iv

message_cyrillic = 'No cyrillic letters are allowed in this field!'


def cid_validation(cid):
    """Validation of CID."""
    cid = iv.test_cyr_tabs_whitespaces(cid, message_cyrillic)
    if len(cid) < 1:  # Minimum 1 character should be present.
        print('Error: Too few characters!')
        cid = input('Repeat "CID" Input: ')
        # cid = cid_validation(cid)  # Recursion.
        # Going to CID checking in modul inputvalid:
        cid = iv.cid_checking('CID', cid)  # Go to !!
    else: pass
    # cid = iv.valid_decimal(cid)  # To test the presence of
    # # decimal digits only.
    cid = valid_isalnum(cid)
    return cid


def valid_isalnum(str_to_valid):
    """Validation the Latin alphabet and decimal digits
    presence only. It's for field CID only.
    Return latters on the upper case.
    """
    if str_to_valid.isalnum():
        pass
    else:
        print('Error: Only decimal digits and Latin latters \
are allowed in this field.')
        str_to_valid = input('Repeat "CID" Input: ')
        # str_to_valid = cid_validation(str_to_valid)  # Go to CID validation.
        # Going to CID checking in modul inputvalid:
        str_to_valid = iv.cid_checking('CID', str_to_valid)  # Go to !!
    return str_to_valid.upper()
