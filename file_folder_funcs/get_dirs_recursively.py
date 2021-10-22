# %%
#######################################
def get_dirs_recursively(thepath=".", stringoutput=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if stringoutput:
        contents = sorted([str(obj) for obj in path_obj.rglob("*") if obj.is_dir()])
    else:
        contents = sorted([obj for obj in path_obj.rglob("*") if obj.is_dir()])
    return contents

