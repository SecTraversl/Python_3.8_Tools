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

