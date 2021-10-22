# %%
#######################################
# This is technically not a Rex Ex function, but it's in-theme with other functions here
def find_and_replace(findlist: str or list, replacelist: str or list, obj: str or list):
    """Takes a string or a list of strings and replaces substrings found in the findlist with those in the replacelist.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> text = "How about something simple"
        >>> find_and_replace("something", "everything", text)\n
        'How about everything simple'

        >>> ##### EXAMPLE 2 #####
        >>> moretext = ["How about something simple", "Or maybe something complex"]
        >>> moretext = ["How about something simple", "Or maybe something complex"]
        >>> find_and_replace("something", "everything", moretext)\n
        ['How about everything simple', 'Or maybe everything complex']

        >>> ##### EXAMPLE 3 #####
        >>> # First we are importing various functions that help us parse the data
        >>> from my_py_funcs.regex_funcs import (
        ...     refind_bookends,
        ...     replace_ipaddress_randomly,
        ...     replace_numbers_randomly,
        ... )

        >>> smallexample = "client 72.192.136.134#64983: query: www.coolhostname8864477.com IN,client 231.12.225.158#32688: query: www.coolhostname2927388.com IN,client 121.189.40.110#32424: query: www.coolhostname9651548.com IN"

        >>> # We create the "find list", which are the substrings we want to replace
        >>> find_list = refind_bookends("query: ", "IN", smallexample, ignorecase=False)
        >>> find_list\n
        ['www.coolhostname8864477.com ', 'www.coolhostname2927388.com ', 'www.coolhostname9651548.com ']

        >>> # Then we create the "replace list", which are the substrings we will use to replace those we found
        >>> replace_list = replace_numbers_randomly(find_list)
        >>> replace_list\n
        ['www.coolhostname0010968.com ', 'www.coolhostname9594644.com ', 'www.coolhostname3977824.com ']
        >>> newstuff = find_and_replace(find_list, replace_list, smallexample)
        >>> newstuff = replace_ipaddress_randomly(newstuff)
        >>> newstuff\n
        'client 90.176.170.125#64983: query: www.coolhostname0010968.com IN,client 165.55.134.210#32688: query: www.coolhostname9594644.com IN,client 194.179.58.197#32424: query: www.coolhostname3977824.com IN'


    Args:
        findlist (object): Reference a substring or list of substrings to find
        replacelist (object): Reference a substring or list of substrings to replace those that were found
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a new string or list of strings
    """

    if isinstance(findlist, str):
        if isinstance(obj, str):
            obj = obj.replace(findlist, replacelist)
            result = obj
        elif isinstance(obj, list):
            result = [find_and_replace(findlist, replacelist, e) for e in obj]

    elif isinstance(findlist, list):
        if isinstance(obj, str):
            for index, item in enumerate(findlist):
                obj = obj.replace(item, replacelist[index])
            result = obj
        elif isinstance(obj, list):
            result = [find_and_replace(findlist, replacelist, e) for e in obj]

    return result

