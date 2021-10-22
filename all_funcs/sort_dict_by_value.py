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

