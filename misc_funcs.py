#######################################
########### MISC FUNCTIONS ############
#######################################
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
def get_functions_in_imported_module(module_name, mymodule=True):
    """Returns objects in a module where "isfunction()" is True.

    References:
        One way to do it, which is the code we settled on for this function
        https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module

        This was another way to do it, which I commented out below for reference
        https://www.tutorialspoint.com/How-to-list-all-functions-in-a-Python-module

        Some other approaches
        https://stackoverflow.com/questions/6315496/display-a-list-of-user-defined-functions-in-the-python-idle-session

    Args:
        module_name (obj): Reference the module to inspect

    Returns:
        list: Returns an array of tuples where the 2nd element "isfunction"
    """
    from inspect import getmembers, isfunction

    # - This returned the whole tuple which shows the memory id() location for each function as well -
    # funcs = [e for e in getmembers(module_name) if isfunction(e[1])]

    funcs = [e[0] for e in getmembers(module_name, isfunction)]

    if mymodule:
        # my functions when initially defined normally have an '_' in the name
        # however the 'aliases' I create for the functions do not have an '_'
        # So this bit of code filters out all functions without an '_'
        myfuncs = [e for e in funcs if "_" in e]
        return myfuncs
    else:
        return funcs


# %%
#######################################
def get_functions_in_all_funcs():
    import pathlib
    import os
    import re

    path_obj = pathlib.Path().home() / "Temp/pyplay/IMPORT_functions/my_py_funcs"
    os.chdir(path_obj)

    from regex_funcs import where_like
    from file_folder_funcs import get_content

    cat = get_content
    myfile = cat("all_funcs.py").splitlines()
    sorted_funcs = sorted(where_like("^def ", myfile))

    results_array = []
    [results_array.extend(re.findall(r"def (\w+)", e)) for e in sorted_funcs]
    return results_array


# %%
#######################################
def get_functions_in_module_file(filename):
    """Takes a given module filename and returns the names of defined functions in the file.

    References:
        Excellent answer by "csl", which is the basis of this function
        https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module

    Args:
        filename (str): Reference the path of the file

    Returns:
        list: Returns a list of sorted function names
    """
    import ast
    import os
    import pathlib

    path_obj = pathlib.Path().home() / "Temp/pyplay/IMPORT_functions/my_py_funcs"
    os.chdir(path_obj)

    with open(filename, "rt") as file:
        ast_parse_result = ast.parse(file.read(), filename=filename)

    # This ast parse result itemizes when a function is defined as an "ast.FunctionDef"
    # and further itemizes each time there is an assignment with "ast.Assign"...
    # This differentiation allows me to remove from the output any function "alias" assignments
    func_def_only = [
        e.name for e in ast_parse_result.body if isinstance(e, ast.FunctionDef)
    ]
    result = sorted(func_def_only)

    return result


# %%
#######################################
def get_random(array=None):
    """The 'get_random' function returns a random list of integers of a random length for the list.

    Examples:
        >>> get_random()\n
        [29, 5, 22, 100, 74, 15, 7, 50, 52, 18, 26, 54, 37, 21, 42, 46, 39, 62, 5, 41, 67, 25, 26, 72, 89, 19]
        >>> get_random()\n
        [28, 87, 92, 87, 18, 24, 49, 90, 9, 37, 75, 43, 36, 92, 82]

        >>> list1\n
        ['353', '1618285621506', '182711621994', '1984', '688', '4991999', '185235691716215851336', '14363109411127', '14113473', '278']

        >>> get_random(list1)\n
        '185235691716215851336'

    References:
        https://www.geeksforgeeks.org/python-select-random-value-from-a-list/

    Returns:
        list: Returns a randomly sized list of random integers.
    """
    import random

    if array:
        # If an array was submitted to the function, get a random value from it
        return random.choice(array)
    else:
        # Here we  create a list of up to 30 elements in size
        size_of_list = random.choice(range(1, 30))
        # The elements will be integers ranging from 1 to 100
        lst = list(range(1, 101))
        # From the "lst" of numbers 1 - 100, there will be multiple random choices, the quantity of which is based off of the number given to "k="
        random_list_of_ints = random.choices(lst, k=size_of_list)
        return random_list_of_ints


# %%
#######################################
def new_random_number(size=None):
    """Creates a large random number string. You can specify the size of the number using the "size" parameter.

    Examples:
        >>> new_random_number()\n
        '88495077433033604864459347219444521153467941653074517'

        >>> new_random_number()\n
        '50687589765828927139866314225259581387781147585513699'

        >>> new_random_number()\n
        '3933481384'

        >>> new_random_number(size=333)\n
        '9714188696247383654871292573098225426647253076733397769390728697759149793081512588524364279370278384692180475130825330801079463843655342153603449199025254084984353138753538945813523746920322710962748572347098357639231982180325558624756995274493507086476515545437136794779622702572568526438176415058625571928676953194838042337245543725816954176121011728783177495855283625899367553099288845402459285860401135256887874543963892694098154533594068558877234595744195741767995977316325571867838167880357384194314525465248320818965444224623264936226428813528010558221318554454332511926659310098247750742688442346813527103355913470354848965473812'

        >>> new_random_number(size=123)\n
        '91214915252828538635886489742232177541769241334437959742634202621180775793449210509188183499799551465326960258663248621524515522562839393141151318716015189324901944462067354183367892964644774711423589068814314271621465396719985816232'

        >>> new_random_number(42)\n
        '577556851583248222148853278534675679332074959294122553484454275175328584499871890'

        >>> new_random_number(7)\n
        '18339518883949'


        Args:
            size (int, optional): Specify a desired number size. Defaults to None.

        Returns:
            str: Returns a long number string
    """
    import random

    if size:
        size_of_list = int(size)
    else:
        # Here we  create a list of up to 30 elements in size
        size_of_list = random.choice(range(1, 30))

    # The elements will be integers ranging from 1 to 100
    lst = list(range(1, 101))
    # From the "lst" of numbers 1 - 100, there will be multiple random choices, the quantity of which is based off of the number given to "k="
    random_list_of_ints = random.choices(lst, k=size_of_list)
    # Then we take that list of random numbers and join them together making one long string of digits
    big_random_number_string = "".join([str(e) for e in random_list_of_ints])
    return big_random_number_string


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
