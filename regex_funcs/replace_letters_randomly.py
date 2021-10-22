# %%
#######################################
# %%
def replace_letters_randomly(obj: str or list, seed=None):
    """Takes a given string or list of strings, finds each substring of consecutive letters, and randomly replaces substring with randomized letters.

    Examples:
        >>> mylist = ['blah','blahblah','blahblahblah']\n
        >>> replace_letters_randomly(mylist)\n
        ['GHXH', 'jfEVOQQJ', 'iAJAZkoXiqgt']

        >>> mytext = "Please excuse my dear aunt sally"\n
        >>> replace_letters_randomly(mytext)\n
        'zPxYZN WcaXbR Pm ZBwT wCMq HXXvy'

        >>> replace_letters_randomly("My test text", seed=42)\n
        'AQ FhAQ FhAQ'
        >>> replace_letters_randomly("My test text", seed=42)\n
        'AQ FhAQ FhAQ'
        >>> replace_letters_randomly("My test text")\n
        'qK wQsI xCBD'
        >>> replace_letters_randomly("My test text", seed='my secret key')\n
        'Sc wVSc wVSc'
        >>> replace_letters_randomly("My test text", seed='my secret key')\n
        'Sc wVSc wVSc'
        >>> replace_letters_randomly("My test text")\n
        'Ee WHkG turs'

    Args:
        obj (object): Reference a string or list of strings

    Returns:
        object: Returns a modified string or list of strings
    """
    import re
    import random
    from string import ascii_letters

    lowercase = ascii_letters[: len(ascii_letters) // 2]
    uppercase = ascii_letters[len(ascii_letters) // 2 :]

    temp_list = []
    for index, item in enumerate(lowercase):
        temp_list.extend([item, uppercase[index]])

    letters = "".join(temp_list)
    # 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'

    if isinstance(obj, str):
        try:
            # We match on each consecutive string of digits
            match_list = re.findall(r"[A-Za-z]+", obj)

            replacement_list = []
            for eachitem in match_list:

                if seed:
                    if isinstance(seed, int):
                        random.seed(seed)
                    elif isinstance(seed, str):
                        # concat_ordinal = ''.join([str(ord(e)) for e in 'where was you at'])
                        concat_ordinal = "".join([str(ord(e)) for e in seed])
                        int_seed = int(concat_ordinal)
                        random.seed(int_seed)

                ### FIRST, WE CREATE A BIG STRING OF RANDOM LETTERS ###
                # Each character in the string of characters found in the "letters" variable, will be randomly retrieved, making a list of random letters the quantity of which (the size of the list) is based off of the number given to "k="
                random_list_of_letters = random.choices(letters, k=420)

                # Then we take that list of random letters and join them together making one long string of random letters
                rand_letter_string = "".join(random_list_of_letters)

                ### THEN, WE USE THAT RANDOM STRING OF LETTERS IN OUR SUBSTITUTION ###
                # We then take the length of the match and use that integer value as the ending point of our slice into the rand_letter_string
                # Finally that slice is reversed and then it is used for the substitution, and then added to the replacement_list
                replacement_list.append(
                    re.sub(
                        r"[A-Za-z]+",
                        lambda x: rand_letter_string[: len(x.group(0))][::-1],
                        eachitem,
                    )
                )

            # We create a list of 2 element tuples - the 1st element is the match, the 2nd is the replacement
            find_and_replace_list = [
                (e[1], replacement_list[e[0]]) for e in enumerate(match_list)
            ]

            # Then we iterate over the find/replace list and replace the first occurrence in the string
            for item in find_and_replace_list:
                obj = obj.replace(item[0], item[1], 1)

            result = obj

        except Exception as e:
            print(f"Received the following error: {e}")

    elif isinstance(obj, list):
        result = [replace_letters_randomly(e) for e in obj]

    return result

