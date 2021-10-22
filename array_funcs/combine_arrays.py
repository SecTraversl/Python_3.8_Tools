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

