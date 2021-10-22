# %%
#######################################
def replace_hexadecimal_randomly(obj: str or list):
    """Takes a string of hexadecimal digits or a list of string hexadecimal digits and randomly replaces the string with one of equivalent length but different hexadecimal numbers.

    Examples:
        >>> replace_hexadecimal_randomly('dst=92:26:72:6e:67:f5 src=02:94:f3:a1:b1:72')\n
        'dst=c2:a2:14:31:61:19 src=4c:22:51:3f:8a:72'

    References:
        # Helpful syntax for hexadecimal matching
        https://stackoverflow.com/questions/8366682/search-for-hexadecimal-number-on-python-using-re

    Args:
        obj (object): Reference either a string of hexadecimal digits or a list of string hexadecimal digits

    Returns:
        object: Returns a new string or a new list of strings
    """
    import re
    import random

    #
    if isinstance(obj, str):
        #
        try:
            #
            # We match on each consecutive string of digits
            match_list = re.findall(r"[0-9a-fA-F]{2,}", obj)
            #
            replacement_list = []
            for eachitem in match_list:
                #
                ### FIRST, WE CREATE A BIG STRING OF RANDOM DIGITS ###
                # The elements will be integers ranging from 1 to 100
                lst = list(range(1, 101))
                #
                # From the "lst" of numbers 1 - 100, there will be multiple random choices, the quantity of which is based off of the number given to "k="
                random_list_of_ints = random.choices(lst, k=420)
                #
                # Then we take that list of random numbers and join them together making one long string of digits
                rand_num_string = "".join([str(e) for e in random_list_of_ints])
                #
                # Then we convert that random number string into a hex string, and remove the leading "0x" designator
                rand_hex_string = hex(int(rand_num_string))[2:]
                #
                ### THEN, WE USE THAT RANDOM STRING OF HEX DIGITS IN OUR SUBSTITUTION ###
                # We then take the length of the match and use that integer value as the ending point of our slice into the rand_hex_string
                # Finally that slice is reversed and then it is used for the substitution, and then added to the replacement_list
                replacement_list.append(
                    re.sub(
                        r"[0-9a-fA-F]{2,}",
                        lambda x: rand_hex_string[: len(x.group(0))][::-1],
                        eachitem,
                    )
                )
            #
            # We create a list of 2 element tuples - the 1st element is the match, the 2nd is the replacement
            find_and_replace_list = [
                (e[1], replacement_list[e[0]]) for e in enumerate(match_list)
            ]
            #
            # Then we iterate over the find/replace list and replace the first occurrence in the string
            for item in find_and_replace_list:
                obj = obj.replace(item[0], item[1], 1)
            #
            result = obj
        #
        except Exception as e:
            print(f"Received the following error: {e}")
    #
    elif isinstance(obj, list):
        result = [replace_hexadecimal_randomly(e) for e in obj]
    #
    return result

