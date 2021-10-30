# %%
#######################################
def get_modules_ready_for_import():
    """Returns a list of modules that are ready to be referenced with an 'import' statement.

    Example:
    >>> get_modules_for_import()\n
        ['workspace', 'workspace_find-replace-in-functions', 'workspace_general', 'workspace_import_all_funcs', '__future__', '_bootlocale', '_collections_abc', '_compat_pickle', '_compression', '_dummy_thread', '_markupbase', '_osx_support', '_py_abc', '_pydecimal', '_pyio', '_sitebuiltins', '_strptime', '_sysconfigdata__linux_x86_64-linux-gnu', '_sysconfigdata__x86_64-linux-gnu', '_threading_local', '_weakrefset', 'abc', 'aifc', 'antigravity', ... ]

    References:
        # Good discussion of what/isn't present in the pkgutil output
        https://stackoverflow.com/questions/37752054/how-can-i-list-all-packages-modules-available-to-python-from-within-a-python-scr\n
        # Additional reference for use of 'pkgtutil.iter_modules()' to get "all importable modules"
        https://stackoverflow.com/questions/8370206/how-to-get-a-list-of-built-in-modules-in-python\n

    Returns:
        list: Returns a list
    """
    import pkgutil
    modules_ready_for_import = [e.name for e in pkgutil.iter_modules()]
    return modules_ready_for_import

