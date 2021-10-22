# %%
#######################################
def replace_numbers_randomly(obj: str or list):
    """Takes a string of digits or a list of string digits and randomly replaces the string with one of equivalent length but different numbers.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> replace_numbers_randomly('8284689631238')\n
        '2236569931001'

        >>> ##### EXAMPLE 2 #####
        >>> list1 = [
        ...     "353",
        ...     "1618285621506",
        ...     "182711621994",
        ...     "1984",
        ...     "688",
        ...     "4991999",
        ...     "185235691716215851336",
        ...     "14363109411127",
        ...     "14113473",
        ...     "278",
        ... ]

        >>> replace_numbers_randomly(list1)\n
        ['731', '3033930836685', '080458221787', '3767', '791', '9974556', '315271283413189987341', '15505063779172', '73258455', '959']

        >>> replace_numbers_randomly(list1)\n
        ['667', '0195643349706', '653864267435', '8832', '461', '5559864', '284670753127581954314', '78844299667563', '51693294', '775']

        >>> ##### EXAMPLE 3 #####
        >>> text = '''Some of the numbers like 15598429414244 or even 23
        ... have an opportunity to be changed.  Something like 311724444
        ... does as well'''

        >>> replace_numbers_randomly(text)\n
        'Some of the numbers like 81284747012392 or even 00\\nhave an opportunity to be changed.  Something like 239203568\\ndoes as well'

        >>> text\n
        'Some of the numbers like 15598429414244 or even 23\\nhave an opportunity to be changed.  Something like 311724444\\ndoes as well'


    Args:
        obj (object): Reference either a string of digits or a list of string digits

    Returns:
        object: Returns a new string or a new list of strings
    """
    import re
    import random

    if isinstance(obj, str):

        try:

            # We match on each consecutive string of digits
            match_list = re.findall(r"\d+", obj)

            replacement_list = []
            for eachitem in match_list:

                ### FIRST, WE CREATE A BIG STRING OF RANDOM DIGITS ###
                # The elements will be integers ranging from 1 to 100
                lst = list(range(1, 101))

                # From the "lst" of numbers 1 - 100, there will be multiple random choices, the quantity of which is based off of the number given to "k="
                random_list_of_ints = random.choices(lst, k=420)

                # Then we take that list of random numbers and join them together making one long string of digits
                rand_num_string = "".join([str(e) for e in random_list_of_ints])

                ### THEN, WE USE THAT RANDOM STRING OF DIGITS IN OUR SUBSTITUTION ###
                # We then take the length of the match and use that integer value as the ending point of our slice into the rand_num_string
                # Finally that slice is reversed and then it is used for the substitution, and then added to the replacement_list
                replacement_list.append(
                    re.sub(
                        r"\d+",
                        lambda x: rand_num_string[: len(x.group(0))][::-1],
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
        result = [replace_numbers_randomly(e) for e in obj]

    return result

