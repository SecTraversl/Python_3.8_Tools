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

