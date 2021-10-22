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

