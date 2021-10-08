#######################################
########## SYSTEM FUNCTIONS ###########
#######################################
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


# %%
#######################################
def get_object_memory_address(obj: object, return_hex=False):
    """Returns the memory address of the given object.

    Examples:
        >>> mylst = [1,1,2,2,3,2,3,4,5,6]\n
        >>> get_object_memory_address(mylst)\n
        140192405518336
        >>> get_object_memory_address(mylst, return_hex=True)\n
        '0x7f811687f800'
    """
    if return_hex:
        return hex(id(obj))
    else:
        return id(obj)


# %%
#######################################
def get_current_python_path():
    """Returns the full path of the python interpreter that is currently in use.

    Examples:
        >>> get_current_python_path()\n
        '/home/cooluser/playground/import_func_venv/bin/python'
    """
    import sys

    return sys.executable


# %%
#######################################
def get_current_python_version():
    """Returns the version of the python interpreter that is currently in use.

    Examples:
        >>> get_current_python_version()\n
        '3.8.5 (default, May 27 2021, 13:30:53) \\n[GCC 9.3.0]'
    """
    import sys

    return sys.version


# %%
#######################################
