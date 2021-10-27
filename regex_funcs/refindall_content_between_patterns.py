# %%
#######################################
def refindall_content_between_patterns(obj: str or list, left_pattern: str, right_pattern: str, ignorecase=True):
    """Takes a given string or a list of strings, along with a left_pattern and right_pattern, and returns the substring that exists between the two patterns.
    
    The default search is case-insensitive, but this can be modified by specifying "ignorecase=False".

    Examples:
        >>> thestring = 'client 90.176.170.125#64983: query: www.coolhostname0010968.com IN,client 165.55.134.210#32688: query: www.coolhostname9594644.com IN,client 194.179.58.197#32424: query: www.coolhostname3977824.com IN'\n

        >>> client_ip = refindall_content_between_patterns(thestring, 'client ', '#')\n
        >>> client_ip\n
        ['90.176.170.125', '165.55.134.210', '194.179.58.197']

        >>> dns_query = refindall_content_between_patterns(thestring, 'query: ', ' IN', ignorecase=False)\n
        >>> dns_query\n
        ['www.coolhostname0010968.com', 'www.coolhostname9594644.com', 'www.coolhostname3977824.com']

    Args:
        left_pattern (str): Specify the pattern on the left
        right_pattern (str): Specify a right_pattern delimiter
        obj (object): Reference a string or a list of strings
        ignorecase (bool, optional): Allows the string search to be case-sensitive or case-insensitive. Defaults to True.

    Returns:
        object: Returns the substring or list of substrings between the two delimiters
    """
    import re

    if ignorecase:
        match_syntax = re.compile(left_pattern + r"(.*?)" + right_pattern, re.IGNORECASE)
    else:
        match_syntax = re.compile(left_pattern + r"(.*?)" + right_pattern)

    if isinstance(obj, str):
        result = re.findall(match_syntax, obj)
    elif isinstance(obj, list):
        result = [refindall_content_between_patterns(e) for e in obj]

    return result

