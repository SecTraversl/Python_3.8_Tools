# %%
#######################################
def get_parent_path(thepath="."):
    """Returns the parent directory as an absolute path.

    Examples:
        >>> import os
        >>> os.getcwd()
        '/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/worksheet_dir'
        >>>
        >>> get_parent_path()
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs')
        >>>
        >>> get_parent_path('bogus file name')
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/worksheet_dir')
        >>>
        >>> get_parent_path('.')
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs')
        >>>
        >>> get_parent_path('_')
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/worksheet_dir')
        >>>
        >>> get_parent_path('/does/this/path/exist')
        PosixPath('/does/this/path')

    Args:
        thepath (str, optional): Specify the path. Defaults to ".".

    Returns:
        pathlib.Path: Returns a pathlib Path() object
    """
    import pathlib

    # return pathlib.Path(thepath).parent.absolute()
    return pathlib.Path(thepath).absolute().parent

