# %%
#######################################
def format_header_block_plus(string: str):
    """Returns a header for use with my function files.

    Example:
        #######################################\n
        ########### ARRAY FUNCTIONS ###########\n
        #######################################\n

    """
    newstring = ""
    newstring += "{0:#<39}".format("") + "\n"
    newstring += "{0:#^39}".format(f" {string} ") + "\n"
    newstring += "{0:#<39}".format("") + "\n\n"
    
    return newstring

