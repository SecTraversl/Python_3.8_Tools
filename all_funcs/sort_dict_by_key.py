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

