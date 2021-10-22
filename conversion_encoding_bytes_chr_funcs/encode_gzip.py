# %%
#######################################
def encode_gzip(obj: object):
    """Encodes the string / bytes string using GZIP / zlib.

    Example:
        >>> encode_gzip('hello')\n
        b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15'

        >>> encode_gzip(b'hello')\n
        b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15'

        >>> decode_gzip(b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15')\n
        b'hello'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj

    result = codecs.encode(temp_obj, "zlib")
    return result


encode_zip = encode_gzip

