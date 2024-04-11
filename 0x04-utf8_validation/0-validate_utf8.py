#!/usr/bin/python3
"""
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore
you only need to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    an implementation of utf rules
    """
    num_bytes = 0
    
    for num in data:
        # Check if the most significant bit (MSB) is set
        if num_bytes == 0:
            mask = 1 << 7
            while mask & num:
                num_bytes += 1
                mask >>= 1

            # No character should be 4 bytes or more
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the first two bits are 10
            if (num >> 6) != 0b10:
                return False
        
        num_bytes -= 1
    
    # If all bytes are processed correctly, num_bytes should be zero
    return num_bytes == 0
