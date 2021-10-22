# %%
#######################################
def copy_directory(thepath: str, dest: str):
    """Copies a directory.

    References:
        https://stackoverflow.com/questions/123198/how-can-a-file-be-copied
        https://www.geeksforgeeks.org/python-move-or-copy-files-and-directories/

    Args:
        thepath (str): Specify the path of the directory you want to copy
        dest (str): Specify the destination or directory copy name
    """
    import shutil
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    copy_path = pathlib.Path(dest).resolve()
    shutil.copytree(str(path_obj), str(copy_path))


cpdir = copy_directory

