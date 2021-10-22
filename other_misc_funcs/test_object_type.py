# %%
#######################################
def test_object_type(obj: object, thetype: type):
    """Tests if the given object is of the specified type.  Returns a Boolean True or False.

    Examples:
        >>> myint = 34
        >>> test_object_type(myint, int)
        True
        >>> isinstance(myint, int)
        True
        >>> test_object_type(myint, str)
        False
    """
    return isinstance(obj, thetype)

