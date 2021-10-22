# %%
#######################################
def encode_hex(obj: object):
    """Encodes the string / bytes string using Hexadecimal.

    Example:
        >>> encode_hex('hello')\n
        b'68656c6c6f'

        >>> encode_hex(b'hello')\n
        b'68656c6c6f'

        >>> decode_hex(b'68656c6c6f')\n
        b'hello'

        >>> decode_hex('68656c6c6f')\n
        b'hello'

        >>> [hex(ord(s)) for s in 'hello']\n
        ['0x68', '0x65', '0x6c', '0x6c', '0x6f']

        >>> ''.join([hex(ord(s)) for s in 'hello'])\n
        '0x680x650x6c0x6c0x6f'

        >>> ''.join([hex(ord(s)) for s in 'hello']).replace('0x','')\n
        '68656c6c6f'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj

    result = codecs.encode(temp_obj, "hex")
    return result

