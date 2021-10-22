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

