#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method
that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    the code performs recussion and
    finds prime factors which equate
    to minimum operations number
    """
    if n <= 1:
        return n
    current_chars = 1
    clipboard = 0
    operations = 2
    while current_chars < n:
        if n % current_chars == 0:
            clipboard = current_chars
            operations += 1
            current_chars += clipboard
        else:
            current_chars += clipboard
            operations += 2

    return operations
