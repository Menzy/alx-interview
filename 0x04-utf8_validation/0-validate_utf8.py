#!/usr/bin/python3
"""Determines a valid UTF-8 encoding"""


def validUTF8(data):
    """
    bit1: Mask to check if the most significant bit is 1.
    bit2: Mask to check if the second most significant bit is 0.
    nbytes: Counter for the number of bytes in the current UTF-8 character.
    data: List of integers representing the data to be validated.
    """

    bit1 = 1 << 7
    bit2 = 1 << 6
    nbytes = 0

    if not data or len(data) == 0:
        return True

    for num in data:
        bit = 1 << 7
        if nbytes == 0:
            while (bit & num):
                nbytes += 1
                bit = bit >> 1

            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:

            if not (num & bit1 and not (num & bit2)):
                return False
        nbytes -= 1

    if nbytes:
        return False
    else:
        return True
