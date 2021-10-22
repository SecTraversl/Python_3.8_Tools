# %%
#######################################
def test_filepath(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    path_exists = path_obj.exists()
    path_isfile = path_obj.is_file()
    if path_exists and path_isfile:
        return True
    else:
        print(f"The path is a file: {path_isfile}")
        print(f"The path exists: {path_exists}")

