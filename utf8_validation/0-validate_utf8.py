#!/usr/bin/python3
"""
A module for UTF-8 validation.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    expected_continuation_bytes = 0

    mask1 = 1 << 7
    mask2 = (1 << 7) | (1 << 6)

    for num in data:
        byte = num & 0xFF

        if expected_continuation_bytes == 0:
            if not (byte & mask1):
                continue

            if (byte >> 5) == 0b110:
                expected_continuation_bytes = 1
            elif (byte >> 4) == 0b1110:
                expected_continuation_bytes = 2
            elif (byte >> 3) == 0b11110:
                expected_continuation_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            expected_continuation_bytes -= 1

    return expected_continuation_bytes == 0
