# %%
#######################################
def encode_rot13(string: str):
    """Encodes the string using ROT-13.

    Example:
        >>> encode_rot13('hello')\n
        'uryyb'
        >>> decode_rot13('uryyb')\n
        'hello'
    """
    import codecs

    return codecs.encode(string, "rot13")

