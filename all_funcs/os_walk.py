# %%
# #######################################
def os_walk(thepath: str):
    """Performs an os.walk on the given path.

    Examples:
        >>> test = os_walk('../worksheet_dir')
        >>> pprint(test)\n
        [('../worksheet_dir',\n
        ['__pycache__'],\n
        ['worksheet_sets.py',
        'worksheet_match_str_len_with_padding.py',
        'worksheet_pathlib.py',
        'worksheet_name_eq_main_demo.py',
        'worksheet_xor_strings.py',
        'worksheet_where_like.py']),\n
        ('../worksheet_dir/__pycache__',\n
        [],\n
        ['worksheet_name_eq_main_demo.cpython-38.pyc'])]

        >>> test[-1]\n
        ('../worksheet_dir/__pycache__', [], ['worksheet_name_eq_main_demo.cpython-38.pyc'])

    Args:
        thepath (str): Reference the path

    Returns:
        list: Returns a list of tuples with 3 elements.  The 1st element is the directory itself, the 2nd element is a list of all subdirectories in that directory, and the 3rd element is a list of all of the files in the directory.
    """
    import os

    result = list(os.walk(thepath))
    return result

