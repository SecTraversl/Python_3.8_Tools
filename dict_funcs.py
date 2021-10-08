#######################################
######## DICTIONARY FUNCTIONS #########
#######################################

# %%
#######################################
def dict_creation_demo():
    print(
        "We can convert a list of tuples into Dictionary Items: dict( [('key1','val1'), ('key2', 'val2')] "
    )
    was_tuple = dict([("key1", "val1"), ("key2", "val2")])
    print(f"This was a list of Tuples: {was_tuple}\n")
    print(
        "We can convert a list of lists into Dictionary Items: dict( [['key1','val1'], ['key2', 'val2']] "
    )
    was_list = dict([["key1", "val1"], ["key2", "val2"]])
    print(f"This was a list of Lists: {was_list} ")


# %%
#######################################
def dict_merge(dict1: dict, dict2: dict):
    """Merges two dictionaries into one.

    Examples:
        >>> x = {'a': 1, 'b': 2}\n
        >>> y = {'b': 3, 'c': 4}\n
        >>> dict_merge(x, y)\n
        {'a': 1, 'b': 3, 'c': 4}

    References:
        https://www.youtube.com/watch?v=Duexw08KaC8
    """
    return {**dict1, **dict2}


# %%
#######################################
def sort_dict_by_value(dict1: dict, reverse=False):
    """For a given dictionary, returns a sorted list of tuples for each item based on the value.

    Examples:
        >>> employees = {'Alice' : 100000,
        ...              'Bob' : 99817,
        ...              'Carol' : 122908,
        ...              'Frank' : 88123,
        ...              'Eve' : 93121}

        >>> sort_dict_by_value(employees)\n
        [('Frank', 88123), ('Eve', 93121), ('Bob', 99817), ('Alice', 100000), ('Carol', 122908)]

        >>> sort_dict_by_value(employees, reverse=True)\n
        [('Carol', 122908), ('Alice', 100000), ('Bob', 99817), ('Eve', 93121), ('Frank', 88123)]

    References:
        https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value?page=1&tab=votes#tab-top
    """
    if reverse:
        return sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    else:
        return sorted(dict1.items(), key=lambda x: x[1])


# %%
#######################################
def sort_dict_by_value_itemgetter(dict1: dict, reverse=False):
    """For a given dictionary, returns a sorted list of tuples for each item based on the value.

    Examples:
        >>> employees = {'Alice' : 100000, 'Bob' : 99817, 'Carol' : 122908, 'Frank' : 88123, 'Eve' : 93121}\n
        >>> sort_dict_by_value_itemgetter(employees)\n
        [('Frank', 88123), ('Eve', 93121), ('Bob', 99817), ('Alice', 100000), ('Carol', 122908)]

        >>> sort_dict_by_value_itemgetter(employees, reverse=True)\n
        [('Carol', 122908), ('Alice', 100000), ('Bob', 99817), ('Eve', 93121), ('Frank', 88123)]

    References:
        https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value?page=1&tab=votes#tab-top
        https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work
    """
    import operator

    if reverse:
        return sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)
    else:
        return sorted(dict1.items(), key=operator.itemgetter(1))


# %%
#######################################
def sort_dict_by_key(dict1: dict, reverse=False):
    """For a given dictionary, returns a sorted list of tuples for each item based on the value.

    Examples:
        >>> employees = {'Alice' : 100000,
        ...              'Bob' : 99817,
        ...              'Carol' : 122908,
        ...              'Frank' : 88123,
        ...              'Eve' : 93121}

        >>> sort_dict_by_key(employees)\n
        [('Alice', 100000), ('Bob', 99817), ('Carol', 122908), ('Eve', 93121), ('Frank', 88123)]
        >>>
        >>> sort_dict_by_key(employees, reverse=True)\n
        [('Frank', 88123), ('Eve', 93121), ('Carol', 122908), ('Bob', 99817), ('Alice', 100000)]
    """
    if reverse:
        return sorted(dict1.items(), reverse=True)
    else:
        return sorted(dict1.items())


# %%
#######################################
def access_nested_dict(thedict: dict):
    """Demo of how to access a nested dictionary with a two dictionary comprehensions

    Examples:
        >>> a_dictionary = {
        ...     "1-2017": {
        ...         "Win7": "0.47",
        ...         "Vista": "0.2",
        ...         "NT*": "0.09",
        ...         "WinXP": "0.06",
        ...         "Linux": "0.17",
        ...         "Mac": "0.04",
        ...         "Mobile": "0.26",
        ...     },
        ...     "2-2017": {
        ...         "Win7": "0.48",
        ...         "Vista": "0.28",
        ...         "NT*": "0.07",
        ...         "WinXP": "0.09",
        ...         "Linux": "0.16",
        ...         "Mac": "0.03",
        ...         "Mobile": "0.27",
        ...     },
        ...     "3-2017": {
        ...         "Win7": "0.41",
        ...         "Vista": "0.25",
        ...         "NT*": "0.05",
        ...         "WinXP": "0.05",
        ...         "Linux": "0.1",
        ...         "Mac": "0.04",
        ...         "Mobile": "0.27",
        ...     },
        ... }

        >>> access_nested_dict(a_dictionary)\n
        {'1-2017': {('NT*', '0.09'), ('Vista', '0.2'), ('WinXP', '0.06')},
        '2-2017': {('NT*', '0.07'), ('Vista', '0.28'), ('WinXP', '0.09')},
        '3-2017': {('NT*', '0.05'), ('Vista', '0.25'), ('WinXP', '0.05')}}

    References:
        https://stackoverflow.com/questions/17915117/nested-dictionary-comprehension-python
    """
    comprehension = {
        outer_k: {
            (inner_k, inner_v)
            for inner_k, inner_v in outer_v.items()
            if inner_k in ["Vista", "NT*", "WinXP"]
        }
        for outer_k, outer_v in thedict.items()
    }
    return comprehension


# %%
#######################################
def dict_from_tuple_list(tuple_list: list):
    """Creates a dictionary from a list of 2-element tuples, where each tuple is in the format of (key, value).

    Examples:
        >>> tuple_list = [('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')]\n
        >>> dict_from_tuple_list(tuple_list)\n
        {'item1': 'I am a raptor', 'item2': 'eat everything', 'item3': 'Till the appearance of man'}
    """
    result = {k: v for k, v in tuple_list}
    return result


# %%
#######################################
def dict_from_two_lists(keys: list, values: list):
    """Creates a dictionary from a list of keys and a list of values.

    Examples:
        >>> keys = ('bztar', 'gztar', 'tar', 'xztar', 'zip')\n
        >>> values = ('.tbz2', '.tgz', '.tar', '.txz', '.zip')\n
        >>> newdict = dict_from_two_lists(keys, values)\n
        >>> pprint(newdict)\n
        {'bztar': '.tbz2',
        'gztar': '.tgz',
        'tar': '.tar',
        'xztar': '.txz',
        'zip': '.zip'}

    Args:
        keys (list): Reference the keys list
        values (list): Reference the values list

    Returns:
        dict: Returns a dictionary
    """
    result = {k: v for k, v in zip(keys, values)}
    return result


# %%

# %%

# %%
#######################################
