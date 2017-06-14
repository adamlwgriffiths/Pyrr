Pyrr
====

[![Build Status](https://travis-ci.org/adamlwgriffiths/Pyrr.png?branch=master)](https://travis-ci.org/adamlwgriffiths/Pyrr)

Provides 3D mathematical functions using the power of NumPy.

Features:
  * Object Oriented and Procedural interfaces
  * Matrix (3x3, 4x4)
  * Quaternion
  * Vector (3D, 4D)
  * Plane
  * Ray
  * Line / Line Segment (3D)
  * Rectangle (2D)
  * Axis Aligned Bounding Box (AABB / AAMBB)
  * Geometric collision / intersection testing

Documentation
-------------

[View Pyrr's documentation online](https://pyrr.readthedocs.org/en/latest/).


Examples
--------

Maintain a rotation (quaternion) and translation (vector) and convert to a matrix

Object Oriented Interface

    from pyrr import Quaternion, Matrix44, Vector3
    import numpy as np

    point = Vector3([1.,2.,3.])
    orientation = Quaternion()
    translation = Vector3()
    scale = Vector3([1.,1.,1.])

    # translate along X by 1
    translation += [1.0, 0.0, 0.0]

    # rotate about Y by pi/2
    rotation = Quaternion.from_y_rotation(np.pi / 2.0)
    orientation = rotation * orientation

    # create a matrix
    # start our matrix off using the scale
    matrix = Matrix44.from_scale(scale)

    # apply our orientation
    # we can multiply matricies and quaternions directly!
    matrix = matrix * orientation

    # apply our translation
    translation = Matrix44.from_translation(translation)
    matrix = matrix * translation

    # transform our point by the matrix
    # vectors are transformable by matrices and quaternions directly
    point = matrix * point


Procedural Interface

    from pyrr import quaternion, matrix44, vector3
    import numpy as np

    point = vector3.create(1.,2.,3.)
    orientation = quaternion.create()
    translation = vector3.create()
    scale = vector3.create(1,1,1)

    # translate along X by 1
    translation += [1.0, 0.0, 0.0]

    # rotate about Y by pi/2
    rotation = quaternion.create_from_y_rotation(np.pi / 2.0)
    orientation = quaternion.cross(rotation, orientation)

    # create a matrix
    # start our matrix off using the scale
    matrix = matrix44.create_from_scale(scale)

    # apply our orientation
    orientation = matrix44.create_from_quaternion(orientation)
    matrix = matrix44.multiply(matrix, orientation)

    # apply our translation
    translation_matrix = matrix44.create_from_translation(translation)
    matrix = matrix44.multiply(matrix, translation_matrix)

    # transform our point by the matrix
    point = matrix44.apply_to_vector(matrix, point)



Object Oriented Features
========================

Convertable types
-----------------


    from pyrr import Quaternion, Matrix33, Matrix44, Vector3, Vector4

    v3 = Vector3([1.,0.,0.])
    v4 = Vector4.from_vector3(v3, w=1.0)
    v3, w = Vector3.from_vector4(v4)

    m44 = Matrix44()
    q = Quaternion(m44)
    m33 = Matrix33(q)

    m33 = Matrix44().matrix33
    m44 = Matrix33().matrix44
    q = Matrix44().quaternion
    q = Matrix33().quaternion

    m33 = Quaternion().matrix33
    m44 = Quaternion().matrix44


Convenient Operators
--------------------

    from pyrr import Quaternion, Matrix44, Matrix33, Vector3, Vector4
    import numpy as np

    # matrix multiplication
    m = Matrix44() * Matrix33()
    m = Matrix44() * Quaternion()
    m = Matrix33() * Quaternion()

    # matrix inverse
    m = ~Matrix44.from_x_rotation(np.pi)

    # quaternion multiplication
    q = Quaternion() * Quaternion()
    q = Quaternion() * Matrix44()
    q = Quaternion() * Matrix33()

    # quaternion inverse (conjugate)
    q = ~Quaternion()

    # quaternion dot product
    d = Quaternion() | Quaternion()

    # vector oprations
    v = Vector3() + Vector3()
    v = Vector4() - Vector4()

    # vector transform
    v = Quaternion() * Vector3()
    v = Matrix44() * Vector3()
    v = Matrix44() * Vector4()
    v = Matrix33() * Vector3()

    # dot and cross products
    dot = Vector3() | Vector3()
    cross = Vector3() ^ Vector3()



Installation
------------

Pyrr is in the PyPi database and can be installed via pip:
```
pip install pyrr
```

Pyrr requires the following software:

  * Python 2.6+ / 3.0+
  * NumPy
  * [multipledispatch](https://github.com/mrocklin/multipledispatch/)


Changelog
---------

[View the changelog](CHANGELOG.md).


Authors
-------

  * [Adam Griffiths](https://github.com/adamlwgriffiths/).
  * [Chris Bates](https://github.com/chrsbats)
  * [Jakub Stasiak](https://github.com/jstasiak/).
  * [Bogdan Teleaga](https://github.com/bogdanteleaga/).
  * [Szabolcs Dombi](https://github.com/cprogrammer1994)

Contributions are welcome.


License
---------------

Pyrr is released under the BSD 2-clause license (a very relaxed licence), but it is encouraged that any modifications are submitted back to the master for inclusion.

Created by Adam Griffiths.

Copyright (c) 2012, Twisted Pair Development.
All rights reserved.

twistedpairdevelopment.wordpress.com
@twistedpairdev

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.
