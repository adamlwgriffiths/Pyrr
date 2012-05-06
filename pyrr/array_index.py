'''
Created on 14/06/2011

@author: adam
'''

def array_3d_position_to_index( size, position ):
    """
    Converts from a 3D position within the chunk, to an index in our
    1D array
    """
    # index = ( (x * ySize) + y) * zSize + z
    x = position[ 0 ]
    y = position[ 1 ]
    z = position[ 2 ]
    y_size = size[ 1 ]
    z_size = size[ 2 ]
    return (((x * y_size) + y) * z_size) + z

def array_3d_index_to_position( size, index ):
    """
    Converts an array index into a 3D position
    """
    y_size = size[ 1 ]
    z_size = size[ 2 ]

    i = index
    
    x = i / (y_size * z_size)
    i -= (x * (y_size * z_size))
    
    y = i / z_size
    
    z = i - (y * z_size)
    
    return (x, y, z)

def array_3d_index_increment_unsafe( size, index, increment ):
    """
    Takes a position and quickly shuffles along an axis.
    This avoids having to calculate the index many times for each vertex.
    This function does not do bounds checking for speed. 

    @param size: the dimensions of the container as a 3d vector.
    @param index: the existing index value.
    @param increment: a 3d vector to increment the position by.
    """
    #index += increment[ 0 ] * size[ 1 ]
    pass


def array_3d_index_increment_x( size, index, increment ):
    """
    Takes a position and quickly shuffles along an axis.
    This avoids having to calculate the index many times for each vertex.
    """
    # TODO:
    pass

