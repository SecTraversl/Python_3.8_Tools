# %%
#######################################
def rename_file(thepath: str, newname: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    target = pathlib.Path(newname)
    path_obj.rename(target)

