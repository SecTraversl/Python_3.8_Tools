# %%
#######################################
def get_allafter_in_array(lst: list, obj: object, include_value=False):
    """Returns a list of all elements after the given value (if that value is in the list).

    Example:
    >>> mylst = ['exit', 'quit', 're', 'sys', 'teststring']\n
    >>> get_allafter_in_array(mylst, 're')\n
    ['sys', 'teststring']
    >>> get_allafter_in_array(mylst, 're', include_value=True)\n
    ['re', 'sys', 'teststring']
    """
    index = lst.index(obj)
    if include_value:
        newlst = list(lst[index::])
    else:
        newlst = list(lst[index + 1 : :])
    return newlst

