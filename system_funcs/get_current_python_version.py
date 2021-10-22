# %%
#######################################
def get_current_python_version():
    """Returns the version of the python interpreter that is currently in use.

    Examples:
        >>> get_current_python_version()\n
        '3.8.5 (default, May 27 2021, 13:30:53) \\n[GCC 9.3.0]'
    """
    import sys

    return sys.version

