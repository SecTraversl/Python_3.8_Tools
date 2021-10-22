# %%
#######################################
def xor_strings(string: str, xor_string="zen"):
    """Returns an XOR'ed string given a string object.  By default the string object will be XOR'ed using a truncated version of the "Zen of Python".  You can change this default by specifying your own "xor_string" value.

    Examples:
        >>> mystring = "Complex is better than complicated."
        >>> xor_strings(mystring)\n
        '\x17\x07\x08P6\x00\x16\x00\x06\x15\x002\x1c\x00\x1c\n\x1c\x0cT\n\x18Nt\n\x02M \t\x1d\x06\x13\x07onl'
        >>> xor_strings(
        ...     "\x17\x07\x08P6\x00\x16\x00\x06\x15\x002\x1c\x00\x1c\n\x1c\x0cT\n\x18Nt\n\x02M \t\x1d\x06\x13\x07onl"
        ... )\n
        'Complex is better than complicated.'

        >>> xor_strings('here is some blah blah', 'and here is a super secret string we use for xor')\n
        '\t\x0b\x16EH\x0c\x01ES\x06\x1eEAB\x1f\x14\x18E\x10L\x12\r'
        >>> xor_strings(
        ...     '\t\x0b\x16EH\x0c\x01ES\x06\x1eEAB\x1f\x14\x18E\x10L\x12\r', 'and here is a super secret string we use for xor'
        ... )\n
        'here is some blah blah'

    Args:
        string (str): The string object you want to XOR
        xor_string (str, optional): The xor_string used to XOR against the given string object. Defaults to "zen".

    Returns:
        str: Returns an XOR'ed string.
    """
    import codecs

    # import this
    from this import s as this_s

    # We initialize an empty string variable which we will += each xor'ed character to for the final string
    result_string = ""

    # We want to know the length of the given string, so we can have an equivalent number of characters from the "Zen of Python"
    len_of_string = len(string)

    if xor_string == "zen":
        # this.s is the zen of python rot13 encoded, so here we are decoding it
        zen = codecs.decode(this_s, "rot13")

        # Then we take the zen of python, and truncate it to match the length of the string we want to XOR
        match_len_for_xor_enum = zen[:len_of_string]
        for index_num, val in enumerate(string):
            result_string += chr(ord(val) ^ ord(match_len_for_xor_enum[index_num]))
        return result_string
    else:
        if len(string) == len(xor_string):
            match_len_for_xor_enum = xor_string
        elif len(string) > len(xor_string):
            makebig = xor_string * len(string)
            match_len_for_xor_enum = makebig[: len(string)]
        elif len(string) < len(xor_string):
            match_len_for_xor_enum = xor_string[: len(string)]

        for index_num, val in enumerate(string):
            result_string += chr(ord(val) ^ ord(match_len_for_xor_enum[index_num]))
        return result_string

