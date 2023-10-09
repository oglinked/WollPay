"""cidvalid.py
CID validation.
"""

from inputvalid import cyrillic_presence_test, remove_tabs_and_whitespaces

message_cyrillic = 'No cyrillic letters are allowed in this field!'


def cid_validation(cid):
    """Validation of CID."""
    cid = cyrillic_presence_test(cid, message_cyrillic)
    cid = remove_tabs_and_whitespaces(cid)
    if len(cid) < 1:  # Minimum 1 character should be present.
        print('Error: Too few characters were inputted.')
        cid = input('Repeat Input: ')
        cid = cid_validation(cid)  # Recursion.
    else: pass
    cid = valid_isalnum(cid)  # To test the presence of
    # Latin alphabet and decimal digits only.
    return cid


def valid_isalnum(str_to_valid):
    """Validation the Latin alphabet and decimal digits
    presence only. It's for field CID only.
    Return latters on the upper case.
    """
    if str_to_valid.isalnum():
        pass
    else:
        print('Error: Only Latin latters and decimal digits \
are allowed in this field.')
        str_to_valid = input('Repeat Input: ')
        str_to_valid = cid_validation(str_to_valid)  # Go to CID validation.
    return str_to_valid.upper()
