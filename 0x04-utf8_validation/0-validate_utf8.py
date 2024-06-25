#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Check the integers inside the passed list
    and return "True" if all of them are a valid UTF-8 encodeing
    or "False" if one of them is not.
    """
    i = 0
    n = len(data)
    while i < n:
        byte1 = data[i]
        if byte1 & 0x80 == 0x00:
            i += 1
        elif byte1 & 0xE0 == 0xC0:
            if i + 1 >= n or data[i + 1] & 0xC0 != 0x80:
                return False
            i += 2
        elif byte1 & 0xF0 == 0xE0:
            if (i + 2 >= n or
               data[i + 1] & 0xC0 != 0x80 or
               data[i + 2] & 0xC0 != 0x80):
                return False
            i += 3
        elif byte1 & 0xF8 == 0xF0:
            if (i + 2 >= n or
               data[i + 1] & 0xC0 != 0x80 or
               data[i + 2] & 0xC0 != 0x80 or
               data[i + 2] & 0xC0 != 0x80):
                return False
            i += 4
        else:
            return False
    return True
