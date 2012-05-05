'''
Created on 21/06/2011

@author: adam
'''

import math

import numpy


w = 0
x = 1
y = 2
z = 3

# TODO: slerp, lerp

def identity( out = None ):
    if out == None:
        out = numpy.empty( 4, dtype = float )
    
    out[:] = [ 1.0, 0.0, 0.0, 0.0 ]
    return out

def set_to_rotation_about_x( theta, out = None ):
    if out == None:
        out = numpy.empty( 4, dtype = float )
    
    thetaOver2 = theta * 0.5
    out[:] = [
        math.cos( thetaOver2 ),
        math.sin( thetaOver2 ),
        0,
        0
        ]
    return out

def set_to_rotation_about_y( theta, out = None ):
    if out == None:
        out = numpy.empty( 4, dtype = float )
    
    thetaOver2 = theta * 0.5
    out[:] = [
        math.cos( thetaOver2 ),
        0,
        math.sin( thetaOver2 ),
        0
        ]
    return out

def set_to_rotation_about_z( theta, out = None ):
    if out == None:
        out = numpy.empty( 4, dtype = float )
    
    thetaOver2 = theta * 0.5
    out[:] = [
        math.cos( thetaOver2 ),
        0,
        0,
        math.sin( thetaOver2 )
        ]
    return out

def set_to_rotation_about_axis( axis, theta, out = None ):
    if out == None:
        out = numpy.empty( 4, dtype = float )
    
    # make sure the vector is normalised
    assert (numpy.linalg.norm( axis, ord = None ) - 1.0) < 0.01
    
    thetaOver2 = theta * 0.5
    sinThetaOver2 = math.sin( thetaOver2 )
    
    out[:] = [
        math.cos( thetaOver2 ),
        axis[ 0 ] * sinThetaOver2,
        axis[ 1 ] * sinThetaOver2,
        axis[ 2 ] * sinThetaOver2
        ]
    return out

def set_to_rotation_object_to_inertial( eulers, out = None ):
    if out == None:
        out = numpy.empty( 4, dtype = float )
    
    pitchOver2 = eulers[ 0 ] * 0.5
    rollOver2 = eulers[ 1 ] * 0.5
    yawOver2 = eulers[ 2 ] * 0.5
    
    sinPitch = math.sin( pitchOver2 )
    cosPitch = math.cos( pitchOver2 )
    sinRoll = math.sin( rollOver2 )
    cosRoll = math.cos( rollOver2 )
    sinYaw = math.sin( yawOver2 )
    cosYaw = math.cos( yawOver2 )
    
    out[:] = [
        # cy * cp * cr + sy * sp * sr
        (cosYaw * cosPitch * cosRoll) + (sinYaw * sinPitch * sinRoll),
        # cy * sp * cr + sy * cp * sr
        (cosYaw * sinPitch * cosRoll) + (sinYaw * cosPitch * sinRoll),
        # -cy * sp * sr + sy * cp * cr
        (-cosYaw * sinPitch * sinRoll) + (sinYaw * cosPitch * cosRoll),
        # -sy * sp * cr + cy * cp * sr
        (-sinYaw * sinPitch * cosRoll) + (cosYaw * cosPitch * sinRoll)
        ]
    return out

def set_to_rotation_inertial_to_object( eulers, out = None ):
    if out == None:
        out = numpy.empty( 4, dtype = float )
    
    pitchOver2 = eulers[ 0 ] * 0.5
    rollOver2 = eulers[ 1 ] * 0.5
    yawOver2 = eulers[ 2 ] * 0.5
    
    sinPitch = math.sin( pitchOver2 )
    cosPitch = math.cos( pitchOver2 )
    sinRoll = math.sin( rollOver2 )
    cosRoll = math.cos( rollOver2 )
    sinYaw = math.sin( yawOver2 )
    cosYaw = math.cos( yawOver2 )
    
    out[:] = [
        # cy * cp * cr + sy * sp * sr
        (cosYaw * cosPitch * cosRoll) + (sinYaw * sinPitch * sinRoll), 
        # -cy * sp * cr - sy * cp * sr
        (-cosYaw * sinPitch * cosRoll) - (sinYaw * cosPitch * sinRoll),
        # cy * sp * sr - sy * cp * cr
        (cosYaw * sinPitch * sinRoll) - (sinYaw * cosPitch * cosRoll),
        # sy * sp * cr - cy * cp * sr
        (sinYaw * sinPitch * cosRoll) - (cosYaw * cosPitch * sinRoll)
        ]
    return out

