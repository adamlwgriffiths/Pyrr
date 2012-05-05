'''
Created on 20/04/2012

@author: adam

Defines a number of functions to test
interactions between various forms of
3D structures.
'''

import numpy

import ray
import vector


def point_is_on_line( line, point ):
    """
    Determines if a point is on a line.
    Performed by checking if the cross-product
    of the point relative to the line is
    0.
    """
    rl = line[ 1 ] - line[ 0 ]
    rp = point - line[ 0 ]
    cross = vector.cross( rl, rp )

    if \
        cross[ 0 ] != 0.0 or \
        cross[ 1 ] != 0.0 or \
        cross[ 2 ] != 0.0:
        return False
    return True

def point_is_on_line_segment( line, point ):
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
    if \
        cross[ 0 ] != 0.0 or \
        cross[ 1 ] != 0.0 or \
        cross[ 2 ] != 0.0:
        return False
    if \
        dot < 0.0 or \
        dot > squared_length:
        return False
    return True

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

def line_intersect_plane( line, plane ):
    """
    Calculates the intersection point of a line
    and a plane.
    """
    pass

def line_segment_intersect_plane( segment, plane ):
    """
    Calculates the intersection point of a segment and a
    plane.
    If the segment is not long enough to intersect the
    plane, None will be returned.
    """
    pass

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

def intersection_of_rays( ray1, ray2 ):
    pass

def intersection_of_lines( line1, line2 ):
    pass

def intersection_of_line_segments( segment1, segment2 ):
    pass

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
    plane_dot = numpy.dot( plane[ 1 ], plane[ 0 ] )
    vector_dot = numpy.dot( vector, plane[ 1 ] )
    return vector + (  plane[ 1 ] * (plane_dot - vector_dot) )



