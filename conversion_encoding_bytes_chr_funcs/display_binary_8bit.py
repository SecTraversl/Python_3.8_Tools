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

