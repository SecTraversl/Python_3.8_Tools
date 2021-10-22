# %%
#######################################
def dict_to_tuple_list(thedict: dict):
    """Takes a Dictionary and converts the .items() into a list of tuples.

    Examples:
    >>> my_dict = {'item1': 'I am a raptor', 'item2': 'eat everything', 'item3': 'Till the appearance of man'}
    >>> my_dict.items()\n
    dict_items([('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')])
    >>> dict_to_tuple_list(my_dict)\n
    [('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')]
    >>> # This has the same effect #
    >>> list(my_dict.items())\n
    [('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')]

    Args:
        thedict (dict): Reference the dictionary

    Returns:
        list: Returns a list of tuples from the .items() method
    """
    my_tuple_list = [(k, v) for k, v in thedict.items()]
    # same as: # list(thedict.items())
    return my_tuple_list

