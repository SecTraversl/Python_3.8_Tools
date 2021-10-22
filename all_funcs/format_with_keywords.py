# %%
#######################################
def format_with_keywords(**kwvars: str):
    """This is a demo exercise of using format() with key/value pairs in order to insert variables into the string.

    Examples:
        >>> mytuplelist = [('item1', 'Slot number 1'), ('item2', 'And the 2nd'), ('item3', 'Then the 3rd')]\n
        >>> mydict = {k:v for k,v in mytuplelist}\n
        >>> mydict\n
        {'item1': 'Slot number 1', 'item2': 'And the 2nd', 'item3': 'Then the 3rd'}

        >>> format_with_keywords(**mydict)\n
        {'item1': 'Slot number 1', 'item2': 'And the 2nd', 'item3': 'Then the 3rd'}\n
        'blah Slot number 1 blah And the 2nd blah Then the 3rd'
    """
    print({**kwvars})
    dict_of_vars = {**kwvars}
    return "blah {item1} blah {item2} blah {item3}".format(**dict_of_vars)

