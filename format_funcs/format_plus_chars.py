# %%
#######################################
def format_plus_chars(obj: str or list, fill_char='.', align=("<", "^", ">")[2], len=44, type='s'):
    """Returns the given string or list of strings with some additional padding/fill characters up to the designated length.

    Examples:
        >>> ##### EXAMPLE 1 ######
        >>> format_plus_chars('blah blah')\n
        '...................................blah blah'

        >>> ##### EXAMPLE 2  ######
        >>> stones = ['Pearl','Amethyst','Jacinth','Chrysoprasus','Topaz','Beryl','Chrysolite','Sardius','Sardonyx','Emerald','Chalcedony','Sapphire','Jasper']
        >>> from pprint import pprint
        >>> pprint( format_plus_chars( stones) )
        ['.......................................Pearl',
        '....................................Amethyst',
        '.....................................Jacinth',
        '................................Chrysoprasus',
        '.......................................Topaz',
        '.......................................Beryl',
        '..................................Chrysolite',
        '.....................................Sardius',
        '....................................Sardonyx',
        '.....................................Emerald',
        '..................................Chalcedony',
        '....................................Sapphire',
        '......................................Jasper']

    Args:
        obj (object): Reference either a str object or a list of str objects
        fill_char (str, optional): This is what we are padding with. Defaults to '.'.
        align (object, optional): Here we have a tuple defining the expected preset arguments. Defaults to ("<", "^", ">")[2].
        len (int, optional): This is the quantity of the padding/fill characters we will be using. Defaults to 44.
        type (str, optional): This is the type specifier we are giving to the format() method.  's' designates a "str" type. Defaults to 's'.

    Returns:
        object: Returns either a str object or a list of str objects.
    """
    if isinstance(obj, str):
        result = '{0:{fill_char}{align}{len}{type}}'.format(obj, fill_char=fill_char, align=align, len=len, type=type)
    elif isinstance(obj, list):
        result = ['{0:{fill_char}{align}{len}{type}}'.format(str(o), fill_char=fill_char, align=align, len=len, type=type) for o in obj]
    return result

