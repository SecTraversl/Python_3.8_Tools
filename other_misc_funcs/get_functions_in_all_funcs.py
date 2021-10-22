# %%
#######################################
def get_functions_in_all_funcs():
    import pathlib
    import os
    import re

    path_obj = pathlib.Path().home() / "Temp/pyplay/IMPORT_functions/Python_3.8_Tools"
    os.chdir(path_obj)

    from regex_funcs import like
    from file_folder_funcs import get_content

    cat = get_content
    myfile = cat("all_funcs.py").splitlines()
    sorted_funcs = sorted(like("^def ", myfile))

    results_array = []
    [results_array.extend(re.findall(r"def (\w+)", e)) for e in sorted_funcs]
    return results_array

