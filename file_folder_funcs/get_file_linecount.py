# %%
#######################################
def get_file_linecount(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with path_obj.open(thepath) as f:
        lines = f.readlines()
    return len(lines)

