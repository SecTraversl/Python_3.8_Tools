# %%
#######################################
def refindall(thepattern: str, obj: str or list, context=(0, (0, 0))[0], ignorecase=True):
    """Given the object (such as a string or an array of strings), this function will search for thepattern in the object. If context is set, this function will return the number of characters before and after the match as specified by the "context" number.

    Examples:
        >>> text = '''
        ... We spent several years building our own database engine,
        ... Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
        ... service with the same or better durability and availability as
        ... the commercial engines, but at one-tenth of the cost. We were
        ... not surprised when this worked.
        ... '''

        >>> # Find exact matches:
        >>> refindall('sql', text)\n
        ['SQL', 'SQL']

        >>> # Find 25 characters before and after the match
        >>> refindall('sql', text, 25)\n
        ['urora, a fully-managed MySQL and PostgreSQL-compatibl']

        >>> # Do a "Greedy" match - this grabs the whole line where the match occurs
        >>> refindall('.*sql.*', text)\n
        ['Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible']

        >>> # Do a "Non-Greedy" match - this creates a separate element for each match on this single line
        >>> refindall('.*?sql.*?', text)\n
        ['Amazon Aurora, a fully-managed MySQL', ' and PostgreSQL']

        >>> # Here we take our example text and create an array of strings
        >>> text.splitlines()\n
        ['', 'We spent several years building our own database engine,', 'Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible', 'service with the same or better durability and availability as', 'the commercial engines, but at one-tenth of the cost. We were', 'not surprised when this worked.']

        >>> # Now each element in the array is evaluated with the match criteria, in this case we are getting the 5 characters before and after the match
        >>> refindall('the', text.splitlines(), 5)\n
        ['with the same', 'h of the cost']

        >>> # Here we are grabbing the whole element where the match occurs in the array
        >>> refindall('.*the.*', text.splitlines())\n
        ['service with the same or better durability and availability as', 'the commercial engines, but at one-tenth of the cost. We were']

    References:
        https://github.com/finxter/PythonOneLiners/blob/master/book/python_tricks/one_liner_05.py
    """
    import re

    if isinstance(context, int):
        left_context = str(context)
        right_context = str(context)
    elif isinstance(context, tuple):
        left, right = context
        left_context = str(left)
        right_context = str(right)

    if ignorecase:
        match_syntax = re.compile(
            r"(.{" + left_context + r"}" + thepattern + r".{" + right_context + r"})",
            re.IGNORECASE,
        )
    else:
        match_syntax = re.compile(
            r"(.{" + left_context + r"}" + thepattern + r".{" + right_context + r"})"
        )

    if isinstance(obj, str):
        result = re.findall(match_syntax, obj)
    elif isinstance(obj, list):
        result = [refindall(e) for e in obj]

    return result

