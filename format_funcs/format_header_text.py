# %%
#######################################
def format_header_text(string: str):
    """Returns a header string that is centered within a space of 39 characters, bordered by "#".

    Examples:
        >>> format_header_text('ARRAY FUNCTIONS')\n
        '########### ARRAY FUNCTIONS ###########'
    """
    return "{0:#^39}".format(f" {string} ")

