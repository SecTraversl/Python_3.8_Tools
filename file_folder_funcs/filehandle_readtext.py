# %%
#######################################
def filehandle_readtext(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    with open(path_obj, "rt") as f:
        content = f.read()

    return content


readtext = filehandle_readtext

