# %%
#######################################
def os_cwd():
    """Returns the pathlib object for the current working directory

    Examples:
        >>> os_cwd()\n
        '/home/cooluser/pyplay'
    """
    import os

    return os.getcwd()

