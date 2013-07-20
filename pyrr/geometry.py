"""Geometry functions.
"""
import numpy


def create_quad(width=1.0, height=1.0, st=False, rgba=False):
    """Returns a Quad composed of Triangles.

    If st is True, texture coordinates are appended to each row.
    If rgba is True, a 4 value RGBA value is appended to each row.
    If rgba is an int or tuple, then the value is converted to a list of 4 values
    and appended to each row.
    If rgba is a tuple, the rgba value is appended to each row.
    """
    shape = (6, 3)
    rgba_start = 3
    if st:
        rgba_start = 5
        shape = (shape[0], shape[1] + 2)
    if rgba:
        if isinstance(rgba, bool):
            rgba = (1.0, 1.0, 1.0, 1.0)
        elif isinstance(rgba, (int, float)):
            rgba = [rgba] * 4
        shape = (shape[0], shape[1] + len(rgba))

    vertices = numpy.empty(shape)
    vertices[:,:3] = [
        ( width, height, 0.0,),
        (-width, height, 0.0,),
        ( width,-height, 0.0,),
        (-width, height, 0.0,),
        (-width,-height, 0.0,),
        ( width,-height, 0.0,),
    ]

    if st:
        vertices[:,3:5] = [
            (1.0, 1.0,),
            (0.0, 1.0,),
            (1.0, 0.0,),
            (0.0, 1.0,),
            (0.0, 0.0,),
            (1.0, 0.0,),
        ]

    if rgba:
        vertices[:,rgba_start:] = rgba

    return vertices

def create_cube(width=1.0, height=1.0, depth=1.0, st=False, rgba=False):
    """Returns a Cube composed of Triangles.

    If rgba is True, a 4 value RGBA value is appended to each row.
    If rgba is an int or tuple, then the value is converted to a list of 4 values
    and appended to each row.
    If rgba is a tuple, the rgba value is appended to each row.
    """
    shape = (36, 3)
    rgba_start = 3
    if st:
        rgba_start = 5
        shape = (shape[0], shape[1] + 2)
    if rgba:
        if isinstance(rgba, bool):
            rgba = (1.0, 1.0, 1.0, 1.0)
        elif isinstance(rgba, (int, float)):
            rgba = [rgba] * 4
        shape = (shape[0], shape[1] + len(rgba))

    vertices = numpy.empty(shape)
    vertices[:,:3] = [
        ( width, height,-depth),
        (-width, height,-depth),
        ( width, height, depth),
        (-width, height,-depth),
        (-width, height, depth),
        ( width, height, depth),

        ( width,-height, depth),
        (-width,-height, depth),
        ( width,-height,-depth),
        (-width,-height, depth),
        (-width,-height,-depth),
        ( width,-height,-depth),

        ( width, height, depth),
        (-width, height, depth),
        ( width,-height, depth),
        (-width, height, depth),
        (-width,-height, depth),
        ( width,-height, depth),

        ( width,-height,-depth),
        (-width,-height,-depth),
        ( width, height,-depth),
        (-width,-height,-depth),
        (-width, height,-depth),
        ( width, height,-depth),

        (-width, height, depth),
        (-width, height,-depth),
        (-width,-height, depth),
        (-width, height,-depth),
        (-width,-height,-depth),
        (-width,-height, depth),

        ( width, height,-depth),
        ( width, height, depth),
        ( width,-height,-depth),
        ( width, height, depth),
        ( width,-height, depth),
        ( width,-height,-depth),
    ]

    if st:
        vertices[:,3:5] = ([
            (1.0, 1.0,),
            (0.0, 1.0,),
            (1.0, 0.0,),
            (0.0, 1.0,),
            (0.0, 0.0,),
            (1.0, 0.0,),
        ] * 6)

    if rgba:
        vertices[:,rgba_start:] = [rgba] * 36

    return vertices
