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
                text_message = ''
                text_message = text_message + "# NOTE: Excludes scapy functions.  To import scapy functions, use 'from scapy_funcs import *'\n"
                text_message = text_message + "# NOTE: Excludes pil image analysis functions.  To import pil image analysis functions, use 'from pil_image_analysis_funcs *'\n\n"
                new_module(eachfuncsdir.as_posix(), prepend_text=text_message)
            elif eachfuncsdir.name == 'scapy_funcs':
                new_module(eachfuncsdir.as_posix(), prepend_text="from scapy.all import *\n\n")
            elif eachfuncsdir.name == 'pil_image_analysis_funcs':
                new_module(eachfuncsdir.as_posix(), prepend_text="from PIL import Image\nfrom PIL.ExifTags import TAGS\n\n")
            else:
                new_module(eachfuncsdir.as_posix())