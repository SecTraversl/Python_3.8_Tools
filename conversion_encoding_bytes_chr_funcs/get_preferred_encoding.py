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

