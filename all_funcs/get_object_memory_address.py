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

