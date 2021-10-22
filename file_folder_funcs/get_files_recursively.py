# %%
#######################################
def get_files_recursively(thepath=".", names=False, stringoutput=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if stringoutput:
        contents = sorted([str(obj) for obj in path_obj.rglob("*") if obj.is_file()])
    else:
        contents = sorted([obj for obj in path_obj.rglob("*") if obj.is_file()])
    return contents

