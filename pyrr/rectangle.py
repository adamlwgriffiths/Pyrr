'''
Created on 11/04/2012

@author: adam
'''

import math

import numpy


class index:
    position = 0
    size = 1

def _empty( data_type = 'float' ):
    return numpy.empty( 4, dtype = data_type )

def zero( out = None, data_type = 'float' ):
    if out == None:
        out = _empty( data_type )
    
    out[:] = [ [0.0, 0.0], [0.0, 0.0] ]
    return out

def create_from_bounds( left, right, bottom, top, out = None, data_type = 'float' ):
    if out == None:
        out = _empty( data_type )

    xmin = min( left, right )
    xmax = max( left, right )
    ymin = min( top, bottom )
    ymax = max( top, bottom )

    out[:] = [
        [ xmin, ymin ],
        [ xmax - xmin, ymax - ymin ]
        ]
    return out

def bounds( rect ):
    left = rect[ 0,0 ]
    right = rect[ 0,0 ] + rect[ 1,0 ]
    top = rect[ 0,1 ]
    bottom = rect[ 0,1 ] + rect[ 1,1 ]

    xmin = min( left, right )
    xmax = max( left, right )
    ymin = min( top, bottom )
    ymax = max( top, bottom )

    return xmin, xmax, ymin, ymax

def position( rect ):
    return rect[ 0 ]

def size( rect ):
    return rect[ 1 ]

def abs_size( rect ):
    return numpy.absolute( size( rect ) )

def width( rect ):
    return rect[ 1,0 ]

def abs_width( rect ):
    return abs( width( rect ) )

def height( rect ):
    return rect[ 1,1 ]

def abs_height( rect ):
    return abs( height( rect ) )

def top( rect ):
    return rect[ 0,1 ] + rect[ 1,1 ]

def bottom( rect ):
    return rect[ 0,1 ]

def left( rect ):
    return rect[ 0,0 ]

def right( rect ):
    return rect[ 0,0 ] + rect[ 1,0 ]

def x_minimum( rect ):
    return min(
        rect[ 0,0 ],
        rect[ 0,0 ] + rect[ 1,0 ]
        )

def x_maximum( rect ):
    return max(
        rect[ 0,0 ],
        rect[ 0,0 ] + rect[ 1,0 ]
        )

def y_minimum( rect ):
    return min(
        rect[ 0,1 ],
        rect[ 0,1 ] + rect[ 1,1 ]
        )

def y_maximum( rect ):
    return max(
        rect[ 0,1 ],
        rect[ 0,1 ] + rect[ 1,1 ]
        )

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

