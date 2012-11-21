'''
Created on 21/06/2011

@author: adam
'''

import math

import numpy

import vector


x = 0
y = 1
z = 2
w = 3

def _empty():
    return numpy.empty( 4, dtype = float )

def create( x, y, z, w ):
    return numpy.array( [ x, y, z, w ], dtype = float )

def identity( out = None ):
    if out == None:
        out = _empty()

    qw = 1.0
    qx = 0.0
    qy = 0.0
    qz = 0.0

    out[:] = [ qx, qy, qz, qw ]
    return out

def set_to_rotation_about_x( theta, out = None ):
    if out == None:
        out = _empty()
    
    thetaOver2 = theta * 0.5
    qw = math.cos( thetaOver2 )
    qx = math.sin( thetaOver2 )
    qy = 0.0
    qz = 0.0

    out[:] = [ qx, qy, qz, qw ]
    return out

def set_to_rotation_about_y( theta, out = None ):
    if out == None:
        out = _empty()
    
    thetaOver2 = theta * 0.5
    qw = math.cos( thetaOver2 )
    qx = 0.0
    qy = math.sin( thetaOver2 )
    qz = 0.0

    out[:] = [ qx, qy, qz, qw ]

    return out

def set_to_rotation_about_z( theta, out = None ):
    if out == None:
        out = _empty()
    
    thetaOver2 = theta * 0.5

    qw = math.cos( thetaOver2 )
    qx = 0.0
    qy = 0.0
    qz = math.sin( thetaOver2 )

    out[:] = [ qx, qy, qz, qw ]
    return out

def set_to_rotation_about_axis( axis, theta, out = None ):
    if out == None:
        out = _empty()
    
    # make sure the vector is normalised
    assert (numpy.linalg.norm( axis, ord = None ) - 1.0) < 0.01
    
    thetaOver2 = theta * 0.5
    sinThetaOver2 = math.sin( thetaOver2 )
    
    qw = math.cos( thetaOver2 )
    qx = axis[ 0 ] * sinThetaOver2
    qy = axis[ 1 ] * sinThetaOver2
    qz = axis[ 2 ] * sinThetaOver2

    out[:] = [ qx, qy, qz, qw ]
    return out

def create_from_eulers( eulers, out = None ):
    """
    Creates a quaternion from a set of Euler angles.

    Eulers are an array of length 3 in the following order:
        [ yaw, pitch, roll ]
    """
    if out == None:
        out = _empty()
    
    halfYaw = eulers[ 0 ] * 0.5
    sinYaw = math.sin( halfYaw )
    cosYaw = math.cos( halfYaw )

    halfPitch = eulers[ 1 ] * 0.5
    sinPitch = math.sin( halfPitch )
    cosPitch = math.cos( halfPitch )

    halfRoll = eulers[ 2 ] * 0.5
    sinRoll = math.sin( halfRoll )
    cosRoll = math.cos( halfRoll )
    
    # cy * cp * cr + sy * sp * sr
    qw = (cosYaw * cosPitch * cosRoll) + (sinYaw * sinPitch * sinRoll) 
    # -cy * sp * cr - sy * cp * sr
    qx = (-cosYaw * sinPitch * cosRoll) - (sinYaw * cosPitch * sinRoll)
    # cy * sp * sr - sy * cp * cr
    qy = (cosYaw * sinPitch * sinRoll) - (sinYaw * cosPitch * cosRoll)
    # sy * sp * cr - cy * cp * sr
    qz = (sinYaw * sinPitch * cosRoll) - (cosYaw * cosPitch * sinRoll)

    out[:] = [ qx, qy, qz, qw ]
    return out

