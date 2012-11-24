import numpy


def identity():
    return numpy.zeros( 3 )

def create_unit_length_x():
    return numpy.array( [ 1.0, 0.0, 0.0 ] )

def create_unit_length_y():
    return numpy.array( [ 0.0, 1.0, 0.0 ] )

def create_unit_length_z():
    return numpy.array( [ 0.0, 0.0, 1.0 ] )

def create_from_vector4( vector ):
    return numpy.array( vector[ :-1 ] )

class unit:
    x = create_unit_length_x()
    y = create_unit_length_y()
    z = create_unit_length_z()
