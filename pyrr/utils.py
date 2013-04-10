# -*- coding: utf-8 -*-
"""Provides common utility functions.
"""
import inspect
from functools import wraps

import numpy


def all_parameters_as_numpy_arrays( fn ):
    """Converts all of a function's arguments to numpy arrays.

    Used as a decorator to reduce duplicate code.
    """
    # wraps allows us to pass the docstring back
    # or the decorator will hide the function from our doc generator
    @wraps( fn )
    def wrapper( *args, **kwargs ):
        np_args = [
            numpy.array( arg ) if arg is not None else arg
            for arg in args
            ]
        np_kwargs = dict(
            (
                key,
                numpy.array( value ) if value is not None else value
                )
            for (key, value) in kwargs
            )
        return fn( *np_args, **np_kwargs )
    return wrapper

def parameters_as_numpy_arrays( *args_to_convert ):
    """Converts specific arguments to numpy arrays.

    Used as a decorator to reduce duplicate code.

    Arguments are specified by their argument name.
    For example
    ::
    
        @parameters_as_numpy_arrays( 'a', 'b', 'optional' )
        def myfunc( a, b, *args, **kwargs ):
            pass

        myfunc( 1, [2,2], optional = [3,3,3] )
    """
    def decorator( fn ):
        # wraps allows us to pass the docstring back
        # or the decorator will hide the function from our doc generator
        @wraps( fn )
        def wrapper( *args, **kwargs ):
            # get the arguements of the function we're decorating
            fn_args = inspect.getargspec( fn )

            # convert any values that are specified
            # if the argument isn't in our list, just pass it through

            # convert the *args list
            # we zip the args with the argument names we received from
            # the inspect function
            np_args = [
                numpy.array( value )
                    if key in args_to_convert and value is not None else value
                for key, value in zip( fn_args.args, args )
                ]

            # convert the **kwargs dict
            np_kwargs = dict(
                (key, (numpy.array( value )
                    if key in args_to_convert and value is not None else value
                    )
                )
                for key, value in kwargs.items()
                )

            # pass the converted values to our function
            return fn( *np_args, **np_kwargs )
        return wrapper
    return decorator
