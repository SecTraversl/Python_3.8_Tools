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

