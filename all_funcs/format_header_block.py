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

