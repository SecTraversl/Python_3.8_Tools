#######################################
###### FUNCTION AND MODULE FUNCS ######
#######################################

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

