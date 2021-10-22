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

