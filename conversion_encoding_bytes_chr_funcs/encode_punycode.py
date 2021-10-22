# %%
#######################################
def encode_punycode(string: str):
    """Encodes the string using Punycode.

    Example:
        >>> encode_punycode('hello')\n
        b'hello-'

        >>> decode_punycode(b'hello-')\n
        'hello'
    """
    import codecs

    if isinstance(string, str):
        temp_obj = string

    result = codecs.encode(temp_obj, "punycode")
    return result

