
def count_bits( int_type ):
    """
    http://wiki.python.org/moin/BitManipulation
    """
    count = 0
    while (int_type):
        count += (int_type & 1)
        int_type >>= 1
    
    return count

