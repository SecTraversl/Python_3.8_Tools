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

