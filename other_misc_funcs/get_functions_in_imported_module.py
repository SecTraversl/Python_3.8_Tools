# %%
#######################################
def get_functions_in_imported_module(module_name, mymodule=True):
    """Returns objects in a module where "isfunction()" is True.

    References:
        One way to do it, which is the code we settled on for this function
        https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module

        This was another way to do it, which I commented out below for reference
        https://www.tutorialspoint.com/How-to-list-all-functions-in-a-Python-module

        Some other approaches
        https://stackoverflow.com/questions/6315496/display-a-list-of-user-defined-functions-in-the-python-idle-session

    Args:
        module_name (obj): Reference the module to inspect

    Returns:
        list: Returns an array of tuples where the 2nd element "isfunction"
    """
    from inspect import getmembers, isfunction

    # - This returned the whole tuple which shows the memory id() location for each function as well -
    # funcs = [e for e in getmembers(module_name) if isfunction(e[1])]

    funcs = [e[0] for e in getmembers(module_name, isfunction)]

    if mymodule:
        # my functions when initially defined normally have an '_' in the name
        # however the 'aliases' I create for the functions do not have an '_'
        # So this bit of code filters out all functions without an '_'
        myfuncs = [e for e in funcs if "_" in e]
        return myfuncs
    else:
        return funcs

