#######################################
########### ARRAY FUNCTIONS ###########
#######################################
# %%
#######################################
def split_array(lst: list, size: int):
    """Splits a list into smaller arrays of the desired size value.

    Examples:
        >>> lst = [1,2,3,4,5,6,7,8,9,10]\n
        >>> split_array(lst, 3)\n
        [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

    References:
        https://youtu.be/pG3L2Ojh1UE?t=336
    """
    created_step_points = range(0, len(lst), size)
    sublists_created = [lst[i : i + size] for i in created_step_points]
    return sublists_created


split_interval = split_array
# %%
#######################################
def get_allbefore_in_array(lst: list, obj: object, include_value=False):
    """Returns a list of all elements before the given value (if that value is in the list).

    Example:
    >>> mylst = ['exit', 'quit', 're', 'sys', 'teststring']\n
    >>> get_allbefore_in_array(mylst, 're')\n
    ['exit', 'quit']
    >>> get_allbefore_in_array(mylst, 're', include_value=True)\n
    ['exit', 'quit', 're']
    """
    index = lst.index(obj)
    if include_value:
        newlst = list(lst[0 : index + 1])
    else:
        newlst = list(lst[0:index])
    return newlst


# %%
#######################################
def get_allafter_in_array(lst: list, obj: object, include_value=False):
    """Returns a list of all elements after the given value (if that value is in the list).

    Example:
    >>> mylst = ['exit', 'quit', 're', 'sys', 'teststring']\n
    >>> get_allafter_in_array(mylst, 're')\n
    ['sys', 'teststring']
    >>> get_allafter_in_array(mylst, 're', include_value=True)\n
    ['re', 'sys', 'teststring']
    """
    index = lst.index(obj)
    if include_value:
        newlst = list(lst[index::])
    else:
        newlst = list(lst[index + 1 : :])
    return newlst


# %%
#######################################
def get_unique_in_array(lst: list):
    """Returns a list of the unique values within the given list.

    Examples:
        >>> mylst = [1,1,2,2,3,2,3,4,5,6]\n
        >>> get_unique_in_array(mylst)\n
        [1, 2, 3, 4, 5, 6]
        >>>
    """
    return list(set(lst))


# %%
#######################################
def remove_falsey_values_in_array(lst: list):
    """Removes falsey values such as 0, '', False, None from the list.

    Examples:
        >>> list_with_falsey = [0, 1, False, 2, '', ' ', 3, 'a', 's', 34, None]\n

        >>> remove_falsey_values_in_array(list_with_falsey)\n
        [1, 2, ' ', 3, 'a', 's', 34]

        >>> filter(bool, list_with_falsey)\n
        <filter object at 0x7f8d02efbd90>

        >>> list( filter(bool, list_with_falsey) )\n
        [1, 2, ' ', 3, 'a', 's', 34]
    """
    return list(filter(bool, lst))


# %%
#######################################
def combine_arrays(*lsts: list):
    """Appends each given list to larger array, returning a list of lists for the final value

    Examples:
        >>> lst_abc = ['a','b','c']\n
        >>> lst_123 = [1,2,3]\n
        >>> lst_names = ['John','Alice','Bob']\n
        >>> combine_arrays(lst_abc,lst_123,lst_names)\n
        [['a', 'b', 'c'], [1, 2, 3], ['John', 'Alice', 'Bob']]
    """
    combined_list = []
    [combined_list.append(e) for e in lsts]
    return combined_list


# %%
#######################################
def merge_arrays(*lsts: list):
    """Merges all arrays into one flat list.

    Examples:
        >>> lst_abc = ['a','b','c']\n
        >>> lst_123 = [1,2,3]\n
        >>> lst_names = ['John','Alice','Bob']\n
        >>> merge_arrays(lst_abc,lst_123,lst_names)\n
        ['a', 'b', 'c', 1, 2, 3, 'John', 'Alice', 'Bob']
    """
    merged_list = []
    [merged_list.extend(e) for e in lsts]
    return merged_list


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


# %%
#######################################
def zip_arrays(lst: list, *lsts: list):
    """Takes two or more lists and zips them together, returning a list of tuples.

    Examples:
        >>> lst_abc = ['a','b','c']\n
        >>> lst_123 = [1,2,3]\n
        >>> lst_names = ['John','Alice','Bob']\n
        >>> zip_arrays(lst_abc, lst_123, lst_names)\n
        [('a', 1, 'John'), ('b', 2, 'Alice'), ('c', 3, 'Bob')]
    """
    return list(zip(lst, *lsts))


# %%
#######################################
def clear_array(lst: list):
    """Takes a given list and clears out all of the elements within the list.

    Examples:
        >>> mylst\n
        [('a', 1, 'John'), ('b', 2, 'Alice'), ('c', 3, 'Bob')]
        >>> clear_array(mylst)\n
        >>> mylst\n
        []
    """
    return lst.clear()


# %%
#######################################
def sum_array(lst: list):
    """Returns the sum of the numbers in the list.

    Example:
        >>> list(range(0,10))\n
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> myrange = list(range(0,10))\n
        >>> sum_array(myrange)\n
        45
        >>> sum(list(range(0,10)))\n
        45
    """
    return sum(lst)


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


# %%
#######################################
