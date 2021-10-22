# %%
#######################################
def get_file_symlink(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    symlink_resolved = path_obj.readlink()
    return symlink_resolved

