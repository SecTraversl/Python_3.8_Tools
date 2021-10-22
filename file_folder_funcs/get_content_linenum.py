# %%
#######################################
def get_content_linenum(thepath: str, linenum: int):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    # The open() function can take a str object or a Path() object as an argument
    with open(path_obj) as f:
        lines = f.readlines()
    return lines[linenum - 1]