if __name__ == '__main__':
    #
    # closest point on line
    #
    import line
    new_line = line.line_from_points(
        [ 0.0, 0.0, 0.0 ],
        [10.0, 0.0, 0.0 ]
        )

    point = closest_point_on_line(
        new_line,
        [ 0.5, 1.0, 0.0 ]
        )
    print point
    assert point[ 0 ] == 0.5
    assert point[ 1 ] == 0.0
    assert point[ 2 ] == 0.0

    #
    # closest point on plane
    #
    import plane
    vectors = numpy.array([
        [ 0.0, 0.0, 1.0 ],
        [ 1.0, 0.0, 1.0 ],
        [ 0.0, 1.0, 1.0 ]
        ])
    new_plane = plane.plane_from_points( vectors[ 0 ], vectors[ 1 ], vectors[ 2 ] )
    plane.flip_normal( new_plane )

    #
    # height above plane
    #
    distance_vector = numpy.array([ 0.0, 0.0, 20.0 ])
    distance = height_above_plane( new_plane, distance_vector )
    # should be 19.0
    print "distance: %f" % distance
    assert distance == 19.0

    closest_point = closest_point_on_plane( new_plane, distance_vector )
    # should be # 0, 0, 1
    print "closestPoint: %s" % str(closest_point)
    assert closest_point[ 0 ] == 0.0
    assert closest_point[ 1 ] == 0.0
    assert closest_point[ 2 ] == 1.0

    #
    # ray intersect plane
    #
    # make a plane that sits on the X/Z axis
    vectors = numpy.array([
        [ 0.0, 0.0, 0.0 ],
        [ 1.0, 0.0, 1.0 ],
        [ 0.0, 0.0,-1.0 ]
        ])
    new_plane = plane.plane_from_points(
        vectors[ 0 ], vectors[ 1 ], vectors[ 2 ]
        )
    # ensure it points upward
    if new_plane[ 1 ][ 1 ] < 0.0:
        plane.flip_normal( new_plane )

    # make a ray that goes right through the Y axis
    # pointing upward
    new_ray = numpy.array(
        [
            [ 0.0, 0.0, 0.0],
            [ 0.0, 1.0, 0.0]
            ],
        dtype = numpy.float
        )
    intersection = ray_intersect_plane( new_ray, new_plane )
    assert intersection[ 0 ] == 0.0
    assert intersection[ 1 ] == 0.0
    assert intersection[ 2 ] == 0.0
    intersection = ray_intersect_plane( new_ray, new_plane, front_only = True )
    assert intersection == None

    #
    # closest point on ray
    #
    # the point shall be at Y = 10
    # this is where the closest point should be
    closest_point = closest_point_on_ray(
        new_ray, 
        numpy.array( [1.0, 10.0, 1.0], dtype = numpy.float )
        )
    print closest_point
    assert closest_point[ 0 ] == 0.0
    assert closest_point[ 1 ] == 10.0
    assert closest_point[ 2 ] == 0.0

    #
    # closest point on line
    #
    new_line = new_line = line.line_from_points(
        [ 0.0, 0.0, 0.0 ],
        [10.0, 0.0, 0.0 ]
        )
    point = closest_point_on_line(
        new_line,
        [ 5.0, 10.0, 0.0 ]
        )
    print point
    assert point[ 0 ] == 5.0
    assert point[ 1 ] == 0.0
    assert point[ 2 ] == 0.0

    point = closest_point_on_line(
        new_line,
        [50.0, 10.0, 0.0 ]
        )
    print point
    assert point[ 0 ] == 50.0
    assert point[ 1 ] == 0.0
    assert point[ 2 ] == 0.0

    #
    # closest point on line segment
    #
    new_line = new_line = line.line_from_points(
        [ 0.0, 0.0, 0.0 ],
        [10.0, 0.0, 0.0 ]
        )
    point = closest_point_on_line_segment(
        new_line,
        [ 5.0, 10.0, 0.0 ]
        )
    print point
    assert point[ 0 ] == 5.0
    assert point[ 1 ] == 0.0
    assert point[ 2 ] == 0.0

    point = closest_point_on_line_segment(
        new_line,
        [50.0, 10.0, 0.0 ]
        )
    print point
    assert point[ 0 ] == 10.0
    assert point[ 1 ] == 0.0
    assert point[ 2 ] == 0.0

    point = closest_point_on_line_segment(
        new_line,
        [-5.0, 10.0, 0.0 ]
        )
    print point
    assert point[ 0 ] == 0.0
    assert point[ 1 ] == 0.0
    assert point[ 2 ] == 0.0


    #
    # point is on line
    #
    new_line = line.line_from_points(
        [ 0.0, 0.0, 0.0 ],
        [10.0, 0.0, 0.0 ]
        )
    assert True == point_is_on_line(
        new_line,
        numpy.array(
            [ 5.0, 0.0, 0.0 ],
            dtype = numpy.float
            )
        )
    assert True == point_is_on_line(
        new_line,
        numpy.array(
            [ 50.0, 0.0, 0.0 ],
            dtype = numpy.float
            )
        )
    assert False == point_is_on_line(
        new_line,
        numpy.array(
            [ 5.0, 1.0, 0.0 ],
            dtype = numpy.float
            )
        )

    #
    # point is on line segment
    #
    assert True == point_is_on_line_segment(
        new_line,
        numpy.array(
            [ 5.0, 0.0, 0.0 ],
            dtype = numpy.float
            )
        )
    assert True == point_is_on_line_segment(
        new_line,
        numpy.array(
            [ 10.0, 0.0, 0.0 ],
            dtype = numpy.float
            )
        )
    assert False == point_is_on_line_segment(
        new_line,
        numpy.array(
            [ 11.0, 0.0, 0.0 ],
            dtype = numpy.float
            )
        )
    assert False == point_is_on_line_segment(
        new_line,
        numpy.array(
            [ 5.0, 1.0, 0.0 ],
            dtype = numpy.float
            )
        )

