# %%
#######################################
def filehandle_append(thepath: str, content: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with open(path_obj, "a") as f:
        f.write(content)


appendtext = filehandle_append

