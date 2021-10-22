# %%
#######################################
def decode_base64(obj: object):
    """Decodes the string / bytes string using BASE64.

    Example:
        >>> encode_base64('hello')\n
        b'aGVsbG8=\\n'
        >>> encode_base64('hello', no_newline=True)\n
        b'aGVsbG8='
        >>> encode_base64('hello', True)\n
        b'aGVsbG8='
        >>>
        >>> decode_base64(b'aGVsbG8=\\n')\n
        b'hello'
        >>> decode_base64(b'aGVsbG8=')\n
        b'hello'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj
    return codecs.decode(temp_obj, "base64")

