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

