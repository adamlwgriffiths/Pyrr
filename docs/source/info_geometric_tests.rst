.. _geometric_tests:

Geometric Tests
***************


.. _geometric_tests_naming_scheme:

Naming Scheme
=============

Geometric Tests, also called Collision Detection, is provided by the geometric_tests module.

Functions match a specific naming scheme. The function name provides information on what types are being checked, and what check is being performed.

Function names adhere to the following format::

    def <type>_<check type>_<type>( ... ):
        pass

The order of parameters matches the order of types given in the function name.

The following are examples of this naming scheme::

    def point_intersect_line(point, line):
        """This function returns the intersection point as a vector or None if there is no intersection.
        """
        pass

    def point_closest_point_on_line_segment(point, segment):
        """The function returns the closest on the line segment, to the given point.
        """
        pass


.. _geometric_tests_types_of_checks:

Types of Checks
===============

Below are some of the types of checks provided. These are the names used by the functions and their meaning.

    * **intersect** Returns the intersection point of the two types or None.
    * **does_intersect** Returns True if the types are intersecting.
    * **height_above** Returns the height of one type above another.
    * **closest_point_on** Returns the closest point on the second type.
    * **parallel** Returns True if the types are parallel to each other.
    * **coincident** Returns True if the types are not only parallel, but are along the same direction axis.
    * **penetration** Returns the penetration distance of one type into the second.

There may be more checks provided by the module than are listed here.
