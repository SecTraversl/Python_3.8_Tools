# %%
#######################################
def os_ls(thepath="."):
    """Displays the content of the given directory.  Default value is the current directory.

    Examples:
        >>> os_ls()\n
        ['temp.py', 'worksheet.py']

        >>> os_ls('../..')\n
        ['ps1_files', 'sec_ops', 'pyplay', 'bashplay']
    """
    import os

    return os.listdir(thepath)

