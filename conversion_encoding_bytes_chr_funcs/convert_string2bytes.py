# %%
#######################################
def convert_string2bytes(string: str):
    """Converts a "str" type object into a "bytes" type object

    Examples:
        >>> convert_string2bytes('nice string')\n
        b'nice string'
    """
    return string.encode()

