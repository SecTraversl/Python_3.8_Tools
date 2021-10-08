#######################################
########## STRING FUNCTIONS ###########
#######################################
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
def format_header_text(string: str):
    """Returns a header string that is centered within a space of 39 characters, bordered by "#".

    Examples:
        >>> format_header_text('ARRAY FUNCTIONS')\n
        '########### ARRAY FUNCTIONS ###########'
    """
    return "{0:#^39}".format(f" {string} ")


# %%
#######################################
def format_header_package(string: str):
    """Prints a header for use with my function files

    Examples:
        #######################################\n
        ########### ARRAY FUNCTIONS ###########\n
        #######################################\n
    """
    newstring = ""
    newstring += "{0:#<39}".format("") + "\n"
    newstring += "{0:#^39}".format(f" {string} ") + "\n"
    newstring += "{0:#<39}".format("") + "\n"
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
def match_str_len_with_padding(
    string1: str, string2: str, padding="#", align=("left", "center", "right")[1]
):
    """Returns a list containing the original longer string, and the smaller string with padding.

    Examples:
        >>> mystring = "Complex is better than complicated."
        >>> secondstring = " blah "
        >>> blah_song = "blah ba blah blah blah"
        >>> match_str_len_with_padding(mystring, secondstring)\n
        ['Complex is better than complicated.', '############## blah ###############']
        >>> match_str_len_with_padding(mystring, blah_song, padding="*")\n
        ['Complex is better than complicated.', '******blah ba blah blah blah*******']
        >>> match_str_len_with_padding(mystring[::-1], mystring)\n
        ['.detacilpmoc naht retteb si xelpmoC', 'Complex is better than complicated.']
        >>> match_str_len_with_padding(mystring, blah_song, padding="&", align='right')\n
        ['Complex is better than complicated.', '&&&&&&&&&&&&&blah ba blah blah blah']
        >>> match_str_len_with_padding(mystring, blah_song, padding="<", align='left')\n
        ['Complex is better than complicated.', 'blah ba blah blah blah<<<<<<<<<<<<<']

    References:
        One liner if/else: https://youtu.be/MHlwl6GsT8s?t=990\n
        Format() with embedded variables for 'format specifiers': https://stackoverflow.com/questions/3228865/how-do-i-format-a-number-with-a-variable-number-of-digits-in-python

    Args:
        string1 (str): String number 1 to use in the comparison
        string2 (str): String number 2 to use in the comparison
        padding (str, optional): Here you can specify the padding character. Defaults to "#".
        align (str, optional): This is used to show valid arguments for this parameter (the default value is 'center'). Defaults to ('left','center','right')[1].

    Returns:
        list: Returns a list containing two strings of the same length, with the smaller string being padded.
    """

    bigger_str = string1 if len(string1) >= len(string2) else string2
    smaller_str = string1 if len(string1) < len(string2) else string2

    length_to_match = len(bigger_str)

    if align == "left":
        padded_string = "{small_str:{somepad}<{thelength}}".format(
            thelength=length_to_match, small_str=smaller_str, somepad=padding
        )
    elif align == "center":
        padded_string = "{small_str:{somepad}^{thelength}}".format(
            thelength=length_to_match, small_str=smaller_str, somepad=padding
        )
    elif align == "right":
        padded_string = "{small_str:{somepad}>{thelength}}".format(
            thelength=length_to_match, small_str=smaller_str, somepad=padding
        )

    if padded_string:
        return [bigger_str, padded_string]


# %%
#######################################
def split_string(string: str, size: int):
    """Splits a string into smaller strings of the desired size value.

    Examples:
    >>> string = 'hey hey hiya'\n
    >>> split_string(string, 4)\n
    ['hey ', 'hey ', 'hiya']

    References:
        https://youtu.be/pG3L2Ojh1UE?t=336
    """
    created_step_points = range(0, len(string), size)
    sublists_created = [string[i : i + size] for i in created_step_points]
    return sublists_created


# %%
#######################################
def reverse_first_half(string: str):
    """Reverse the first half of a given string.

    Examples:
        >>> reverse_first_half('sandwich')\n
        'dnaswich'
    """
    halfway_point = len(string) // 2
    first_half_reversed = string[:halfway_point][::-1]
    last_half = string[halfway_point:]
    return first_half_reversed + last_half


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


# %%
#######################################
