# %%
#######################################
def test_dirpath(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    path_exists = path_obj.exists()
    path_isdir = path_obj.is_dir()
    if path_exists and path_isdir:
        return True
    else:
        print(f"The path is a directory: {path_isdir}")
        print(f"The path exists: {path_exists}")

