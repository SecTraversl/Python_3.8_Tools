# %%
#######################################
def refind_bookends(left: str, right: str, obj: str or list, ignorecase=True):
    """Takes a given string or list of strings, along with a left and right delimiter, in order to return the substring that exists between the two delimiters.  The default search is case-insensitive, but this can be modified by specifying "ignorecase=False".

    Examples:
        >>> from my_py_funcs.regex_funcs import refind_bookends\n

        >>> newstuff = 'client 90.176.170.125#64983: query: www.coolhostname0010968.com IN,client 165.55.134.210#32688: query: www.coolhostname9594644.com IN,client 194.179.58.197#32424: query: www.coolhostname3977824.com IN'\n

        >>> client_ip = refind_bookends('client ', '#', newstuff)\n
        >>> client_ip\n
        ['90.176.170.125', '165.55.134.210', '194.179.58.197']

        >>> dns_query = refind_bookends('query: ', ' IN', newstuff, ignorecase=False)\n
        >>> dns_query\n
        ['www.coolhostname0010968.com', 'www.coolhostname9594644.com', 'www.coolhostname3977824.com']

    Args:
        left (str): Specify a left delimiter
        right (str): Specify a right delimiter
        obj (object): Reference a string or a list of strings
        ignorecase (bool, optional): Allows the string search to be case-sensitive or case-insensitive. Defaults to True.

    Returns:
        object: Returns the substring or list of substrings between the two delimiters
    """
    import re

    if ignorecase:
        match_syntax = re.compile(left + r"(.*?)" + right, re.IGNORECASE)
    else:
        match_syntax = re.compile(left + r"(.*?)" + right)

    if isinstance(obj, str):
        result = re.findall(match_syntax, obj)
    elif isinstance(obj, list):
        result = [refind_bookends(e) for e in obj]

    return result


bookends = refind_bookends

