Pyrr
====

[![Build Status](https://travis-ci.org/adamlwgriffiths/Pyrr.png?branch=master)](https://travis-ci.org/adamlwgriffiths/Pyrr)

Provides 3D mathematical functions using the power of NumPy.

Features:
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

    from pyrr import quaternion, matrix44, vector3
    import numpy as np

    orientation = quaternion.create(dtype=np.float32)        
    translation = vector3.create(dtype=np.float32)
    scale = vector3.create(1,1,1,dtype=np.float32)

    # translate along X by 1
    translation += [1.0, 0.0, 0.0]

    # rotate about Y by pi/2
    rotation = quaternion.create_from_y_rotation(math.pi / 2.0, dtype=np.float32)
    orientation = quaternion.cross(rotation, orientation)

    # create a matrix
    # start our matrix off using the scale
    matrix = matrix44.create_from_scale(scale, dtype=np.float32)

    # apply our orientation
    orientation = matrix44.create_from_quaternion(orientation)
    matrix = matrix44.multiply(matrix, orientation)

    # apply our translation
    translation = matrix44.create_from_translation(translation)
    matrix = matrix44.multiply(matrix, translation)


Installation
------------

Pyrr is in the PyPi database and can be installed via pip:
```
pip install pyrr
```

Pyrr requires the following software:

    * Python 2.6+ / 3.0+
    * NumPy


Authors
-------

    * [Adam Griffiths](https://github.com/adamlwgriffiths/).
    * [Jakub Stasiak](https://github.com/jstasiak/).

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
