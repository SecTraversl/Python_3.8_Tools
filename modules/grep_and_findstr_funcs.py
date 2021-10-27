#######################################
####### GREP AND FINDSTR FUNCS ########
#######################################

# %%
#######################################
def findstr_files_containing_string(
    string: str, thedir=".", recurse=False, ignorecase=True
):
    """Searches the files under a given directory which contain a given string.  Equivalent of "grep searchstring directory_name -l" or "grep searchstring directory_name -rl"

    Examples:
        >>> from pprint import pprint\n
        >>> results = findstr_files_containing_string('website', '/home/student/Public/log', recurse=True)\n
        The bytes string 'b'website'' exists in the following files:\n
        >>> pprint(results)\n
        [PosixPath('/home/student/Public/log/dnslogs/17.log'),\n
        PosixPath('/home/student/Public/log/dnslogs/11.log'),\n
        PosixPath('/home/student/Public/log/dnslogs/13.log'),\n
        PosixPath('/home/student/Public/log/dnslogs/10.log'),\n
        PosixPath('/home/student/Public/log/dnslogs/14.log')]

    Args:
        string (str): Specify the string to search for
        thedir (str): Specify the starting directory. Default is the current directory.
        recurse (bool, optional): Specify this parameter to recurse through subdirectories. Defaults to False.

    Returns:
        list: Returns a list of files that contained the string.
    """
    import pathlib

    if isinstance(string, str):
        searchstring = string.encode()
    elif isinstance(string, bytes):
        searchstring = string

    path_obj = pathlib.Path(thedir).resolve()

    if recurse:
        theglob = path_obj.rglob("*")
    else:
        theglob = path_obj.glob("*")

    if ignorecase:
        results = [
            file
            for file in theglob
            if file.is_file() and searchstring.lower() in file.read_bytes().lower()
        ]
    else:
        results = [
            file
            for file in theglob
            if file.is_file() and searchstring in file.read_bytes()
        ]

    print(f"The bytes string '{searchstring}' exists in the following files: ")
    return results


grep_files_containing_string = findstr_files_containing_string

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

