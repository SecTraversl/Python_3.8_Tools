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

