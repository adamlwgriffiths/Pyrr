# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import math

import numpy

from pyrr.utils import all_parameters_as_numpy_arrays, parameters_as_numpy_arrays


class index:
    position = 0
    size = 1

def zeros( dtype = None ):
    return numpy.zeros( (2,2), dtype = dtype )

def create_from_position( x, y, width, height, dtype = None ):
    return numpy.array(
        [
            [ x, y ],
            [ width, height ]
            ],
        dtype = dtype
        )

def create_from_bounds( left, right, bottom, top, dtype = None ):
    xmin = min( left, right )
    xmax = max( left, right )
    ymin = min( top, bottom )
    ymax = max( top, bottom )

    return create_from_position(
        xmin,
        ymin,
        xmax - xmin,
        ymax - ymin,
        dtype
        )

@all_parameters_as_numpy_arrays
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

@all_parameters_as_numpy_arrays
def width( rect ):
    return rect[ 1,0 ]

def abs_width( rect ):
    return abs( width( rect ) )

@all_parameters_as_numpy_arrays
def height( rect ):
    return rect[ 1,1 ]

def abs_height( rect ):
    return abs( height( rect ) )

@all_parameters_as_numpy_arrays
def top( rect ):
    return rect[ 0,1 ] + rect[ 1,1 ]

@all_parameters_as_numpy_arrays
def bottom( rect ):
    return rect[ 0,1 ]

@all_parameters_as_numpy_arrays
def left( rect ):
    return rect[ 0,0 ]

@all_parameters_as_numpy_arrays
def right( rect ):
    return rect[ 0,0 ] + rect[ 1,0 ]

@all_parameters_as_numpy_arrays
def x_minimum( rect ):
    return min(
        rect[ 0,0 ],
        rect[ 0,0 ] + rect[ 1,0 ]
        )

@all_parameters_as_numpy_arrays
def x_maximum( rect ):
    return max(
        rect[ 0,0 ],
        rect[ 0,0 ] + rect[ 1,0 ]
        )

@all_parameters_as_numpy_arrays
def y_minimum( rect ):
    return min(
        rect[ 0,1 ],
        rect[ 0,1 ] + rect[ 1,1 ]
        )

@all_parameters_as_numpy_arrays
def y_maximum( rect ):
    return max(
        rect[ 0,1 ],
        rect[ 0,1 ] + rect[ 1,1 ]
        )

@parameters_as_numpy_arrays( 'rect' )
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

