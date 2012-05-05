'''
Created on 29/04/2012

@author: adam
'''

import math


def calculate_fov( height, distance ):
    """
    Calculates the required FOV to set the
    view frustrum to have a view with the specified height
    at the specified distance.

    @param height: The desired view height at the specified
    distance.
    @param distance: The distance to calculate the FOV for.
    @return: The FOV to use.
    """
    # http://www.glprogramming.com/red/chapter03.html
    rad_theta = 2.0 * math.atan2( height / 2.0, distance )
    return math.degrees( rad_theta )

def calculate_height( fov, distance ):
    """
    Performs the opposite of calculate_fov.
    Used to find the current height at a specific distance.

    @param fov: The current FOV.
    @param distance: The distance to calculate the height
    for.
    @return: The height at the specified distance for the
    specified FOV.
    """
    pass

def calculate_plane_size( aspect_ratio, fov, distance ):
    """
    Calculates the width and height of a plane at the
    specified distance using the FOV of the frustrum
    and aspect ratio of the viewport.

    @param aspect_ratio: The aspect ratio of the viewport.
    @param fov: The FOV of the frustrum.
    @param distance: The distance from the origin/camera
    of the plane to calculate.
    @return (width, height): The width and height of
    the plane.
    """
    # http://www.songho.ca/opengl/gl_transform.html
    # http://nehe.gamedev.net/article/replacement_for_gluperspective/21002/
    # http://steinsoft.net/index.php?site=Programming/Code%20Snippets/OpenGL/gluperspective&printable=1
    tangent = math.radians( fov )
    height = distance * tangent
    width = height * aspect_ratio

    return width * 2.0, height * 2.0

