#######################################
########## FILE FOLDER FUNCS ##########
#######################################

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
def get_content_linenum(thepath: str, linenum: int):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    # The open() function can take a str object or a Path() object as an argument
    with open(path_obj) as f:
        lines = f.readlines()
    return lines[linenum - 1]

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
def get_files_recursively(thepath=".", names=False, stringoutput=False):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    if stringoutput:
        contents = sorted([str(obj) for obj in path_obj.rglob("*") if obj.is_file()])
    else:
        contents = sorted([obj for obj in path_obj.rglob("*") if obj.is_file()])
    return contents

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
def filehandle_write(thepath: str, content: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with open(path_obj, "w") as f:
        f.write(content)


writetext = filehandle_write

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
def rename_file(thepath: str, newname: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    target = pathlib.Path(newname)
    path_obj.rename(target)

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
def get_file_size(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    file_byte_size = path_obj.stat().st_size
    return file_byte_size

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
def get_file_linecount(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with path_obj.open(thepath) as f:
        lines = f.readlines()
    return len(lines)

