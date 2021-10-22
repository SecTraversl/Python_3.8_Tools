# %%
#######################################
def get_help_as_text(function_name: object):
    """Outputs the "help" docstring for the given function as text.

    Examples:
        >>> get_help_as_text(len)\n
        'Help on built-in function len in module builtins:\\n\\nlen(obj, /)\\n    Return the number of items in a container.\\n\\n'
        >>> print( get_help_as_text(len) )\n
        Help on built-in function len in module builtins:

        len(obj, /)
            Return the number of items in a container.

    References:
        https://stackoverflow.com/questions/11265603/how-do-i-export-the-output-of-pythons-built-in-help-function

        https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout
    """
    import contextlib
    import io

    with contextlib.redirect_stdout(io.StringIO()) as f:
        help(function_name)
    return f.getvalue()

