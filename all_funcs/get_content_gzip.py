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

