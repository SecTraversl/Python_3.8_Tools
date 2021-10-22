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

