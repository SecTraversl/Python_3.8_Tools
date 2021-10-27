#######################################
# CONVERSION ENCODING BYTES CHR FUNCS #
#######################################

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

# %%
#######################################
def get_preferred_encoding():
    """Shows the preferred encoding of the local machine (often it is "UTF-8").

    Examples:
        >>> get_preferred_encoding()\n
        'UTF-8'

    References:
        https://realpython.com/python-encodings-guide/
    """
    import locale

    return locale.getpreferredencoding()

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

# %%
#######################################
def display_binary_4bit(num: int):
    """Displays the binary string representation for a given integer.  If the number is within 4 bits, the output will be 4 binary digits; if the number is 8 bits then 8 binary digits will be the output.

    Examples:
        >>> display_binary_4bit(151)\n
        '10010111'

        >>> display_binary_4bit(11)\n
        '1011'
    """
    return format(num, "04b")

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

# %%
#######################################
def decode_bz2(obj: object):
    """Decodes the string / bytes string using BZ2.

    Example:
        >>> encode_bz2('hello')\n
        b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80'

        >>> encode_bz2(b'hello')\n
        b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80'

        >>> decode_bz2(b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80')\n
        b'hello'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj
    return codecs.decode(temp_obj, "bz2")

# %%
#######################################
def display_chr_value(num: int):
    """Displays the glyph representation of a given integer.

    Examples:
        >>> display_chr_value(128013)
        '🐍'

        >>> display_chr_value(77)
        'M'

        display_chr_value(700)
        'ʼ'
    """
    return chr(num)

# %%
#######################################
def xor_strings(string: str, xor_string="zen"):
    """Returns an XOR'ed string given a string object.  By default the string object will be XOR'ed using a truncated version of the "Zen of Python".  You can change this default by specifying your own "xor_string" value.

    Examples:
        >>> mystring = "Complex is better than complicated."
        >>> xor_strings(mystring)\n
        '\x17\x07\x08P6\x00\x16\x00\x06\x15\x002\x1c\x00\x1c\n\x1c\x0cT\n\x18Nt\n\x02M \t\x1d\x06\x13\x07onl'
        >>> xor_strings(
        ...     "\x17\x07\x08P6\x00\x16\x00\x06\x15\x002\x1c\x00\x1c\n\x1c\x0cT\n\x18Nt\n\x02M \t\x1d\x06\x13\x07onl"
        ... )\n
        'Complex is better than complicated.'

        >>> xor_strings('here is some blah blah', 'and here is a super secret string we use for xor')\n
        '\t\x0b\x16EH\x0c\x01ES\x06\x1eEAB\x1f\x14\x18E\x10L\x12\r'
        >>> xor_strings(
        ...     '\t\x0b\x16EH\x0c\x01ES\x06\x1eEAB\x1f\x14\x18E\x10L\x12\r', 'and here is a super secret string we use for xor'
        ... )\n
        'here is some blah blah'

    Args:
        string (str): The string object you want to XOR
        xor_string (str, optional): The xor_string used to XOR against the given string object. Defaults to "zen".

    Returns:
        str: Returns an XOR'ed string.
    """
    import codecs

    # import this
    from this import s as this_s

    # We initialize an empty string variable which we will += each xor'ed character to for the final string
    result_string = ""

    # We want to know the length of the given string, so we can have an equivalent number of characters from the "Zen of Python"
    len_of_string = len(string)

    if xor_string == "zen":
        # this.s is the zen of python rot13 encoded, so here we are decoding it
        zen = codecs.decode(this_s, "rot13")

        # Then we take the zen of python, and truncate it to match the length of the string we want to XOR
        match_len_for_xor_enum = zen[:len_of_string]
        for index_num, val in enumerate(string):
            result_string += chr(ord(val) ^ ord(match_len_for_xor_enum[index_num]))
        return result_string
    else:
        if len(string) == len(xor_string):
            match_len_for_xor_enum = xor_string
        elif len(string) > len(xor_string):
            makebig = xor_string * len(string)
            match_len_for_xor_enum = makebig[: len(string)]
        elif len(string) < len(xor_string):
            match_len_for_xor_enum = xor_string[: len(string)]

        for index_num, val in enumerate(string):
            result_string += chr(ord(val) ^ ord(match_len_for_xor_enum[index_num]))
        return result_string

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

# %%
#######################################
def encode_base64(obj: object, no_newline=False):
    """Encodes the string / bytes string using BASE64.

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

    if no_newline:
        result = codecs.encode(temp_obj, "base64")
        result = result.decode().rstrip("\n")
        result = result.encode()
    else:
        result = codecs.encode(temp_obj, "base64")
    return result

# %%
#######################################
def get_size_in_bytes(string: str):
    """Takes a given string and return the number of bytes used for all of the glyphs in the string.

    Examples:
        >>> shrug = r'¯\_(ツ)_/¯'\n
        >>> get_size_in_bytes(shrug)\n
        13
        >>> shrug.encode()\n
        b'\xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf'
        >>> shrug.encode('utf-8')\n
        b'\xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf'
        >>> shrug.encode('utf8')\n
        b'\xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf'
        >>> shrug.encode('utf-16')\n
        b'\xff\xfe\xaf\x00\\\x00_\x00(\x00\xc40)\x00_\x00/\x00\xaf\x00'
        >>>
        >>> len(shrug.encode())\n
        13
    """
    return len(string.encode())

