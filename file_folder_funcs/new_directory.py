# %%
#######################################
def new_directory(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    path_obj.mkdir()


mkdir = new_directory

