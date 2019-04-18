# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [0.10.2] - 2019-03-13

- Add MANIFEST.in and add /tests and /docs to source dist (#90)

## [0.10.1] - Unreleased

## [0.10.0] - 2018-12-23

- Fix unit tests failing due to changes in numpy.testing (#77)
- Drop Python 3.3 as numpy no longer supports it.
- Ensure the latest versions of dependencies are installed when testing (#79)
- Add quaternion exp method (#74)
- Remove todo notes about quaternion methods that exist (#73)
- Remove Python 2.6 Support (#76)
- Add methods to create a quaternion from an axis (#72)
- Handle negative values in ray_intersect_aabb (#71)
- Made create_from_eulers use configurable order from euler.py (#69)
- Affine matrix decomposition (#65)
- Added equality operators for quaternion and matrices objects (#67)

## [0.9.2] - 2017-07-18
### Added
- Add `pyrr.vector3.generate_vertex_normals`

### Fixed
- Fix ignored `normalize_result` in `pyrr.vector3.generate_normals`

## [0.9.1] - 2017-07-06
### Fixed
- Fix `dtype` to numpy array conversion.

## [0.9.0] - 2017-06-28

Thanks to [Szabolcs Dombi](https://github.com/cprogrammer1994) for his contributions to this release.

### Added
- Add slerp / lerp to Quaternion.
- Add American spelling variation of 'normalise' ('normalize').
- Deprecate matrix functions with `*_matrix` in the name. Use the new alternatives provided.
- Add `create_look_at` in Matrix.

## [0.8.4]
### Fixed
- Fix Matrix33 / Matrix44 object API multiplication being logically backwards.

## [0.8.3]
### Fixed
- Fix rotation of zero length vector by a quaternion causing error

## [0.8.2]
### Fixed
- Fix Matrix <-> Quaternion conversions

## [0.8.1]
### Removed
- Remove notes about customising euler indices. If you change the axis indices then create_from_(x,y,z)_rotation will no longer work.

## [0.8.0]
### Changed
- Change euler parameter order for create function, was (pitch, roll, yaw, ...), now (roll, pitch, yaw, ..).
- Make eulers always use the indices for extracting and putting values.
- Make euler indices configurable by modifying euler.index.(pitch,roll,yaw)

### Fixed
- Fix euler -> matrix33 conversion.

### Added
- Add euler.create_from_(x,y,z)_rotation. This ignores pitch, roll, yaw indices and is a straight insertion into the x, y z values of the array.
- Add tests to ensure euler, quaternion, and matrix rotations are all equivalent.

## [0.7.2]
### Fixed
- Merge #37 - fix test suite name

## [0.7.1]
### Fixed
- Fix #36 Move tests inside pyrr, include in pkg

## [0.7.0]

> Note: that this version corrected an issue with quaternion rotations (quaternion cross) being inverted. Please ensure any quaternion logic is updated accordingly.

### Fixed
- Fixed quaternion cross product being reversed.

### Added
- Add more tests including quaternion identities.
- Added subtraction support to object api, this is to support np.allclose.

## [0.6.5]
### Added
* Add tests for Vector3/4 |^ operators
* Add support for numpy.number types

## [0.6.4]
### Fixed
* Fix Vector3/4 normalise failing.

## [0.6.3]
### Added
* Add support for +- Matrix33/44. Fixes #24.
* Add scalar support to Matrix33/44. Fixes #23.
* Add scalar support to Vector3/4. Fixes #22.
### Fixed
* Update version (0.6.2 was marked as 0.6.1!)

## [0.6.2]

* Remove import of unicode_literals. It seems to bebuggering up 'from pyrr import *'
* Move import tests into each module

## [0.6.1]

* Readd vector3|4.from_matrix44_translation.
* Remove unused import
* Use type(obj) instead of obj.__class__
* Add tests for = and += on NpProxy

## [0.6.0]

* Remove unused imports.
* Add docstrings to functions.
* Remove Matrix44.translation. Multiply a vector by the matrix to get this.
* Rename vector3|4.negative to inverse. This matches matrix.
* Remove ambiguous conversions in object api Matrix44->Vector, etc.
* Add Vector4.from_vector3 with w parameter, default w=0.0.
* Add Vector4.xyw.

## [0.5.1]

* Add multipledispatch to setup.py requirements

## [0.5.0]

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

## [0.4.0]

* Make vec4 w component default to 0.
* Remove Vector3 and Vector4 interoperability

## [0.3.0]

* Add object oriented API.
* Fix python 3 errors and numpy deprecated calls (np.array != None).
* Finally track down and fully resolve matrix / quaternion rotations.
Matrices were rotating in the opposite direction.

## [0.2.4]

* Remove unittest2

## [0.2.3]

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

## [0.2.2]

* skipped

## [0.2.1]

* Fix matrix44.create_from_eulers calling function with invalid params.
* Fix quaternion inverse calling squared_length instead of length.
* Fix matrix33.create_from_inverse_of_quaternion, had a - instead of a +.
* Fix syntax error in quaternion.power.
* Remove matrix33.apply_scale. Function was a duplicate of matrix33.create_from_scale
with an incorrect name.

[Unreleased]: https://github.com/adamlwgriffiths/Pyrr/compare/0.9.2...master
[0.9.2]: https://github.com/adamlwgriffiths/Pyrr/compare/0.9.1...0.9.2
[0.9.1]: https://github.com/adamlwgriffiths/Pyrr/compare/0.9.0...0.9.1
[0.9.0]: https://github.com/adamlwgriffiths/Pyrr/tree/0.9.0
[0.8.4]: https://github.com/adamlwgriffiths/Pyrr/compare/0.8.3...0.8.4
[0.8.3]: https://github.com/adamlwgriffiths/Pyrr/compare/0.8.2...0.8.3
[0.8.2]: https://github.com/adamlwgriffiths/Pyrr/compare/0.8.1...0.8.2
[0.8.1]: https://github.com/adamlwgriffiths/Pyrr/compare/0.8.0...0.8.1
[0.8.0]: https://github.com/adamlwgriffiths/Pyrr/tree/0.8.0
[0.7.2]: https://github.com/adamlwgriffiths/Pyrr/compare/0.7.1...0.7.2
[0.7.1]: https://github.com/adamlwgriffiths/Pyrr/compare/0.7.0...0.7.1
[0.7.0]: https://github.com/adamlwgriffiths/Pyrr/tree/0.7.0
[0.6.5]: https://github.com/adamlwgriffiths/Pyrr/compare/0.6.4...0.6.5
[0.6.4]: https://github.com/adamlwgriffiths/Pyrr/compare/0.6.3...0.6.4
[0.6.3]: https://github.com/adamlwgriffiths/Pyrr/compare/0.6.2...0.6.3
[0.6.2]: https://github.com/adamlwgriffiths/Pyrr/compare/0.6.1...0.6.2
[0.6.1]: https://github.com/adamlwgriffiths/Pyrr/compare/0.6.0...0.6.1
[0.6.0]: https://github.com/adamlwgriffiths/Pyrr/tree/0.6.0
[0.5.1]: https://github.com/adamlwgriffiths/Pyrr/compare/0.5.0...0.5.1
[0.5.0]: https://github.com/adamlwgriffiths/Pyrr/tree/0.5.0
[0.4.0]: https://github.com/adamlwgriffiths/Pyrr/tree/0.4.0
[0.3.0]: https://github.com/adamlwgriffiths/Pyrr/tree/0.3.0
[0.2.4]: https://github.com/adamlwgriffiths/Pyrr/compare/0.2.3...0.2.4
[0.2.3]: https://github.com/adamlwgriffiths/Pyrr/compare/0.2.2...0.2.3
[0.2.2]: https://github.com/adamlwgriffiths/Pyrr/compare/0.2.1...0.2.2
[0.2.1]: https://github.com/adamlwgriffiths/Pyrr/tree/0.2.1
