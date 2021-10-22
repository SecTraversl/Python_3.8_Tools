# %%
#######################################
def format_with_braces(*vars: str):
    """This is a demo exercise of using format() with positional {} in order to insert variables into the string.

    Examples:
        >>> format_with_braces('hi','there','fella')\n
        hi there fella\n
        ['hi', 'there', 'fella']\n
        'blah hi blah there blah fella'

        >>> format_with_braces('hi')\n
        hi\n
        ['hi']\n
        'blah hi blah default2 blah default3'

        >>> format_with_braces('hi','there','fella','David')\n
        hi there fella David\n
        ['hi', 'there', 'fella', 'David']\n
        'blah hi blah there blah fella'
    """
    print(*vars)
    list_of_vars = [*vars]
    print([*vars])
    if len(list_of_vars) < 3:
        while len(list_of_vars) < 3:
            number = len(list_of_vars)
            list_of_vars.append("default" + str(number + 1))
    return "blah {} blah {} blah {}".format(*list_of_vars)

