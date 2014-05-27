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

* Class implementations shall have a function equivalent, where appropriate.

For example, a Sphere object may provide a function to collide against a Plane.
In this case, there must be a function that performs the same operation without the use of the Sphere class.

Higher level logic may be left exclusive to Classes.
For example, a generic collision handler function which can select the appropriate collision function based on the colliding objects.


.. _coding_standard_function_names:

Function names
==============

* Function names and parameters shall be lower-case with underscores delimiting words::

    def an_example_function(with_some, parameters):
       pass

* Each type shall have a basic *create* function which returns a zero-ed type, where it makes sense.

A good example::

    # vector3.py
    def create():
        # vectors are commonly initialised manually
        # so this is ok
        pass

    # matrix33.py
    def create_identity():
        # creates the matrix in a standard, known state
        pass

A bad example::

    # matrix33.py
    def create():
        # matrices aren't initialised manually
        # so this isn't ok
        pass

* Where multiple creation functions are defined, each function shall be prefixed with *create_*::

    def create_identity():
        pass

    def create_unit_length_x():
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

* Each function shall have a test case associated with it::

    # vector3.py
    def create_identity():
        pass

    # test_vector3.py
    def test_create_identity():
        vec = vector3.create_identity()
        expected = [ 0.0, 0.0, 0.0 ]
        self.assertTrue(numpy.array_equal(vec, expected), "Vector zeros not zeroed")


.. _coding_standard_layout:

Layout
======

These are not strict rules, but are merely suggestions to keep the layout of code in Pyrr consistent.

There are times when the following rules may be broken to improve readability.

* Code shall be spaced vertically rather than extending horizontally too far. Vertical spacing shall be performed at variable or data type boundaries.

A good example::

    # laying out over multiple lines helps improve readability.
    # brackets and parenthesis are laid out to more clearly indicate
    # the end of an array / type.
    # where appropriate, values are still laid out horizontally.
    # provide links where appropriate
    #  http://www.example.com/a/link/to/a/relevant/explanation/of/this/code
    my_value = numpy.array(
        [
            # X = some comment about how X is calculated
            (0.0, 0.0, 0.0),
            # Y = some comment about how Y is calculated
            (1.0, 1.0, 1.0)
        ],
        dtype=[('position', 'float32', (3,))]
    )

    # laying out parameters vertically can improve readability.
    # we'll be less likely to accidently pass an invalid value
    # and we can more easily, and more clearly, add logic to the parameters.
    some_complex_function_call(
        param_one,
        param_two,
        param_three,
        param_four,
        True if param_five else False
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

* Classes should have 2 lines between them and any other definition::

    class X:
        pass


    class Y:
        pass


* Class variables and functions shall be separated by a single white line::

    class X:
        a = 1

        def __init__( self ):
            pass

* Class members and variables shall begin immediately below the class declaration::

    class X:
        a = 1
        b = 2

* Variables and methods should have a single, empty line between them::

    class X:
        a = 1
        b = 2

        def do_something( self ):
            pass

* Imports and functions should have two empty lines between them::

    import math
    import numpy


    def some_function():
        pass


