# %%
#######################################
def duplicate_randomly(thelist: list, maxduplication=3):
    """Takes a list of objects and will randomly duplicate the occurrence of each object in the list.  The maximum threshold of how many duplicates are created is limited by the 'maxduplication' parameter and defaults to 3.

    Args:
        thelist (list): Reference an existing list
        maxduplication (int, optional): Specify the max number of duplicates that will be created. Defaults to 3.

    Returns:
        list: Returns a list.
    """
    import random
    
    newlist = []
    for item in thelist:
        templist = []
        templist.append(item)
        multiplyby = random.randint(1, maxduplication)
        templist = templist * multiplyby
        newlist.extend(templist)
    return newlist

