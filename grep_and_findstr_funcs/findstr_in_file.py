# %%
#######################################
def findstr_in_file(string: str, thefile: str, ignorecase=True):
    import pathlib

    path_obj = pathlib.Path(thefile).resolve()

    if isinstance(string, str):
        searchstring = string.encode()
    elif isinstance(string, bytes):
        searchstring = string

    results = []

    if path_obj.is_file():
        line_match = []
        if ignorecase:
            [
                line_match.append(line.decode())
                for line in path_obj.read_bytes().splitlines()
                if searchstring.lower() in line.lower()
            ]
            if line_match:
                # results.append((path_obj.name, line_match))
                results.extend(line_match)

        else:
            [
                line_match.append(line.decode())
                for line in path_obj.read_bytes().splitlines()
                if searchstring in line
            ]
            if line_match:
                # results.append((path_obj.name, line_match))
                results.extend(line_match)

    return results


grep_in_file = findstr_in_file

