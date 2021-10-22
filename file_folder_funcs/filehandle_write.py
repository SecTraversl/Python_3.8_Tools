# %%
#######################################
def filehandle_write(thepath: str, content: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with open(path_obj, "w") as f:
        f.write(content)


writetext = filehandle_write

