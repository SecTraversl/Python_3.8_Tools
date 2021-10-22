# %%
#######################################
def dirplus(obj=None):
    """Behaves similar to the dir() function, but omits the "dunder" objects from the output.

    Examples:
    >>> blah = 'Here is some blah blah'

    >>> dirplus()\n
    ['dirplus', 'blah']

    >>> type(blah)\n
    <class 'str'>

    >>> dirplus(blah)\n
    ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

    References:
        # This was a valuable reference for information about namespaces, globals(), locals(), and such like:
        https://realpython.com/python-namespaces-scope/

    Args:
        obj (object, optional): Reference the desired object. Defaults to None.

    Returns:
        list: Returns a list of the pertinent "dir()" output
    """
    if obj:
        return [e for e in dir(obj) if not e.startswith("__")]
    else:
        return [e for e in globals().keys() if not e.startswith("__")]

