# %%
#######################################
def remove_file(filepath: str or list):
    """Removes the specified file.

    References:
        https://stackoverflow.com/questions/42636018/python-difference-between-os-remove-and-os-unlink-and-which-one-to-use

    Args:
        filepath (str): Specify the path of the file
    """
    import pathlib

    if isinstance(filepath, str):
        path_obj = pathlib.Path(filepath).resolve()
        if path_obj.is_file():
            path_obj.unlink()
    elif isinstance(filepath, list):
        for eachitem in filepath:
            path_obj = pathlib.Path(eachitem).resolve()
            if path_obj.is_file():
                path_obj.unlink()


rm = remove_file

