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