# %%
#######################################
def bitwise_compliment_comparison(num: int):
    """Prints a comparison table of the number, its complement (the num * -1), and the

    Args:
        num (int): [description]

    Returns:
        [type]: [description]
    """
    from pprint import pprint

    dict1 = {}
    dict1["num_orig"] = (num, format(num, "08b"))
    dict1["num_neg"] = (num * -1, format(num * -1, "08b"))
    dict1["bitcomp"] = (~num, format(~num, "08b"))
    pprint(list(dict1.items()))

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

# %%
#######################################
def encode_bz2(obj: object):
    """Encodes the string / bytes string using BZ2.

    Example:
        >>> encode_bz2('hello')\n
        b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80'

        >>> encode_bz2(b'hello')\n
        b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80'

        >>> decode_bz2(b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80')\n
        b'hello'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj

    result = codecs.encode(temp_obj, "bz2")
    return result

# %%
#######################################
def bit_shifter(num: int, shiftright: int):
    """Shifts the bits of the given number (int) by the designated number (int) given to the "shiftright" parameter.

    Examples:
        >>> bit_shifter(151, 4)\n
        9
        >>> bin(151)\n
        '0b10010111'
        >>> bin(151 >> 1)\n
        '0b1001011'
        >>> bin(151 >> 2)\n
        '0b100101'
        >>> bin(151 >> 3)\n
        '0b10010'
        >>> bin(151 >> 4)\n
        '0b1001'
        >>> int('0b1001', 2)\n
        9
        >>> format(151, '08b')\n
        '10010111'
        >>> format(151 >> 4, '04b')\n
        '1001'
        >>> int('1001', 2)\n
        9
    """
    return num >> shiftright

# %%
#######################################
def convert_bytes2string(thebytes: bytes):
    """Converts a "bytes" type object into a "str" type object

    Examples:
        >>> convert_bytes2string(b'nice string')\n
        'nice string'
    """
    return thebytes.decode()

# %%
#######################################
def display_binary_8bit(num: int):
    """Displays the binary string representation for a given integer.  If the number is within 4 bits, the output will be 8 binary digits (left padded with four 0s); if the number is 8 bits then 8 binary digits will be the output.

    Examples:
        >>> display_binary_8bit(151)\n
        '10010111'

        >>> bin(151)\n
        '0b10010111'

        >>> display_binary_8bit(11)\n
        '00001011'
    """
    return format(num, "08b")

# %%
#######################################
def get_emojis():
    """Retrieves hundreds of emoji glyphs derived from the UTF-8 character table.

    Examples:
        >>> moji = get_emojis()\n
        >>> moji[1540:1547]\n
        '🤠 🤡 🤢 🤣'
    """
    emoji_list_1 = [chr(i) for i in range(127744, 127994)]
    emoji_list_2 = [chr(e) for e in range(128000, 128501)]
    remove_list_for_list_3 = [
        129394,
        129399,
        129400,
        129401,
        129443,
        129444,
        129451,
        129452,
        129453,
        129483,
        129484,
    ]
    emoji_list_3 = [
        chr(e) for e in range(129293, 129536) if e not in remove_list_for_list_3
    ]

    agg_list = emoji_list_1 + emoji_list_2 + emoji_list_3
    one_space_sep_string = " ".join(agg_list)
    return one_space_sep_string

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

# %%
#######################################
def xor_string(string: str, xor_int_value=42):
    """Takes a given string and does an XOR operation on the converted ord() value of each character with the "xor_int_value", which by default is 42

    Examples:
        >>> string2encode = 'Now is better than never.'\n
        >>> xor_string(string2encode)\n
        'dE]\nCY\nHO^^OX\n^BKD\nDO\\OX\x04'

        >>> xor_string('dE]\nCY\nHO^^OX\n^BKD\nDO\\OX\x04')\n
        'Now is better than never.'

        >>> chr(97)\n
        'a'
        >>> ord('a')\n
        97
        >>> hex(97)\n
        '0x61'
        >>> int('0x61', 16)\n
        97
        >>> xor_string(string2encode, xor_int_value = 97)\n
        '/\x0e\x16A\x08\x12A\x03\x04\x15\x15\x04\x13A\x15\t\x00\x0fA\x0f\x04\x17\x04\x13O'
        >>>
        >>> xor_string('/\x0e\x16A\x08\x12A\x03\x04\x15\x15\x04\x13A\x15\t\x00\x0fA\x0f\x04\x17\x04\x13O', 97)\n
        'Now is better than never.'

    Args:
        string (str): The string you want to XOR (each character will be XORed by the xor_int_value)
        xor_int_value (int, optional): The integer value that is used for the XOR operation. Defaults to 42.

    Returns:
        str: Returns an XORed string
    """
    xored_result = "".join([chr(ord(c) ^ xor_int_value) for c in string])
    return xored_result

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

# %%
#######################################
def display_ordinal_value(glyph: str):
    """Displays the integer value of the given glyph

    Examples:
        >>> display_ordinal_value('🐍')\n
        128013

        >>> display_ordinal_value('G')\n
        71

        >>> display_ordinal_value('g')\n
        103
    """
    return ord(glyph)

# %%
#######################################
def convert_string2bytes(string: str):
    """Converts a "str" type object into a "bytes" type object

    Examples:
        >>> convert_string2bytes('nice string')\n
        b'nice string'
    """
    return string.encode()

