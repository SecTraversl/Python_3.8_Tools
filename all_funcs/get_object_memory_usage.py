# %%
#######################################
def get_object_memory_usage(obj: object):
    """Calculates the size of the object, stored in memory, in bytes.

    Examples:
        >>> myvar = 30\n
        >>> get_object_memory_usage(myvar)\n
        28
        >>> shrug = r'¯\_(ツ)_/¯'\n
        >>> get_object_memory_usage(shrug)\n
        92

    References:
        https://docs.python.org/3/library/sys.html#sys.getsizeof
    """
    import sys

    return sys.getsizeof(obj)

