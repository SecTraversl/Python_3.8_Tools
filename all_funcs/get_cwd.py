# %%
#######################################
def get_cwd(stringoutput=False):
    """Returns the pathlib object for the current working directory

    Examples:
        >>> get_cwd()\n
        '/home/cooluser/pyplay'

    References:
        https://realpython.com/python-pathlib/
    """
    import pathlib

    result = pathlib.Path.cwd().as_posix()
    return result


pwd = get_cwd

