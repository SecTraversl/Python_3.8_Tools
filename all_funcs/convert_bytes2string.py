# %%
#######################################
def convert_bytes2string(thebytes: bytes):
    """Converts a "bytes" type object into a "str" type object

    Examples:
        >>> convert_bytes2string(b'nice string')\n
        'nice string'
    """
    return thebytes.decode()

