# %%
#######################################
def get_functions_in_module_file(filename):
    """Takes a given module filename and returns the names of defined functions in the file.

    References:
        Excellent answer by "csl", which is the basis of this function
        https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module

    Args:
        filename (str): Reference the path of the file

    Returns:
        list: Returns a list of sorted function names
    """
    import ast
    import os
    import pathlib

    path_obj = pathlib.Path().home() / "Temp/pyplay/IMPORT_functions/my_py_funcs"
    os.chdir(path_obj)

    with open(filename, "rt") as file:
        ast_parse_result = ast.parse(file.read(), filename=filename)

    # This ast parse result itemizes when a function is defined as an "ast.FunctionDef"
    # and further itemizes each time there is an assignment with "ast.Assign"...
    # This differentiation allows me to remove from the output any function "alias" assignments
    func_def_only = [
        e.name for e in ast_parse_result.body if isinstance(e, ast.FunctionDef)
    ]
    result = sorted(func_def_only)

    return result

