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

