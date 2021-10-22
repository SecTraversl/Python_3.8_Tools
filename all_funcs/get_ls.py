# %%
#######################################
def get_ls(thepath=".", names=False, stringoutput=False, recurse=False):
    """Displays directory contents of a directory.

    Examples:
        >>> get_ls()\n
        [PosixPath('/home/pengin/worksheet_dir/__pycache__'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_match_str_len_with_padding.py'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_name_eq_main_demo.py'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_pathlib.py'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_sets.py'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_where_like.py'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_xor_strings.py')]

        >>> get_ls('.', stringoutput=True)\n
        ['/home/pengin/worksheet_dir/__pycache__',\n
        '/home/pengin/worksheet_dir/worksheet_match_str_len_with_padding.py',\n
        '/home/pengin/worksheet_dir/worksheet_name_eq_main_demo.py',\n
        '/home/pengin/worksheet_dir/worksheet_pathlib.py',\n
        '/home/pengin/worksheet_dir/worksheet_sets.py',\n
        '/home/pengin/worksheet_dir/worksheet_where_like.py',\n
        '/home/pengin/worksheet_dir/worksheet_xor_strings.py']

        >>> get_ls(names=True)\n
        ['__pycache__', 'worksheet_match_str_len_with_padding.py', 'worksheet_name_eq_main_demo.py', 'worksheet_pathlib.py', 'worksheet_sets.py', 'worksheet_where_like.py', 'worksheet_xor_strings.py']

    Args:
        thepath (str, optional): Specify the path. Defaults to ".".
        names (bool, optional): Use this to output the name only and not the full path. Defaults to False.
        stringoutput (bool, optional): Use this to output the file/folder objects as string objects. Defaults to False.


    Returns:
        list: Returns an array of the directory contents.
    """
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    if recurse:
        myglob = path_obj.rglob("*")
    else:
        myglob = path_obj.glob("*")

    if stringoutput:
        contents = sorted([str(obj) for obj in myglob])
    else:
        contents = sorted([obj for obj in myglob])

    if names:
        contents = [str(e).split("/")[-1] for e in contents]

    return contents

