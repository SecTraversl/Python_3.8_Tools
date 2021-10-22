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

