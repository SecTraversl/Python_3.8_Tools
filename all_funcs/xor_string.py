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

