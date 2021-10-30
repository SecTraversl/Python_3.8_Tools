# %%
#######################################
def invoke_module_reload(module_name: str):
    """For a given module_name reloads the respective module by that name.

    Reference:
        https://stackoverflow.com/questions/7271082/how-to-reload-a-modules-function-in-python

    Args:
        module_name (str): Reference the name of the module you want to reload.
    """
    import sys
    import importlib
    importlib.reload(sys.modules[module_name])

