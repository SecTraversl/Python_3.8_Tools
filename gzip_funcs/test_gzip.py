# %%
#######################################
def test_gzip(thepath: str or list, recurse=False):
    import pathlib

    results_array = []

    if isinstance(thepath, str):

        path_obj = pathlib.Path(thepath).resolve()

        if path_obj.is_file():
            path_obj.read_bytes()[:3]

        elif path_obj.is_dir():
            if recurse:
                [
                    results_array.append(
                        (
                            str(file),
                            {"is_gzip": file.read_bytes()[:3] == b"\x1f\x8b\x08"},
                            {"magic_bytes": file.read_bytes()[:3]},
                        )
                    )
                    for file in path_obj.rglob("*")
                    if file.is_file()
                ]
            else:
                [
                    results_array.append(
                        (
                            str(file),
                            {"is_gzip": file.read_bytes()[:3] == b"\x1f\x8b\x08"},
                            {"magic_bytes": file.read_bytes()[:3]},
                        )
                    )
                    for file in path_obj.glob("*")
                    if file.is_file()
                ]

        return results_array

    elif isinstance(thepath, list):
        array = thepath
        for item in array:
            path_obj = pathlib.Path(item).resolve()
            results_array.append(
                (
                    str(path_obj),
                    {"is_gzip": path_obj.read_bytes()[:3] == b"\x1f\x8b\x08"},
                    {"magic_bytes": path_obj.read_bytes()[:3]},
                )
            )

        return results_array

