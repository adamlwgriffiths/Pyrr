.. _coding_standard:

Coding Standard
***************

* Follow PEP-8


.. _coding_standard_modules:

Modules
=======

Each value type is given its own module.

Functions that reside in these modules include:

* Creation

* Conversion

* Manipulation


.. _coding_standard_functions:

Functions
=========

* Existing numpy operations shall be wrapped where it may not be obvious how to perform the operation.

A good example::

    def multiply(m1, m2):
        # it may not be obvious that the 'dot' operator is the
        # equivalent of multiplication when using arrays as matrices
        # so this is good to help point users in the right direction
        return numpy.dot(m1, m2)

A bad example::

    def add(v1, v2):
        # this functionality is too obvious and too basic
        return v1 + v2

* Functions shall not modify data in-place.

* Procedural and Class implementations shall remain in lock-step.


.. _coding_standard_function_names:

Function names
==============

* Each type shall provide convenience *create* functions for conversions and other initialisations.

* Each type shall have a basic *create* function which returns a zero-ed type, where it makes sense.

A good example::

    # vector3.py
    def create(x=0., y=0., z=0., dtype=None):
        if isinstance(x, (list, np.ndarray)):
            raise ValueError('Function requires non-list arguments')
        return np.array([x,y,z], dtype=dtype)

    def create_unit_length_x(dtype=None):
        return np.array([1.0, 0.0, 0.0], dtype=dtype)

    def create_unit_length_y(dtype=None):
        return np.array([0.0, 1.0, 0.0], dtype=dtype)

    def create_unit_length_z(dtype=None):
        return np.array([0.0, 0.0, 1.0], dtype=dtype)


A bad example::

    # matrix33.py
    def create():
        # matrices aren't initialised manually
        # so this isn't ok
        pass

* Conversion functions shall be prefixed with *create_from_* followed by the type being converted from::

    def create_from_matrix(matrix):
        # converts from one type to another
        # this would have to support both matrix33 and matrix44
        pass

    def create_from_matrix33(matrix):
        # converts from a very specific type
        # only has to support matrix33
        pass


.. _coding_standard_supplimentary_data:

Supplimentary Data
==================

When dealing with arrays and other complex data types, it is helpful to provide methods to identify which array index relates to what data.

A good method to do this is to provide a class definition which contains these values::

    class index:
        x = 0
        y = 1
        z = 2
        w = 3


.. _coding_standard_tests:

Tests
=====

* A test class for each module shall be provided in the *pyrr/test* directory.

* A test class shall be the only class in the test module.

* Each source file shall have its own test file.

* Each test function shall have a test case associated with it

* All test cases for a function shall be in a single test function

.. _coding_standard_layout:

Layout
======

These are not strict rules, but are merely suggestions to keep the layout of code in Pyrr consistent.

* Code shall be spaced vertically where doing so helps the readability of complex mathematical functions. Vertical spacing shall be performed at variable or data type boundaries.

A good example::

    # laying out over multiple lines helps improve readability.
    # brackets and parenthesis are laid out to more clearly indicate
    # the end of an array / type.
    # where appropriate, values are still laid out horizontally.
    # provide links where appropriate
    #  http://www.example.com/a/link/to/a/relevant/explanation/of/this/code
    my_value = numpy.array([
        # X = some comment about how X is calculated
        (0.0, 0.0, 0.0),
        # Y = some comment about how Y is calculated
        (1.0, 1.0, 1.0)
    ], dtype=[('position', 'float32', (3,))]
    )

    # laying out parameters vertically can improve readability.
    # we'll be less likely to accidently pass an invalid value
    # and we can more easily, and more clearly, add logic to the parameters.
    some_complex_function_call(
        param_one,
        param_two,
        param_three,
        param_four,
        True if param_five else False,
    )

A more complicated example::

    return np.array(
        [
            # m1
            [
                # m11 = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
                1.0 - 2.0 * (y2 + z2),
                # m21 = 2.0 * (q.x * q.y + q.w * q.z)
                2.0 * (xy + wz),
                # m31 = 2.0 * (q.x * q.z - q.w * q.y)
                2.0 * (xz - wy),
            ],
            # m2
            [
                # m12 = 2.0 * (q.x * q.y - q.w * q.z)
                2.0 * (xy - wz),
                # m22 = 1.0 - 2.0 * (q.x * q.x + q.z * q.z)
                1.0 - 2.0 * (x2 + z2),
                # m32 = 2.0 * (q.y * q.z + q.w * q.x)
                2.0 * (yz + wx),
            ],
            # m3
            [
                # m13 = 2.0 * ( q.x * q.z + q.w * q.y)
                2.0 * (xz + wy),
                # m23 = 2.0 * (q.y * q.z - q.w * q.x)
                2.0 * (yz - wx),
                # m33 = 1.0 - 2.0 * (q.x * q.x + q.y * q.y)
                1.0 - 2.0 * (x2 + y2),
            ]
        ],
        dtype=dtype
    )

A bad example::

    # leaving this on a single line would not compromise readability
    my_value = numpy.empty(
        (3,)
    )

The same applies to function definitions::

    def some_function(that_takes, many_parameters, and_is, hard_to_read, because, its_so, big):
        pass

Should become::

    def some_function(
        that_takes,
        many_parameters,
        and_is,
        hard_to_read,
        because,
        its_so,
        big
    ):
        pass


* Code may extend beyond 80 columns, where appropriate.
