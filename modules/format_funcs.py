#######################################
############ FORMAT FUNCS #############
#######################################

# %%
#######################################
def format_header_text(string: str):
    """Returns a header string that is centered within a space of 39 characters, bordered by "#".

    Examples:
        >>> format_header_text('ARRAY FUNCTIONS')\n
        '########### ARRAY FUNCTIONS ###########'
    """
    return "{0:#^39}".format(f" {string} ")

# %%
#######################################
def format_with_numbers(*vars: str):
    """This is a demo exercise of using format() with numbered {} in order to insert variables into the string.

    Examples:
        >>> format_with_numbers('hi','there','fella')\n
        hi there fella\n
        ['hi', 'there', 'fella']\n
        'blah hi blah there blah fella'

        >>> format_with_numbers('hi')\n
        hi\n
        ['hi']\n
        'blah hi blah default2 blah default3'

        >>> format_with_numbers('hi','there','fella','David')\n
        hi there fella David\n
        ['hi', 'there', 'fella', 'David']\n
        'blah hi blah there blah fella'
    """
    print(*vars)
    list_of_vars = [*vars]
    print([*vars])
    if len(list_of_vars) < 3:
        while len(list_of_vars) < 3:
            number = len(list_of_vars)
            list_of_vars.append("default" + str(number + 1))
    return "blah {2} blah {0} blah {1}".format(*list_of_vars)

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

# %%
#######################################
def format_with_braces(*vars: str):
    """This is a demo exercise of using format() with positional {} in order to insert variables into the string.

    Examples:
        >>> format_with_braces('hi','there','fella')\n
        hi there fella\n
        ['hi', 'there', 'fella']\n
        'blah hi blah there blah fella'

        >>> format_with_braces('hi')\n
        hi\n
        ['hi']\n
        'blah hi blah default2 blah default3'

        >>> format_with_braces('hi','there','fella','David')\n
        hi there fella David\n
        ['hi', 'there', 'fella', 'David']\n
        'blah hi blah there blah fella'
    """
    print(*vars)
    list_of_vars = [*vars]
    print([*vars])
    if len(list_of_vars) < 3:
        while len(list_of_vars) < 3:
            number = len(list_of_vars)
            list_of_vars.append("default" + str(number + 1))
    return "blah {} blah {} blah {}".format(*list_of_vars)

# %%
#######################################
def format_with_keywords(**kwvars: str):
    """This is a demo exercise of using format() with key/value pairs in order to insert variables into the string.

    Examples:
        >>> mytuplelist = [('item1', 'Slot number 1'), ('item2', 'And the 2nd'), ('item3', 'Then the 3rd')]\n
        >>> mydict = {k:v for k,v in mytuplelist}\n
        >>> mydict\n
        {'item1': 'Slot number 1', 'item2': 'And the 2nd', 'item3': 'Then the 3rd'}

        >>> format_with_keywords(**mydict)\n
        {'item1': 'Slot number 1', 'item2': 'And the 2nd', 'item3': 'Then the 3rd'}\n
        'blah Slot number 1 blah And the 2nd blah Then the 3rd'
    """
    print({**kwvars})
    dict_of_vars = {**kwvars}
    return "blah {item1} blah {item2} blah {item3}".format(**dict_of_vars)

# %%
#######################################
def format_demo():
    """Prints multiple examples of format() syntax using many 'presentation types' as the 'format specifiers'; also includes the output of each line of code

    References:
        Format Specifiecation Mini-Language:  https://docs.python.org/3/library/string.html#formatspec
    """
    demo_string = """
    # STRING NOTATION - THIS DOES NOT CONVERT THE TYPE
    '{0:-^42s}'.format( 42 )
    # ValueError: Unknown format code 's' for object of type 'int'
    '{0:-^42s}'.format( '42' )
    # '--------------------42--------------------'
    '{0:-^42}'.format( '42' )
    # '--------------------42--------------------'
    str(42)
    # '42'  # this function converts the type, however


    # DECIMAL OR INTEGER NOTATION
    '{0:-^42d}'.format( 42 )
    # '--------------------42--------------------'
    '{0:-^42}'.format( 42 )
    # '--------------------42--------------------'


    # FLOAT NOTATION
    '{0:-^42f}'.format( 42 ) 
    # '----------------42.000000-----------------'
    '{0:-^42f}'.format( .42 ) 
    # '-----------------0.420000-----------------'


    # HEXADECIMAL - SMALL / LARGE LETTERS
    '{0:-^42x}'.format( 42 )
    # '--------------------2a--------------------'
    '{0:-^42x}'.format( 420 )
    # '-------------------1a4--------------------'
    '{0:-^42X}'.format( 42 )
    # '--------------------2A--------------------'
    '{0:-^42X}'.format( 420 )
    # '-------------------1A4--------------------'
    hex(420)
    # '0x1a4'
    int('0x1a4', 16)
    # 420


    # PERCENT NOTATION
    '{0:-^42%}'.format( 42 ) 
    # '---------------4200.000000%---------------'
    '{0:-^42%}'.format( .42 ) 
    # '----------------42.000000%----------------'


    # INTEGER TO CHARACTER CONVERSTION
    '{0:-^42c}'.format( 42 )
    # '--------------------*---------------------'
    '{0:-^42c}'.format( 420 )
    # '--------------------Ƥ---------------------'
    '{0:-^42c}'.format( 4200 )
    # '--------------------ၨ---------------------'
    chr(420)
    # 'Ƥ'
    ord('Ƥ')
    # 420


    # OCTAL NOTATION
    '{0:-^42o}'.format( 42 )
    # '--------------------52--------------------'
    '{0:-^42o}'.format( 420 )
    # '-------------------644--------------------'
    int('644', 8)
    # 420
    oct(420)
    # '0o644'


    # EXPONENTIAL NOTATION
    '{0:-^42e}'.format( 42 )
    # '---------------4.200000e+01---------------'
    '{0:-^42e}'.format( 4.2 )
    # '---------------4.200000e+00---------------'
    '{0:-^42e}'.format( 420 )
    # '---------------4.200000e+02---------------'


    # BINARY NOTATION
    '{0:-^42b}'.format( 42 )
    # '------------------101010------------------'
    '{0:-^42b}'.format( 420 )
    # '----------------110100100-----------------'
    int('110100100', 2)
    # 420
    bin(420)
    # '0b110100100'
    """
    print(demo_string)

# %%
#######################################
def format_header_break():
    """Returns a header break of 39 '#' glyphs.

    Examples:
        >>> format_header_break()\n
        '#######################################'
    """
    return "{0:#<39}".format("")

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

