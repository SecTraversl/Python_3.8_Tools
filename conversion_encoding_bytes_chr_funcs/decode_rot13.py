# %%
#######################################
def decode_rot13(string: str):
    """Decodes the string using ROT-13.

    Examples:
        >>> encode_rot13('hello')\n
        'uryyb'
        >>> decode_rot13('uryyb')\n
        'hello'
    """
    import codecs

    return codecs.decode(string, "rot13")

