.. _data_types:

Data types
**********


.. _data_types_modules:

Modules
=======

Each data type resides in its own module named after the specified type.

Where there may be multiple versions of a data type, each version is located in its own module.

Functions which are able to handle all versions of a data type are located in the central module. Otherwise, functions reside in the specific data type's module.

For example:

    * **vector3.py** Provides functions for creating and manipulating 3D vectors (x,y,z).
    * **vector4.py** Provides functions for creating and manipulating 4D vectors (x,y,z,w).
    * **vector.py** Provides functions that work with both 3D and 4D vectors.


.. _data_types_conversion:

Conversion
==========

Data conversion functions are provided in the module of the type being converted to.

For example::

    # module matrix44.py
    def create_from_matrix33(mat) :
        pass

    def create_from_eulers(eulers):
        pass

    def create_from_quaternion(quat):
        pass
