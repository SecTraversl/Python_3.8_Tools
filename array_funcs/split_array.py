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

