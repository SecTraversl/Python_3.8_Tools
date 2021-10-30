# %%
#######################################
def get_modules_complete_list():
    """Returns a complete list of available modules.

    References:
        https://stackoverflow.com/questions/37752054/how-can-i-list-all-packages-modules-available-to-python-from-within-a-python-scr

    Returns:
        list: Returns a list of available module names
    """
    import sys
    from pydoc import ModuleScanner
    import warnings

    original_sys_path_tuple = tuple(sys.path)
    
    def scan_modules():
        """Scans for available modules using pydoc.ModuleScanner, taken from help('modules')"""
        modules = {}
        
        def callback(path, modname, desc, modules=modules):
            if modname and modname[-9:] == ".__init__":
                modname = modname[:-9] + " (package)"
            if modname.find(".") < 0:
                modules[modname] = 1
                
        def onerror(modname):
            callback(None, modname, None)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # ignore warnings from importing deprecated modules
            ModuleScanner().run(callback, onerror=onerror)
        return modules

    all_modules = sorted(scan_modules().keys())
    del sys.path
    sys.path = list(original_sys_path_tuple)
    return all_modules

