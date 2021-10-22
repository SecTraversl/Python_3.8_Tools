# %%
#######################################
def get_dirs(thepath=".", names=False, stringoutput=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if stringoutput:
        contents = sorted([str(obj) for obj in path_obj.glob("*") if obj.is_dir()])
    else:
        contents = sorted([obj for obj in path_obj.glob("*") if obj.is_dir()])

    if names:
        contents = [str(e).split("/")[-1] for e in contents]

    return contents


# lsdirs = get_dirs

