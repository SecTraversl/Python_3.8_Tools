#######################################
####### FILE & FOLDER FUNCTIONS #######
#######################################
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
def get_cwd(stringoutput=False):
    """Returns the pathlib object for the current working directory

    Examples:
        >>> get_cwd()\n
        PosixPath('/home/cooluser/pyplay')

        >>> get_cwd(stringoutput=True)\n
        '/home/cooluser/pyplay'

    References:
        https://realpython.com/python-pathlib/
    """
    import pathlib

    if stringoutput:
        result = str(pathlib.Path.cwd())
    else:
        result = pathlib.Path.cwd()
    return result


pwd = get_cwd


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
def split_path(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    parts = path_obj.parts
    return parts


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


ls = get_ls


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


lsfiles = get_files


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


lsdirs = get_dirs


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
def get_file_size(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    file_byte_size = path_obj.stat().st_size
    return file_byte_size


# %%
#######################################
def get_file_stats(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    file_stats = path_obj.stat()
    return file_stats


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
def get_file_symlink(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    symlink_resolved = path_obj.readlink()
    return symlink_resolved


# %%
#######################################
def rename_file(thepath: str, newname: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    target = pathlib.Path(newname)
    path_obj.rename(target)


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
def get_content_linenum(thepath: str, linenum: int):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    # The open() function can take a str object or a Path() object as an argument
    with open(path_obj) as f:
        lines = f.readlines()
    return lines[linenum - 1]


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
def new_directory(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    path_obj.mkdir()


mkdir = new_directory


# %%
#######################################
# PREVIOUS VERSION
# def copy_file(thepath: str, dest: str):
#     """Copies a file.

#     References:
#         https://stackoverflow.com/questions/123198/how-can-a-file-be-copied
#         https://www.geeksforgeeks.org/python-move-or-copy-files-and-directories/

#     Args:
#         thepath (str): Specify the path of the file you want to copy
#         dest (str): Specify the destination or file copy name
#     """
#     import shutil
#     import pathlib

#     path_obj = pathlib.Path(thepath).resolve()
#     copy_path = pathlib.Path(dest).resolve()
#     shutil.copy2(str(path_obj), str(copy_path))


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
# PREVIOUS VERSION
# def remove_file(thepath: str):
#     """Removes the specified file.

#     References:
#         https://stackoverflow.com/questions/42636018/python-difference-between-os-remove-and-os-unlink-and-which-one-to-use

#     Args:
#         thepath (str): Specify the path of the file
#     """
#     import pathlib

#     path_obj = pathlib.Path(thepath).resolve()
#     path_obj.unlink()


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


# ANOTHER VERSION THAT WAS BEING TESTED
# def remove_directory(thepath: str or list, force=False):
#     """Removes a directory.  If the directory has contents, use force=True to recursively delete the children and delete the parent.

#     Examples:
#         >>> get_dirs(names=True)\n
#         ['__pycache__', 'copy_test_dir', 'push_bitbucket_dir', 'test_copy_of_a_directory', 'worksheet_dir']

#         >>> remove_directory('test_copy_of_a_directory', force=True)\n
#         >>> get_dirs(names=True)\n
#         ['__pycache__', 'copy_test_dir', 'push_bitbucket_dir', 'worksheet_dir']

#     References:
#         https://stackoverflow.com/questions/50186904/pathlib-recursively-remove-directory

#     Args:
#         thepath (str): Specify the path
#         force (bool, optional): Allows for a recursive delete. Defaults to False.
#     """
#     import pathlib

#     if isinstance(thepath, str):
#         path_obj = pathlib.Path(thepath).resolve()

#         if force:
#             for child in path_obj.rglob("*"):
#                 if child.is_file():
#                     child.unlink()
#                 elif child.is_dir():
#                     remove_directory(child, force=True)
#             path_obj.rmdir()
#         else:
#             path_obj.rmdir()
#     elif isinstance(thepath, list):
#         for eachitem in thepath:
#             path_obj = pathlib.Path(eachitem).resolve()

#             if force:
#                 for child in path_obj.rglob("*"):
#                     if child.is_file():
#                         child.unlink()
#                     elif child.is_dir():
#                         remove_directory(child, force=True)
#                 path_obj.rmdir()
#             else:
#                 path_obj.rmdir()


rmdir = remove_directory


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
# PREVIOUS VERSION... PRIOR TO INCORPORATING 'rt'

# def get_content_gzip(thepath: str):
#     """Displays the content of a gzip compressed file.

#     Examples:
#         >>> zcat = get_content_gzip\n
#         >>> test = zcat('test_text.txt.gz')\n
#         >>> test\n
#         b'ok\\nso here is some\\n\'blah blah\'\\nWe are planning\\nTo use this \\nin not only\\nnormal testing...\\nbut also for "gzip compressed \\ntext searching"\\nI know... sounds cool\\nLet\'s see if it works!\\n'
#         >>> test.decode().splitlines()\n
#         ['ok', 'so here is some', "'blah blah'", 'We are planning', 'To use this ', 'in not only', 'normal testing...', 'but also for "gzip compressed ', 'text searching"', 'I know... sounds cool', "Let's see if it works!"]

#     Args:
#         thepath (str): Specify the path of the file.

#     Returns:
#         bytes: Returns a bytes string
#     """
#     import gzip

#     with gzip.open(thepath) as f:
#         return f.read()


# zcat = get_content_gzip


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


previewgfiles = get_files_preview


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
def filehandle_readtext(thepath: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()

    with open(path_obj, "rt") as f:
        content = f.read()

    return content


readtext = filehandle_readtext


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
def filehandle_append(thepath: str, content: str):
    import pathlib

    path_obj = pathlib.Path(thepath).resolve()
    with open(path_obj, "a") as f:
        f.write(content)


appendtext = filehandle_append


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
