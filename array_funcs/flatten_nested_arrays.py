# %%
#######################################
def flatten_nested_arrays(lst: list):
    """Creates a single flat list out of a given list containing nested lists.

    Examples:
        >>> nested_list = [1, [2], [[3], 4], 5]\n
        >>> flatten_nested_arrays(nested_list)\n
        [1, 2, 3, 4, 5]
        >>> more_nesting = [1, [2], [[3,[7,8,9]], 4], 5]\n
        >>> flatten_nested_arrays(more_nesting)\n
        [1, 2, 3, 7, 8, 9, 4, 5]

    References:
        https://www.youtube.com/watch?v=pG3L2Ojh1UE
    """
    flattened_list = []
    for obj in lst:
        if isinstance(obj, list):
            flattened_list.extend(flatten_nested_arrays(obj))
        else:
            flattened_list.append(obj)
    return flattened_list

