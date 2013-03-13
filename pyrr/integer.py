# -*- coding: utf-8 -*-
"""Provide functions for the manipulation of integers.
"""

def count_bits( int_type ):
    """Counts the number of bits set to 1 in an integer.
    
    http://wiki.python.org/moin/BitManipulation
    """
    count = 0
    while (int_type):
        count += (int_type & 1)
        int_type >>= 1
    
    return count

