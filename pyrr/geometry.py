"""Geometry functions.

.. TODO:: Add 'st=False', if true, stack texture coords onto array
.. TODO:: Add 'rgba=False', if true, stack rgba values onto array
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
    vertices = numpy.array([
        ( width, height, 0.0,),
        (-width, height, 0.0,),
        ( width,-height, 0.0,),
        (-width, height, 0.0,),
        (-width,-height, 0.0,),
        ( width,-height, 0.0,),
    ])

    if st:
        coords = numpy.array([
            (1.0, 1.0,),
            (0.0, 1.0,),
            (1.0, 0.0,),
            (0.0, 1.0,),
            (0.0, 0.0,),
            (1.0, 0.0,),
        ])
        vertices = numpy.column_stack((vertices, coords,))

    if rgba:
        if isinstance(rgba, bool):
            rgba = (1.0, 1.0, 1.0, 1.0)
        elif isinstance(rgba, (int, float)):
            rgba = [rgba] * 4
        colours = numpy.array([rgba] * 6)
        vertices = numpy.column_stack((vertices, colours,))
    return vertices

def create_cube(width=1.0, height=1.0, depth=1.0, st=False, rgba=False):
    """Returns a Cube composed of Triangles.

    If rgba is True, a 4 value RGBA value is appended to each row.
    If rgba is an int or tuple, then the value is converted to a list of 4 values
    and appended to each row.
    If rgba is a tuple, the rgba value is appended to each row.
    """
    vertices = numpy.array([
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
    ])

    if st:
        coords = numpy.array([
            (1.0, 1.0,),
            (0.0, 1.0,),
            (1.0, 0.0,),
            (0.0, 1.0,),
            (0.0, 0.0,),
            (1.0, 0.0,),
        ] * 6)
        vertices = numpy.column_stack((vertices, coords,))

    if rgba:
        if isinstance(rgba, bool):
            rgba = (1.0, 1.0, 1.0, 1.0)
        elif isinstance(rgba, (int, float)):
            rgba = [rgba] * 4
        colours = numpy.array([rgba] * 36)
        vertices = numpy.column_stack((vertices, colours,))

    return vertices
