# %%
#######################################
def get_current_python_path():
    """Returns the full path of the python interpreter that is currently in use.

    Examples:
        >>> get_current_python_path()\n
        '/home/cooluser/playground/import_func_venv/bin/python'
    """
    import sys

    return sys.executable

