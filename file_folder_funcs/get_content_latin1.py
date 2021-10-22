# %%
#######################################
def get_content_latin1(thepath: str):
    """Returns the file content by interpreting the encoding as "LATIN-1" instead of UTF-8.  LATIN-1 has exactly 255 possible characters with no gaps, so it is perfect for reading text and binary data without errors.

    Examples:
        >>> test = get_content_latin1('test_text.txt')\n
        >>> test.splitlines()\n
        ['ok', 'so here is some', "'blah blah'", 'We are planning', 'To use this ', 'in not only', 'normal testing...', 'but also for "gzip compressed ', 'text searching"', 'I know... sounds cool', "Let's see if it works!"]

        >>> binary_test = get_content_latin1('/bin/bash')\n
        >>> binary_test[:15]\n
        '\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'

    Args:
        thepath (str): Reference the file to read.

    Returns:
        str: Returns the content of the file as one long string
    """
    with open(thepath, encoding="latin-1") as f:
        content = f.read()
    return content


catlatin1 = get_content_latin1

