# %%
#######################################
def get_file_stats(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    file_stats = path_obj.stat()
    return file_stats

