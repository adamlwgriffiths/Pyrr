# -*- coding: utf-8 -*-
"""Provide functions for the manipulation of integers.
"""

def count_bits(int_type):
    """Counts the number of bits set to 1 in an integer.

    For example::

        >>> pyrr.integer.count_bits( 8 )
        1
        >>> pyrr.integer.count_bits( 3 )
        2
        >>> pyrr.integer.count_bits( 0xf )
        4
    
    :param int int_type: An integer.
    :rtype: integer
    :return: The count of bits set to 1.

    .. seealso:: http://wiki.python.org/moin/BitManipulation
    """
    count = 0
    while (int_type):
        count += (int_type & 1)
        int_type >>= 1
    
    return count

