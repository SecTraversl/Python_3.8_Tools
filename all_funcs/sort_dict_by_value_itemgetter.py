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

