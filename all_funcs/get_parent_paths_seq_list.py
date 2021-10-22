# %%
#######################################
def get_parent_paths_seq_list(thepath="."):
    """Returns a list containing the absolute path of each parent.

    Examples:
        >>> get_parent_paths_seq_list()\n
        [PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs'),\n
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions'),\n
        PosixPath('/home/pengwin/Temp/pyplay'),\n
        PosixPath('/home/pengwin/Temp'),\n
        PosixPath('/home/pengwin'),\n
        PosixPath('/home'),\n
        PosixPath('/')]

    Args:
        thepath (str, optional): Specify the path you want to work with. Defaults to '.'.

    Returns:
        list: Returns a list of results
    """
    import pathlib

    return [p for p in pathlib.Path(thepath).absolute().parents]

