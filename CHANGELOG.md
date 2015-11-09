Changelog
=========

0.7.0
-----

Note: that this version corrected an issue with quaternion rotations (quaternion
cross) being inverted.
Please ensure any quaternion logic is updated accordingly.

* Fixed quaternion cross product being reversed.
* Add more tests including quaternion identities.


0.6.5
-----

* Add tests for Vector3/4 |^ operators
* Add support for numpy.number types


0.6.4
-----

* Fix Vector3/4 normalise failing.


0.6.3
-----

* Add support for +- Matrix33/44. Fixes #24.
* Add scalar support to Matrix33/44. Fixes #23.
* Add scalar support to Vector3/4. Fixes #22.
* Update version (0.6.2 was marked as 0.6.1!)


0.6.2
-----

* Remove import of unicode_literals.
It seems to be buggering up 'from pyrr import *'

* Move import tests into each module


0.6.1
-----

* Readd vector3|4.from_matrix44_translation.

* Remove unused import

* Use type(obj) instead of obj.__class__

* Add tests for = and += on NpProxy


0.6.0
-----

* Remove unused imports.

* Add docstrings to functions.

* Remove Matrix44.translation. Multiply a vector by
the matrix to get this.

* Rename vector3|4.negative to inverse. This matches matrix.

* Remove ambiguous conversions in object api Matrix44->Vector, etc.

* Add Vector4.from_vector3 with w parameter, default w=0.0.

* Add Vector4.xyw.


0.5.1
-----

* Add multipledispatch to setup.py requirements


0.5.0
-----

* Add quaternion.is_identity

* Remove vector3.create_from_vector4, this is ambiguous
and was assuming 3d graphics style conversion (w=1.0).
Do this manually instead to remove ambiguities.

* Remove vector3|4.create_from_matrix44_translation.
This was assuming vector4 had w=1.0 again.
Instead create a basic vector and multiply it by the
matrix.

* Move vector.cross into vector3. This is ambiguous
for vector4.

* Move vector.generate_normals into vector3. This is
ambiguous for vector4.

* Change how quaternion.apply_to_vector works.
Previously vectors were converted to vec3s with w=0.
Now vectors are converted to vec4s, with vector 4's being
untouched.

* Change how matrix44 works with vector4s.
It no longer divides by W for vector4s.
Vector 3's are converted to vec4s during the calculation
and back again. They were previously not divided by W
if W was 0. Now they are converted to [np.inf, ...]
in the case that W is 0.

* Remove conversions from Vector4 and Vector3 in the OO API.
These were ambiguous.

* Remove Vector3|4.vector3 and Vector3|4.vector4.
These conversions were ambiguous, convert manually.

* Remove ability to transform vector4's in matrix33.apply_to_vector.
This was ambiguous. Perform the conversion manually then call this.
Or convert to a matrix44 and then transform.

* Make matrix44.create_perspective_projection_matrix use
matrix44.create_perspective_projection_matrix_from_bounds
based on code from GLU.


0.4.0
-----

* Make vec4 w component default to 0.
* Remove Vector3 and Vector4 interoperability


0.3.0
-----

* Add object oriented API.
* Fix python 3 errors and numpy deprecated calls (np.array != None).
* Finally track down and fully resolve matrix / quaternion rotations.
Matrices were rotating in the opposite direction.


0.2.4
-----

* Remove unittest2


0.2.3
-----

* Add unittest2 on Travis for python 2.6 to enable skipping tests rather than
commenting them out.
* Fixing matrix / quaternion rotation differences.
* Add tests for nearly all functions.
* Fix plane.create_xy|yz|xz and add a distance parameter.
* Change rect default to np.float, was np.int.
* Clean up matrix33.create_direction_scale.
* Fix some functions incorrectly using 'all_parameters_as_numpy_arrays', which
would attempt to np.array the dtype parameters.
* Fix geometric_tests.point_closest_point_on_line not keeping the normalised
vector and therefore returning incorrect results.
* Fix aambb calling np.zeros as np.zeroEs.
* Rename aambb functions parameter bbs to aabbs.
* Fix aambb.add_points.
* Fix aabb.clamp_points.
* Fix aabb.zeros.


0.2.2
-----

* skipped


0.2.1
-----

* Fix matrix44.create_from_eulers calling function with invalid params.
* Fix quaternion inverse calling squared_length instead of length.
* Fix matrix33.create_from_inverse_of_quaternion, had a - instead of a +.
* Fix syntax error in quaternion.power.
* Remove matrix33.apply_scale. Function was a duplicate of matrix33.create_from_scale
with an incorrect name.
