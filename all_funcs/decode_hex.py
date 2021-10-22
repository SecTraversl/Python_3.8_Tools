# %%
#######################################
def decode_hex(obj: object):
    """Decodes the string / bytes string using Hexadecimal.

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

        #######################################
        >>> data = ['6e', '75', '64', '67', '65', '20', '6e', '75', '64', '67', '65', '20', '77', '69', '6e', '6b', '20', '77', '69', '6e', '6b']\n
        >>> [decode_hex(hexa) for hexa in data]\n

        [b'n', b'u', b'd', b'g', b'e', b' ', b'n', b'u', b'd', b'g', b'e', b' ', b'w', b'i', b'n', b'k', b' ', b'w', b'i', b'n', b'k']

        >>> [decode_hex(hexa).decode() for hexa in data]\n
        ['n', 'u', 'd', 'g', 'e', ' ', 'n', 'u', 'd', 'g', 'e', ' ', 'w', 'i', 'n', 'k', ' ', 'w', 'i', 'n', 'k']

        >>> ''.join([decode_hex(hexa).decode() for hexa in data])\n
        'nudge nudge wink wink'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj
    return codecs.decode(temp_obj, "hex")

