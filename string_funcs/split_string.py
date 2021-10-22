# %%
#######################################
def split_string(string: str, size: int):
    """Splits a string into smaller strings of the desired size value.

    Examples:
    >>> string = 'hey hey hiya'\n
    >>> split_string(string, 4)\n
    ['hey ', 'hey ', 'hiya']

    References:
        https://youtu.be/pG3L2Ojh1UE?t=336
    """
    created_step_points = range(0, len(string), size)
    sublists_created = [string[i : i + size] for i in created_step_points]
    return sublists_created

