#!/usr/bin/python3
"""
Module for Minimum Operations algorithm.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n 'H' characters in a file.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Reduce n by dividing it by its smallest prime factors
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