def create_from_inverse_of_eulers( eulers, out = None ):
    """
    Creates a quaternion from the inverse of a set of Euler angles.

    Eulers are an array of length 3 in the following order:
        [ yaw, pitch, roll ]
    """
    if out == None:
        out = _empty()
    
    halfYaw = eulers[ 0 ] * 0.5
    sinYaw = math.sin( halfYaw )
    cosYaw = math.cos( halfYaw )

    halfPitch = eulers[ 1 ] * 0.5
    sinPitch = math.sin( halfPitch )
    cosPitch = math.cos( halfPitch )
    
    halfRoll = eulers[ 2 ] * 0.5
    sinRoll = math.sin( halfRoll )
    cosRoll = math.cos( halfRoll )
    
    # cy * cp * cr + sy * sp * sr
    qw = (cosYaw * cosPitch * cosRoll) + (sinYaw * sinPitch * sinRoll)
    # cy * sp * cr + sy * cp * sr
    qx = (cosYaw * sinPitch * cosRoll) + (sinYaw * cosPitch * sinRoll)
    # -cy * sp * sr + sy * cp * cr
    qy = (-cosYaw * sinPitch * sinRoll) + (sinYaw * cosPitch * cosRoll)
    # -sy * sp * cr + cy * cp * sr
    qz = (-sinYaw * sinPitch * cosRoll) + (cosYaw * cosPitch * sinRoll)

    out[:] = [ qx, qy, qz, qw ]
    return out

def cross( quat1, quat2, out = None ):
    """
    Returns the cross-product of the two quaternions.
    Order is important.
    This is NOT the same as a vector cross-product. Quaternion cross-product
    is the equivalent of matrix multiplication.
    """
    if out == None:
        out = _empty()

    # q1.w * q2.w - q1.x * q2.x - q1.y * q2.y - q1.z * q2.z
    qw = (quat1[ w ] * quat2[ w ]) - (quat1[ x ] * quat2[ x ]) - (quat1[ y ] * quat2[ y ]) - (quat1[ z ] * quat2[ z ])
    # q1.w * q2.x + q1.x * q2.w + q1.z * q2.y - q1.y * q2.z 
    qx = (quat1[ w ] * quat2[ x ]) + (quat1[ x ] * quat2[ w ]) + (quat1[ z ] * quat2[ y ]) - (quat1[ y ] * quat2[ z ])
    # q1.w * q2.y + q1.y * q2.w + q1.x * q2.z - q1.z * q2.x
    qy = (quat1[ w ] * quat2[ y ]) + (quat1[ y ] * quat2[ w ]) + (quat1[ x ] * quat2[ z ]) - (quat1[ z ] * quat2[ x ])
    # q1.w * q2.z + q1.z * q2.w + q1.y * q2.x - q1.x * q2.y
    qz = (quat1[ w ] * quat2[ z ]) + (quat1[ z ] * quat2[ w ]) + (quat1[ y ] * quat2[ x ]) - (quat1[ x ] * quat2[ y ])

    out[:] = [ qx, qy, qz, qw ]
    return out

def is_zero_length( quat ):
    """
    Checks if a quaternion is zero length.

    @param quat: The quaternion to check.
    @return: Returns True if the quaternion is
    zero length, otherwise returns False.
    """
    return quat[ 0 ] == quat[ 1 ] == quat[ 2 ] == quat[ 3 ] == 0.0

def is_non_zero_length( quat ):
    """
    Checks if a quaternion is not zero length.

    This is the opposite to 'is_zero_length'.
    This is provided for readabilities sake.

    @param quat: The quaternion to check.
    @return: Returns False if the quaternion is
    zero length, otherwise returns True.
    """
    return not is_zero_length( quat )

def squared_length( quat ):
    """
    Returns the squared length of a quaternion.
    Useful for avoiding the performanc penalty of
    the square root function.

    @param quat: The quaternion to measure.
    @return: The squared length of the quaternion.
    """
    return quat[ w ]**2 + quat[ x ]**2 + quat[ y ]**2 + quat[ z ]**2

