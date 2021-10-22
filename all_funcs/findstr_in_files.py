# %%
#######################################
def findstr_in_files(string: str, thedir=".", recurse=False, ignorecase=True):
    import pathlib

    path_obj = pathlib.Path(thedir).resolve()

    if isinstance(string, str):
        searchstring = string.encode()
    elif isinstance(string, bytes):
        searchstring = string

    results = []

    if recurse:
        theglob = path_obj.rglob("*")
    else:
        theglob = path_obj.glob("*")

    for file in theglob:
        if file.is_file():
            line_match = []
            if ignorecase:
                [
                    line_match.append(line.decode())
                    for line in file.read_bytes().splitlines()
                    if searchstring.lower() in line.lower()
                ]
                if line_match:
                    results.append((file.name, line_match))
            else:
                [
                    line_match.append(line.decode())
                    for line in file.read_bytes().splitlines()
                    if searchstring in line
                ]
                if line_match:
                    results.append((file.name, line_match))

    return results


grep_in_files = findstr_in_files

