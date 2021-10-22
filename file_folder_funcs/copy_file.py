# %%
#######################################
def copy_file(filepath: str or list, dest: str):
    """Copies a file.

    References:
        https://stackoverflow.com/questions/123198/how-can-a-file-be-copied
        https://www.geeksforgeeks.org/python-move-or-copy-files-and-directories/

    Args:
        filepath (str): Specify the path of the file you want to copy
        dest (str): Specify the destination or file copy name
    """
    import shutil
    import pathlib

    if isinstance(filepath, str):
        path_obj = pathlib.Path(filepath).resolve()
        dest_path = pathlib.Path(dest).resolve()
        shutil.copy2(str(path_obj), str(dest_path))
    elif isinstance(filepath, list):

        dest_path = pathlib.Path(dest).resolve()

        for eachitem in filepath:
            path_obj = pathlib.Path(eachitem).resolve()
            shutil.copy2(str(path_obj), str(dest_path))


cpfile = copy_file

