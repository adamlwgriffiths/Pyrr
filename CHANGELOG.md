Changelog
=========

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
