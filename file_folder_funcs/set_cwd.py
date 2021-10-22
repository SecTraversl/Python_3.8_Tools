# %%
#######################################
def set_cwd(thepath: str):
    """Change the current directory you are in.

    References:
        https://stackoverflow.com/questions/41742317/how-can-i-change-directory-with-python-pathlib

    Args:
        thepath (str): Specify the path
    """
    import os

    os.chdir(thepath)


cd = set_cwd

