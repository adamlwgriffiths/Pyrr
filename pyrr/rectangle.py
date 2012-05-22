'''
Created on 11/04/2012

@author: adam
'''

import math

import numpy


def zero( out = None, data_type = numpy.float ):
    if out == None:
        out = numpy.empty( (2,2), dtype = data_type )
    
    out[:] = [ [0.0, 0.0], [0.0, 0.0] ]
    return out

def create_from_bounds( left, right, bottom, top, out = None, data_type = numpy.float ):
    if out == None:
        out = numpy.empty( (2,2), dtype = data_type )

    out[:] = [
        [ left, bottom ],
        [ right - left, top - bottom ]
        ]
    return out

def bounds( rect ):
    left = min(
        rect[ 0,0 ],
        rect[ 0,0 ] + rect[ 1,0 ]
        )
    right = max(
        rect[ 0,0 ],
        rect[ 0,0 ] + rect[ 1,0 ]
        )
    bottom = min(
        rect[ 0,1 ],
        rect[ 0,1 ] + rect[ 1,1 ]
        )
    top = max(
        rect[ 0,1 ],
        rect[ 0,1 ] + rect[ 1,1 ]
        )
    return left, right, bottom, top

def width( rect ):
    return rect[ 1,0 ]

def height( rect ):
    return rect[ 1,1 ]

def top( rect ):
    return rect[ 0,1 ] + rect[ 1,1 ]

def bottom( rect ):
    return rect[ 0,1 ]

def left( rect ):
    return rect[ 0,0 ]

def right( rect ):
    return rect[ 0,0 ] + rect[ 1,0 ]

def scale_by_vector( rect, vec ):
    """
    Scales a rectangle by a 2D vector.

    Note that this will also scale the X,Y
    value of the rectangle, which will cause
    the rectangle to move, not just increase
    in size.

    @param rect: the rectangle to scale.
    Both x,y and width,height will be scaled.
    The value will NOT be scaled in place.
    @param vec: A 2D vector to scale the rect
    by.
    @return Returns the rect scaled by vec.
    """
    if rect.shape != (2,2):
        raise ValueError( "Rect must be shape (2,2)" )
    if len(vec) != 2:
        raise ValueError( "Vec must be length 2" )
    return rect * vec