def length( quat ):
    """
    Length of a quaternion is defined as
    sqrt( w^2 + x^2 + y^2 + z^2 )
    
    @param quat: The quaternion to measure.
    @return: The length of the quaternion.
    """
    return math.sqrt( quat[ w ]**2 + quat[ x ]**2 + quat[ y ]**2 + quat[ z ]**2 )

def normalise( quat ):
    """
    Normalise a quaternion by finding it's length
    then dividing each component by 1.0 / length.
    """
    mag = length( quat )
    if mag > 0.0:
        quat /= numpy.linalg.norm( quat, ord = None )
    else:
        raise ValueError( "Cannot normalise zero length quaternion" )

    return quat

def get_rotation_angle( quat ):
    thetaOver2 = math.acos( quat[ w ] )
    return thetaOver2 * 2.0

def get_rotation_axis( quat, out = None ):
    if out == None:
        out = numpy.empty( 3, dtype = float )
    
    sinThetaOver2Sq = 1.0 - ( quat[ w ] * quat[ w ] )
    
    if sinThetaOver2Sq <= 0.0:
        # assert here for the time being
        assert False
        print "rotation axis was identity"
        
        # identity quaternion or numerical imprecision.
        # just return a valid vector
        # we'll treat -Z as the default
        out[:] = [ 0.0, 0.0, -1.0 ]
        return out
    
    oneOverSinThetaOver2 = 1.0 / math.sqrt( sinThetaOver2Sq )
    
    out[:] = [
        quat[ x ] * oneOverSinThetaOver2,
        quat[ y ] * oneOverSinThetaOver2,
        quat[ z ] * oneOverSinThetaOver2
        ]
    return out

def dot_product( quat1, quat2 ):
    return (
        (quat1[ w ] * quat2[ w ]) + \
        (quat1[ x ] * quat2[ x ]) + \
        (quat1[ y ] * quat2[ y ]) + \
        (quat1[ z ] * quat2[ z ])
        )

def conjugate( quat, out = None ):
    """
    Returns a quaternion with the opposite rotation as the original quaternion
    """
    if out == None:
        out = _empty()
    
    qw = quat[ w  ]
    qx = -quat[ x ]
    qy = -quat[ y ]
    qz = -quat[ z ]

    out[:] = [ qx, qy, qz, qw ]
    return out

def power( quat, exponent, out = None ):
    if out == None:
        out = _empty()
    
    # check for identify quaternion
    if math.fabs( quat[ w ] ) > 0.9999:
        # assert for the time being
        assert False
        print "rotation axis was identity"
        
        out[:] = quat
        return out
    
    alpha = math.acos( quat[ w ] )
    newAlpha = alpha * exponent
    multi = math.sin( newAlpha ) / math.sin( alpha )
    
    qw = math.cos( newAlpha )
    qx = quat[ x ] * multi
    qy = quat[ y ] * multi
    qz = quat[ z ] * multi

    out[:] = [ qx, qy, qz, qw ]
    return out

def inverse( quat, out = None ):
    """
    The inverse of a quaternion is defined as
    the conjugate of the quaternion divided
    by the magnitude of the original quaternion.

    @param quat: The quaternion to invert.
    @param out: Optional out param that will be
    used to perform the operation in place.
    @return: Returns the inverse quaternion.
    """
    out = conjugate( quat, out )
    out /= length( quat )

    return out

def negate( quat, out = None ):
    if out == None:
        out = _empty()

    out[:] = quat
    out *= -1.0

    return out

def apply_to_vector( quat, vec ):
    """Rotates a vector by a quaternion.

    quat and vec must be 1d arrays.
    
    http://content.gpwiki.org/index.php/OpenGL:Tutorials:Using_Quaternions_to_represent_rotation
    """
    # create a new quaternion
    vq = create( w = 0.0, x = vec[ 0 ], y = vec[ 1 ], z = vec[ 2 ] )

    # quat * vec * quat^-1
    result = cross( quat, cross( vq, conjugate( quat ) ) )

    # ignore w component
    return result[ 1: ]
