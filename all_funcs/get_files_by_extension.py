# %%
#######################################
def get_files_by_extension(thepath=".", extension="*", stringoutput=False):
    """Returns a list of the files ending in the given extension

    Examples:
        >>> get_files_by_extension(extension='txt')\n
        [PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/test_text.txt')]

        >>> get_files_by_extension(extension='txt', stringoutput=True)\n
        ['/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/test_text.txt']

    Args:
        thepath (str, optional): Specify the path. Defaults to ".".
        extension (str, optional): Specify the extension. Defaults to '*'.
        stringoutput (bool, optional): Switch to allow for the output to be a str object. Defaults to False.

    Returns:
        list: Returns an array of files matching the criteria
    """
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if extension != "*":
        myglob = path_obj.glob(f"*{extension}")
    else:
        myglob = path_obj.glob("*")

    if stringoutput:
        results = sorted([str(file) for file in myglob if file.is_file()])
    else:
        results = sorted([file for file in myglob if file.is_file()])

    return results

