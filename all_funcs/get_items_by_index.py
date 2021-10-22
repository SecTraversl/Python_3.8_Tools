# %%
#######################################
def get_items_by_index(lst: list, *index_nums: int):
    """Returns the items from the list at the given index positions.

    Examples:
        >>> employees = {'Alice' : 100000,
        ...              'Bob' : 99817,
        ...              'Carol' : 122908,
        ...              'Frank' : 88123,
        ...              'Eve' : 93121}

        >>> mylst = list(employees.items())\n
        >>> get_items_by_index(mylst, 1,3,0)\n
        (('Bob', 99817), ('Frank', 88123), ('Alice', 100000))

        #######################################
        >>> import operator\n
        >>> operator.itemgetter(1,3,0)(list(employees.items()))\n
        (('Bob', 99817), ('Frank', 88123), ('Alice', 100000))
    """
    import operator

    return operator.itemgetter(*index_nums)(lst)

