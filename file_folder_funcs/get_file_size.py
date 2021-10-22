# %%
#######################################
def get_file_size(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    file_byte_size = path_obj.stat().st_size
    return file_byte_size

