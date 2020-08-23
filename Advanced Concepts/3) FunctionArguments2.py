"""
**kwargs (standing for keyword arguments) allows you to handle named arguments
that you have not defined in advance.
The keyword arguments return a dictionary in which the keys
are the argument names, and the values are the argument values.
"""


def my_func(x, *args, **kwargs):
    print(args)
    print(kwargs)


my_func(2, 3, 4, 5, 6, a=7, b=8, c=9)