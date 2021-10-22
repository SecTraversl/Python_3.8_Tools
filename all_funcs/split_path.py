# %%
#######################################
def split_path(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    parts = path_obj.parts
    return parts

