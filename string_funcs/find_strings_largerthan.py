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