def cross_product( quat1, quat2, out = None ):
    """
    Returns the cross-product of the two quaternions.
    Order is important.
    This is NOT the same as a vector cross-product. Quaternion cross-product
    is the equivalent of matrix multiplication.
    """
    if out == None:
        out = numpy.empty( 4, dtype = float )
    # TODO: this isn't triggering the scene node's setOrientation property function!
    out[:] = [
        # q1.w * q2.w - q1.x * q2.x - q1.y * q2.y - q1.z * q2.z
        (quat1[ w ] * quat2[ w ]) - (quat1[ x ] * quat2[ x ]) - \
            (quat1[ y ] * quat2[ y ]) - (quat1[ z ] * quat2[ z ]),
        # q1.w * q2.x + q1.x * q2.w + q1.z * q2.y - q1.y * q2.z 
        (quat1[ w ] * quat2[ x ]) + (quat1[ x ] * quat2[ w ]) + \
            (quat1[ z ] * quat2[ y ]) - (quat1[ y ] * quat2[ z ]),
        # q1.w * q2.y + q1.y * q2.w + q1.x * q2.z - q1.z * q2.x
        (quat1[ w ] * quat2[ y ]) + (quat1[ y ] * quat2[ w ]) + \
            (quat1[ x ] * quat2[ z ]) - (quat1[ z ] * quat2[ x ]),
        # q1.w * q2.z + q1.z * q2.w + q1.y * q2.x - q1.x * q2.y
        (quat1[ w ] * quat2[ z ]) + (quat1[ z ] * quat2[ w ]) + \
            (quat1[ y ] * quat2[ x ]) - (quat1[ x ] * quat2[ y ]), 
        ]
    return out

def length( quat ):
    return math.sqrt(
        quat[ w ]**2 + \
        quat[ x ]**2 + \
        quat[ y ]**2 + \
        quat[ z ]**2
        )

def normalise( quat ):
    mag = length( quat )
    if mag > 0.0:
        oneOverMag = 1.0 / mag
        quat[ w ] *= oneOverMag
        quat[ x ] *= oneOverMag
        quat[ y ] *= oneOverMag
        quat[ z ] *= oneOverMag
    else:
        assert False
    assert 0.9 < length( quat )
    assert 1.1 > length( quat )
    #quat /= numpy.linalg.norm( quat, ord = None )
    #assert numpy.linalg.norm( quat, ord = None ) == 1.0
    return quat

def get_rotation_angle( quat ):
    thetaOver2 = math.acos( quat[ w ] )
    return thetaOver2 * 2.0

def get_rotation_axis( quat, out = None ):
    if out == None:
        out = numpy.empty( 3, dtype = float )
    
    sinThetaOver2Sq = 1.0 - (quat[ w ]**quat[ w ])
    
    if sinThetaOver2Sq <= 0.0:
        # assert here for the time being
        #assert False
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
    return \
        (quat1[ w ] * quat2[ w ]) + \
        (quat1[ x ] * quat2[ x ]) + \
        (quat1[ y ] * quat2[ y ]) + \
        (quat1[ z ] * quat2[ z ])

def conjugate( quat, out = None ):
    """
    Returns a quaternion with the opposite rotation as the original quaternion
    """
    if out == None:
        out = numpy.empty( 4, dtype = float )
    
    out[:] = [
        quat[ w ],
        -quat[ x ],
        -quat[ y ],
        -quat[ z ]
        ]
    return out

def power( quat, exponent, out = None ):
    if out == None:
        out = numpy.empty( 4, dtype = float )
    
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
    
    out[:] = [
        math.cos( newAlpha ),
        quat[ x ] * multi,
        quat[ y ] * multi,
        quat[ z ] * multi
        ]
    return out


if __name__ == "__main__":
    quat = numpy.array( [0.0, 0.0, 0.0, 0.0], dtype = float )
    quat2 = quat
    
    identity( quat )
    assert quat[ w ] == 1.0
    assert quat[ x ] == 0.0
    assert quat[ y ] == 0.0
    assert quat[ z ] == 0.0
    assert quat2 is quat
    
    quat = identity()
    assert quat[ w ] == 1.0
    assert quat[ x ] == 0.0
    assert quat[ y ] == 0.0
    assert quat[ z ] == 0.0
    assert quat2 is not quat
    
    normalise( quat )
    assert quat[ w ] == 1.0
    assert quat[ x ] == 0.0
    assert quat[ y ] == 0.0
    assert quat[ z ] == 0.0
    
    quat[ w ] = 2.0
    normalise( quat )
    assert quat[ w ] == 1.0
    assert quat[ x ] == 0.0
    assert quat[ y ] == 0.0
    assert quat[ z ] == 0.0
    
    del quat2

