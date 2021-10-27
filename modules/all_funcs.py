#######################################
############## ALL FUNCS ##############
#######################################

# NOTE: Excludes scapy functions.  To import scapy functions, use 'from scapy_funcs import *'

# %%
#######################################
def new_directory(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    path_obj.mkdir()


mkdir = new_directory

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

# %%
#######################################
def get_items_by_index(lst: list, *index_nums: int):
    """Returns the items from the list at the given index positions.

    Examples:
        >>> employees = {'Alice' : 100000,
        ...              'Bob' : 99817,
        ...              'Carol' : 122908,
        ...              'Frank' : 88123,
        ...              'Eve' : 93121}

        >>> mylst = list(employees.items())\n
        >>> get_items_by_index(mylst, 1,3,0)\n
        (('Bob', 99817), ('Frank', 88123), ('Alice', 100000))

        #######################################
        >>> import operator\n
        >>> operator.itemgetter(1,3,0)(list(employees.items()))\n
        (('Bob', 99817), ('Frank', 88123), ('Alice', 100000))
    """
    import operator

    return operator.itemgetter(*index_nums)(lst)

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

# %%
#######################################
def split_array(lst: list, size: int):
    """Splits a list into smaller arrays of the desired size value.

    Examples:
        >>> lst = [1,2,3,4,5,6,7,8,9,10]\n
        >>> split_array(lst, 3)\n
        [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

    References:
        https://youtu.be/pG3L2Ojh1UE?t=336
    """
    created_step_points = range(0, len(lst), size)
    sublists_created = [lst[i : i + size] for i in created_step_points]
    return sublists_created


split_interval = split_array

# %%
#######################################
def get_content_linenum(thepath: str, linenum: int):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    # The open() function can take a str object or a Path() object as an argument
    with open(path_obj) as f:
        lines = f.readlines()
    return lines[linenum - 1]

# %%
#######################################
def floor_division(dividend: int, divisor: int):
    """Describes and gives an example of how floor division and the "//" symbols are used in Python.

    Examples:
        >>> floor_division(15, 6)\n
        Floor division returns the nearest whole number as the quotient, rounding down when there is a remainder.\n
          dividend // divisor\n
          15 // 6\n

        2

    Args:
        dividend (int): Supply a dividend
        divisor (int): Supply a divisor

    Returns:
        int: Returns the quotient of the floor division operation
    """
    print(
        "Floor division returns the nearest whole number as the quotient, rounding down when there is a remainder."
    )
    print("  dividend // divisor ")
    print(f"  {dividend} // {divisor}")
    print("")
    return dividend // divisor

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
def get_allafter_in_array(lst: list, obj: object, include_value=False):
    """Returns a list of all elements after the given value (if that value is in the list).

    Example:
    >>> mylst = ['exit', 'quit', 're', 'sys', 'teststring']\n
    >>> get_allafter_in_array(mylst, 're')\n
    ['sys', 'teststring']
    >>> get_allafter_in_array(mylst, 're', include_value=True)\n
    ['re', 'sys', 'teststring']
    """
    index = lst.index(obj)
    if include_value:
        newlst = list(lst[index::])
    else:
        newlst = list(lst[index + 1 : :])
    return newlst

# %%
#######################################
def new_module_header(source_dir_name: str):
    
    def format_header_block(string: str):
        """Prints a header for use with my function files

        Examples:
            #######################################\n
            ########### ARRAY FUNCTIONS ###########\n
            #######################################\n


        """
        newstring = ""
        newstring += "{0:#<39}".format("") + "\n"
        newstring += "{0:#^39}".format(f" {string} ") + "\n"
        newstring += "{0:#<39}".format("") + "\n\n"
        
        return newstring
    
    header_name = source_dir_name.replace('_', ' ').upper()
    new_header = format_header_block(header_name)
    return new_header

# %%
#######################################
def get_dirs(thepath=".", names=False, stringoutput=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if stringoutput:
        contents = sorted([str(obj) for obj in path_obj.glob("*") if obj.is_dir()])
    else:
        contents = sorted([obj for obj in path_obj.glob("*") if obj.is_dir()])

    if names:
        contents = [str(e).split("/")[-1] for e in contents]

    return contents


# lsdirs = get_dirs

# %%
#######################################
# %%
def replace_letters_randomly(obj: str or list, seed=None):
    """Takes a given string or list of strings, finds each substring of consecutive letters, and randomly replaces substring with randomized letters.

    Examples:
        >>> mylist = ['blah','blahblah','blahblahblah']\n
        >>> replace_letters_randomly(mylist)\n
        ['GHXH', 'jfEVOQQJ', 'iAJAZkoXiqgt']

        >>> mytext = "Please excuse my dear aunt sally"\n
        >>> replace_letters_randomly(mytext)\n
        'zPxYZN WcaXbR Pm ZBwT wCMq HXXvy'

        >>> replace_letters_randomly("My test text", seed=42)\n
        'AQ FhAQ FhAQ'
        >>> replace_letters_randomly("My test text", seed=42)\n
        'AQ FhAQ FhAQ'
        >>> replace_letters_randomly("My test text")\n
        'qK wQsI xCBD'
        >>> replace_letters_randomly("My test text", seed='my secret key')\n
        'Sc wVSc wVSc'
        >>> replace_letters_randomly("My test text", seed='my secret key')\n
        'Sc wVSc wVSc'
        >>> replace_letters_randomly("My test text")\n
        'Ee WHkG turs'

    Args:
        obj (object): Reference a string or list of strings

    Returns:
        object: Returns a modified string or list of strings
    """
    import re
    import random
    from string import ascii_letters

    lowercase = ascii_letters[: len(ascii_letters) // 2]
    uppercase = ascii_letters[len(ascii_letters) // 2 :]

    temp_list = []
    for index, item in enumerate(lowercase):
        temp_list.extend([item, uppercase[index]])

    letters = "".join(temp_list)
    # 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'

    if isinstance(obj, str):
        try:
            # We match on each consecutive string of digits
            match_list = re.findall(r"[A-Za-z]+", obj)

            replacement_list = []
            for eachitem in match_list:

                if seed:
                    if isinstance(seed, int):
                        random.seed(seed)
                    elif isinstance(seed, str):
                        # concat_ordinal = ''.join([str(ord(e)) for e in 'where was you at'])
                        concat_ordinal = "".join([str(ord(e)) for e in seed])
                        int_seed = int(concat_ordinal)
                        random.seed(int_seed)

                ### FIRST, WE CREATE A BIG STRING OF RANDOM LETTERS ###
                # Each character in the string of characters found in the "letters" variable, will be randomly retrieved, making a list of random letters the quantity of which (the size of the list) is based off of the number given to "k="
                random_list_of_letters = random.choices(letters, k=420)

                # Then we take that list of random letters and join them together making one long string of random letters
                rand_letter_string = "".join(random_list_of_letters)

                ### THEN, WE USE THAT RANDOM STRING OF LETTERS IN OUR SUBSTITUTION ###
                # We then take the length of the match and use that integer value as the ending point of our slice into the rand_letter_string
                # Finally that slice is reversed and then it is used for the substitution, and then added to the replacement_list
                replacement_list.append(
                    re.sub(
                        r"[A-Za-z]+",
                        lambda x: rand_letter_string[: len(x.group(0))][::-1],
                        eachitem,
                    )
                )

            # We create a list of 2 element tuples - the 1st element is the match, the 2nd is the replacement
            find_and_replace_list = [
                (e[1], replacement_list[e[0]]) for e in enumerate(match_list)
            ]

            # Then we iterate over the find/replace list and replace the first occurrence in the string
            for item in find_and_replace_list:
                obj = obj.replace(item[0], item[1], 1)

            result = obj

        except Exception as e:
            print(f"Received the following error: {e}")

    elif isinstance(obj, list):
        result = [replace_letters_randomly(e) for e in obj]

    return result

# %%
#######################################
def update_module_files():
    import pathlib
#    
    def new_module(source_dir: str, prepend_text = None):
        """Creates a new module file consisting of all functions that reside in a given folder.  This tool is intended to receive the path of a given folder where the individual function .py files reside, and it will retrieve the content of each of those .py files, and put all of the content together in a single file in the "modules" directory (hard-coded in this script).  The new single file will have the same name as the given "source_dir" folder + the ".py" extension.

        Reference:
            https://stackoverflow.com/questions/47518669/create-new-folder-with-pathlib-and-write-files-into-it

        Args:
            source_dir (str): Reference the path of the directory where the function .py files reside
        """
        import pathlib
        
        source_dir_pathobj = pathlib.Path(source_dir).resolve()
        if not source_dir_pathobj.is_dir():
            print('The given source_dir is not a directory.')
            exit()
        
        dest_dir_pathobj = pathlib.Path().home() / "Temp/pyplay/IMPORT_functions/Python_3.8_Tools/modules/"
        
        def new_module_header(source_dir_name: str):
            
            def format_header_block(string: str):
                """Prints a header for use with my function files

                Examples:
                    #######################################\n
                    ########### ARRAY FUNCTIONS ###########\n
                    #######################################\n

                """
                newstring = ""
                newstring += "{0:#<39}".format("") + "\n"
                newstring += "{0:#^39}".format(f" {string} ") + "\n"
                newstring += "{0:#<39}".format("") + "\n\n"
                
                return newstring
            
            header_name = source_dir_name.replace('_', ' ').upper()
            new_header = format_header_block(header_name)
            return new_header
        
        header_content = new_module_header(source_dir_pathobj.name)
        all_funcs_content_from_source_dir = ''.join([ e.read_text() for e in source_dir_pathobj.glob('*') if e.is_file() and e.name.endswith('.py')])
        
        if prepend_text:
            full_content = header_content + prepend_text + all_funcs_content_from_source_dir
        else:
            full_content = header_content + all_funcs_content_from_source_dir
        
        new_module_name = source_dir_pathobj.name + '.py'
        
        module_filepath = dest_dir_pathobj / new_module_name
        
        with module_filepath.open('w') as f:
            f.write(full_content)
#

    thepath = pathlib.Path.home() / 'Temp/pyplay/IMPORT_functions/Python_3.8_Tools/'
    
    for eachdir in thepath.glob('*'):
        if eachdir.is_dir() and eachdir.name.endswith('_funcs'):
            eachfuncsdir = eachdir
            if eachfuncsdir.name == 'all_funcs':
                new_module(eachfuncsdir.as_posix(), prepend_text="# NOTE: Excludes scapy functions.  To import scapy functions, use 'from scapy_funcs import *'\n\n")
            elif eachfuncsdir.name == 'scapy_funcs':
                new_module(eachfuncsdir.as_posix(), prepend_text="from scapy.all import *\n\n")
            else:
                new_module(eachfuncsdir.as_posix())# %%
#######################################
def copy_directory(thepath: str, dest: str):
    """Copies a directory.

    References:
        https://stackoverflow.com/questions/123198/how-can-a-file-be-copied
        https://www.geeksforgeeks.org/python-move-or-copy-files-and-directories/

    Args:
        thepath (str): Specify the path of the directory you want to copy
        dest (str): Specify the destination or directory copy name
    """
    import shutil
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    copy_path = pathlib.Path(dest).resolve()
    shutil.copytree(str(path_obj), str(copy_path))


cpdir = copy_directory

# %%
#######################################
def duplicate_randomly(thelist: list, maxduplication=3):
    """Takes a list of objects and will randomly duplicate the occurrence of each object in the list.  The maximum threshold of how many duplicates are created is limited by the 'maxduplication' parameter and defaults to 3.

    Args:
        thelist (list): Reference an existing list
        maxduplication (int, optional): Specify the max number of duplicates that will be created. Defaults to 3.

    Returns:
        list: Returns a list.
    """
    import random
    
    newlist = []
    for item in thelist:
        templist = []
        templist.append(item)
        multiplyby = random.randint(1, maxduplication)
        templist = templist * multiplyby
        newlist.extend(templist)
    return newlist

# %%
#######################################
def get_help_as_text(function_name: object):
    """Outputs the "help" docstring for the given function as text.

    Examples:
        >>> get_help_as_text(len)\n
        'Help on built-in function len in module builtins:\\n\\nlen(obj, /)\\n    Return the number of items in a container.\\n\\n'
        >>> print( get_help_as_text(len) )\n
        Help on built-in function len in module builtins:

        len(obj, /)
            Return the number of items in a container.

    References:
        https://stackoverflow.com/questions/11265603/how-do-i-export-the-output-of-pythons-built-in-help-function

        https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout
    """
    import contextlib
    import io

    with contextlib.redirect_stdout(io.StringIO()) as f:
        help(function_name)
    return f.getvalue()

# %%
#######################################
def replace_ipaddress_randomly(obj: str or list):
    """Takes a given string or a list of strings and replaces each IP Address with a randomly generated substitution.

    Examples:
        >>> example\n
        'client 210.52.249.246#19232,client 55.156.45.4#33065,client 189.43.24.227#37534,client 239.68.189.30#30097,client 103.209.157.229#48600,client 162.155.156.194#35500,client 21.186.183.234#34398,client 195.112.201.182#14423,client 229.109.221.127#46930,client 100.70.77.31#13513'

        >>> replace_ipaddress_randomly(example)\n
        'client 184.42.243.125#19232,client 74.230.98.2#33065,client 203.10.69.128#37534,client 176.29.181.74#30097,client 145.234.153.143#48600,client 193.224.213.148#35500,client 77.214.218.163#34398,client 150.197.184.211#14423,client 245.175.122.227#46930,client 125.68.48.34#13513'

        >>> iplist = [
        ...     "210.52.249.246",
        ...     "55.156.45.4",
        ...     "189.43.24.227",
        ...     "239.68.189.30",
        ...     "103.209.157.229",
        ...     "162.155.156.194",
        ...     "21.186.183.234",
        ...     "195.112.201.182",
        ...     "229.109.221.127",
        ...     "100.70.77.31",
        ... ]

        >>> replace_ipaddress_randomly(iplist)\n
        ['242.21.117.149', '24.248.33.9', '199.62.94.229', '197.96.239.66', '132.221.212.220', '182.243.176.207', '52.124.125.221', '170.198.120.180', '242.183.115.107', '117.24.83.16']

    References:
        IP Address reg ex matching syntax retrieved from:
        https://www.regular-expressions.info/ip.html

    Args:
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a string or list of strings with replaced IP Addresses.
    """
    import re
    import random

    # Syntax retrieved from: https://www.regular-expressions.info/ip.html
    match_syntax = re.compile(
        r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        + r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        + r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        + r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b"
    )

    single_digits = [str(e) for e in range(1, 10)]
    double_digits = [str(e) for e in range(10, 100)]
    triple_digits = [str(e) for e in range(100, 256)]

    if isinstance(obj, str):
        find_results = re.findall(match_syntax, obj)
        find_replace_list = []

        for ipaddress_sections in find_results:

            orig_ip = ".".join(ipaddress_sections)
            replacement_octets = []

            for octet in ipaddress_sections:
                temp_octet = ""
                if len(octet) == 1:
                    temp_octet = random.choice(single_digits)
                    replacement_octets.append(temp_octet)
                elif len(octet) == 2:
                    temp_octet = random.choice(double_digits)
                    replacement_octets.append(temp_octet)
                elif len(octet) == 3:
                    temp_octet = random.choice(triple_digits)
                    replacement_octets.append(temp_octet)

                replacement_ip = ".".join(replacement_octets)

            find_replace_list.append((orig_ip, replacement_ip))

        # This replacement will replace a particular IP with the same substitution throughout the string
        # Use .replace(match, replacement, 1) if you want a random replacement for each occurrence of a given IP address
        for replacement in find_replace_list:
            obj = re.sub(replacement[0], replacement[1], obj)

        result = obj

    elif isinstance(obj, list):
        result = [replace_ipaddress_randomly(e) for e in obj]

    return result

# %%
#######################################
def get_current_python_path():
    """Returns the full path of the python interpreter that is currently in use.

    Examples:
        >>> get_current_python_path()\n
        '/home/cooluser/playground/import_func_venv/bin/python'
    """
    import sys

    return sys.executable

# %%
#######################################
def get_file_symlink(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    symlink_resolved = path_obj.readlink()
    return symlink_resolved

# %%
#######################################
def split_path(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    parts = path_obj.parts
    return parts

# %%
#######################################
def decode_base64(obj: object):
    """Decodes the string / bytes string using BASE64.

    Example:
        >>> encode_base64('hello')\n
        b'aGVsbG8=\\n'
        >>> encode_base64('hello', no_newline=True)\n
        b'aGVsbG8='
        >>> encode_base64('hello', True)\n
        b'aGVsbG8='
        >>>
        >>> decode_base64(b'aGVsbG8=\\n')\n
        b'hello'
        >>> decode_base64(b'aGVsbG8=')\n
        b'hello'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj
    return codecs.decode(temp_obj, "base64")

# %%
#######################################
def get_functions_in_imported_module(module_name, mymodule=True):
    """Returns objects in a module where "isfunction()" is True.

    References:
        One way to do it, which is the code we settled on for this function
        https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module

        This was another way to do it, which I commented out below for reference
        https://www.tutorialspoint.com/How-to-list-all-functions-in-a-Python-module

        Some other approaches
        https://stackoverflow.com/questions/6315496/display-a-list-of-user-defined-functions-in-the-python-idle-session

    Args:
        module_name (obj): Reference the module to inspect

    Returns:
        list: Returns an array of tuples where the 2nd element "isfunction"
    """
    from inspect import getmembers, isfunction

    # - This returned the whole tuple which shows the memory id() location for each function as well -
    # funcs = [e for e in getmembers(module_name) if isfunction(e[1])]

    funcs = [e[0] for e in getmembers(module_name, isfunction)]

    if mymodule:
        # my functions when initially defined normally have an '_' in the name
        # however the 'aliases' I create for the functions do not have an '_'
        # So this bit of code filters out all functions without an '_'
        myfuncs = [e for e in funcs if "_" in e]
        return myfuncs
    else:
        return funcs

# %%
#######################################
def match_str_len_with_padding(
    string1: str, string2: str, padding="#", align=("left", "center", "right")[1]
):
    """Returns a list containing the original longer string, and the smaller string with padding.

    Examples:
        >>> mystring = "Complex is better than complicated."
        >>> secondstring = " blah "
        >>> blah_song = "blah ba blah blah blah"
        >>> match_str_len_with_padding(mystring, secondstring)\n
        ['Complex is better than complicated.', '############## blah ###############']
        >>> match_str_len_with_padding(mystring, blah_song, padding="*")\n
        ['Complex is better than complicated.', '******blah ba blah blah blah*******']
        >>> match_str_len_with_padding(mystring[::-1], mystring)\n
        ['.detacilpmoc naht retteb si xelpmoC', 'Complex is better than complicated.']
        >>> match_str_len_with_padding(mystring, blah_song, padding="&", align='right')\n
        ['Complex is better than complicated.', '&&&&&&&&&&&&&blah ba blah blah blah']
        >>> match_str_len_with_padding(mystring, blah_song, padding="<", align='left')\n
        ['Complex is better than complicated.', 'blah ba blah blah blah<<<<<<<<<<<<<']

    References:
        One liner if/else: https://youtu.be/MHlwl6GsT8s?t=990\n
        Format() with embedded variables for 'format specifiers': https://stackoverflow.com/questions/3228865/how-do-i-format-a-number-with-a-variable-number-of-digits-in-python

    Args:
        string1 (str): String number 1 to use in the comparison
        string2 (str): String number 2 to use in the comparison
        padding (str, optional): Here you can specify the padding character. Defaults to "#".
        align (str, optional): This is used to show valid arguments for this parameter (the default value is 'center'). Defaults to ('left','center','right')[1].

    Returns:
        list: Returns a list containing two strings of the same length, with the smaller string being padded.
    """

    bigger_str = string1 if len(string1) >= len(string2) else string2
    smaller_str = string1 if len(string1) < len(string2) else string2

    length_to_match = len(bigger_str)

    if align == "left":
        padded_string = "{small_str:{somepad}<{thelength}}".format(
            thelength=length_to_match, small_str=smaller_str, somepad=padding
        )
    elif align == "center":
        padded_string = "{small_str:{somepad}^{thelength}}".format(
            thelength=length_to_match, small_str=smaller_str, somepad=padding
        )
    elif align == "right":
        padded_string = "{small_str:{somepad}>{thelength}}".format(
            thelength=length_to_match, small_str=smaller_str, somepad=padding
        )

    if padded_string:
        return [bigger_str, padded_string]

# %%
#######################################
def remove_duplicates(thelist: list):
    """Takes a list containing duplicates and returns a list of unique elements only.

    Example:
        >>> myduplicates\n
        ['Bartók', 'vigilant', 'vigilant', 'Julianne', 'Julianne', 'Julianne', 'camera', 'camera', 'camera', "Espinoza's", "Espinoza's", 'Amgen', 'Amgen', 'Amgen', "Tomlin's", 'tenuring', 'encroached', 'encroached', 'laxatives', 'laxatives', 'laxatives']

        >>> remove_duplicates(myduplicates)\n
        ['Bartók', 'vigilant', 'Julianne', 'camera', "Espinoza's", 'Amgen', "Tomlin's", 'tenuring', 'encroached', 'laxatives']

    Args:
        thelist (list): Reference an existing list.

    Returns:
        list: Returns a list of unique values.
    """
    temp_dict = {}
    for item in thelist:
        temp_dict[item] = "the value doesn't matter, we want the key"
    results_list = list(temp_dict.keys())  #  Any duplicate "item"/"key" was overwritten, so the new list contains unique elements only
    return results_list

# %%
#######################################
# This is technically not a Rex Ex function, but it's in-theme with other functions here
def find_and_replace(findlist: str or list, replacelist: str or list, obj: str or list):
    """Takes a string or a list of strings and replaces substrings found in the findlist with those in the replacelist.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> text = "How about something simple"
        >>> find_and_replace("something", "everything", text)\n
        'How about everything simple'

        >>> ##### EXAMPLE 2 #####
        >>> moretext = ["How about something simple", "Or maybe something complex"]
        >>> moretext = ["How about something simple", "Or maybe something complex"]
        >>> find_and_replace("something", "everything", moretext)\n
        ['How about everything simple', 'Or maybe everything complex']

        >>> ##### EXAMPLE 3 #####
        >>> # First we are importing various functions that help us parse the data
        >>> from my_py_funcs.regex_funcs import (
        ...     refind_bookends,
        ...     replace_ipaddress_randomly,
        ...     replace_numbers_randomly,
        ... )

        >>> smallexample = "client 72.192.136.134#64983: query: www.coolhostname8864477.com IN,client 231.12.225.158#32688: query: www.coolhostname2927388.com IN,client 121.189.40.110#32424: query: www.coolhostname9651548.com IN"

        >>> # We create the "find list", which are the substrings we want to replace
        >>> find_list = refind_bookends("query: ", "IN", smallexample, ignorecase=False)
        >>> find_list\n
        ['www.coolhostname8864477.com ', 'www.coolhostname2927388.com ', 'www.coolhostname9651548.com ']

        >>> # Then we create the "replace list", which are the substrings we will use to replace those we found
        >>> replace_list = replace_numbers_randomly(find_list)
        >>> replace_list\n
        ['www.coolhostname0010968.com ', 'www.coolhostname9594644.com ', 'www.coolhostname3977824.com ']
        >>> newstuff = find_and_replace(find_list, replace_list, smallexample)
        >>> newstuff = replace_ipaddress_randomly(newstuff)
        >>> newstuff\n
        'client 90.176.170.125#64983: query: www.coolhostname0010968.com IN,client 165.55.134.210#32688: query: www.coolhostname9594644.com IN,client 194.179.58.197#32424: query: www.coolhostname3977824.com IN'


    Args:
        findlist (object): Reference a substring or list of substrings to find
        replacelist (object): Reference a substring or list of substrings to replace those that were found
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a new string or list of strings
    """

    if isinstance(findlist, str):
        if isinstance(obj, str):
            obj = obj.replace(findlist, replacelist)
            result = obj
        elif isinstance(obj, list):
            result = [find_and_replace(findlist, replacelist, e) for e in obj]

    elif isinstance(findlist, list):
        if isinstance(obj, str):
            for index, item in enumerate(findlist):
                obj = obj.replace(item, replacelist[index])
            result = obj
        elif isinstance(obj, list):
            result = [find_and_replace(findlist, replacelist, e) for e in obj]

    return result

# %%
#######################################
def replace_hexadecimal_randomly(obj: str or list):
    """Takes a string of hexadecimal digits or a list of string hexadecimal digits and randomly replaces the string with one of equivalent length but different hexadecimal numbers.

    Examples:
        >>> replace_hexadecimal_randomly('dst=92:26:72:6e:67:f5 src=02:94:f3:a1:b1:72')\n
        'dst=c2:a2:14:31:61:19 src=4c:22:51:3f:8a:72'

    References:
        # Helpful syntax for hexadecimal matching
        https://stackoverflow.com/questions/8366682/search-for-hexadecimal-number-on-python-using-re

    Args:
        obj (object): Reference either a string of hexadecimal digits or a list of string hexadecimal digits

    Returns:
        object: Returns a new string or a new list of strings
    """
    import re
    import random

    #
    if isinstance(obj, str):
        #
        try:
            #
            # We match on each consecutive string of digits
            match_list = re.findall(r"[0-9a-fA-F]{2,}", obj)
            #
            replacement_list = []
            for eachitem in match_list:
                #
                ### FIRST, WE CREATE A BIG STRING OF RANDOM DIGITS ###
                # The elements will be integers ranging from 1 to 100
                lst = list(range(1, 101))
                #
                # From the "lst" of numbers 1 - 100, there will be multiple random choices, the quantity of which is based off of the number given to "k="
                random_list_of_ints = random.choices(lst, k=420)
                #
                # Then we take that list of random numbers and join them together making one long string of digits
                rand_num_string = "".join([str(e) for e in random_list_of_ints])
                #
                # Then we convert that random number string into a hex string, and remove the leading "0x" designator
                rand_hex_string = hex(int(rand_num_string))[2:]
                #
                ### THEN, WE USE THAT RANDOM STRING OF HEX DIGITS IN OUR SUBSTITUTION ###
                # We then take the length of the match and use that integer value as the ending point of our slice into the rand_hex_string
                # Finally that slice is reversed and then it is used for the substitution, and then added to the replacement_list
                replacement_list.append(
                    re.sub(
                        r"[0-9a-fA-F]{2,}",
                        lambda x: rand_hex_string[: len(x.group(0))][::-1],
                        eachitem,
                    )
                )
            #
            # We create a list of 2 element tuples - the 1st element is the match, the 2nd is the replacement
            find_and_replace_list = [
                (e[1], replacement_list[e[0]]) for e in enumerate(match_list)
            ]
            #
            # Then we iterate over the find/replace list and replace the first occurrence in the string
            for item in find_and_replace_list:
                obj = obj.replace(item[0], item[1], 1)
            #
            result = obj
        #
        except Exception as e:
            print(f"Received the following error: {e}")
    #
    elif isinstance(obj, list):
        result = [replace_hexadecimal_randomly(e) for e in obj]
    #
    return result

# %%
#######################################
def get_preferred_encoding():
    """Shows the preferred encoding of the local machine (often it is "UTF-8").

    Examples:
        >>> get_preferred_encoding()\n
        'UTF-8'

    References:
        https://realpython.com/python-encodings-guide/
    """
    import locale

    return locale.getpreferredencoding()

# %%
#######################################
def lsfiles(thepath='.', recurse=False):
    import pathlib
    
    path_obj = pathlib.Path(thepath).resolve()

    if recurse:
        results = [e.as_posix() for e in path_obj.rglob('*') if e.is_file()]
    else:
        results = [e.name for e in path_obj.glob('*') if e.is_file()]
    return results

# %%
#######################################
def copy_file(filepath: str or list, dest: str):
    """Copies a file.

    References:
        https://stackoverflow.com/questions/123198/how-can-a-file-be-copied
        https://www.geeksforgeeks.org/python-move-or-copy-files-and-directories/

    Args:
        filepath (str): Specify the path of the file you want to copy
        dest (str): Specify the destination or file copy name
    """
    import shutil
    import pathlib

    if isinstance(filepath, str):
        path_obj = pathlib.Path(filepath).resolve()
        dest_path = pathlib.Path(dest).resolve()
        shutil.copy2(str(path_obj), str(dest_path))
    elif isinstance(filepath, list):

        dest_path = pathlib.Path(dest).resolve()

        for eachitem in filepath:
            path_obj = pathlib.Path(eachitem).resolve()
            shutil.copy2(str(path_obj), str(dest_path))


cpfile = copy_file

# %%
#######################################
def filehandle_append(thepath: str, content: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with open(path_obj, "a") as f:
        f.write(content)


appendtext = filehandle_append

# %%
#######################################
def get_etc_shadow_salt(string: str):
    """Returns the salt found within the line retreived from the /etc/shadow file

    Examples:
        >>> line_from_etc_shadow = 'root:$1$umqC71l2$370xDLmeGD9m4aF/ciIlC.:14425:0:99999:7:::'\n
        >>> get_etc_shadow_salt(line_from_etc_shadow)\n
        'umqC71l2'

    References:
        https://linuxize.com/post/etc-shadow-file/
    """
    (
        username,
        hash_string,
        last_pw_change,
        min_pw_age,
        max_pw_age,
        warn_period,
        exp_date,
    ) = string.split(":")[:-2]
    if "$" in hash_string:
        algorithm, salt, thehash = hash_string.split("$")[1:]
        return salt

    else:
        return "There is no $ in the hash_string value."

# %%
#######################################
def lsdirs(thepath='.', recurse=False):
    import pathlib
    
    path_obj = pathlib.Path(thepath).resolve()
    
    if recurse:
        results = [e.as_posix() for e in path_obj.rglob('*') if e.is_dir()]
    else:
        results = [e.name for e in path_obj.glob('*') if e.is_dir()]
    return results

# %%
#######################################
def encode_punycode(string: str):
    """Encodes the string using Punycode.

    Example:
        >>> encode_punycode('hello')\n
        b'hello-'

        >>> decode_punycode(b'hello-')\n
        'hello'
    """
    import codecs

    if isinstance(string, str):
        temp_obj = string

    result = codecs.encode(temp_obj, "punycode")
    return result

# %%
#######################################
def format_header_text(string: str):
    """Returns a header string that is centered within a space of 39 characters, bordered by "#".

    Examples:
        >>> format_header_text('ARRAY FUNCTIONS')\n
        '########### ARRAY FUNCTIONS ###########'
    """
    return "{0:#^39}".format(f" {string} ")

# %%
#######################################
def display_binary_4bit(num: int):
    """Displays the binary string representation for a given integer.  If the number is within 4 bits, the output will be 4 binary digits; if the number is 8 bits then 8 binary digits will be the output.

    Examples:
        >>> display_binary_4bit(151)\n
        '10010111'

        >>> display_binary_4bit(11)\n
        '1011'
    """
    return format(num, "04b")

# %%
#######################################
def sort_by_multiple_indexes(lst: list, *index_nums: int, reverse=False):
    """With a two dimensional array, returns the rows sorted by one or more column index numbers.

    Example:
        >>> mylst = []
            # create the table (name, age, job)
        >>> mylst.append(["Nick", 30, "Doctor"])
        >>> mylst.append(["John",  8, "Student"])
        >>> mylst.append(["Paul", 22, "Car Dealer"])
        >>> mylst.append(["Mark", 66, "Retired"])
        >>> mylst.append(['Yolo', 22, 'Student'])
        >>> mylst.append(['Mark', 66, 'Doctor'])

        # Sort by the "Name"
        >>> sort_by_multiple_indexes(mylst, 0)\n
        [['John', 8, 'Student'], ['Mark', 66, 'Retired'], ['Mark', 66, 'Doctor'], ['Nick', 30, 'Doctor'], ['Paul', 22, 'Car Dealer'], ['Yolo', 22, 'Student']]

        # Sort by the "Name", then the "Job"
        >>> sort_by_multiple_indexes(mylst, 0,2)\n
        [['John', 8, 'Student'], ['Mark', 66, 'Doctor'], ['Mark', 66, 'Retired'], ['Nick', 30, 'Doctor'], ['Paul', 22, 'Car Dealer'], ['Yolo', 22, 'Student']]

        # Sort by the "Job"
        >>> sort_by_multiple_indexes(mylst, 2)\n
        [['Paul', 22, 'Car Dealer'], ['Nick', 30, 'Doctor'], ['Mark', 66, 'Doctor'], ['Mark', 66, 'Retired'], ['John', 8, 'Student'], ['Yolo', 22, 'Student']]

        # Sort by the "Job", then the "Age"
        >>> sort_by_multiple_indexes(mylst, 2,1)\n
        [['Paul', 22, 'Car Dealer'], ['Nick', 30, 'Doctor'], ['Mark', 66, 'Doctor'], ['Mark', 66, 'Retired'], ['John', 8, 'Student'], ['Yolo', 22, 'Student']]

        # Sort by age in descending order
        >>> sort_by_multiple_indexes(mylst, 1, reverse=True)\n
        [['Mark', 66, 'Retired'], ['Mark', 66, 'Doctor'], ['Nick', 30, 'Doctor'], ['Paul', 22, 'Car Dealer'], ['Yolo', 22, 'Student'], ['John', 8, 'Student']]

    References:
        https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work
        https://docs.python.org/3/library/operator.html#operator.itemgetter
    """
    import operator

    if reverse:
        return sorted(lst, key=operator.itemgetter(*index_nums), reverse=True)
    else:
        return sorted(lst, key=operator.itemgetter(*index_nums))

# %%
#######################################
def get_content(thepath: str, as_bytes=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if as_bytes:
        contents = path_obj.read_bytes()
    else:
        contents = path_obj.read_text()
    return contents


cat = get_content

# %%
#######################################
def decode_rot13(string: str):
    """Decodes the string using ROT-13.

    Examples:
        >>> encode_rot13('hello')\n
        'uryyb'
        >>> decode_rot13('uryyb')\n
        'hello'
    """
    import codecs

    return codecs.decode(string, "rot13")

# %%
#######################################
def set_cwd(thepath: str):
    """Change the current directory you are in.

    References:
        https://stackoverflow.com/questions/41742317/how-can-i-change-directory-with-python-pathlib

    Args:
        thepath (str): Specify the path
    """
    import os

    os.chdir(thepath)


cd = set_cwd

# %%
#######################################
def get_files_by_extension(thepath=".", extension="*", stringoutput=False):
    """Returns a list of the files ending in the given extension

    Examples:
        >>> get_files_by_extension(extension='txt')\n
        [PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/test_text.txt')]

        >>> get_files_by_extension(extension='txt', stringoutput=True)\n
        ['/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/test_text.txt']

    Args:
        thepath (str, optional): Specify the path. Defaults to ".".
        extension (str, optional): Specify the extension. Defaults to '*'.
        stringoutput (bool, optional): Switch to allow for the output to be a str object. Defaults to False.

    Returns:
        list: Returns an array of files matching the criteria
    """
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if extension != "*":
        myglob = path_obj.glob(f"*{extension}")
    else:
        myglob = path_obj.glob("*")

    if stringoutput:
        results = sorted([str(file) for file in myglob if file.is_file()])
    else:
        results = sorted([file for file in myglob if file.is_file()])

    return results

# %%
#######################################
def get_functions_in_module_file(filename):
    """Takes a given module filename and returns the names of defined functions in the file.

    References:
        Excellent answer by "csl", which is the basis of this function
        https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module

    Args:
        filename (str): Reference the path of the file

    Returns:
        list: Returns a list of sorted function names
    """
    import ast
    import os
    import pathlib

    path_obj = pathlib.Path().home() / "Temp/pyplay/IMPORT_functions/my_py_funcs"
    os.chdir(path_obj)

    with open(filename, "rt") as file:
        ast_parse_result = ast.parse(file.read(), filename=filename)

    # This ast parse result itemizes when a function is defined as an "ast.FunctionDef"
    # and further itemizes each time there is an assignment with "ast.Assign"...
    # This differentiation allows me to remove from the output any function "alias" assignments
    func_def_only = [
        e.name for e in ast_parse_result.body if isinstance(e, ast.FunctionDef)
    ]
    result = sorted(func_def_only)

    return result

# %%
#######################################
def refindall_ssn(obj: str or list):
    """Takes a string or list of strings and pulls out possible Social Security Numbers (SSNs) within the string.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> ssn_list = [
        ...     "131-77-1772",
        ...     "189 58 6514",
        ...     "285552842",
        ...     "396668332",
        ...     "343524281",
        ...     "683 96 1179",
        ...     "993 89 8127",
        ...     "331 65 0902",
        ...     "104-53-7752",
        ...     "626 22 7897",
        ...     "481-56-5808",
        ...     "772 97 1352",
        ...     "235734843",
        ... ]

        >>> refindall_ssn(ssn_list)
        ['131-77-1772', '189-58-6514', '285-55-2842', '396-66-8332', '343-52-4281', '683-96-1179', '993-89-8127', '331-65-0902', '104-53-7752', '626-22-7897', '481-56-5808', '772-97-1352', '235-73-4843']

        >>> ##### EXAMPLE 2 #####
        >>> newdata = "hKedOp M341-31-3346I BlA uNACVG bJzH-o FdkVhlRlkFgAj489 33 0132ho-jUO gdUjp HNVWXUrIkJJ-MzY966678227-hoMa cdhgoAI UONbfjgQWrAP-FsoWT-t522489534sARAtvH-ENXMPazpPY yhwt -m002857865GLm fWX-DYt-Lhqyhj679 13 8344pNmUrXJdGg V eINyF mG-rIs592 76 1624iH j OyPr QbuchOEiPycnC y hGmIJ757 84 6898bBvQDisd-a F c-R-nVm835-16-6964bCLxlBNjTaFgQMQvXrCl434 96 6239MxKZ ThyaFE-CBvBQnEMznbZCxbp928-36-4379mDIb jl sNkdCgPUxgpnypCAeywuD907 82 1576TPMLyYnhrDTqJLzpClNtGUxZIET825216383wllgM q"

        >>> refindall_ssn(newdata)\n
        ['341-31-3346', '489-33-0132', '966-67-8227', '522-48-9534', '002-85-7865', '679-13-8344', '592-76-1624', '757-84-6898', '835-16-6964', '434-96-6239', '928-36-4379', '907-82-1576', '825-21-6383']

    Args:
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a list of SSNs found within the string
    """
    import re

    if isinstance(obj, str):
        match_syntax = re.compile(r"(\d{3})[\s-]?(\d\d)[\s-]?(\d{4})")
        result = re.findall(match_syntax, obj)
        final = ["-".join(e) for e in result]
    elif isinstance(obj, list):
        final = []
        for item in obj:
            match_syntax = re.compile(r"(\d{3})[\s-]?(\d\d)[\s-]?(\d{4})")
            result = re.findall(match_syntax, item)
            final.extend(["-".join(e) for e in result])
    return final

# %%
#######################################
def get_random(thelist: list, samplesize=10):
    import random
    
    results_list = random.choices(thelist, k=samplesize)
    return results_list

# %%
#######################################
def get_content_latin1(thepath: str):
    """Returns the file content by interpreting the encoding as "LATIN-1" instead of UTF-8.  LATIN-1 has exactly 255 possible characters with no gaps, so it is perfect for reading text and binary data without errors.

    Examples:
        >>> test = get_content_latin1('test_text.txt')\n
        >>> test.splitlines()\n
        ['ok', 'so here is some', "'blah blah'", 'We are planning', 'To use this ', 'in not only', 'normal testing...', 'but also for "gzip compressed ', 'text searching"', 'I know... sounds cool', "Let's see if it works!"]

        >>> binary_test = get_content_latin1('/bin/bash')\n
        >>> binary_test[:15]\n
        '\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'

    Args:
        thepath (str): Reference the file to read.

    Returns:
        str: Returns the content of the file as one long string
    """
    with open(thepath, encoding="latin-1") as f:
        content = f.read()
    return content


catlatin1 = get_content_latin1

# %%
#######################################
def dirplus(obj=None):
    """Behaves similar to the dir() function, but omits the "dunder" objects from the output.

    Examples:
    >>> blah = 'Here is some blah blah'

    >>> dirplus()\n
    ['dirplus', 'blah']

    >>> type(blah)\n
    <class 'str'>

    >>> dirplus(blah)\n
    ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

    References:
        # This was a valuable reference for information about namespaces, globals(), locals(), and such like:
        https://realpython.com/python-namespaces-scope/

    Args:
        obj (object, optional): Reference the desired object. Defaults to None.

    Returns:
        list: Returns a list of the pertinent "dir()" output
    """
    if obj:
        return [e for e in dir(obj) if not e.startswith("__")]
    else:
        return [e for e in globals().keys() if not e.startswith("__")]

# %%
#######################################
def deep_copy(obj_to_copy: object):
    """Returns a copy.deepcopy() of the given object.

    Example:
        >>> frag3_pcap = rdpcap('fragments3.pcap')
        >>> frag3_pcap\n
        <fragments3.pcap: TCP:15 UDP:0 ICMP:0 Other:114>
        >>> id(frag3_pcap)\n
        140567994637504

        >>> frag3_pcap_copy = deep_copy(frag3_pcap)
        >>> frag3_pcap_copy\n
        <fragments3.pcap: TCP:15 UDP:0 ICMP:0 Other:114>
        >>> id(frag3_pcap_copy)\n
        140568023743440

    Reference:
        https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy

    Args:
        obj_to_copy (object): Reference an existing object

    Returns:
        object: Returns a deepcopy of the given object
    """
    from copy import deepcopy
    return deepcopy(obj_to_copy)

# %%
#######################################
def encode_gzip(obj: object):
    """Encodes the string / bytes string using GZIP / zlib.

    Example:
        >>> encode_gzip('hello')\n
        b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15'

        >>> encode_gzip(b'hello')\n
        b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15'

        >>> decode_gzip(b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15')\n
        b'hello'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj

    result = codecs.encode(temp_obj, "zlib")
    return result


encode_zip = encode_gzip

# %%
#######################################
def get_allbefore_in_array(lst: list, obj: object, include_value=False):
    """Returns a list of all elements before the given value (if that value is in the list).

    Example:
    >>> mylst = ['exit', 'quit', 're', 'sys', 'teststring']\n
    >>> get_allbefore_in_array(mylst, 're')\n
    ['exit', 'quit']
    >>> get_allbefore_in_array(mylst, 're', include_value=True)\n
    ['exit', 'quit', 're']
    """
    index = lst.index(obj)
    if include_value:
        newlst = list(lst[0 : index + 1])
    else:
        newlst = list(lst[0:index])
    return newlst

# %%
#######################################
def refindall_ipaddress(obj: str or list):
    """Takes a given string or list of strings and returns the IP Addresses in the string.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> myexample = "client 218.19.144.132#19232,client 53.173.21.9#33065,client 132.72.64.130#37534,client 220.65.223.96#30097,client 109.136.221.226#48600,client 165.224.250.158#35500,client 42.187.220.133#34398,client 234.181.156.136#14423,client 248.189.187.101#46930,client 201.75.90.98#13513"

        >>> refindall_ipaddress(myexample)\n
        ['218.19.144.132', '53.173.21.9', '132.72.64.130', '220.65.223.96', '109.136.221.226', '165.224.250.158', '42.187.220.133', '234.181.156.136', '248.189.187.101', '201.75.90.98']

        >>> ##### EXAMPLE 2 #####
        >>> mylist = [
        ...     "IP at some time: 216.90.223.255",
        ...     "Here is another ... 60.231.93.2",
        ...     "178.83.41.251, and this one too",
        ...     "More 105.45.185.55 to come soon",
        ...     "For the win, 101.184.120.113",
        ...     "199.227.198.206 -- looks promising",
        ...     "Possible bogey _ 10.164.142.233",
        ...     "190.253.191.105; coming in with artillery",
        ...     "fast and high 165.179.143.113",
        ...     "one final go +249.64.38.17",
        ... ]

        >>> refindall_ipaddress(mylist)\n
        [['216.90.223.255'], ['60.231.93.2'], ['178.83.41.251'], ['105.45.185.55'], ['101.184.120.113'], ['199.227.198.206'], ['10.164.142.233'], ['190.253.191.105'], ['165.179.143.113'], ['249.64.38.17']]

    References:
        IP Address reg ex matching syntax retrieved from:
        https://www.regular-expressions.info/ip.html

    Args:
        obj (object): Reference a string or list of strings.

    Returns:
        list: Returns a list of strings containing the matched IP Addresses
    """
    import re

    # Syntax retrieved from: https://www.regular-expressions.info/ip.html
    match_syntax = re.compile(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}"
        + r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b"
    )

    if isinstance(obj, str):
        result = re.findall(match_syntax, obj)
    elif isinstance(obj, list):
        result = [refindall_ipaddress(e) for e in obj]

    return result

# %%
#######################################
def decode_bz2(obj: object):
    """Decodes the string / bytes string using BZ2.

    Example:
        >>> encode_bz2('hello')\n
        b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80'

        >>> encode_bz2(b'hello')\n
        b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80'

        >>> decode_bz2(b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80')\n
        b'hello'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj
    return codecs.decode(temp_obj, "bz2")

# %%
#######################################
def update_allfuncs_dir():
    import pathlib
    
    def remove_file(filepath: str or list):
        """Removes the specified file.

        References:
            https://stackoverflow.com/questions/42636018/python-difference-between-os-remove-and-os-unlink-and-which-one-to-use

        Args:
            filepath (str): Specify the path of the file
        """
        import pathlib

        if isinstance(filepath, str):
            path_obj = pathlib.Path(filepath).resolve()
            if path_obj.is_file():
                path_obj.unlink()
        elif isinstance(filepath, list):
            for eachitem in filepath:
                path_obj = pathlib.Path(eachitem).resolve()
                if path_obj.is_file():
                    path_obj.unlink()
                    

    def copy_file(filepath: str or list, dest: str):
        """Copies a file.

        References:
            https://stackoverflow.com/questions/123198/how-can-a-file-be-copied
            https://www.geeksforgeeks.org/python-move-or-copy-files-and-directories/

        Args:
            filepath (str): Specify the path of the file you want to copy
            dest (str): Specify the destination or file copy name
        """
        import shutil
        import pathlib

        if isinstance(filepath, str):
            path_obj = pathlib.Path(filepath).resolve()
            dest_path = pathlib.Path(dest).resolve()
            shutil.copy2(str(path_obj), str(dest_path))
        elif isinstance(filepath, list):

            dest_path = pathlib.Path(dest).resolve()

            for eachitem in filepath:
                path_obj = pathlib.Path(eachitem).resolve()
                shutil.copy2(str(path_obj), str(dest_path))

                    
    # This is the parent path containing the "*_funcs" child directories (which, in turn, contain all of the function .py files)
    thepath = pathlib.Path.home() / 'Temp/pyplay/IMPORT_functions/Python_3.8_Tools/'
    
    # This is the destination path to where we will be copying each function .py file
    allfuncsdir_path = thepath / 'all_funcs'
    
    # Here we remove all of the old files in the 'all_funcs' directory
    [ remove_file( e.as_posix() )  for e in allfuncsdir_path.glob('*') ]
    
    for eachdir in thepath.glob('*'):
        if eachdir.is_dir() and eachdir.name.endswith('_funcs'):
            eachfuncsdir = eachdir
            if eachfuncsdir.name == 'all_funcs' or eachfuncsdir.name == 'scapy_funcs':
                # ignore these two directories
                pass
            else:
                # for each file ending in .py (these should be the individual function tools ending in .py), copy that file to the destination dir
                for funcpy in eachfuncsdir.glob('*.py'):
                    copy_file( funcpy.as_posix(), allfuncsdir_path.as_posix() )

# %%
#######################################
def dict_merge(dict1: dict, dict2: dict):
    """Merges two dictionaries into one.

    Examples:
        >>> x = {'a': 1, 'b': 2}\n
        >>> y = {'b': 3, 'c': 4}\n
        >>> dict_merge(x, y)\n
        {'a': 1, 'b': 3, 'c': 4}

    References:
        https://www.youtube.com/watch?v=Duexw08KaC8
    """
    return {**dict1, **dict2}

# %%
#######################################
def get_files_recursively(thepath=".", names=False, stringoutput=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if stringoutput:
        contents = sorted([str(obj) for obj in path_obj.rglob("*") if obj.is_file()])
    else:
        contents = sorted([obj for obj in path_obj.rglob("*") if obj.is_file()])
    return contents

# %%
#######################################
def display_chr_value(num: int):
    """Displays the glyph representation of a given integer.

    Examples:
        >>> display_chr_value(128013)
        '🐍'

        >>> display_chr_value(77)
        'M'

        display_chr_value(700)
        'ʼ'
    """
    return chr(num)

# %%
#######################################
def clear_array(lst: list):
    """Takes a given list and clears out all of the elements within the list.

    Examples:
        >>> mylst\n
        [('a', 1, 'John'), ('b', 2, 'Alice'), ('c', 3, 'Bob')]
        >>> clear_array(mylst)\n
        >>> mylst\n
        []
    """
    return lst.clear()

# %%
#######################################
def new_random_numberslist(listsize=10, min_num=0, max_num=1000):
    """Returns a list of random words.  The default size of the list is 10, but this can be modified with the "listsize" parameter.

    Args:
        listsize (int, optional): Specify the desired length of the list. Defaults to 10.
        min_num (int, optional): Specify the lowest number. Defaults to 0.
        max_num (int, optional): Specify the highest number. Defaults to 1000.

    Returns:
        list: Returns a list of integers.
    """
    import random
    
    results_list = []
    for i in range(listsize):
        rand_num = random.randint(min_num, max_num)
        results_list.append(rand_num)
    return results_list

# %%
#######################################
def flatten_nested_arrays(lst: list):
    """Creates a single flat list out of a given list containing nested lists.

    Examples:
        >>> nested_list = [1, [2], [[3], 4], 5]\n
        >>> flatten_nested_arrays(nested_list)\n
        [1, 2, 3, 4, 5]
        >>> more_nesting = [1, [2], [[3,[7,8,9]], 4], 5]\n
        >>> flatten_nested_arrays(more_nesting)\n
        [1, 2, 3, 7, 8, 9, 4, 5]

    References:
        https://www.youtube.com/watch?v=pG3L2Ojh1UE
    """
    flattened_list = []
    for obj in lst:
        if isinstance(obj, list):
            flattened_list.extend(flatten_nested_arrays(obj))
        else:
            flattened_list.append(obj)
    return flattened_list

# %%
# #######################################
def os_walk(thepath: str):
    """Performs an os.walk on the given path.

    Examples:
        >>> test = os_walk('../worksheet_dir')
        >>> pprint(test)\n
        [('../worksheet_dir',\n
        ['__pycache__'],\n
        ['worksheet_sets.py',
        'worksheet_match_str_len_with_padding.py',
        'worksheet_pathlib.py',
        'worksheet_name_eq_main_demo.py',
        'worksheet_xor_strings.py',
        'worksheet_where_like.py']),\n
        ('../worksheet_dir/__pycache__',\n
        [],\n
        ['worksheet_name_eq_main_demo.cpython-38.pyc'])]

        >>> test[-1]\n
        ('../worksheet_dir/__pycache__', [], ['worksheet_name_eq_main_demo.cpython-38.pyc'])

    Args:
        thepath (str): Reference the path

    Returns:
        list: Returns a list of tuples with 3 elements.  The 1st element is the directory itself, the 2nd element is a list of all subdirectories in that directory, and the 3rd element is a list of all of the files in the directory.
    """
    import os

    result = list(os.walk(thepath))
    return result

# %%
#######################################
def get_dirs_recursively(thepath=".", stringoutput=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if stringoutput:
        contents = sorted([str(obj) for obj in path_obj.rglob("*") if obj.is_dir()])
    else:
        contents = sorted([obj for obj in path_obj.rglob("*") if obj.is_dir()])
    return contents

# %%
#######################################
def new_random_number(size=None):
    """Creates a large random number string. You can specify the size of the number using the "size" parameter.

    Examples:
        >>> new_random_number()\n
        '88495077433033604864459347219444521153467941653074517'

        >>> new_random_number()\n
        '50687589765828927139866314225259581387781147585513699'

        >>> new_random_number()\n
        '3933481384'

        >>> new_random_number(size=333)\n
        '9714188696247383654871292573098225426647253076733397769390728697759149793081512588524364279370278384692180475130825330801079463843655342153603449199025254084984353138753538945813523746920322710962748572347098357639231982180325558624756995274493507086476515545437136794779622702572568526438176415058625571928676953194838042337245543725816954176121011728783177495855283625899367553099288845402459285860401135256887874543963892694098154533594068558877234595744195741767995977316325571867838167880357384194314525465248320818965444224623264936226428813528010558221318554454332511926659310098247750742688442346813527103355913470354848965473812'

        >>> new_random_number(size=123)\n
        '91214915252828538635886489742232177541769241334437959742634202621180775793449210509188183499799551465326960258663248621524515522562839393141151318716015189324901944462067354183367892964644774711423589068814314271621465396719985816232'

        >>> new_random_number(42)\n
        '577556851583248222148853278534675679332074959294122553484454275175328584499871890'

        >>> new_random_number(7)\n
        '18339518883949'


        Args:
            size (int, optional): Specify a desired number size. Defaults to None.

        Returns:
            str: Returns a long number string
    """
    import random

    if size:
        size_of_list = int(size)
    else:
        # Here we  create a list of up to 30 elements in size
        size_of_list = random.choice(range(1, 30))

    # The elements will be integers ranging from 1 to 100
    lst = list(range(1, 101))
    # From the "lst" of numbers 1 - 100, there will be multiple random choices, the quantity of which is based off of the number given to "k="
    random_list_of_ints = random.choices(lst, k=size_of_list)
    # Then we take that list of random numbers and join them together making one long string of digits
    big_random_number_string = "".join([str(e) for e in random_list_of_ints])
    return big_random_number_string

# %%
#######################################
def combine_arrays(*lsts: list):
    """Appends each given list to larger array, returning a list of lists for the final value

    Examples:
        >>> lst_abc = ['a','b','c']\n
        >>> lst_123 = [1,2,3]\n
        >>> lst_names = ['John','Alice','Bob']\n
        >>> combine_arrays(lst_abc,lst_123,lst_names)\n
        [['a', 'b', 'c'], [1, 2, 3], ['John', 'Alice', 'Bob']]
    """
    combined_list = []
    [combined_list.append(e) for e in lsts]
    return combined_list

# %%
#######################################
def xor_strings(string: str, xor_string="zen"):
    """Returns an XOR'ed string given a string object.  By default the string object will be XOR'ed using a truncated version of the "Zen of Python".  You can change this default by specifying your own "xor_string" value.

    Examples:
        >>> mystring = "Complex is better than complicated."
        >>> xor_strings(mystring)\n
        '\x17\x07\x08P6\x00\x16\x00\x06\x15\x002\x1c\x00\x1c\n\x1c\x0cT\n\x18Nt\n\x02M \t\x1d\x06\x13\x07onl'
        >>> xor_strings(
        ...     "\x17\x07\x08P6\x00\x16\x00\x06\x15\x002\x1c\x00\x1c\n\x1c\x0cT\n\x18Nt\n\x02M \t\x1d\x06\x13\x07onl"
        ... )\n
        'Complex is better than complicated.'

        >>> xor_strings('here is some blah blah', 'and here is a super secret string we use for xor')\n
        '\t\x0b\x16EH\x0c\x01ES\x06\x1eEAB\x1f\x14\x18E\x10L\x12\r'
        >>> xor_strings(
        ...     '\t\x0b\x16EH\x0c\x01ES\x06\x1eEAB\x1f\x14\x18E\x10L\x12\r', 'and here is a super secret string we use for xor'
        ... )\n
        'here is some blah blah'

    Args:
        string (str): The string object you want to XOR
        xor_string (str, optional): The xor_string used to XOR against the given string object. Defaults to "zen".

    Returns:
        str: Returns an XOR'ed string.
    """
    import codecs

    # import this
    from this import s as this_s

    # We initialize an empty string variable which we will += each xor'ed character to for the final string
    result_string = ""

    # We want to know the length of the given string, so we can have an equivalent number of characters from the "Zen of Python"
    len_of_string = len(string)

    if xor_string == "zen":
        # this.s is the zen of python rot13 encoded, so here we are decoding it
        zen = codecs.decode(this_s, "rot13")

        # Then we take the zen of python, and truncate it to match the length of the string we want to XOR
        match_len_for_xor_enum = zen[:len_of_string]
        for index_num, val in enumerate(string):
            result_string += chr(ord(val) ^ ord(match_len_for_xor_enum[index_num]))
        return result_string
    else:
        if len(string) == len(xor_string):
            match_len_for_xor_enum = xor_string
        elif len(string) > len(xor_string):
            makebig = xor_string * len(string)
            match_len_for_xor_enum = makebig[: len(string)]
        elif len(string) < len(xor_string):
            match_len_for_xor_enum = xor_string[: len(string)]

        for index_num, val in enumerate(string):
            result_string += chr(ord(val) ^ ord(match_len_for_xor_enum[index_num]))
        return result_string

# %%
#######################################
def sort_by_multiple_indexes_granular_reverse(lst: list, reverse_age_not_job=False):
    """Demo of how to reverse one column but ensuring the other column is not reversed during the sort

    Examples:
        >>> mylst = [['Nick', 30, 'Doctor'], ['John', 8, 'Student'], ['Paul', 22, 'Car Dealer'], ['Mark', 66, 'Retired'], ['Yolo', 22, 'Student'], ['Mark', 66, 'Doctor']]\n

        >>> sort_by_multiple_indexes_granular_reverse(mylst)\n
        [['Mark', 66, 'Retired'], ['Mark', 66, 'Doctor'], ['Nick', 30, 'Doctor'], ['Paul', 22, 'Car Dealer'], ['Yolo', 22, 'Student'], ['John', 8, 'Student']]

        >>> sort_by_multiple_indexes_granular_reverse(mylst, reverse_age_not_job=True)\n
        [['Mark', 66, 'Doctor'], ['Mark', 66, 'Retired'], ['Nick', 30, 'Doctor'], ['Paul', 22, 'Car Dealer'], ['Yolo', 22, 'Student'], ['John', 8, 'Student']]

    References:
        https://stackoverflow.com/questions/14466068/sort-a-list-of-tuples-by-second-value-reverse-true-and-then-by-key-reverse-fal
        https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work
    """
    # Reverse by age, do not reverse by job title
    if reverse_age_not_job:
        return sorted(lst, key=lambda x: (-x[1], x[2]))
    else:
        # Reverse by age
        return sorted(lst, key=lambda x: (-x[1]))

# %%
#######################################
def get_files_preview(thepath=".", preview_size=40):
    """Returns a tuple containing the file name and the first 40 characters of the file for each file in a given directory. Includes gzip files. Excludes .tar files.

    Examples:
        >>> from pprint import pprint\n

        >>> pprint( previewgzipfiles() )\n
        [('misc_funcs.py', '#######################################\\n'),\n
        ('repl_tricks.py', '# %%\\n###################################'),\n
        ('test_text.txt.gz', "ok\\nso here is some\\n'blah blah'\\nWe are pl"),\n
        ('all_funcs.py', '#######################################\\n'),\n
        ('system_funcs.py', '#######################################\\n'),\n
        ('two_dimension_funcs.py', '#######################################\\n'),\n
        ('test_text.txt', "ok\\nso here is some\\n'blah blah'\\nWe are pl"),\n
        ('string_funcs.py', '#######################################\\n'),\n
        ('regex_funcs.py', '#######################################\\n'),\n
        ('lambda_and_map_examples.py', ''),\n
        ('array_funcs.py', '#######################################\\n'),\n
        ('specific_use_case_funcs.py', '#######################################\\n'),\n
        ('dict_funcs.py', '#######################################\\n'),\n
        ('file_folder_funcs.py', '#######################################\\n'),\n
        ('test.txt', "ok\\nso here is some\\n'blah blah'\\nWe are pl"),\n
        ('notes.py', '# %%\\n###################################'),\n
        ('conversion_encoding_bytes_chr_funcs.py',\n
        '#######################################\\n'),\n
        ('test_copy.txt', "ok\\nso here is some\\n'blah blah'\\nWe are pl")]

    Args:
        thepath (str, optional): Specify the directory. Defaults to ".".
        preview_size (int, optional): Specify the number of characters to preview. Defaults to 40.

    Returns:
        list: Returns a list of tuples where the 1st element is the file name, and the 2nd element is the first 40 characters of the file
    """
    import pathlib
    import gzip

    path_obj = pathlib.Path(thepath).resolve()
    results_preview = []
    for file in path_obj.glob("*"):
        if file.is_file() and ".tar" not in file.name:
            if file.name.endswith(".gz"):
                with gzip.open(file, "rt") as f:
                    preview = f.read()[:preview_size]
                results_preview.append((file.name, preview))
            else:
                results_preview.append((file.name, file.read_text()[:preview_size]))

    return results_preview


previewfiles = get_files_preview

# %%
#######################################
def oneliner_ifelse_demo():
    """This code demonstrates how to successfully implement a one-liner if/else statement

    Examples:
        >>> mystring = 'Complex is better than complicated.'\n
        >>> secondstring = ' blah '\n
        >>> bigger_string = mystring if mystring > secondstring else secondstring\n
        >>> bigger_string\n
        'Complex is better than complicated.'

    References:
        One liner if/else: https://youtu.be/MHlwl6GsT8s?t=990
    """
    demo_string = """
    >>> mystring = 'Complex is better than complicated.'
    >>> secondstring = ' blah '
    >>> bigger_string = mystring if mystring > secondstring else secondstring
    >>> bigger_string
    'Complex is better than complicated.'
    """
    print(demo_string)

# %%
#######################################
def filehandle_write(thepath: str, content: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with open(path_obj, "w") as f:
        f.write(content)


writetext = filehandle_write

# %%
#######################################
def remove_falsey_values_in_array(lst: list):
    """Removes falsey values such as 0, '', False, None from the list.

    Examples:
        >>> list_with_falsey = [0, 1, False, 2, '', ' ', 3, 'a', 's', 34, None]\n

        >>> remove_falsey_values_in_array(list_with_falsey)\n
        [1, 2, ' ', 3, 'a', 's', 34]

        >>> filter(bool, list_with_falsey)\n
        <filter object at 0x7f8d02efbd90>

        >>> list( filter(bool, list_with_falsey) )\n
        [1, 2, ' ', 3, 'a', 's', 34]
    """
    return list(filter(bool, lst))

# %%
#######################################
def new_module(source_dir: str, prepend_text=None):
    """Creates a new module file consisting of all functions that reside in a given folder.  This tool is intended to receive the path of a given folder where the individual function .py files reside, and it will retrieve the content of each of those .py files, and put all of the content together in a single file in the "modules" directory (hard-coded in this script).  The new single file will have the same name as the given "source_dir" folder + the ".py" extension.

    Reference:
        https://stackoverflow.com/questions/47518669/create-new-folder-with-pathlib-and-write-files-into-it

    Args:
        source_dir (str): Reference the path of the directory where the function .py files reside
    """
    import pathlib
    
    source_dir_pathobj = pathlib.Path(source_dir).resolve()
    if not source_dir_pathobj.is_dir():
        print('The given source_dir is not a directory.')
        exit()
    
    dest_dir_pathobj = pathlib.Path().home() / "Temp/pyplay/IMPORT_functions/Python_3.8_Tools/modules/"
    
    def new_module_header(source_dir_name: str):
        
        def format_header_block(string: str):
            """Prints a header for use with my function files

            Examples:
                #######################################\n
                ########### ARRAY FUNCTIONS ###########\n
                #######################################\n

            """
            newstring = ""
            newstring += "{0:#<39}".format("") + "\n"
            newstring += "{0:#^39}".format(f" {string} ") + "\n"
            newstring += "{0:#<39}".format("") + "\n\n"
            
            return newstring
        
        header_name = source_dir_name.replace('_', ' ').upper()
        new_header = format_header_block(header_name)
        return new_header
    
    header_content = new_module_header(source_dir_pathobj.name)
    all_funcs_content_from_source_dir = ''.join([ e.read_text() for e in source_dir_pathobj.glob('*') if e.is_file() and e.name.endswith('.py')])
    
    if prepend_text:
        full_content = header_content + prepend_text + all_funcs_content_from_source_dir
    else:
        full_content = header_content + all_funcs_content_from_source_dir
    
    new_module_name = source_dir_pathobj.name + '.py'
    
    module_filepath = dest_dir_pathobj / new_module_name
    
    with module_filepath.open('w') as f:
        f.write(full_content)

# %%
#######################################
def test_object_type(obj: object, thetype: type):
    """Tests if the given object is of the specified type.  Returns a Boolean True or False.

    Examples:
        >>> myint = 34
        >>> test_object_type(myint, int)
        True
        >>> isinstance(myint, int)
        True
        >>> test_object_type(myint, str)
        False
    """
    return isinstance(obj, thetype)

# %%
#######################################
def dict_to_tuple_list(thedict: dict):
    """Takes a Dictionary and converts the .items() into a list of tuples.

    Examples:
    >>> my_dict = {'item1': 'I am a raptor', 'item2': 'eat everything', 'item3': 'Till the appearance of man'}
    >>> my_dict.items()\n
    dict_items([('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')])
    >>> dict_to_tuple_list(my_dict)\n
    [('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')]
    >>> # This has the same effect #
    >>> list(my_dict.items())\n
    [('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')]

    Args:
        thedict (dict): Reference the dictionary

    Returns:
        list: Returns a list of tuples from the .items() method
    """
    my_tuple_list = [(k, v) for k, v in thedict.items()]
    # same as: # list(thedict.items())
    return my_tuple_list

# %%
#######################################
def decode_hex(obj: object):
    """Decodes the string / bytes string using Hexadecimal.

    Example:
        >>> encode_hex('hello')\n
        b'68656c6c6f'

        >>> encode_hex(b'hello')\n
        b'68656c6c6f'

        >>> decode_hex(b'68656c6c6f')\n
        b'hello'

        >>> decode_hex('68656c6c6f')\n
        b'hello'

        >>> [hex(ord(s)) for s in 'hello']\n
        ['0x68', '0x65', '0x6c', '0x6c', '0x6f']

        >>> ''.join([hex(ord(s)) for s in 'hello'])\n
        '0x680x650x6c0x6c0x6f'

        >>> ''.join([hex(ord(s)) for s in 'hello']).replace('0x','')\n
        '68656c6c6f'

        #######################################
        >>> data = ['6e', '75', '64', '67', '65', '20', '6e', '75', '64', '67', '65', '20', '77', '69', '6e', '6b', '20', '77', '69', '6e', '6b']\n
        >>> [decode_hex(hexa) for hexa in data]\n

        [b'n', b'u', b'd', b'g', b'e', b' ', b'n', b'u', b'd', b'g', b'e', b' ', b'w', b'i', b'n', b'k', b' ', b'w', b'i', b'n', b'k']

        >>> [decode_hex(hexa).decode() for hexa in data]\n
        ['n', 'u', 'd', 'g', 'e', ' ', 'n', 'u', 'd', 'g', 'e', ' ', 'w', 'i', 'n', 'k', ' ', 'w', 'i', 'n', 'k']

        >>> ''.join([decode_hex(hexa).decode() for hexa in data])\n
        'nudge nudge wink wink'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj
    return codecs.decode(temp_obj, "hex")

# %%
#######################################
def merge_arrays(*lsts: list):
    """Merges all arrays into one flat list.

    Examples:
        >>> lst_abc = ['a','b','c']\n
        >>> lst_123 = [1,2,3]\n
        >>> lst_names = ['John','Alice','Bob']\n
        >>> merge_arrays(lst_abc,lst_123,lst_names)\n
        ['a', 'b', 'c', 1, 2, 3, 'John', 'Alice', 'Bob']
    """
    merged_list = []
    [merged_list.extend(e) for e in lsts]
    return merged_list

# %%
#######################################
def find_nth_occurrence(thestring: str or bytes, pattern: str or bytes, occur_wanted=None, context=50):
    import string
    
    total_found = thestring.count(pattern)
    print(f'\nThere are x number of occurrences: {total_found}\n')
    
    if total_found == 0:
        return None
    
    # If the 'occurrence wanted' is not specified, prompt the user for it
    if not occur_wanted:
        occur_wanted = input('Enter in the number of the occurrence you want (e.g. for the 4th occurrence input the number 4) :  ')

    # We need to get the length of the pattern we are trying to match
    multiplier = len(pattern)
    
    # Our default replacement_character is '~', however if that character exists in the 'pattern' we are searching for, we will choose another ascii character that is NOT in the 'pattern'
    # We have two ways for the evaluation, one is for a 'bytes' string and the other a 'str' object
    if isinstance(pattern, bytes):
        if b'~' in pattern:
            my_ascii_chars = string.printable[:-5]
            for item in my_ascii_chars:
                if item.encode() not in pattern:
                    replacement_character = item.encode()
                    break
        else:
            replacement_character = b'~'
    elif isinstance(pattern, str):
        if '~' in pattern:
            my_ascii_chars = string.printable[:-5]
            for item in my_ascii_chars:
                if item not in pattern:
                    replacement_character = item
                    break
        else:
            replacement_character = '~'
        
    the_replacement_string = replacement_character * multiplier
    
    index_loc = thestring.replace(pattern, the_replacement_string, occur_wanted - 1).index(pattern)
    
    # The context parameter has a default value of 50, but this can be changed
    return thestring[index_loc:index_loc + context]

# %%
#######################################
def format_with_numbers(*vars: str):
    """This is a demo exercise of using format() with numbered {} in order to insert variables into the string.

    Examples:
        >>> format_with_numbers('hi','there','fella')\n
        hi there fella\n
        ['hi', 'there', 'fella']\n
        'blah hi blah there blah fella'

        >>> format_with_numbers('hi')\n
        hi\n
        ['hi']\n
        'blah hi blah default2 blah default3'

        >>> format_with_numbers('hi','there','fella','David')\n
        hi there fella David\n
        ['hi', 'there', 'fella', 'David']\n
        'blah hi blah there blah fella'
    """
    print(*vars)
    list_of_vars = [*vars]
    print([*vars])
    if len(list_of_vars) < 3:
        while len(list_of_vars) < 3:
            number = len(list_of_vars)
            list_of_vars.append("default" + str(number + 1))
    return "blah {2} blah {0} blah {1}".format(*list_of_vars)

# %%
#######################################
def encode_base64(obj: object, no_newline=False):
    """Encodes the string / bytes string using BASE64.

    Example:
        >>> encode_base64('hello')\n
        b'aGVsbG8=\\n'
        >>> encode_base64('hello', no_newline=True)\n
        b'aGVsbG8='
        >>> encode_base64('hello', True)\n
        b'aGVsbG8='
        >>>
        >>> decode_base64(b'aGVsbG8=\\n')\n
        b'hello'
        >>> decode_base64(b'aGVsbG8=')\n
        b'hello'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj

    if no_newline:
        result = codecs.encode(temp_obj, "base64")
        result = result.decode().rstrip("\n")
        result = result.encode()
    else:
        result = codecs.encode(temp_obj, "base64")
    return result

# %%
#######################################
def get_size_in_bytes(string: str):
    """Takes a given string and return the number of bytes used for all of the glyphs in the string.

    Examples:
        >>> shrug = r'¯\_(ツ)_/¯'\n
        >>> get_size_in_bytes(shrug)\n
        13
        >>> shrug.encode()\n
        b'\xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf'
        >>> shrug.encode('utf-8')\n
        b'\xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf'
        >>> shrug.encode('utf8')\n
        b'\xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf'
        >>> shrug.encode('utf-16')\n
        b'\xff\xfe\xaf\x00\\\x00_\x00(\x00\xc40)\x00_\x00/\x00\xaf\x00'
        >>>
        >>> len(shrug.encode())\n
        13
    """
    return len(string.encode())

# %%
#######################################
def bitwise_compliment_comparison(num: int):
    """Prints a comparison table of the number, its complement (the num * -1), and the

    Args:
        num (int): [description]

    Returns:
        [type]: [description]
    """
    from pprint import pprint

    dict1 = {}
    dict1["num_orig"] = (num, format(num, "08b"))
    dict1["num_neg"] = (num * -1, format(num * -1, "08b"))
    dict1["bitcomp"] = (~num, format(~num, "08b"))
    pprint(list(dict1.items()))

# %%
#######################################
def encode_rot13(string: str):
    """Encodes the string using ROT-13.

    Example:
        >>> encode_rot13('hello')\n
        'uryyb'
        >>> decode_rot13('uryyb')\n
        'hello'
    """
    import codecs

    return codecs.encode(string, "rot13")

# %%
#######################################
def get_current_python_version():
    """Returns the version of the python interpreter that is currently in use.

    Examples:
        >>> get_current_python_version()\n
        '3.8.5 (default, May 27 2021, 13:30:53) \\n[GCC 9.3.0]'
    """
    import sys

    return sys.version

# %%
#######################################
def get_parent_paths_seq_list(thepath="."):
    """Returns a list containing the absolute path of each parent.

    Examples:
        >>> get_parent_paths_seq_list()\n
        [PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs'),\n
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions'),\n
        PosixPath('/home/pengwin/Temp/pyplay'),\n
        PosixPath('/home/pengwin/Temp'),\n
        PosixPath('/home/pengwin'),\n
        PosixPath('/home'),\n
        PosixPath('/')]

    Args:
        thepath (str, optional): Specify the path you want to work with. Defaults to '.'.

    Returns:
        list: Returns a list of results
    """
    import pathlib

    return [p for p in pathlib.Path(thepath).absolute().parents]

# %%
#######################################
def os_cwd():
    """Returns the pathlib object for the current working directory

    Examples:
        >>> os_cwd()\n
        '/home/cooluser/pyplay'
    """
    import os

    return os.getcwd()

# %%
#######################################
def replace_numbers_randomly(obj: str or list):
    """Takes a string of digits or a list of string digits and randomly replaces the string with one of equivalent length but different numbers.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> replace_numbers_randomly('8284689631238')\n
        '2236569931001'

        >>> ##### EXAMPLE 2 #####
        >>> list1 = [
        ...     "353",
        ...     "1618285621506",
        ...     "182711621994",
        ...     "1984",
        ...     "688",
        ...     "4991999",
        ...     "185235691716215851336",
        ...     "14363109411127",
        ...     "14113473",
        ...     "278",
        ... ]

        >>> replace_numbers_randomly(list1)\n
        ['731', '3033930836685', '080458221787', '3767', '791', '9974556', '315271283413189987341', '15505063779172', '73258455', '959']

        >>> replace_numbers_randomly(list1)\n
        ['667', '0195643349706', '653864267435', '8832', '461', '5559864', '284670753127581954314', '78844299667563', '51693294', '775']

        >>> ##### EXAMPLE 3 #####
        >>> text = '''Some of the numbers like 15598429414244 or even 23
        ... have an opportunity to be changed.  Something like 311724444
        ... does as well'''

        >>> replace_numbers_randomly(text)\n
        'Some of the numbers like 81284747012392 or even 00\\nhave an opportunity to be changed.  Something like 239203568\\ndoes as well'

        >>> text\n
        'Some of the numbers like 15598429414244 or even 23\\nhave an opportunity to be changed.  Something like 311724444\\ndoes as well'


    Args:
        obj (object): Reference either a string of digits or a list of string digits

    Returns:
        object: Returns a new string or a new list of strings
    """
    import re
    import random

    if isinstance(obj, str):

        try:

            # We match on each consecutive string of digits
            match_list = re.findall(r"\d+", obj)

            replacement_list = []
            for eachitem in match_list:

                ### FIRST, WE CREATE A BIG STRING OF RANDOM DIGITS ###
                # The elements will be integers ranging from 1 to 100
                lst = list(range(1, 101))

                # From the "lst" of numbers 1 - 100, there will be multiple random choices, the quantity of which is based off of the number given to "k="
                random_list_of_ints = random.choices(lst, k=420)

                # Then we take that list of random numbers and join them together making one long string of digits
                rand_num_string = "".join([str(e) for e in random_list_of_ints])

                ### THEN, WE USE THAT RANDOM STRING OF DIGITS IN OUR SUBSTITUTION ###
                # We then take the length of the match and use that integer value as the ending point of our slice into the rand_num_string
                # Finally that slice is reversed and then it is used for the substitution, and then added to the replacement_list
                replacement_list.append(
                    re.sub(
                        r"\d+",
                        lambda x: rand_num_string[: len(x.group(0))][::-1],
                        eachitem,
                    )
                )

            # We create a list of 2 element tuples - the 1st element is the match, the 2nd is the replacement
            find_and_replace_list = [
                (e[1], replacement_list[e[0]]) for e in enumerate(match_list)
            ]

            # Then we iterate over the find/replace list and replace the first occurrence in the string
            for item in find_and_replace_list:
                obj = obj.replace(item[0], item[1], 1)

            result = obj

        except Exception as e:
            print(f"Received the following error: {e}")

    elif isinstance(obj, list):
        result = [replace_numbers_randomly(e) for e in obj]

    return result

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

# %%
#######################################
def ls(thepath='.', recurse=False):
    import pathlib
    
    path_obj = pathlib.Path(thepath).resolve()
    if recurse:
        results = [e.as_posix() for e in path_obj.rglob('*')]
    else:
        results = [e.name for e in path_obj.glob('*')]
    return results

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

# %%
#######################################
def format_header_block(string: str):
    """Prints a header for use with my function files

    Examples:
        #######################################\n
        ########### ARRAY FUNCTIONS ###########\n
        #######################################\n
    """
    newstring = ""
    newstring += "{0:#<39}".format("") + "\n"
    newstring += "{0:#^39}".format(f" {string} ") + "\n"
    newstring += "{0:#<39}".format("") + "\n\n"
    print(newstring)

# %%
#######################################
def dict_creation_demo():
    print(
        "We can convert a list of tuples into Dictionary Items: dict( [('key1','val1'), ('key2', 'val2')] "
    )
    was_tuple = dict([("key1", "val1"), ("key2", "val2")])
    print(f"This was a list of Tuples: {was_tuple}\n")
    print(
        "We can convert a list of lists into Dictionary Items: dict( [['key1','val1'], ['key2', 'val2']] "
    )
    was_list = dict([["key1", "val1"], ["key2", "val2"]])
    print(f"This was a list of Lists: {was_list} ")

# %%
#######################################
def encode_bz2(obj: object):
    """Encodes the string / bytes string using BZ2.

    Example:
        >>> encode_bz2('hello')\n
        b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80'

        >>> encode_bz2(b'hello')\n
        b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80'

        >>> decode_bz2(b'BZh91AY&SY\x191e=\x00\x00\x00\x81\x00\x02D\xa0\x00!\x9ah3M\x073\x8b\xb9"\x9c(H\x0c\x98\xb2\x9e\x80')\n
        b'hello'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj

    result = codecs.encode(temp_obj, "bz2")
    return result

# %%
#######################################
def invoke_lambda_demo(*args):
    """Demo of a stand-alone way of using lambda

    Examples:
        >>> invoke_lambda_demo(10, 25, 'blah')\n
        Here is what is happening:
        (lambda x: x + x)(item)

        [20, 50, 'blahblah']

    Returns:
        object: Returns double of the given argument.
    """
    print("Here is what is happening:")
    print("  (lambda x: x + x)(item)")
    print("")
    results = []
    for item in args:
        results.append((lambda x: x + x)(item))
    return results

# %%
#######################################
def new_random_wordslist(listsize=10):
    """Returns a list of random words.  The default size of the list is 10, but this can be modified with the "listsize" parameter.

    Args:
        listsize (int, optional): Specify the desired length of the list. Defaults to 10.

    Returns:
        list: Returns a list of words.
    """
    import random
    word_file = "/usr/share/dict/words"
    with open(word_file) as f:
        content = f.readlines()
        results_list = random.choices(content, k=listsize)
        results_list = [w.strip() for w in results_list] # Removes the trailing '\n' line feed character
        return results_list

# %%
#######################################
def reverse_first_half(string: str):
    """Reverse the first half of a given string.

    Examples:
        >>> reverse_first_half('sandwich')\n
        'dnaswich'
    """
    halfway_point = len(string) // 2
    first_half_reversed = string[:halfway_point][::-1]
    last_half = string[halfway_point:]
    return first_half_reversed + last_half

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
def bit_shifter(num: int, shiftright: int):
    """Shifts the bits of the given number (int) by the designated number (int) given to the "shiftright" parameter.

    Examples:
        >>> bit_shifter(151, 4)\n
        9
        >>> bin(151)\n
        '0b10010111'
        >>> bin(151 >> 1)\n
        '0b1001011'
        >>> bin(151 >> 2)\n
        '0b100101'
        >>> bin(151 >> 3)\n
        '0b10010'
        >>> bin(151 >> 4)\n
        '0b1001'
        >>> int('0b1001', 2)\n
        9
        >>> format(151, '08b')\n
        '10010111'
        >>> format(151 >> 4, '04b')\n
        '1001'
        >>> int('1001', 2)\n
        9
    """
    return num >> shiftright

# %%
#######################################
def get_unique(thelist: list):
    """Takes a list containing duplicates and returns a list of unique elements only.

    Example:
        >>> myduplicates\n
        ['Bartók', 'vigilant', 'vigilant', 'Julianne', 'Julianne', 'Julianne', 'camera', 'camera', 'camera', "Espinoza's", "Espinoza's", 'Amgen', 'Amgen', 'Amgen', "Tomlin's", 'tenuring', 'encroached', 'encroached', 'laxatives', 'laxatives', 'laxatives']

        >>> get_unique(myduplicates)\n
        ['Bartók', 'vigilant', 'Julianne', 'camera', "Espinoza's", 'Amgen', "Tomlin's", 'tenuring', 'encroached', 'laxatives']

    Args:
        thelist (list): Reference an existing list.

    Returns:
        list: Returns a list of unique values.
    """
    temp_dict = {}
    for item in thelist:
        temp_dict[item] = "the value doesn't matter, we want the key"
    results_list = list(temp_dict.keys())  #  Any duplicate "item"/"key" was overwritten, so the new list contains unique elements only
    return results_list

# %%
#######################################
def remove_file(filepath: str or list):
    """Removes the specified file.

    References:
        https://stackoverflow.com/questions/42636018/python-difference-between-os-remove-and-os-unlink-and-which-one-to-use

    Args:
        filepath (str): Specify the path of the file
    """
    import pathlib

    if isinstance(filepath, str):
        path_obj = pathlib.Path(filepath).resolve()
        if path_obj.is_file():
            path_obj.unlink()
    elif isinstance(filepath, list):
        for eachitem in filepath:
            path_obj = pathlib.Path(eachitem).resolve()
            if path_obj.is_file():
                path_obj.unlink()


rm = remove_file

# %%
#######################################
def get_object_memory_usage(obj: object):
    """Calculates the size of the object, stored in memory, in bytes.

    Examples:
        >>> myvar = 30\n
        >>> get_object_memory_usage(myvar)\n
        28
        >>> shrug = r'¯\_(ツ)_/¯'\n
        >>> get_object_memory_usage(shrug)\n
        92

    References:
        https://docs.python.org/3/library/sys.html#sys.getsizeof
    """
    import sys

    return sys.getsizeof(obj)

# %%
#######################################
def refindall(thepattern: str, obj: str or list, context=(0, (0, 0))[0], ignorecase=True):
    """Given the object (such as a string or an array of strings), this function will search for thepattern in the object. If context is set, this function will return the number of characters before and after the match as specified by the "context" number.

    Examples:
        >>> text = '''
        ... We spent several years building our own database engine,
        ... Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
        ... service with the same or better durability and availability as
        ... the commercial engines, but at one-tenth of the cost. We were
        ... not surprised when this worked.
        ... '''

        >>> # Find exact matches:
        >>> refindall('sql', text)\n
        ['SQL', 'SQL']

        >>> # Find 25 characters before and after the match
        >>> refindall('sql', text, 25)\n
        ['urora, a fully-managed MySQL and PostgreSQL-compatibl']

        >>> # Do a "Greedy" match - this grabs the whole line where the match occurs
        >>> refindall('.*sql.*', text)\n
        ['Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible']

        >>> # Do a "Non-Greedy" match - this creates a separate element for each match on this single line
        >>> refindall('.*?sql.*?', text)\n
        ['Amazon Aurora, a fully-managed MySQL', ' and PostgreSQL']

        >>> # Here we take our example text and create an array of strings
        >>> text.splitlines()\n
        ['', 'We spent several years building our own database engine,', 'Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible', 'service with the same or better durability and availability as', 'the commercial engines, but at one-tenth of the cost. We were', 'not surprised when this worked.']

        >>> # Now each element in the array is evaluated with the match criteria, in this case we are getting the 5 characters before and after the match
        >>> refindall('the', text.splitlines(), 5)\n
        ['with the same', 'h of the cost']

        >>> # Here we are grabbing the whole element where the match occurs in the array
        >>> refindall('.*the.*', text.splitlines())\n
        ['service with the same or better durability and availability as', 'the commercial engines, but at one-tenth of the cost. We were']

    References:
        https://github.com/finxter/PythonOneLiners/blob/master/book/python_tricks/one_liner_05.py
    """
    import re

    if isinstance(context, int):
        left_context = str(context)
        right_context = str(context)
    elif isinstance(context, tuple):
        left, right = context
        left_context = str(left)
        right_context = str(right)

    if ignorecase:
        match_syntax = re.compile(
            r"(.{" + left_context + r"}" + thepattern + r".{" + right_context + r"})",
            re.IGNORECASE,
        )
    else:
        match_syntax = re.compile(
            r"(.{" + left_context + r"}" + thepattern + r".{" + right_context + r"})"
        )

    if isinstance(obj, str):
        result = re.findall(match_syntax, obj)
    elif isinstance(obj, list):
        result = [refindall(e) for e in obj]

    return result

# %%
#######################################
def zip_arrays(lst: list, *lsts: list):
    """Takes two or more lists and zips them together, returning a list of tuples.

    Examples:
        >>> lst_abc = ['a','b','c']\n
        >>> lst_123 = [1,2,3]\n
        >>> lst_names = ['John','Alice','Bob']\n
        >>> zip_arrays(lst_abc, lst_123, lst_names)\n
        [('a', 1, 'John'), ('b', 2, 'Alice'), ('c', 3, 'Bob')]
    """
    return list(zip(lst, *lsts))

# %%
#######################################
def access_nested_dict(thedict: dict):
    """Demo of how to access a nested dictionary with a two dictionary comprehensions

    Examples:
        >>> a_dictionary = {
        ...     "1-2017": {
        ...         "Win7": "0.47",
        ...         "Vista": "0.2",
        ...         "NT*": "0.09",
        ...         "WinXP": "0.06",
        ...         "Linux": "0.17",
        ...         "Mac": "0.04",
        ...         "Mobile": "0.26",
        ...     },
        ...     "2-2017": {
        ...         "Win7": "0.48",
        ...         "Vista": "0.28",
        ...         "NT*": "0.07",
        ...         "WinXP": "0.09",
        ...         "Linux": "0.16",
        ...         "Mac": "0.03",
        ...         "Mobile": "0.27",
        ...     },
        ...     "3-2017": {
        ...         "Win7": "0.41",
        ...         "Vista": "0.25",
        ...         "NT*": "0.05",
        ...         "WinXP": "0.05",
        ...         "Linux": "0.1",
        ...         "Mac": "0.04",
        ...         "Mobile": "0.27",
        ...     },
        ... }

        >>> access_nested_dict(a_dictionary)\n
        {'1-2017': {('NT*', '0.09'), ('Vista', '0.2'), ('WinXP', '0.06')},
        '2-2017': {('NT*', '0.07'), ('Vista', '0.28'), ('WinXP', '0.09')},
        '3-2017': {('NT*', '0.05'), ('Vista', '0.25'), ('WinXP', '0.05')}}

    References:
        https://stackoverflow.com/questions/17915117/nested-dictionary-comprehension-python
    """
    comprehension = {
        outer_k: {
            (inner_k, inner_v)
            for inner_k, inner_v in outer_v.items()
            if inner_k in ["Vista", "NT*", "WinXP"]
        }
        for outer_k, outer_v in thedict.items()
    }
    return comprehension

# %%
#######################################
def gzip_file(thepath: str, gzip_name=None):
    """Create a compressed version of a given file.

    References:
        This was where I got the basic code for this function
        https://stackoverflow.com/questions/8156707/gzip-a-file-in-python

    Args:
        thepath (str): Reference the file to gzip compress
        gzip_name (str, optional): Use this if you want to the name of the compressed file to be something other than "filename.gz". Defaults to None.
    """
    import gzip

    if gzip_name:
        pass
    else:
        gzip_name = f"{thepath}.gz"

    with open(thepath, "rb") as f_in, gzip.open(gzip_name, "wb") as f_out:
        f_out.writelines(f_in)

# %%
#######################################
def rename_file(thepath: str, newname: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    target = pathlib.Path(newname)
    path_obj.rename(target)

# %%
#######################################
def dict_iterator(thedict: dict):
    """Iterates over the values in a given dictionary.

    Example:
        >>> sessions_pcap = rdpcap('sessions.pcap')\n
        >>> dict_iterator( sessions_pcap.sessions() )\n
        (0, <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>)
        (1, <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>)
        (2, <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>)
        (3, <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>)

    Args:
        thedict (dict): Reference an existing dict object
    """
    counter = 0
    for eachkey in thedict.keys():
        print( (counter, thedict[eachkey]) )
        counter += 1

# %%
#######################################
def get_ls(thepath=".", names=False, stringoutput=False, recurse=False):
    """Displays directory contents of a directory.

    Examples:
        >>> get_ls()\n
        [PosixPath('/home/pengin/worksheet_dir/__pycache__'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_match_str_len_with_padding.py'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_name_eq_main_demo.py'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_pathlib.py'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_sets.py'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_where_like.py'),\n
        PosixPath('/home/pengin/worksheet_dir/worksheet_xor_strings.py')]

        >>> get_ls('.', stringoutput=True)\n
        ['/home/pengin/worksheet_dir/__pycache__',\n
        '/home/pengin/worksheet_dir/worksheet_match_str_len_with_padding.py',\n
        '/home/pengin/worksheet_dir/worksheet_name_eq_main_demo.py',\n
        '/home/pengin/worksheet_dir/worksheet_pathlib.py',\n
        '/home/pengin/worksheet_dir/worksheet_sets.py',\n
        '/home/pengin/worksheet_dir/worksheet_where_like.py',\n
        '/home/pengin/worksheet_dir/worksheet_xor_strings.py']

        >>> get_ls(names=True)\n
        ['__pycache__', 'worksheet_match_str_len_with_padding.py', 'worksheet_name_eq_main_demo.py', 'worksheet_pathlib.py', 'worksheet_sets.py', 'worksheet_where_like.py', 'worksheet_xor_strings.py']

    Args:
        thepath (str, optional): Specify the path. Defaults to ".".
        names (bool, optional): Use this to output the name only and not the full path. Defaults to False.
        stringoutput (bool, optional): Use this to output the file/folder objects as string objects. Defaults to False.


    Returns:
        list: Returns an array of the directory contents.
    """
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    if recurse:
        myglob = path_obj.rglob("*")
    else:
        myglob = path_obj.glob("*")

    if stringoutput:
        contents = sorted([str(obj) for obj in myglob])
    else:
        contents = sorted([obj for obj in myglob])

    if names:
        contents = [str(e).split("/")[-1] for e in contents]

    return contents

# %%
#######################################
def filehandle_readbytes(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with open(path_obj, "rb") as f:
        content = f.read()

    return content


readbytes = filehandle_readbytes

# %%
#######################################
def get_file_stats(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    file_stats = path_obj.stat()
    return file_stats

# %%
#######################################
def convert_bytes2string(thebytes: bytes):
    """Converts a "bytes" type object into a "str" type object

    Examples:
        >>> convert_bytes2string(b'nice string')\n
        'nice string'
    """
    return thebytes.decode()

# %%
#######################################
def display_binary_8bit(num: int):
    """Displays the binary string representation for a given integer.  If the number is within 4 bits, the output will be 8 binary digits (left padded with four 0s); if the number is 8 bits then 8 binary digits will be the output.

    Examples:
        >>> display_binary_8bit(151)\n
        '10010111'

        >>> bin(151)\n
        '0b10010111'

        >>> display_binary_8bit(11)\n
        '00001011'
    """
    return format(num, "08b")

# %%
#######################################
def refindall_content_between_patterns(obj: str or list, left_pattern: str, right_pattern: str, ignorecase=True):
    """Takes a given string or a list of strings, along with a left_pattern and right_pattern, and returns the substring that exists between the two patterns.
    
    The default search is case-insensitive, but this can be modified by specifying "ignorecase=False".

    Examples:
        >>> thestring = 'client 90.176.170.125#64983: query: www.coolhostname0010968.com IN,client 165.55.134.210#32688: query: www.coolhostname9594644.com IN,client 194.179.58.197#32424: query: www.coolhostname3977824.com IN'\n

        >>> client_ip = refindall_content_between_patterns(thestring, 'client ', '#')\n
        >>> client_ip\n
        ['90.176.170.125', '165.55.134.210', '194.179.58.197']

        >>> dns_query = refindall_content_between_patterns(thestring, 'query: ', ' IN', ignorecase=False)\n
        >>> dns_query\n
        ['www.coolhostname0010968.com', 'www.coolhostname9594644.com', 'www.coolhostname3977824.com']

    Args:
        left_pattern (str): Specify the pattern on the left
        right_pattern (str): Specify a right_pattern delimiter
        obj (object): Reference a string or a list of strings
        ignorecase (bool, optional): Allows the string search to be case-sensitive or case-insensitive. Defaults to True.

    Returns:
        object: Returns the substring or list of substrings between the two delimiters
    """
    import re

    if ignorecase:
        match_syntax = re.compile(left_pattern + r"(.*?)" + right_pattern, re.IGNORECASE)
    else:
        match_syntax = re.compile(left_pattern + r"(.*?)" + right_pattern)

    if isinstance(obj, str):
        result = re.findall(match_syntax, obj)
    elif isinstance(obj, list):
        result = [refindall_content_between_patterns(e) for e in obj]

    return result

# %%
#######################################
def os_ls(thepath="."):
    """Displays the content of the given directory.  Default value is the current directory.

    Examples:
        >>> os_ls()\n
        ['temp.py', 'worksheet.py']

        >>> os_ls('../..')\n
        ['ps1_files', 'sec_ops', 'pyplay', 'bashplay']
    """
    import os

    return os.listdir(thepath)

# %%
#######################################
def ungzip_file(thepath: str, out_filename=None):
    import gzip

    if out_filename:
        pass
    else:
        out_filename = thepath.replace(".gz", "")

    with gzip.open(thepath, "rt") as f_in, open(out_filename, "w") as f_out:
        f_out.writelines(f_in)

# %%
#######################################
def format_with_braces(*vars: str):
    """This is a demo exercise of using format() with positional {} in order to insert variables into the string.

    Examples:
        >>> format_with_braces('hi','there','fella')\n
        hi there fella\n
        ['hi', 'there', 'fella']\n
        'blah hi blah there blah fella'

        >>> format_with_braces('hi')\n
        hi\n
        ['hi']\n
        'blah hi blah default2 blah default3'

        >>> format_with_braces('hi','there','fella','David')\n
        hi there fella David\n
        ['hi', 'there', 'fella', 'David']\n
        'blah hi blah there blah fella'
    """
    print(*vars)
    list_of_vars = [*vars]
    print([*vars])
    if len(list_of_vars) < 3:
        while len(list_of_vars) < 3:
            number = len(list_of_vars)
            list_of_vars.append("default" + str(number + 1))
    return "blah {} blah {} blah {}".format(*list_of_vars)

# %%
#######################################
def get_cwd(stringoutput=False):
    """Returns the pathlib object for the current working directory

    Examples:
        >>> get_cwd()\n
        '/home/cooluser/pyplay'

    References:
        https://realpython.com/python-pathlib/
    """
    import pathlib

    result = pathlib.Path.cwd().as_posix()
    return result


pwd = get_cwd

# %%
#######################################
def split_string(string: str, size: int):
    """Splits a string into smaller strings of the desired size value.

    Examples:
    >>> string = 'hey hey hiya'\n
    >>> split_string(string, 4)\n
    ['hey ', 'hey ', 'hiya']

    References:
        https://youtu.be/pG3L2Ojh1UE?t=336
    """
    created_step_points = range(0, len(string), size)
    sublists_created = [string[i : i + size] for i in created_step_points]
    return sublists_created

# %%
#######################################
def find_strings_largerthan(string: str, size: int):
    """Returns a list of strings that are larger than the size specified.

    Examples:
        >>> text = 'It is a way I have of driving off the spleen, and regulating the circulation. - Moby'\n
        >>> find_strings_largerthan(text, 4)\n
        ['driving', 'spleen,', 'regulating', 'circulation.']
    """
    result_list = [e for e in string.split() if len(e) > size]
    return result_list

# %%
#######################################
def remove_directory(thepath: str, force=False):
    """Removes a directory.  If the directory has contents, use force=True to recursively delete the children and delete the parent.

    Examples:
        >>> get_dirs(names=True)\n
        ['__pycache__', 'copy_test_dir', 'push_bitbucket_dir', 'test_copy_of_a_directory', 'worksheet_dir']

        >>> remove_directory('test_copy_of_a_directory', force=True)\n
        >>> get_dirs(names=True)\n
        ['__pycache__', 'copy_test_dir', 'push_bitbucket_dir', 'worksheet_dir']

    References:
        https://stackoverflow.com/questions/50186904/pathlib-recursively-remove-directory

    Args:
        thepath (str): Specify the path
        force (bool, optional): Allows for a recursive delete. Defaults to False.
    """
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    if force:
        for child in path_obj.rglob("*"):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                remove_directory(child, force=True)
        path_obj.rmdir()
    else:
        path_obj.rmdir()


rmdir = remove_directory

# %%
#######################################
def sort_dict_by_key(dict1: dict, reverse=False):
    """For a given dictionary, returns a sorted list of tuples for each item based on the value.

    Examples:
        >>> employees = {'Alice' : 100000,
        ...              'Bob' : 99817,
        ...              'Carol' : 122908,
        ...              'Frank' : 88123,
        ...              'Eve' : 93121}

        >>> sort_dict_by_key(employees)\n
        [('Alice', 100000), ('Bob', 99817), ('Carol', 122908), ('Eve', 93121), ('Frank', 88123)]
        >>>
        >>> sort_dict_by_key(employees, reverse=True)\n
        [('Frank', 88123), ('Eve', 93121), ('Carol', 122908), ('Bob', 99817), ('Alice', 100000)]
    """
    if reverse:
        return sorted(dict1.items(), reverse=True)
    else:
        return sorted(dict1.items())

# %%
#######################################
def replace_numbers_reversed(obj: str or list):
    """Takes a group of string digits and reverses their order in place.

    Examples:
        >>> replace_numbers_reversed('1984')\n
        '4891'

        >>> from pprint import pprint

        >>> list1 = ['353',
        ...  '1618285621506',
        ...  '182711621994',
        ...  '1984',
        ...  '688',
        ...  '4991999',
        ...  '185235691716215851336',
        ...  '14363109411127',
        ...  '14113473',
        ...  '278']

        >>> test = replace_numbers_reversed(list1)
        >>> pprint(test)\n
        ['353',\n
        '6051265828161',\n
        '499126117281',\n
        '4891',\n
        '886',\n
        '9991994',\n
        '633158512617196532581',\n
        '72111490136341',\n
        '37431141',\n
        '872']

    Args:
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a string with reversed digits, or a list of strings with reversed digits
    """
    import re

    if isinstance(obj, str):
        result = re.sub(r"\d+", lambda x: x.group(0)[::-1], obj)
    elif isinstance(obj, list):
        result = [replace_numbers_reversed(e) for e in obj]

    return result

# %%
#######################################
def compress_archive(
    thepath: str,
    arch_format=("bztar", "gztar", "tar", "xztar", "zip")[1],
    arch_name=None,
):
    """Creates an archive of a given directory.

    Examples:
        >>> [e for e in ls(names=True) if e.startswith('work')]\n
        ['worksheet_dir']
        >>> compress_archive('worksheet_dir')\n
        >>> [e for e in ls(names=True) if e.startswith('work')]\n
        ['worksheet_dir', 'worksheet_dir.tar.gz']
        >>> compress_archive('worksheet_dir','tar')\n
        >>> [e for e in ls(names=True) if e.startswith('work')]\n
        ['worksheet_dir', 'worksheet_dir.tar', 'worksheet_dir.tar.gz'

    References:
        Using sys.exit() to exit a function if a certain condition occurs
        https://stackoverflow.com/questions/6190776/what-is-the-best-way-to-exit-a-function-which-has-no-return-value-in-python-be

        shutil Archive operations
        https://docs.python.org/3/library/shutil.html#archiving-operations

        Using shutil.make_archive()
        https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory-in-python

        Using shutil.unpack_archive()
        https://stackoverflow.com/questions/3451111/unzipping-files-in-python

        Diff between tar and zip
        https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip

        Diff between .tar, .gz, .zip, .tar.gz
        https://www.quora.com/What-is-the-difference-between-tar-gz-zip-and-tar-gz-in-Linux?share=1

        Other...
        https://stackoverflow.com/questions/3874837/how-do-i-compress-a-folder-with-the-python-gzip-module


    Args:
        thepath (str): Reference the directory you want to archive
        arch_format (str, optional): Use this to specify what archive format to use. Defaults to 'gztar' or .tar.gz as shown here - ("bztar", "gztar", "tar", "xztar", "zip")[1].
        arch_name (str, optional): Use this if you want a different name than what what is produced by "shutil.make_archive()". Defaults to None.
    """
    import pathlib
    import shutil

    # import sys

    path_obj = pathlib.Path(thepath).resolve()

    # shutil.get_archive_formats()
    # shutil.get_unpack_formats()
    archive_lookup_table = {
        "bztar": [".tar.bz2", ".tbz2"],
        "gztar": [".tar.gz", ".tgz"],
        "tar": [".tar"],
        "xztar": [".tar.xz", ".txz"],
        "zip": [".zip"],
    }

    if arch_format in archive_lookup_table:
        # extension = archive_lookup_table.get(arch_format)
        archive_type = arch_format
    else:
        print(
            'The "arch_format" must be one of the following: ("bztar", "gztar", "tar", "xztar", "zip")'
        )
        return None
        # sys.exit(
        #     'The "arch_format" must be one of the following: ("bztar", "gztar", "tar", "xztar", "zip")'
        # )

    if arch_name:
        pass
    else:
        # arch_name = pathlib.Path(path_obj.name + extension)
        arch_name = path_obj

    # shutil.make_archive(path_obj, extension, arch_name)
    shutil.make_archive(arch_name, archive_type, path_obj)

# %%
# #######################################
def expand_archive(
    thepath: str,
    extract_dir=None,
    arch_format=("auto", "bztar", "gztar", "tar", "xztar", "zip")[0],
):
    """Extracts the contents of a given archive

    Examples:
        >>> ls(names=True)\n
        ['worksheet_dir.tar', 'worksheet_dir.tar.gz']

        >>> expand_archive('worksheet_dir.tar.gz','worksheet_dir')\n

        >>> ls(names=True)\n
        ['worksheet_dir', 'worksheet_dir.tar', 'worksheet_dir.tar.gz']

        >>> ls('worksheet_dir',names=True)\n
        ['__pycache__', 'worksheet_match_str_len_with_padding.py', 'worksheet_name_eq_main_demo.py', 'worksheet_pathlib.py', 'worksheet_sets.py', 'worksheet_where_like.py', 'worksheet_xor_strings.py']

    References:
        Using sys.exit() to exit a function if a certain condition occurs
        https://stackoverflow.com/questions/6190776/what-is-the-best-way-to-exit-a-function-which-has-no-return-value-in-python-be

        shutil Archive operations
        https://docs.python.org/3/library/shutil.html#archiving-operations

        Using shutil.make_archive()
        https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory-in-python

        Using shutil.unpack_archive()
        https://stackoverflow.com/questions/3451111/unzipping-files-in-python

        Diff between tar and zip
        https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip

        Diff between .tar, .gz, .zip, .tar.gz
        https://www.quora.com/What-is-the-difference-between-tar-gz-zip-and-tar-gz-in-Linux?share=1

        Other...
        https://stackoverflow.com/questions/3874837/how-do-i-compress-a-folder-with-the-python-gzip-module


    Args:
        thepath (str): Specify the archive you want to expand
        extract_dir (str, optional): Specify the directory to extract the files to. Defaults to None, which means that all archive contents will be extracted to the current working directory
        arch_format (str, optional): If your archive does not end with a known-extension you will want to specify the type of archive format the file is. Defaults to "auto" - meaning that the default expects the archive to end in a well-known extension - ("auto", "bztar", "gztar", "tar", "xztar", "zip")[0].

    """
    import pathlib
    import shutil

    # import sys

    path_obj = pathlib.Path(thepath).resolve()
    # shutil.get_archive_formats()
    # shutil.get_unpack_formats()
    archive_lookup_table = {
        "auto": ["use the built-in process for unpack_archive"],
        "bztar": [".tar.bz2", ".tbz2"],
        "gztar": [".tar.gz", ".tgz"],
        "tar": [".tar"],
        "xztar": [".tar.xz", ".txz"],
        "zip": [".zip"],
    }
    if arch_format == "auto":
        default_behavior = True
    elif arch_format in archive_lookup_table:
        # extension = archive_lookup_table.get(arch_format)
        archive_type = arch_format
    else:
        print(
            'The "arch_format" must be one of the following: ("bztar", "gztar", "tar", "xztar", "zip")'
        )
        return None
        # sys.exit(
        #     'The "arch_format" must be one of the following: ("bztar", "gztar", "tar", "xztar", "zip")'
        # )
    if extract_dir:
        pass
    else:
        extract_dir = "."
    if default_behavior:
        shutil.unpack_archive(path_obj, extract_dir)
    else:
        shutil.unpack_archive(path_obj, extract_dir, archive_type)

# %%
#######################################
def notlike(matchlist: list, array: list, andop=False):
    """Returns a list of non-matches in the given array by excluding each object that contains one of the values in the matchlist parameter.

    Examples:
        >>> subdir_list = ['get_random.py',
        ...  'day6_15_payload-by-port.py',
        ...  'worksheet_get_exif.py',
        ...  'worksheet_get_random.py',
        ...  'day6_19_browser-snob.py',
        ...  'day6_12_letterpassword.py',
        ...  'day6_21_exif-tag.py',
        ...  'day6_17_subprocess_ssh.py',
        ...  'day6_16._just_use_split.py']

        >>> notlike('day6',subdir_list)\n
        ['get_random.py', 'worksheet_get_exif.py', 'worksheet_get_random.py']
        >>>
        >>> notlike(['exif','_1'],subdir_list)\n
        ['get_random.py', 'worksheet_get_random.py']

    Args:
        matchlist (list): Submit one or many substrings to exclude
        array (list): This is the list that we want to filter
        andop (bool, optional): This will determine if the matchlist criteria is an "And Operation" or an "Or Operation. Defaults to False (which is the "Or Operation").  Only applies when multiple arguments are used for the "matchlist" parameter

    Returns:
        list: Returns a result list derived after the matchlist exclusions have been made

    References:
        https://stackoverflow.com/questions/469913/regular-expressions-is-there-an-and-operator
        https://stackoverflow.com/questions/3041320/regex-and-operator
        https://stackoverflow.com/questions/717644/regular-expression-that-doesnt-contain-certain-string
    """
    import re

    if isinstance(matchlist, str):
        # matchlist is a single string object
        thecompile = re.compile(rf"^(?!.*{matchlist}).*$")
        result_list = [x for x in array if re.findall(thecompile, x)]
        return result_list
    else:
        if andop:
            # We will be doing an "AND" match or an "And" "Operation"
            match_string = r"(?!.*?" + r".*?)(?!.*?".join(matchlist) + r".*?)"
            # e.g. for the above... ['6_19','6_21','6_24'] turns to: '(?!.*?6_19.*?)(?!.*?6_21.*?)(?!.*?6_24.*?)'
            thecompile = re.compile(rf"^{match_string}.*$")
            # equivalent to: '^(?!.*?6_19.*?)(?!.*?6_21.*?)(?!.*?6_24.*?).*$'
            result_list = [x for x in array if re.findall(thecompile, x)]
            return result_list
        else:
            # We will be doing an "OR" match
            match_string = r"(?!.*" + r"|.*".join(matchlist) + ")"
            # e.g. for the above... ['6_19','6_21','6_24'] turns to: '(?!.*6_19|.*6_21|.*6_24)'
            thecompile = re.compile(rf"^{match_string}.*$")
            # equivalent to: '^(?!.*6_19|.*6_21|.*6_24).*$'
            result_list = [x for x in array if re.findall(thecompile, x)]
            return result_list

# %%
#######################################
def get_emojis():
    """Retrieves hundreds of emoji glyphs derived from the UTF-8 character table.

    Examples:
        >>> moji = get_emojis()\n
        >>> moji[1540:1547]\n
        '🤠 🤡 🤢 🤣'
    """
    emoji_list_1 = [chr(i) for i in range(127744, 127994)]
    emoji_list_2 = [chr(e) for e in range(128000, 128501)]
    remove_list_for_list_3 = [
        129394,
        129399,
        129400,
        129401,
        129443,
        129444,
        129451,
        129452,
        129453,
        129483,
        129484,
    ]
    emoji_list_3 = [
        chr(e) for e in range(129293, 129536) if e not in remove_list_for_list_3
    ]

    agg_list = emoji_list_1 + emoji_list_2 + emoji_list_3
    one_space_sep_string = " ".join(agg_list)
    return one_space_sep_string

# %%
#######################################
def get_path(thepath="."):
    """Returns a pathlib object in the form of an absolute path.

    Examples:
        >>> get_path()\n
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/worksheet_dir')

        >>> get_path('no file by this name')\n
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/worksheet_dir/no file by this name')

        >>> get_path('/does/this/path/exist')\n
        PosixPath('/does/this/path/exist')

    Args:
        thepath (str, optional): Specify the path. Defaults to ".".

    Returns:
        pathlib.Path: Returns a pathlib Path() object
    """
    import pathlib

    return pathlib.Path(thepath).absolute()

# %%
#######################################
def print_docstring(obj: object):
    """Prints the docstring for a given function

    Example:
        >>> print_docstring(len)
        Return the number of items in a container.

    References:

    """
    print(obj.__doc__)

# %%
#######################################
def encode_hex(obj: object):
    """Encodes the string / bytes string using Hexadecimal.

    Example:
        >>> encode_hex('hello')\n
        b'68656c6c6f'

        >>> encode_hex(b'hello')\n
        b'68656c6c6f'

        >>> decode_hex(b'68656c6c6f')\n
        b'hello'

        >>> decode_hex('68656c6c6f')\n
        b'hello'

        >>> [hex(ord(s)) for s in 'hello']\n
        ['0x68', '0x65', '0x6c', '0x6c', '0x6f']

        >>> ''.join([hex(ord(s)) for s in 'hello'])\n
        '0x680x650x6c0x6c0x6f'

        >>> ''.join([hex(ord(s)) for s in 'hello']).replace('0x','')\n
        '68656c6c6f'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj

    result = codecs.encode(temp_obj, "hex")
    return result

# %%
#######################################
def get_etc_shadow_algorithm(string: str):
    """Returns the salt found within the line retreived from the /etc/shadow file

    Examples:
        >>> line_from_etc_shadow = 'root:$1$umqC71l2$370xDLmeGD9m4aF/ciIlC.:14425:0:99999:7:::'\n
        >>> get_etc_shadow_algorithm(line_from_etc_shadow)\n
        'MD5'

        >>> another_line = 'user:0.7QYSH8yshtus8d:18233:0:99999:7:::'\n
        >>> get_etc_shadow_algorithm(another_line)\n
        'There is no $ in the hash_string value.'

    References:
        https://linuxize.com/post/etc-shadow-file/
    """
    (
        username,
        hash_string,
        last_pw_change,
        min_pw_age,
        max_pw_age,
        warn_period,
        exp_date,
    ) = string.split(":")[:-2]

    if "$" in hash_string:
        algorithm, salt, thehash = hash_string.split("$")[1:]
        hash_alg_lookup_table = {
            "1": "MD5",
            "2a": "Blowfish",
            "2y": "EksBlowfish",
            "5": "SHA-256",
            "6": "SHA-512",
        }
        algorithm_name = hash_alg_lookup_table.get(algorithm, "Unknown")
        return algorithm_name

    else:
        return "There is no $ in the hash_string value."

# %%
#######################################
def format_with_keywords(**kwvars: str):
    """This is a demo exercise of using format() with key/value pairs in order to insert variables into the string.

    Examples:
        >>> mytuplelist = [('item1', 'Slot number 1'), ('item2', 'And the 2nd'), ('item3', 'Then the 3rd')]\n
        >>> mydict = {k:v for k,v in mytuplelist}\n
        >>> mydict\n
        {'item1': 'Slot number 1', 'item2': 'And the 2nd', 'item3': 'Then the 3rd'}

        >>> format_with_keywords(**mydict)\n
        {'item1': 'Slot number 1', 'item2': 'And the 2nd', 'item3': 'Then the 3rd'}\n
        'blah Slot number 1 blah And the 2nd blah Then the 3rd'
    """
    print({**kwvars})
    dict_of_vars = {**kwvars}
    return "blah {item1} blah {item2} blah {item3}".format(**dict_of_vars)

# %%
#######################################
def decode_gzip(obj: object):
    """Decodes the string / bytes string using GZIP / zlib.

    Example:
        >>> encode_gzip('hello')\n
        b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15'

        >>> encode_gzip(b'hello')\n
        b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15'

        >>> decode_gzip(b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15')\n
        b'hello'
    """
    import codecs

    if isinstance(obj, str):
        temp_obj = obj.encode()
    elif isinstance(obj, bytes):
        temp_obj = obj
    return codecs.decode(temp_obj, "zlib")


decode_zip = decode_gzip

# %%
#######################################
def get_group_members(group_name=None):
    """Returns a DataFrame containing the local computer's groups, GID, and group members.

    Examples:
        >>> get_group_members()\n
                           0  1     2                  3\n
        0               root  x     0                 []\n
        1             daemon  x     1                 []\n
        2                bin  x     2                 []\n
        3                sys  x     3                 []\n
        4                adm  x     4  [syslog, pengwin]\n
        ..               ... ..   ...                ...\n
        71  systemd-coredump  x   999                 []\n
        72           pengwin  x  1000                 []\n
        73           lightdm  x   133                 []\n
        74     nopasswdlogin  x   134                 []\n
        75          testuser  x  1001                 []\n

    Args:
        group_name (str, optional): Reference the name of a particular group. Defaults to None.

    Returns:
        pandas.core.frame.DataFrame: Returns a pandas DataFrame with the group information.
    """
    import grp
    import pandas as pd

    all_groups = grp.getgrall()
    df = pd.DataFrame(all_groups)
    return df

# %%
#######################################
def xor_string(string: str, xor_int_value=42):
    """Takes a given string and does an XOR operation on the converted ord() value of each character with the "xor_int_value", which by default is 42

    Examples:
        >>> string2encode = 'Now is better than never.'\n
        >>> xor_string(string2encode)\n
        'dE]\nCY\nHO^^OX\n^BKD\nDO\\OX\x04'

        >>> xor_string('dE]\nCY\nHO^^OX\n^BKD\nDO\\OX\x04')\n
        'Now is better than never.'

        >>> chr(97)\n
        'a'
        >>> ord('a')\n
        97
        >>> hex(97)\n
        '0x61'
        >>> int('0x61', 16)\n
        97
        >>> xor_string(string2encode, xor_int_value = 97)\n
        '/\x0e\x16A\x08\x12A\x03\x04\x15\x15\x04\x13A\x15\t\x00\x0fA\x0f\x04\x17\x04\x13O'
        >>>
        >>> xor_string('/\x0e\x16A\x08\x12A\x03\x04\x15\x15\x04\x13A\x15\t\x00\x0fA\x0f\x04\x17\x04\x13O', 97)\n
        'Now is better than never.'

    Args:
        string (str): The string you want to XOR (each character will be XORed by the xor_int_value)
        xor_int_value (int, optional): The integer value that is used for the XOR operation. Defaults to 42.

    Returns:
        str: Returns an XORed string
    """
    xored_result = "".join([chr(ord(c) ^ xor_int_value) for c in string])
    return xored_result

# %%
#######################################
def dict_from_two_lists(keys: list, values: list):
    """Creates a dictionary from a list of keys and a list of values.

    Examples:
        >>> keys = ('bztar', 'gztar', 'tar', 'xztar', 'zip')\n
        >>> values = ('.tbz2', '.tgz', '.tar', '.txz', '.zip')\n
        >>> newdict = dict_from_two_lists(keys, values)\n
        >>> pprint(newdict)\n
        {'bztar': '.tbz2',
        'gztar': '.tgz',
        'tar': '.tar',
        'xztar': '.txz',
        'zip': '.zip'}

    Args:
        keys (list): Reference the keys list
        values (list): Reference the values list

    Returns:
        dict: Returns a dictionary
    """
    result = {k: v for k, v in zip(keys, values)}
    return result

# %%
#######################################
def dict_from_tuple_list(tuple_list: list):
    """Creates a dictionary from a list of 2-element tuples, where each tuple is in the format of (key, value).

    Examples:
        >>> tuple_list = [('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')]\n
        >>> dict_from_tuple_list(tuple_list)\n
        {'item1': 'I am a raptor', 'item2': 'eat everything', 'item3': 'Till the appearance of man'}
    """
    result = {k: v for k, v in tuple_list}
    return result

# %%
#######################################
def get_file_size(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    file_byte_size = path_obj.stat().st_size
    return file_byte_size

# %%
#######################################
def decode_punycode(thebytes: bytes):
    """Decodes the bytes string using Punycode.

    Example:
        >>> encode_punycode('hello')\n
        b'hello-'

        >>> decode_punycode(b'hello-')\n
        'hello'
    """
    import codecs

    if isinstance(thebytes, bytes):
        temp_obj = thebytes

    return codecs.decode(temp_obj, "punycode")

# %%
#######################################
def get_unique_in_array(lst: list):
    """Returns a list of the unique values within the given list.

    Examples:
        >>> mylst = [1,1,2,2,3,2,3,4,5,6]\n
        >>> get_unique_in_array(mylst)\n
        [1, 2, 3, 4, 5, 6]
        >>>
    """
    return list(set(lst))

# %%
#######################################
def like(matchlist: list, array: list, andop=False):
    """Returns a list of matches in the given array by doing a comparison of each object with the values given to the matchlist parameter.

    Examples:
        >>> subdir_list = ['get_random.py',
        ...  'day6_15_payload-by-port.py',
        ...  'worksheet_get_exif.py',
        ...  'worksheet_get_random.py',
        ...  'day6_19_browser-snob.py',
        ...  'day6_12_letterpassword.py',
        ...  'day6_21_exif-tag.py',
        ...  'day6_17_subprocess_ssh.py',
        ...  'day6_16._just_use_split.py']

        >>> like('day', subdir_list)\n
        ['day6_15_payload-by-port.py', 'day6_19_browser-snob.py', 'day6_12_letterpassword.py', 'day6_21_exif-tag.py', 'day6_17_subprocess_ssh.py', 'day6_16._just_use_split.py']

        >>> like(['get','exif'], subdir_list)\n
        ['get_random.py', 'worksheet_get_exif.py', 'worksheet_get_random.py', 'day6_21_exif-tag.py']

        >>> like(['get','exif'], subdir_list, andop=True)\n
        ['worksheet_get_exif.py']

    Args:
        matchlist (list): Submit one or many substrings to match against
        array (list): This is the list that we want to filter
        andop (bool, optional): This will determine if the matchlist criteria is an "And Operation" or an "Or Operation. Defaults to False (which is the "Or Operation").  Only applies when multiple arguments are used for the "matchlist" parameter

    Returns:
        list: Returns a list of matches

    References:
        https://stackoverflow.com/questions/469913/regular-expressions-is-there-an-and-operator
        https://stackoverflow.com/questions/3041320/regex-and-operator
        https://stackoverflow.com/questions/717644/regular-expression-that-doesnt-contain-certain-string
    """
    import re

    if isinstance(matchlist, str):
        # matchlist is a single string object
        thecompile = re.compile(rf"^(?=.*{matchlist}).*$")
        result_list = [x for x in array if re.findall(thecompile, x)]
        return result_list
    else:
        if andop:
            # We will be doing an "AND" match or an "And" "Operation"
            match_string = r"(?=.*?" + r".*?)(?=.*?".join(matchlist) + r".*?)"
            # e.g. for the above... ['6_19','6_21','6_24'] turns to: '(?=.*?6_19.*?)(?=.*?6_21.*?)(?=.*?6_24.*?)'
            thecompile = re.compile(rf"^{match_string}.*$")
            # equivalent to: '^(?=.*?6_19.*?)(?=.*?6_21.*?)(?=.*?6_24.*?).*$'
            result_list = [x for x in array if re.findall(thecompile, x)]
            return result_list
        else:
            # We will be doing an "OR" match
            match_string = r"(?=.*" + r"|.*".join(matchlist) + ")"
            # e.g. for the above... ['6_19','6_21','6_24'] turns to: '(?=.*6_19|.*6_21|.*6_24)'
            thecompile = re.compile(rf"^{match_string}.*$")
            # equivalent to: '^(?=.*6_19|.*6_21|.*6_24).*$'
            result_list = [x for x in array if re.findall(thecompile, x)]
            return result_list

# %%
#######################################
def filehandle_readtext(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    with open(path_obj, "rt") as f:
        content = f.read()

    return content


readtext = filehandle_readtext

# %%
#######################################
def format_demo():
    """Prints multiple examples of format() syntax using many 'presentation types' as the 'format specifiers'; also includes the output of each line of code

    References:
        Format Specifiecation Mini-Language:  https://docs.python.org/3/library/string.html#formatspec
    """
    demo_string = """
    # STRING NOTATION - THIS DOES NOT CONVERT THE TYPE
    '{0:-^42s}'.format( 42 )
    # ValueError: Unknown format code 's' for object of type 'int'
    '{0:-^42s}'.format( '42' )
    # '--------------------42--------------------'
    '{0:-^42}'.format( '42' )
    # '--------------------42--------------------'
    str(42)
    # '42'  # this function converts the type, however


    # DECIMAL OR INTEGER NOTATION
    '{0:-^42d}'.format( 42 )
    # '--------------------42--------------------'
    '{0:-^42}'.format( 42 )
    # '--------------------42--------------------'


    # FLOAT NOTATION
    '{0:-^42f}'.format( 42 ) 
    # '----------------42.000000-----------------'
    '{0:-^42f}'.format( .42 ) 
    # '-----------------0.420000-----------------'


    # HEXADECIMAL - SMALL / LARGE LETTERS
    '{0:-^42x}'.format( 42 )
    # '--------------------2a--------------------'
    '{0:-^42x}'.format( 420 )
    # '-------------------1a4--------------------'
    '{0:-^42X}'.format( 42 )
    # '--------------------2A--------------------'
    '{0:-^42X}'.format( 420 )
    # '-------------------1A4--------------------'
    hex(420)
    # '0x1a4'
    int('0x1a4', 16)
    # 420


    # PERCENT NOTATION
    '{0:-^42%}'.format( 42 ) 
    # '---------------4200.000000%---------------'
    '{0:-^42%}'.format( .42 ) 
    # '----------------42.000000%----------------'


    # INTEGER TO CHARACTER CONVERSTION
    '{0:-^42c}'.format( 42 )
    # '--------------------*---------------------'
    '{0:-^42c}'.format( 420 )
    # '--------------------Ƥ---------------------'
    '{0:-^42c}'.format( 4200 )
    # '--------------------ၨ---------------------'
    chr(420)
    # 'Ƥ'
    ord('Ƥ')
    # 420


    # OCTAL NOTATION
    '{0:-^42o}'.format( 42 )
    # '--------------------52--------------------'
    '{0:-^42o}'.format( 420 )
    # '-------------------644--------------------'
    int('644', 8)
    # 420
    oct(420)
    # '0o644'


    # EXPONENTIAL NOTATION
    '{0:-^42e}'.format( 42 )
    # '---------------4.200000e+01---------------'
    '{0:-^42e}'.format( 4.2 )
    # '---------------4.200000e+00---------------'
    '{0:-^42e}'.format( 420 )
    # '---------------4.200000e+02---------------'


    # BINARY NOTATION
    '{0:-^42b}'.format( 42 )
    # '------------------101010------------------'
    '{0:-^42b}'.format( 420 )
    # '----------------110100100-----------------'
    int('110100100', 2)
    # 420
    bin(420)
    # '0b110100100'
    """
    print(demo_string)

# %%
#######################################
def get_content_gzip(thepath: str):
    """Displays the content of a gzip compressed file.

        Examples:
    >>> zcat = get_content_gzip\n
    >>> test = zcat('test_text.txt.gz')>>> test\n
    'ok\\nso here is some\\n\'blah blah\'\\nWe are planning\\nTo use this \\nin not only\\nnormal testing...\\nbut also for "gzip compressed \\ntext searching"\\nI know... sounds cool\\nLet\'s see if it works!\\n'
    >>> test.splitlines()
    ['ok', 'so here is some', "'blah blah'", 'We are planning', 'To use this ', 'in not only', 'normal testing...', 'but also for "gzip compressed ', 'text searching"', 'I know... sounds cool', "Let's see if it works!"]

        Args:
            thepath (str): Specify the path of the file.

        Returns:
            bytes: Returns a bytes string
    """
    import gzip

    # Here we are specifying that we want to "Read Text" with 'rt' instead of the default read for gzip.open() which is 'rb' or 'Read Bytes'
    with gzip.open(thepath, "rt") as f:
        return f.read()


zcat = get_content_gzip

# %%
#######################################
def get_content_linenum_gzip(thepath: str, linenum: int):
    """Returns the line number of the specified gzipped file.

    Examples:
        >>> get_content_linenum_gzip('test_text.txt.gz', 3)\n
        "'blah blah'\\n"

    Args:
        thepath (str): Reference the file
        linenum (int): Specify the line number

    Returns:
        str: Returns the line number in the specified gzipped file
    """
    import pathlib
    import gzip

    path_obj = pathlib.Path(thepath).resolve()

    # The open() function can take a str object or a Path() object as an argument
    with gzip.open(path_obj, "rt") as f:
        lines = f.readlines()
    return lines[linenum - 1]

# %%
#######################################
def sort_dict_by_value(dict1: dict, reverse=False):
    """For a given dictionary, returns a sorted list of tuples for each item based on the value.

    Examples:
        >>> employees = {'Alice' : 100000,
        ...              'Bob' : 99817,
        ...              'Carol' : 122908,
        ...              'Frank' : 88123,
        ...              'Eve' : 93121}

        >>> sort_dict_by_value(employees)\n
        [('Frank', 88123), ('Eve', 93121), ('Bob', 99817), ('Alice', 100000), ('Carol', 122908)]

        >>> sort_dict_by_value(employees, reverse=True)\n
        [('Carol', 122908), ('Alice', 100000), ('Bob', 99817), ('Eve', 93121), ('Frank', 88123)]

    References:
        https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value?page=1&tab=votes#tab-top
    """
    if reverse:
        return sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    else:
        return sorted(dict1.items(), key=lambda x: x[1])

# %%
#######################################
def sort_dict_by_value_itemgetter(dict1: dict, reverse=False):
    """For a given dictionary, returns a sorted list of tuples for each item based on the value.

    Examples:
        >>> employees = {'Alice' : 100000, 'Bob' : 99817, 'Carol' : 122908, 'Frank' : 88123, 'Eve' : 93121}\n
        >>> sort_dict_by_value_itemgetter(employees)\n
        [('Frank', 88123), ('Eve', 93121), ('Bob', 99817), ('Alice', 100000), ('Carol', 122908)]

        >>> sort_dict_by_value_itemgetter(employees, reverse=True)\n
        [('Carol', 122908), ('Alice', 100000), ('Bob', 99817), ('Eve', 93121), ('Frank', 88123)]

    References:
        https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value?page=1&tab=votes#tab-top
        https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work
    """
    import operator

    if reverse:
        return sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)
    else:
        return sorted(dict1.items(), key=operator.itemgetter(1))

# %%
#######################################
def sum_array(lst: list):
    """Returns the sum of the numbers in the list.

    Example:
        >>> list(range(0,10))\n
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> myrange = list(range(0,10))\n
        >>> sum_array(myrange)\n
        45
        >>> sum(list(range(0,10)))\n
        45
    """
    return sum(lst)

# %%
#######################################
def format_header_break():
    """Returns a header break of 39 '#' glyphs.

    Examples:
        >>> format_header_break()\n
        '#######################################'
    """
    return "{0:#<39}".format("")

# %%
#######################################
def get_functions_in_all_funcs():
    import pathlib
    import os
    import re

    path_obj = pathlib.Path().home() / "Temp/pyplay/IMPORT_functions/Python_3.8_Tools"
    os.chdir(path_obj)

    from regex_funcs import like
    from file_folder_funcs import get_content

    cat = get_content
    myfile = cat("all_funcs.py").splitlines()
    sorted_funcs = sorted(like("^def ", myfile))

    results_array = []
    [results_array.extend(re.findall(r"def (\w+)", e)) for e in sorted_funcs]
    return results_array

# %%
#######################################
def get_files(thepath=".", names=False, stringoutput=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if stringoutput:
        contents = sorted([str(obj) for obj in path_obj.glob("*") if obj.is_file()])
    else:
        contents = sorted([obj for obj in path_obj.glob("*") if obj.is_file()])

    if names:
        contents = [str(e).split("/")[-1] for e in contents]

    return contents

# %%
#######################################
def display_ordinal_value(glyph: str):
    """Displays the integer value of the given glyph

    Examples:
        >>> display_ordinal_value('🐍')\n
        128013

        >>> display_ordinal_value('G')\n
        71

        >>> display_ordinal_value('g')\n
        103
    """
    return ord(glyph)

# %%
#######################################
def get_parent_path(thepath="."):
    """Returns the parent directory as an absolute path.

    Examples:
        >>> import os
        >>> os.getcwd()
        '/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/worksheet_dir'
        >>>
        >>> get_parent_path()
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs')
        >>>
        >>> get_parent_path('bogus file name')
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/worksheet_dir')
        >>>
        >>> get_parent_path('.')
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs')
        >>>
        >>> get_parent_path('_')
        PosixPath('/home/pengwin/Temp/pyplay/IMPORT_functions/my_py_funcs/worksheet_dir')
        >>>
        >>> get_parent_path('/does/this/path/exist')
        PosixPath('/does/this/path')

    Args:
        thepath (str, optional): Specify the path. Defaults to ".".

    Returns:
        pathlib.Path: Returns a pathlib Path() object
    """
    import pathlib

    # return pathlib.Path(thepath).parent.absolute()
    return pathlib.Path(thepath).absolute().parent

# %%
#######################################
def dict_iterator_itervalues(thedict: dict):
    """Iterates over the values in a given dictionary and further loops over the values.
    
    Example:
        >>> sessions_pcap = rdpcap('sessions.pcap')\n
        >>> dict_iterator_itervalues( sessions_pcap.sessions() )\n
        (0, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=52 id=37579 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3bb8 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470518139 ack=626548773 dataofs=8 reserved=0 flags=FA window=229 chksum=0x6c67 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264020, 910859633))] |>>>)\n
        (1, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=89 id=37576 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3b96 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470517854 ack=626548773 dataofs=8 reserved=0 flags=PA window=229 chksum=0x302c urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264018, 910859633))] |<Raw  load='			of virtually every computer crime' |>>>>)\n
        (2, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=85 id=37566 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3ba4 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470517611 ack=626548773 dataofs=8 reserved=0 flags=PA window=229 chksum=0xd944 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264018, 910859633))] |<Raw  load='			security number, you pay your' |>>>>)\n
        (3, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=109 id=37556 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3b96 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470517283 ack=626548773 dataofs=8 reserved=0 flags=PA window=229 chksum=0xb42a urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264016, 910859633))] |<Raw  load='He opens the file.  Paper rattle marks the silence as he' |>>>>)

    Args:
        thedict (dict): Reference an existing dict object.
    """
    counter = 0
    for eachkey in thedict.keys():  
        for val in thedict[eachkey]:
            print( (counter, val ) )
            counter += 1 

# %%
#######################################
def get_object_memory_address(obj: object, return_hex=False):
    """Returns the memory address of the given object.

    Examples:
        >>> mylst = [1,1,2,2,3,2,3,4,5,6]\n
        >>> get_object_memory_address(mylst)\n
        140192405518336
        >>> get_object_memory_address(mylst, return_hex=True)\n
        '0x7f811687f800'
    """
    if return_hex:
        return hex(id(obj))
    else:
        return id(obj)

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

# %%
#######################################
def format_plus_chars(obj: str or list, fill_char='.', align=("<", "^", ">")[2], len=44, type='s'):
    """Returns the given string or list of strings with some additional padding/fill characters up to the designated length.

    Examples:
        >>> ##### EXAMPLE 1 ######
        >>> format_plus_chars('blah blah')\n
        '...................................blah blah'

        >>> ##### EXAMPLE 2  ######
        >>> stones = ['Pearl','Amethyst','Jacinth','Chrysoprasus','Topaz','Beryl','Chrysolite','Sardius','Sardonyx','Emerald','Chalcedony','Sapphire','Jasper']
        >>> from pprint import pprint
        >>> pprint( format_plus_chars( stones) )
        ['.......................................Pearl',
        '....................................Amethyst',
        '.....................................Jacinth',
        '................................Chrysoprasus',
        '.......................................Topaz',
        '.......................................Beryl',
        '..................................Chrysolite',
        '.....................................Sardius',
        '....................................Sardonyx',
        '.....................................Emerald',
        '..................................Chalcedony',
        '....................................Sapphire',
        '......................................Jasper']

    Args:
        obj (object): Reference either a str object or a list of str objects
        fill_char (str, optional): This is what we are padding with. Defaults to '.'.
        align (object, optional): Here we have a tuple defining the expected preset arguments. Defaults to ("<", "^", ">")[2].
        len (int, optional): This is the quantity of the padding/fill characters we will be using. Defaults to 44.
        type (str, optional): This is the type specifier we are giving to the format() method.  's' designates a "str" type. Defaults to 's'.

    Returns:
        object: Returns either a str object or a list of str objects.
    """
    if isinstance(obj, str):
        result = '{0:{fill_char}{align}{len}{type}}'.format(obj, fill_char=fill_char, align=align, len=len, type=type)
    elif isinstance(obj, list):
        result = ['{0:{fill_char}{align}{len}{type}}'.format(str(o), fill_char=fill_char, align=align, len=len, type=type) for o in obj]
    return result

# %%
#######################################
def boolean_content_matcher(string_array: str, substring: str):
    """Returns a list of tuples containing True/False if the substring is found in each element in the array.

    Examples:
        >>> text_list = ['lambda functions are anonymous functions.',
        ...        'anonymous functions dont have a name.',
        ...        'functions are objects in Python.']

        >>> boolean_content_matcher(text_list, 'anony')\n
        [(True, 'lambda functions are anonymous functions.'), (True, 'anonymous functions dont have a name.'), (False, 'functions are objects in Python.')]

    References:
        https://github.com/finxter/PythonOneLiners/blob/master/book/python_tricks/one_liner_04.py
    """
    result = list(
        map(lambda x: (True, x) if substring in x else (False, x), string_array)
    )
    return result

# %%
#######################################
def convert_string2bytes(string: str):
    """Converts a "str" type object into a "bytes" type object

    Examples:
        >>> convert_string2bytes('nice string')\n
        b'nice string'
    """
    return string.encode()

# %%
#######################################
def get_file_linecount(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with path_obj.open(thepath) as f:
        lines = f.readlines()
    return len(lines)

# %%
#######################################
def refindall_border_demo():
    import re

    example1 = "987!5887315075505 963273979167!1792 424 8829428 758423813480156538725 80338918230792#82063912 *891"
    example2 = "823!03270182 997 868!465#891*0105#46535832231!296!2364#1903 406333702!355536717 1204!827205710879978416468!3357 *711"

    print(
        r'For the first example I will take the string and isolate each sequence of 3 digits surrounded by a "border character" or "\b"',
        "\n",
    )
    print(f"Example1 String: {example1}\n")

    # Here we are specifying each group of 3 digits surrounded by a "border character" or "\b"
    match_syntax1 = re.compile(r"\b\d{3}\b")
    print(f"Using the match syntax: {match_syntax1}")

    result1 = re.findall(match_syntax1, example1)
    print(f"Result for Example #1: {result1}")
    # Output:   Result for Example #1: ['987', '424', '891']

    print("\n\n")

    print(
        r'For the second example I will take the string and isolate each sequence of 4 digits surrounded by a "border character" or "\b"',
        "\n",
    )
    print(f"Example2 String: {example2}\n")

    # Here we are specifying each group of 4 digits surrounded by a "border character" or "\b"
    match_syntax2 = re.compile(r"\b\d{4}\b")
    print(f"Using the match syntax: {match_syntax2}")

    result2 = re.findall(match_syntax2, example2)
    print(f"Result for Example #2: {result2}")
    # Output:   Result for Example #2: ['0105', '2364', '1903', '1204', '3357']

