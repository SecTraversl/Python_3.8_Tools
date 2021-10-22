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

