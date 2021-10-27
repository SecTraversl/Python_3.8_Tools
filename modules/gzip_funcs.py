#######################################
############# GZIP FUNCS ##############
#######################################

# %%
#######################################
def test_gzip(thepath: str or list, recurse=False):
    import pathlib

    results_array = []

    if isinstance(thepath, str):

        path_obj = pathlib.Path(thepath).resolve()

        if path_obj.is_file():
            path_obj.read_bytes()[:3]

        elif path_obj.is_dir():
            if recurse:
                [
                    results_array.append(
                        (
                            str(file),
                            {"is_gzip": file.read_bytes()[:3] == b"\x1f\x8b\x08"},
                            {"magic_bytes": file.read_bytes()[:3]},
                        )
                    )
                    for file in path_obj.rglob("*")
                    if file.is_file()
                ]
            else:
                [
                    results_array.append(
                        (
                            str(file),
                            {"is_gzip": file.read_bytes()[:3] == b"\x1f\x8b\x08"},
                            {"magic_bytes": file.read_bytes()[:3]},
                        )
                    )
                    for file in path_obj.glob("*")
                    if file.is_file()
                ]

        return results_array

    elif isinstance(thepath, list):
        array = thepath
        for item in array:
            path_obj = pathlib.Path(item).resolve()
            results_array.append(
                (
                    str(path_obj),
                    {"is_gzip": path_obj.read_bytes()[:3] == b"\x1f\x8b\x08"},
                    {"magic_bytes": path_obj.read_bytes()[:3]},
                )
            )

        return results_array

# %%
#######################################
def gzip_file(thepath: str, gzip_name=None):
    """Create a compressed version of a given file.

    References:
        This was where I got the basic code for this function
        https://stackoverflow.com/questions/8156707/gzip-a-file-in-python

    Args:
        thepath (str): Reference the file to gzip compress
        gzip_name (str, optional): Use this if you want to the name of the compressed file to be something other than "filename.gz". Defaults to None.
    """
    import gzip

    if gzip_name:
        pass
    else:
        gzip_name = f"{thepath}.gz"

    with open(thepath, "rb") as f_in, gzip.open(gzip_name, "wb") as f_out:
        f_out.writelines(f_in)

# %%
#######################################
def ungzip_file(thepath: str, out_filename=None):
    import gzip

    if out_filename:
        pass
    else:
        out_filename = thepath.replace(".gz", "")

    with gzip.open(thepath, "rt") as f_in, open(out_filename, "w") as f_out:
        f_out.writelines(f_in)

# %%
#######################################
def get_content_gzip(thepath: str):
    """Displays the content of a gzip compressed file.

        Examples:
    >>> zcat = get_content_gzip\n
    >>> test = zcat('test_text.txt.gz')>>> test\n
    'ok\\nso here is some\\n\'blah blah\'\\nWe are planning\\nTo use this \\nin not only\\nnormal testing...\\nbut also for "gzip compressed \\ntext searching"\\nI know... sounds cool\\nLet\'s see if it works!\\n'
    >>> test.splitlines()
    ['ok', 'so here is some', "'blah blah'", 'We are planning', 'To use this ', 'in not only', 'normal testing...', 'but also for "gzip compressed ', 'text searching"', 'I know... sounds cool', "Let's see if it works!"]

        Args:
            thepath (str): Specify the path of the file.

        Returns:
            bytes: Returns a bytes string
    """
    import gzip

    # Here we are specifying that we want to "Read Text" with 'rt' instead of the default read for gzip.open() which is 'rb' or 'Read Bytes'
    with gzip.open(thepath, "rt") as f:
        return f.read()


zcat = get_content_gzip

# %%
#######################################
def get_content_linenum_gzip(thepath: str, linenum: int):
    """Returns the line number of the specified gzipped file.

    Examples:
        >>> get_content_linenum_gzip('test_text.txt.gz', 3)\n
        "'blah blah'\\n"

    Args:
        thepath (str): Reference the file
        linenum (int): Specify the line number

    Returns:
        str: Returns the line number in the specified gzipped file
    """
    import pathlib
    import gzip

    path_obj = pathlib.Path(thepath).resolve()

    # The open() function can take a str object or a Path() object as an argument
    with gzip.open(path_obj, "rt") as f:
        lines = f.readlines()
    return lines[linenum - 1]

