# %%
#######################################
def get_magic_bytes(thepath: str or list, recurse=False, byte_num=4):
    import pathlib

    results_array = []

    if isinstance(thepath, str):

        path_obj = pathlib.Path(thepath).resolve()

        if path_obj.is_file():
            path_obj.read_bytes()[:byte_num]

        elif path_obj.is_dir():
            if recurse:
                [
                    results_array.append((str(file), file.read_bytes()[:byte_num]))
                    for file in path_obj.rglob("*")
                    if file.is_file()
                ]
            else:
                [
                    results_array.append((str(file), file.read_bytes()[:byte_num]))
                    for file in path_obj.glob("*")
                    if file.is_file()
                ]

        return results_array

    elif isinstance(thepath, list):
        array = thepath
        for item in array:
            path_obj = pathlib.Path(item).resolve()
            results_array.append((str(path_obj), path_obj.read_bytes()[:byte_num]))

        return results_array

