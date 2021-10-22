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

