# %%
#######################################
def filehandle_readbytes(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with open(path_obj, "rb") as f:
        content = f.read()

    return content


readbytes = filehandle_readbytes

