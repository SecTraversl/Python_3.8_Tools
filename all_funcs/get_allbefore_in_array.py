# %%
#######################################
def get_allbefore_in_array(lst: list, obj: object, include_value=False):
    """Returns a list of all elements before the given value (if that value is in the list).

    Example:
    >>> mylst = ['exit', 'quit', 're', 'sys', 'teststring']\n
    >>> get_allbefore_in_array(mylst, 're')\n
    ['exit', 'quit']
    >>> get_allbefore_in_array(mylst, 're', include_value=True)\n
    ['exit', 'quit', 're']
    """
    index = lst.index(obj)
    if include_value:
        newlst = list(lst[0 : index + 1])
    else:
        newlst = list(lst[0:index])
    return newlst

