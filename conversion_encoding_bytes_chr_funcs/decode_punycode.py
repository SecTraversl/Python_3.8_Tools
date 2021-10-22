# %%
#######################################
def decode_punycode(thebytes: bytes):
    """Decodes the bytes string using Punycode.

    Example:
        >>> encode_punycode('hello')\n
        b'hello-'

        >>> decode_punycode(b'hello-')\n
        'hello'
    """
    import codecs

    if isinstance(thebytes, bytes):
        temp_obj = thebytes

    return codecs.decode(temp_obj, "punycode")

