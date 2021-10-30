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
            if eachfuncsdir.name == 'all_funcs' or eachfuncsdir.name == 'scapy_funcs' or eachfuncsdir.name == 'pil_image_analysis_funcs':
                # ignore these directories
                pass
            else:
                # for each file ending in .py (these should be the individual function tools ending in .py), copy that file to the destination dir
                for funcpy in eachfuncsdir.glob('*.py'):
                    copy_file( funcpy.as_posix(), allfuncsdir_path.as_posix() )

