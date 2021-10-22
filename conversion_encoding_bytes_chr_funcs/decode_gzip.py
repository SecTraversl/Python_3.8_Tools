# %%
#######################################
def decode_gzip(obj: object):
    """Decodes the string / bytes string using GZIP / zlib.

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
    return codecs.decode(temp_obj, "zlib")


decode_zip = decode_gzip

