# %%
#######################################
def get_path(thepath="."):
    """Returns a pathlib object in the form of an absolute path.

    Examples:
        >>> get_path()\n
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/worksheet_dir')

        >>> get_path('no file by this name')\n
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/worksheet_dir/no file by this name')

        >>> get_path('/does/this/path/exist')\n
        PosixPath('/does/this/path/exist')

    Args:
        thepath (str, optional): Specify the path. Defaults to ".".

    Returns:
        pathlib.Path: Returns a pathlib Path() object
    """
    import pathlib

    return pathlib.Path(thepath).absolute()

