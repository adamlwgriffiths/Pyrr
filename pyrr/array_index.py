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
    return (((position[ 0 ] * size[ 1 ]) + position[ 1 ]) * size[ 2 ]) + position[ 2 ]

def array_3d_index_to_position( size, index ):
    """
    Converts an array index into a 3D position
    """
    i = index
    
    x = i / (size[ 1 ] * size[ 2 ])
    i -= (x * (size[ 1 ] * size[ 2 ]))
    
    y = i / size[ 2 ]
    
    z = i - (y * size[ 2 ])
    
    return (x, y, z)

def array_3d_index_increment_x_unsafe( size, index, increment ):
    """
    Takes a position and quickly shuffles along an axis.
    This avoids having to calculate the index many times for each vertex.
    This function does not do bounds checking for speed. 
    """
    # TODO:
    pass


def array_3d_index_increment_x( size, index, increment ):
    """
    Takes a position and quickly shuffles along an axis.
    This avoids having to calculate the index many times for each vertex.
    """
    # TODO:
    pass

