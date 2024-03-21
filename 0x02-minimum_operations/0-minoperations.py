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
    i = 0
    a = 0
    b = 0
    primes = [2, 3, 5, 7]
    while (i < len(primes)):
        if n % primes[i] == 0:
            a = primes[i]
            b = n / primes[i]
            break
        i += 1
    if a == 0 and b == 0:
        return 0
    if b in primes:
        return int(a) + int(b)
    return int(a) + int(minOperations(b))
