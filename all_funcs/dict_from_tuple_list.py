# %%
#######################################
def dict_from_tuple_list(tuple_list: list):
    """Creates a dictionary from a list of 2-element tuples, where each tuple is in the format of (key, value).

    Examples:
        >>> tuple_list = [('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')]\n
        >>> dict_from_tuple_list(tuple_list)\n
        {'item1': 'I am a raptor', 'item2': 'eat everything', 'item3': 'Till the appearance of man'}
    """
    result = {k: v for k, v in tuple_list}
    return result

