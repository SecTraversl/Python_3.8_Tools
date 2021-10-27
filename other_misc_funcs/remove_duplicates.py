# %%
#######################################
def remove_duplicates(thelist: list):
    """Takes a list containing duplicates and returns a list of unique elements only.

    Example:
        >>> myduplicates\n
        ['Bartók', 'vigilant', 'vigilant', 'Julianne', 'Julianne', 'Julianne', 'camera', 'camera', 'camera', "Espinoza's", "Espinoza's", 'Amgen', 'Amgen', 'Amgen', "Tomlin's", 'tenuring', 'encroached', 'encroached', 'laxatives', 'laxatives', 'laxatives']

        >>> remove_duplicates(myduplicates)\n
        ['Bartók', 'vigilant', 'Julianne', 'camera', "Espinoza's", 'Amgen', "Tomlin's", 'tenuring', 'encroached', 'laxatives']

    Args:
        thelist (list): Reference an existing list.

    Returns:
        list: Returns a list of unique values.
    """
    temp_dict = {}
    for item in thelist:
        temp_dict[item] = "the value doesn't matter, we want the key"
    results_list = list(temp_dict.keys())  #  Any duplicate "item"/"key" was overwritten, so the new list contains unique elements only
    return results_list

