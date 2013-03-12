# -*- coding: utf-8 -*-
"""
Defines a number of functions to test
interactions between various forms of
3D structures.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import numpy

from pyrr import ray, rectangle, vector
from pyrr.utils import all_parameters_as_numpy_arrays, parameters_as_numpy_arrays


@all_parameters_as_numpy_arrays
def point_intersect_line( line, point ):
    """
    Determines if a point is on a line.
    Performed by checking if the cross-product
    of the point relative to the line is
    0.
    """
    rl = line[ 1 ] - line[ 0 ]
    rp = point - line[ 0 ]
    cross = vector.cross( rl, rp )

    # check if the cross product is zero
    if numpy.count_nonzero( cross ) > 0:
        return None
    return point

@all_parameters_as_numpy_arrays
def point_intersect_line_segment( line, point ):
    """
    Determines if a point is on a segment.
    Performed by checking if the cross-product
    of the point relative to the line is
    0 and if the dot product of the point
    relative to the line start AND the end
    point relative to the line start is
    less than the segment's squared length.
    """
    rl = line[ 1 ] - line[ 0 ]
    rp = point - line[ 0 ]
    cross = vector.cross( rl, rp )
    dot = vector.dot( rp, rl )
    squared_length = vector.squared_length( rl )

    if numpy.count_nonzero( cross ) > 0:
        return None

    if \
        dot < 0.0 or \
        dot > squared_length:
        return None
    return point

@all_parameters_as_numpy_arrays
def point_intersect_rectangle( point, rect ):
    """
    Determines if a point is within a 2D rectangle.

    For 3D points, the Z axis will be ignored.

    @return: Returns True if the point is touching
    or within the rectangle.
    """
    left, right, bottom, top = rectangle.bounds( rect )
    if \
        point[ 0 ] < left or \
        point[ 0 ] > right or \
        point[ 1 ] < bottom or \
        point[ 1 ] > top:
        return None
    return point

@parameters_as_numpy_arrays( 'ray', 'plane' )
def ray_intersect_plane( ray, plane, front_only = False ):
    """
    Distance to plane is defined as
    t = (pd - p0.n) / rd.n
    where:
    rd is the ray direction
    pd is the point on plane . plane normal
    p0 is the ray position
    n is the plane normal

    if rd.n == 0, the ray is parallel to the
    plane.

    @param front_only: Specifies if the ray should
    only hit the front of the plane.
    Collisions from the rear of the plane will be
    ignored.

    @return The intersection point, or None
    if the ray is parallel to the plane.
    Returns None if the ray intersects the back
    of the plane and front_only is True.
    """
    rd_n = vector.dot( ray[ 1 ], plane[ 1 ] )

    if rd_n == 0.0:
        return None

    if front_only == True:
        if rd_n >= 0.0:
            return None

    pd = vector.dot( plane[ 0 ], plane[ 1 ] )
    p0_n = vector.dot( ray[ 0 ], plane[ 1 ] )
    t = (pd - p0_n) / rd_n
    return ray[ 0 ] + (ray[ 1 ] * t)

@all_parameters_as_numpy_arrays
def line_intersect_plane( line, plane ):
    """
    Calculates the intersection point of a line
    and a plane.
    """
    pass

@all_parameters_as_numpy_arrays
def line_segment_intersect_plane( segment, plane ):
    """
    Calculates the intersection point of a segment and a
    plane.
    If the segment is not long enough to intersect the
    plane, None will be returned.
    """
    pass

@all_parameters_as_numpy_arrays
def closest_point_on_ray( ray, point ):
    """
    Calculates the closest point on a ray.
    t = (p - rp).n
    cp = rp + (n * t)
    where
    p is the point
    rp is the ray origin
    n is the ray normal of unit length
    t is the distance along the ray to the point
    """
    normalised_n = vector.normalise( ray[ 1 ] )
    relative_point = (point - ray[ 0 ])
    t = vector.dot( relative_point, normalised_n )
    return ray[ 0 ] + ( normalised_n * t )

@all_parameters_as_numpy_arrays
def closest_point_on_line( line, point ):
    """
    Calculates the point on the line that is the
    closest to the specified point.
    rl = va->b (relative line)
    rp = va->p (relative point)
    u' = u / |u| (normalise)
    cp = a + (u' * (u'.v))
    where:
    a = line start
    b = line end
    p = point
    cp = closest point
    """
    rl = line[ 1 ] - line[ 0 ]
    rp = point - line[ 0 ]
    vector.normalise( rl )
    dot = vector.dot( rl, rp )
    return line[ 0 ] + (rl * dot)

@all_parameters_as_numpy_arrays
def closest_point_on_line_segment( segment, point ):
    """
    Calculates the point on the line segment that is
    the closest to the specified point.
    """
    # check if the line has any length
    rl = segment[ 1 ] - segment[ 0 ]
    squared_length = vector.squared_length( rl )
    if squared_length == 0.0:
        return segment[ 0 ]

    rp = point - segment[ 0 ]
    # check that / squared_length is correct
    dot = vector.dot( rp, rl ) / squared_length;

    if dot < 0.0:
        return segment[ 0 ]
    elif dot > 1.0:
        return segment[ 1 ]

    # within segment
    # perform the same calculation as closest_point_on_line
    return segment[ 0 ] + (rl * dot)

@all_parameters_as_numpy_arrays
def are_rays_parallel( ray1, ray2 ):
    cross = vector.cross( ray1[ 1 ], ray2[ 1 ] )
    if numpy.count_nonzero( cross ) > 0:
        return False
    return True

@all_parameters_as_numpy_arrays
def are_rays_coincident( ray1, ray2 ):
    # ensure the ray's directions are the same
    if numpy.array_equal( ray1[ 0 ], ray2[ 0 ] ):
        # get the delta between the two ray's start point
        delta = ray2[ 0 ] - ray1[ 0 ]

        # get the cross product of the ray delta and
        # the direction of the rays
        cross = vector.cross( ray1[ 1 ], ray2[ 1 ] )

        # if the cross product is zero, the start of the
        # second ray is in line with the direction of the
        # first ray
        if numpy.count_nonzero( cross ) > 0:
            return False

        return True
    return False

@all_parameters_as_numpy_arrays
def ray_intersect_aabb( ray, aabb ):
    # http://gamedev.stackexchange.com/questions/18436/most-efficient-aabb-vs-ray-collision-algorithms
    
    # this is basically "numpy.divide( 1.0, ray[ 1 ] )"
    # except we're trying to avoid a divide by zero warning
    # so where the ray direction value is 0.0, just use infinity
    # which is what we want anyway
    direction = ray[ 1 ]
    dir_fraction = numpy.empty( 3, dtype = ray.dtype )
    dir_fraction[ direction == 0.0 ] = numpy.inf
    dir_fraction[ direction != 0.0 ] = numpy.divide( 1.0, direction[ direction != 0.0 ] )

    t1 = (aabb[0,0] - ray[0,0]) * dir_fraction[ 0 ]
    t2 = (aabb[1,0] - ray[0,0]) * dir_fraction[ 0 ]
    t3 = (aabb[0,1] - ray[0,1]) * dir_fraction[ 1 ]
    t4 = (aabb[1,1] - ray[0,1]) * dir_fraction[ 1 ]
    t5 = (aabb[0,2] - ray[0,2]) * dir_fraction[ 2 ]
    t6 = (aabb[1,2] - ray[0,2]) * dir_fraction[ 2 ]


    tmin = max(min(t1, t2), min(t3, t4), min(t5, t6))
    tmax = min(max(t1, t2), max(t3, t4), max(t5, t6))

    # if tmax < 0, ray (line) is intersecting AABB
    # but the whole AABB is behind the ray start
    if tmax < 0:
        return None

    # if tmin > tmax, ray doesn't intersect AABB
    if tmin > tmax:
        return None

    # t is the distance from the ray point
    # to intersection

    t = abs(tmin)
    point = ray[ 0 ] + (ray[ 1 ] * t)
    return point

@all_parameters_as_numpy_arrays
def ray_intersect_ray( ray1, ray2 ):
    pass

@all_parameters_as_numpy_arrays
def line_intersect_line( line1, line2 ):
    pass

@all_parameters_as_numpy_arrays
def line_segment_intersect_line_segment( segment1, segment2 ):
    pass

@all_parameters_as_numpy_arrays
def height_above_plane( plane, vector ):
    """
    Returns the height above the plane.
    Performs no checking of the vector being within the plane's surface
    if one is defined.

    @return: The height above the plane as a float
    """
    plane_dot = numpy.dot( plane[ 1 ], plane[ 0 ] )
    vector_dot = numpy.dot( vector, plane[ 1 ] )
    return vector_dot - plane_dot

@all_parameters_as_numpy_arrays
def closest_point_on_plane( plane, vector ):
    """
    point on plane is defined as:
    q' = q + (d - q.n)n
    where:
    q' is the point on the plane
    q is the point we are checking
    d is the value of normal dot position
    n is the plane normal
    """
    d = numpy.dot( plane[ 1 ], plane[ 0 ] )
    qn = numpy.dot( vector, plane[ 1 ] )
    return vector + ( plane[ 1 ] * (d - qn) )

@all_parameters_as_numpy_arrays
def does_sphere_intersect_sphere( c1, c2 ):
    """
    Determines if two spheres overlap.

    Note: This will return True if the two spheres are
    touching perfectly but sphere_penetration_sphere
    will return 0.0 as the touch but don't penetrate.

    This is faster than circle_penetrate_amount_circle
    as it avoids a square root calculation.

    @param c1: The first circle.
    @param c2: The second circle.
    @return: Returns True if the circles overlap.
    Otherwise, returns False.
    """
    delta = c2[ 0 ] - c1[ 0 ]
    distance_squared = vector.length_squared( delta )

    radii_squared = math.pow( c1[ 1 ] + c2[ 1 ], 2.0 )

    if distance_squared > radii_squared:
        return False
    return True

@all_parameters_as_numpy_arrays
def sphere_penetration_sphere( c1, c2 ):
    """
    Calculates the distance two spheres have
    penetrated into one another.

    @param c1: The first circle.
    @param c2: The second circle.
    @return: The total overlap of the two spheres.
    This is essentially:
    r1 + r2 - distance 
    Where r1 and r2 are the radii of circle 1 and 2
    and distance is the length of the vector p2 - p1.
    Will return 0.0 if the circles do not overlap.
    """
    delta = c2[ 0 ] - c1[ 0 ]
    distance = vector.length( delta )

    combined_radii = c1[ 1 ] + c2[ 1 ]
    penetration = combined_radii - distance

    if penetration <= 0.0:
        return 0.0
    return penetration


