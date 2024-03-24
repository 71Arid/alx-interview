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
    op = 0
    cp = 0
    dn = 1
    while dn < n:
        if cp == 0:
            cp = dn
            dn += cp
            op += 2
        elif n - dn > 0 and (n - dn) % dn == 0:
            cp = dn
            dn += cp
            op += 2
        elif cp > 0:
            dn += cp
            op += 1
    return op
