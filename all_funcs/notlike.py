# %%
#######################################
def notlike(matchlist: list, array: list, andop=False):
    """Returns a list of non-matches in the given array by excluding each object that contains one of the values in the matchlist parameter.

    Examples:
        >>> subdir_list = ['get_random.py',
        ...  'day6_15_payload-by-port.py',
        ...  'worksheet_get_exif.py',
        ...  'worksheet_get_random.py',
        ...  'day6_19_browser-snob.py',
        ...  'day6_12_letterpassword.py',
        ...  'day6_21_exif-tag.py',
        ...  'day6_17_subprocess_ssh.py',
        ...  'day6_16._just_use_split.py']

        >>> notlike('day6',subdir_list)\n
        ['get_random.py', 'worksheet_get_exif.py', 'worksheet_get_random.py']
        >>>
        >>> notlike(['exif','_1'],subdir_list)\n
        ['get_random.py', 'worksheet_get_random.py']

    Args:
        matchlist (list): Submit one or many substrings to exclude
        array (list): This is the list that we want to filter
        andop (bool, optional): This will determine if the matchlist criteria is an "And Operation" or an "Or Operation. Defaults to False (which is the "Or Operation").  Only applies when multiple arguments are used for the "matchlist" parameter

    Returns:
        list: Returns a result list derived after the matchlist exclusions have been made

    References:
        https://stackoverflow.com/questions/469913/regular-expressions-is-there-an-and-operator
        https://stackoverflow.com/questions/3041320/regex-and-operator
        https://stackoverflow.com/questions/717644/regular-expression-that-doesnt-contain-certain-string
    """
    import re

    if isinstance(matchlist, str):
        # matchlist is a single string object
        thecompile = re.compile(rf"^(?!.*{matchlist}).*$")
        result_list = [x for x in array if re.findall(thecompile, x)]
        return result_list
    else:
        if andop:
            # We will be doing an "AND" match or an "And" "Operation"
            match_string = r"(?!.*?" + r".*?)(?!.*?".join(matchlist) + r".*?)"
            # e.g. for the above... ['6_19','6_21','6_24'] turns to: '(?!.*?6_19.*?)(?!.*?6_21.*?)(?!.*?6_24.*?)'
            thecompile = re.compile(rf"^{match_string}.*$")
            # equivalent to: '^(?!.*?6_19.*?)(?!.*?6_21.*?)(?!.*?6_24.*?).*$'
            result_list = [x for x in array if re.findall(thecompile, x)]
            return result_list
        else:
            # We will be doing an "OR" match
            match_string = r"(?!.*" + r"|.*".join(matchlist) + ")"
            # e.g. for the above... ['6_19','6_21','6_24'] turns to: '(?!.*6_19|.*6_21|.*6_24)'
            thecompile = re.compile(rf"^{match_string}.*$")
            # equivalent to: '^(?!.*6_19|.*6_21|.*6_24).*$'
            result_list = [x for x in array if re.findall(thecompile, x)]
            return result_list

