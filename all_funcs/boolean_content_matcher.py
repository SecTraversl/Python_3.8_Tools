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

