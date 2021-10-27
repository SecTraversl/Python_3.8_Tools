#######################################
########## OTHER MISC FUNCS ###########
#######################################

# %%
#######################################
def floor_division(dividend: int, divisor: int):
    """Describes and gives an example of how floor division and the "//" symbols are used in Python.

    Examples:
        >>> floor_division(15, 6)\n
        Floor division returns the nearest whole number as the quotient, rounding down when there is a remainder.\n
          dividend // divisor\n
          15 // 6\n

        2

    Args:
        dividend (int): Supply a dividend
        divisor (int): Supply a divisor

    Returns:
        int: Returns the quotient of the floor division operation
    """
    print(
        "Floor division returns the nearest whole number as the quotient, rounding down when there is a remainder."
    )
    print("  dividend // divisor ")
    print(f"  {dividend} // {divisor}")
    print("")
    return dividend // divisor

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

# %%
#######################################
def remove_duplicates(thelist: list):
    """Takes a list containing duplicates and returns a list of unique elements only.

    Example:
        >>> myduplicates\n
        ['Bartók', 'vigilant', 'vigilant', 'Julianne', 'Julianne', 'Julianne', 'camera', 'camera', 'camera', "Espinoza's", "Espinoza's", 'Amgen', 'Amgen', 'Amgen', "Tomlin's", 'tenuring', 'encroached', 'encroached', 'laxatives', 'laxatives', 'laxatives']

        >>> remove_duplicates(myduplicates)\n
        ['Bartók', 'vigilant', 'Julianne', 'camera', "Espinoza's", 'Amgen', "Tomlin's", 'tenuring', 'encroached', 'laxatives']

    Args:
        thelist (list): Reference an existing list.

    Returns:
        list: Returns a list of unique values.
    """
    temp_dict = {}
    for item in thelist:
        temp_dict[item] = "the value doesn't matter, we want the key"
    results_list = list(temp_dict.keys())  #  Any duplicate "item"/"key" was overwritten, so the new list contains unique elements only
    return results_list

# %%
#######################################
def dirplus(obj=None):
    """Behaves similar to the dir() function, but omits the "dunder" objects from the output.

    Examples:
    >>> blah = 'Here is some blah blah'

    >>> dirplus()\n
    ['dirplus', 'blah']

    >>> type(blah)\n
    <class 'str'>

    >>> dirplus(blah)\n
    ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

    References:
        # This was a valuable reference for information about namespaces, globals(), locals(), and such like:
        https://realpython.com/python-namespaces-scope/

    Args:
        obj (object, optional): Reference the desired object. Defaults to None.

    Returns:
        list: Returns a list of the pertinent "dir()" output
    """
    if obj:
        return [e for e in dir(obj) if not e.startswith("__")]
    else:
        return [e for e in globals().keys() if not e.startswith("__")]

# %%
#######################################
def deep_copy(obj_to_copy: object):
    """Returns a copy.deepcopy() of the given object.

    Example:
        >>> frag3_pcap = rdpcap('fragments3.pcap')
        >>> frag3_pcap\n
        <fragments3.pcap: TCP:15 UDP:0 ICMP:0 Other:114>
        >>> id(frag3_pcap)\n
        140567994637504

        >>> frag3_pcap_copy = deep_copy(frag3_pcap)
        >>> frag3_pcap_copy\n
        <fragments3.pcap: TCP:15 UDP:0 ICMP:0 Other:114>
        >>> id(frag3_pcap_copy)\n
        140568023743440

    Reference:
        https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy

    Args:
        obj_to_copy (object): Reference an existing object

    Returns:
        object: Returns a deepcopy of the given object
    """
    from copy import deepcopy
    return deepcopy(obj_to_copy)

# %%
#######################################
def oneliner_ifelse_demo():
    """This code demonstrates how to successfully implement a one-liner if/else statement

    Examples:
        >>> mystring = 'Complex is better than complicated.'\n
        >>> secondstring = ' blah '\n
        >>> bigger_string = mystring if mystring > secondstring else secondstring\n
        >>> bigger_string\n
        'Complex is better than complicated.'

    References:
        One liner if/else: https://youtu.be/MHlwl6GsT8s?t=990
    """
    demo_string = """
    >>> mystring = 'Complex is better than complicated.'
    >>> secondstring = ' blah '
    >>> bigger_string = mystring if mystring > secondstring else secondstring
    >>> bigger_string
    'Complex is better than complicated.'
    """
    print(demo_string)

# %%
#######################################
def test_object_type(obj: object, thetype: type):
    """Tests if the given object is of the specified type.  Returns a Boolean True or False.

    Examples:
        >>> myint = 34
        >>> test_object_type(myint, int)
        True
        >>> isinstance(myint, int)
        True
        >>> test_object_type(myint, str)
        False
    """
    return isinstance(obj, thetype)

# %%
#######################################
def invoke_lambda_demo(*args):
    """Demo of a stand-alone way of using lambda

    Examples:
        >>> invoke_lambda_demo(10, 25, 'blah')\n
        Here is what is happening:
        (lambda x: x + x)(item)

        [20, 50, 'blahblah']

    Returns:
        object: Returns double of the given argument.
    """
    print("Here is what is happening:")
    print("  (lambda x: x + x)(item)")
    print("")
    results = []
    for item in args:
        results.append((lambda x: x + x)(item))
    return results

# %%
#######################################
def get_unique(thelist: list):
    """Takes a list containing duplicates and returns a list of unique elements only.

    Example:
        >>> myduplicates\n
        ['Bartók', 'vigilant', 'vigilant', 'Julianne', 'Julianne', 'Julianne', 'camera', 'camera', 'camera', "Espinoza's", "Espinoza's", 'Amgen', 'Amgen', 'Amgen', "Tomlin's", 'tenuring', 'encroached', 'encroached', 'laxatives', 'laxatives', 'laxatives']

        >>> get_unique(myduplicates)\n
        ['Bartók', 'vigilant', 'Julianne', 'camera', "Espinoza's", 'Amgen', "Tomlin's", 'tenuring', 'encroached', 'laxatives']

    Args:
        thelist (list): Reference an existing list.

    Returns:
        list: Returns a list of unique values.
    """
    temp_dict = {}
    for item in thelist:
        temp_dict[item] = "the value doesn't matter, we want the key"
    results_list = list(temp_dict.keys())  #  Any duplicate "item"/"key" was overwritten, so the new list contains unique elements only
    return results_list

# %%
#######################################
def print_docstring(obj: object):
    """Prints the docstring for a given function

    Example:
        >>> print_docstring(len)
        Return the number of items in a container.

    References:

    """
    print(obj.__doc__)

# %%
#######################################
def boolean_content_matcher(string_array: str, substring: str):
    """Returns a list of tuples containing True/False if the substring is found in each element in the array.

    Examples:
        >>> text_list = ['lambda functions are anonymous functions.',
        ...        'anonymous functions dont have a name.',
        ...        'functions are objects in Python.']

        >>> boolean_content_matcher(text_list, 'anony')\n
        [(True, 'lambda functions are anonymous functions.'), (True, 'anonymous functions dont have a name.'), (False, 'functions are objects in Python.')]

    References:
        https://github.com/finxter/PythonOneLiners/blob/master/book/python_tricks/one_liner_04.py
    """
    result = list(
        map(lambda x: (True, x) if substring in x else (False, x), string_array)
    )
    return result

