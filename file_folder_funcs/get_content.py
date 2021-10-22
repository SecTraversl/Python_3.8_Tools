# %%
#######################################
def get_content(thepath: str, as_bytes=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if as_bytes:
        contents = path_obj.read_bytes()
    else:
        contents = path_obj.read_text()
    return contents


cat = get_content

