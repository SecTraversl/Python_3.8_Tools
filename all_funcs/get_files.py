# %%
#######################################
def get_files(thepath=".", names=False, stringoutput=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if stringoutput:
        contents = sorted([str(obj) for obj in path_obj.glob("*") if obj.is_file()])
    else:
        contents = sorted([obj for obj in path_obj.glob("*") if obj.is_file()])

    if names:
        contents = [str(e).split("/")[-1] for e in contents]

    return contents

