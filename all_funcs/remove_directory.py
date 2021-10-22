# %%
#######################################
def remove_directory(thepath: str, force=False):
    """Removes a directory.  If the directory has contents, use force=True to recursively delete the children and delete the parent.

    Examples:
        >>> get_dirs(names=True)\n
        ['__pycache__', 'copy_test_dir', 'push_bitbucket_dir', 'test_copy_of_a_directory', 'worksheet_dir']

        >>> remove_directory('test_copy_of_a_directory', force=True)\n
        >>> get_dirs(names=True)\n
        ['__pycache__', 'copy_test_dir', 'push_bitbucket_dir', 'worksheet_dir']

    References:
        https://stackoverflow.com/questions/50186904/pathlib-recursively-remove-directory

    Args:
        thepath (str): Specify the path
        force (bool, optional): Allows for a recursive delete. Defaults to False.
    """
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    if force:
        for child in path_obj.rglob("*"):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                remove_directory(child, force=True)
        path_obj.rmdir()
    else:
        path_obj.rmdir()


rmdir = remove_directory

