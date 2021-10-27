#######################################
############# REGEX FUNCS #############
#######################################

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

# %%
#######################################
def replace_ipaddress_randomly(obj: str or list):
    """Takes a given string or a list of strings and replaces each IP Address with a randomly generated substitution.

    Examples:
        >>> example\n
        'client 210.52.249.246#19232,client 55.156.45.4#33065,client 189.43.24.227#37534,client 239.68.189.30#30097,client 103.209.157.229#48600,client 162.155.156.194#35500,client 21.186.183.234#34398,client 195.112.201.182#14423,client 229.109.221.127#46930,client 100.70.77.31#13513'

        >>> replace_ipaddress_randomly(example)\n
        'client 184.42.243.125#19232,client 74.230.98.2#33065,client 203.10.69.128#37534,client 176.29.181.74#30097,client 145.234.153.143#48600,client 193.224.213.148#35500,client 77.214.218.163#34398,client 150.197.184.211#14423,client 245.175.122.227#46930,client 125.68.48.34#13513'

        >>> iplist = [
        ...     "210.52.249.246",
        ...     "55.156.45.4",
        ...     "189.43.24.227",
        ...     "239.68.189.30",
        ...     "103.209.157.229",
        ...     "162.155.156.194",
        ...     "21.186.183.234",
        ...     "195.112.201.182",
        ...     "229.109.221.127",
        ...     "100.70.77.31",
        ... ]

        >>> replace_ipaddress_randomly(iplist)\n
        ['242.21.117.149', '24.248.33.9', '199.62.94.229', '197.96.239.66', '132.221.212.220', '182.243.176.207', '52.124.125.221', '170.198.120.180', '242.183.115.107', '117.24.83.16']

    References:
        IP Address reg ex matching syntax retrieved from:
        https://www.regular-expressions.info/ip.html

    Args:
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a string or list of strings with replaced IP Addresses.
    """
    import re
    import random

    # Syntax retrieved from: https://www.regular-expressions.info/ip.html
    match_syntax = re.compile(
        r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        + r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        + r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        + r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b"
    )

    single_digits = [str(e) for e in range(1, 10)]
    double_digits = [str(e) for e in range(10, 100)]
    triple_digits = [str(e) for e in range(100, 256)]

    if isinstance(obj, str):
        find_results = re.findall(match_syntax, obj)
        find_replace_list = []

        for ipaddress_sections in find_results:

            orig_ip = ".".join(ipaddress_sections)
            replacement_octets = []

            for octet in ipaddress_sections:
                temp_octet = ""
                if len(octet) == 1:
                    temp_octet = random.choice(single_digits)
                    replacement_octets.append(temp_octet)
                elif len(octet) == 2:
                    temp_octet = random.choice(double_digits)
                    replacement_octets.append(temp_octet)
                elif len(octet) == 3:
                    temp_octet = random.choice(triple_digits)
                    replacement_octets.append(temp_octet)

                replacement_ip = ".".join(replacement_octets)

            find_replace_list.append((orig_ip, replacement_ip))

        # This replacement will replace a particular IP with the same substitution throughout the string
        # Use .replace(match, replacement, 1) if you want a random replacement for each occurrence of a given IP address
        for replacement in find_replace_list:
            obj = re.sub(replacement[0], replacement[1], obj)

        result = obj

    elif isinstance(obj, list):
        result = [replace_ipaddress_randomly(e) for e in obj]

    return result

# %%
#######################################
# This is technically not a Rex Ex function, but it's in-theme with other functions here
def find_and_replace(findlist: str or list, replacelist: str or list, obj: str or list):
    """Takes a string or a list of strings and replaces substrings found in the findlist with those in the replacelist.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> text = "How about something simple"
        >>> find_and_replace("something", "everything", text)\n
        'How about everything simple'

        >>> ##### EXAMPLE 2 #####
        >>> moretext = ["How about something simple", "Or maybe something complex"]
        >>> moretext = ["How about something simple", "Or maybe something complex"]
        >>> find_and_replace("something", "everything", moretext)\n
        ['How about everything simple', 'Or maybe everything complex']

        >>> ##### EXAMPLE 3 #####
        >>> # First we are importing various functions that help us parse the data
        >>> from my_py_funcs.regex_funcs import (
        ...     refind_bookends,
        ...     replace_ipaddress_randomly,
        ...     replace_numbers_randomly,
        ... )

        >>> smallexample = "client 72.192.136.134#64983: query: www.coolhostname8864477.com IN,client 231.12.225.158#32688: query: www.coolhostname2927388.com IN,client 121.189.40.110#32424: query: www.coolhostname9651548.com IN"

        >>> # We create the "find list", which are the substrings we want to replace
        >>> find_list = refind_bookends("query: ", "IN", smallexample, ignorecase=False)
        >>> find_list\n
        ['www.coolhostname8864477.com ', 'www.coolhostname2927388.com ', 'www.coolhostname9651548.com ']

        >>> # Then we create the "replace list", which are the substrings we will use to replace those we found
        >>> replace_list = replace_numbers_randomly(find_list)
        >>> replace_list\n
        ['www.coolhostname0010968.com ', 'www.coolhostname9594644.com ', 'www.coolhostname3977824.com ']
        >>> newstuff = find_and_replace(find_list, replace_list, smallexample)
        >>> newstuff = replace_ipaddress_randomly(newstuff)
        >>> newstuff\n
        'client 90.176.170.125#64983: query: www.coolhostname0010968.com IN,client 165.55.134.210#32688: query: www.coolhostname9594644.com IN,client 194.179.58.197#32424: query: www.coolhostname3977824.com IN'


    Args:
        findlist (object): Reference a substring or list of substrings to find
        replacelist (object): Reference a substring or list of substrings to replace those that were found
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a new string or list of strings
    """

    if isinstance(findlist, str):
        if isinstance(obj, str):
            obj = obj.replace(findlist, replacelist)
            result = obj
        elif isinstance(obj, list):
            result = [find_and_replace(findlist, replacelist, e) for e in obj]

    elif isinstance(findlist, list):
        if isinstance(obj, str):
            for index, item in enumerate(findlist):
                obj = obj.replace(item, replacelist[index])
            result = obj
        elif isinstance(obj, list):
            result = [find_and_replace(findlist, replacelist, e) for e in obj]

    return result

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

# %%
#######################################
def refindall_ssn(obj: str or list):
    """Takes a string or list of strings and pulls out possible Social Security Numbers (SSNs) within the string.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> ssn_list = [
        ...     "131-77-1772",
        ...     "189 58 6514",
        ...     "285552842",
        ...     "396668332",
        ...     "343524281",
        ...     "683 96 1179",
        ...     "993 89 8127",
        ...     "331 65 0902",
        ...     "104-53-7752",
        ...     "626 22 7897",
        ...     "481-56-5808",
        ...     "772 97 1352",
        ...     "235734843",
        ... ]

        >>> refindall_ssn(ssn_list)
        ['131-77-1772', '189-58-6514', '285-55-2842', '396-66-8332', '343-52-4281', '683-96-1179', '993-89-8127', '331-65-0902', '104-53-7752', '626-22-7897', '481-56-5808', '772-97-1352', '235-73-4843']

        >>> ##### EXAMPLE 2 #####
        >>> newdata = "hKedOp M341-31-3346I BlA uNACVG bJzH-o FdkVhlRlkFgAj489 33 0132ho-jUO gdUjp HNVWXUrIkJJ-MzY966678227-hoMa cdhgoAI UONbfjgQWrAP-FsoWT-t522489534sARAtvH-ENXMPazpPY yhwt -m002857865GLm fWX-DYt-Lhqyhj679 13 8344pNmUrXJdGg V eINyF mG-rIs592 76 1624iH j OyPr QbuchOEiPycnC y hGmIJ757 84 6898bBvQDisd-a F c-R-nVm835-16-6964bCLxlBNjTaFgQMQvXrCl434 96 6239MxKZ ThyaFE-CBvBQnEMznbZCxbp928-36-4379mDIb jl sNkdCgPUxgpnypCAeywuD907 82 1576TPMLyYnhrDTqJLzpClNtGUxZIET825216383wllgM q"

        >>> refindall_ssn(newdata)\n
        ['341-31-3346', '489-33-0132', '966-67-8227', '522-48-9534', '002-85-7865', '679-13-8344', '592-76-1624', '757-84-6898', '835-16-6964', '434-96-6239', '928-36-4379', '907-82-1576', '825-21-6383']

    Args:
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a list of SSNs found within the string
    """
    import re

    if isinstance(obj, str):
        match_syntax = re.compile(r"(\d{3})[\s-]?(\d\d)[\s-]?(\d{4})")
        result = re.findall(match_syntax, obj)
        final = ["-".join(e) for e in result]
    elif isinstance(obj, list):
        final = []
        for item in obj:
            match_syntax = re.compile(r"(\d{3})[\s-]?(\d\d)[\s-]?(\d{4})")
            result = re.findall(match_syntax, item)
            final.extend(["-".join(e) for e in result])
    return final

# %%
#######################################
def refindall_ipaddress(obj: str or list):
    """Takes a given string or list of strings and returns the IP Addresses in the string.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> myexample = "client 218.19.144.132#19232,client 53.173.21.9#33065,client 132.72.64.130#37534,client 220.65.223.96#30097,client 109.136.221.226#48600,client 165.224.250.158#35500,client 42.187.220.133#34398,client 234.181.156.136#14423,client 248.189.187.101#46930,client 201.75.90.98#13513"

        >>> refindall_ipaddress(myexample)\n
        ['218.19.144.132', '53.173.21.9', '132.72.64.130', '220.65.223.96', '109.136.221.226', '165.224.250.158', '42.187.220.133', '234.181.156.136', '248.189.187.101', '201.75.90.98']

        >>> ##### EXAMPLE 2 #####
        >>> mylist = [
        ...     "IP at some time: 216.90.223.255",
        ...     "Here is another ... 60.231.93.2",
        ...     "178.83.41.251, and this one too",
        ...     "More 105.45.185.55 to come soon",
        ...     "For the win, 101.184.120.113",
        ...     "199.227.198.206 -- looks promising",
        ...     "Possible bogey _ 10.164.142.233",
        ...     "190.253.191.105; coming in with artillery",
        ...     "fast and high 165.179.143.113",
        ...     "one final go +249.64.38.17",
        ... ]

        >>> refindall_ipaddress(mylist)\n
        [['216.90.223.255'], ['60.231.93.2'], ['178.83.41.251'], ['105.45.185.55'], ['101.184.120.113'], ['199.227.198.206'], ['10.164.142.233'], ['190.253.191.105'], ['165.179.143.113'], ['249.64.38.17']]

    References:
        IP Address reg ex matching syntax retrieved from:
        https://www.regular-expressions.info/ip.html

    Args:
        obj (object): Reference a string or list of strings.

    Returns:
        list: Returns a list of strings containing the matched IP Addresses
    """
    import re

    # Syntax retrieved from: https://www.regular-expressions.info/ip.html
    match_syntax = re.compile(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}"
        + r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b"
    )

    if isinstance(obj, str):
        result = re.findall(match_syntax, obj)
    elif isinstance(obj, list):
        result = [refindall_ipaddress(e) for e in obj]

    return result

# %%
#######################################
def find_nth_occurrence(thestring: str or bytes, pattern: str or bytes, occur_wanted=None, context=50):
    import string
    
    total_found = thestring.count(pattern)
    print(f'\nThere are x number of occurrences: {total_found}\n')
    
    if total_found == 0:
        return None
    
    # If the 'occurrence wanted' is not specified, prompt the user for it
    if not occur_wanted:
        occur_wanted = input('Enter in the number of the occurrence you want (e.g. for the 4th occurrence input the number 4) :  ')

    # We need to get the length of the pattern we are trying to match
    multiplier = len(pattern)
    
    # Our default replacement_character is '~', however if that character exists in the 'pattern' we are searching for, we will choose another ascii character that is NOT in the 'pattern'
    # We have two ways for the evaluation, one is for a 'bytes' string and the other a 'str' object
    if isinstance(pattern, bytes):
        if b'~' in pattern:
            my_ascii_chars = string.printable[:-5]
            for item in my_ascii_chars:
                if item.encode() not in pattern:
                    replacement_character = item.encode()
                    break
        else:
            replacement_character = b'~'
    elif isinstance(pattern, str):
        if '~' in pattern:
            my_ascii_chars = string.printable[:-5]
            for item in my_ascii_chars:
                if item not in pattern:
                    replacement_character = item
                    break
        else:
            replacement_character = '~'
        
    the_replacement_string = replacement_character * multiplier
    
    index_loc = thestring.replace(pattern, the_replacement_string, occur_wanted - 1).index(pattern)
    
    # The context parameter has a default value of 50, but this can be changed
    return thestring[index_loc:index_loc + context]

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

# %%
#######################################
def refindall(thepattern: str, obj: str or list, context=(0, (0, 0))[0], ignorecase=True):
    """Given the object (such as a string or an array of strings), this function will search for thepattern in the object. If context is set, this function will return the number of characters before and after the match as specified by the "context" number.

    Examples:
        >>> text = '''
        ... We spent several years building our own database engine,
        ... Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
        ... service with the same or better durability and availability as
        ... the commercial engines, but at one-tenth of the cost. We were
        ... not surprised when this worked.
        ... '''

        >>> # Find exact matches:
        >>> refindall('sql', text)\n
        ['SQL', 'SQL']

        >>> # Find 25 characters before and after the match
        >>> refindall('sql', text, 25)\n
        ['urora, a fully-managed MySQL and PostgreSQL-compatibl']

        >>> # Do a "Greedy" match - this grabs the whole line where the match occurs
        >>> refindall('.*sql.*', text)\n
        ['Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible']

        >>> # Do a "Non-Greedy" match - this creates a separate element for each match on this single line
        >>> refindall('.*?sql.*?', text)\n
        ['Amazon Aurora, a fully-managed MySQL', ' and PostgreSQL']

        >>> # Here we take our example text and create an array of strings
        >>> text.splitlines()\n
        ['', 'We spent several years building our own database engine,', 'Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible', 'service with the same or better durability and availability as', 'the commercial engines, but at one-tenth of the cost. We were', 'not surprised when this worked.']

        >>> # Now each element in the array is evaluated with the match criteria, in this case we are getting the 5 characters before and after the match
        >>> refindall('the', text.splitlines(), 5)\n
        ['with the same', 'h of the cost']

        >>> # Here we are grabbing the whole element where the match occurs in the array
        >>> refindall('.*the.*', text.splitlines())\n
        ['service with the same or better durability and availability as', 'the commercial engines, but at one-tenth of the cost. We were']

    References:
        https://github.com/finxter/PythonOneLiners/blob/master/book/python_tricks/one_liner_05.py
    """
    import re

    if isinstance(context, int):
        left_context = str(context)
        right_context = str(context)
    elif isinstance(context, tuple):
        left, right = context
        left_context = str(left)
        right_context = str(right)

    if ignorecase:
        match_syntax = re.compile(
            r"(.{" + left_context + r"}" + thepattern + r".{" + right_context + r"})",
            re.IGNORECASE,
        )
    else:
        match_syntax = re.compile(
            r"(.{" + left_context + r"}" + thepattern + r".{" + right_context + r"})"
        )

    if isinstance(obj, str):
        result = re.findall(match_syntax, obj)
    elif isinstance(obj, list):
        result = [refindall(e) for e in obj]

    return result

# %%
#######################################
def refindall_content_between_patterns(obj: str or list, left_pattern: str, right_pattern: str, ignorecase=True):
    """Takes a given string or a list of strings, along with a left_pattern and right_pattern, and returns the substring that exists between the two patterns.
    
    The default search is case-insensitive, but this can be modified by specifying "ignorecase=False".

    Examples:
        >>> thestring = 'client 90.176.170.125#64983: query: www.coolhostname0010968.com IN,client 165.55.134.210#32688: query: www.coolhostname9594644.com IN,client 194.179.58.197#32424: query: www.coolhostname3977824.com IN'\n

        >>> client_ip = refindall_content_between_patterns(thestring, 'client ', '#')\n
        >>> client_ip\n
        ['90.176.170.125', '165.55.134.210', '194.179.58.197']

        >>> dns_query = refindall_content_between_patterns(thestring, 'query: ', ' IN', ignorecase=False)\n
        >>> dns_query\n
        ['www.coolhostname0010968.com', 'www.coolhostname9594644.com', 'www.coolhostname3977824.com']

    Args:
        left_pattern (str): Specify the pattern on the left
        right_pattern (str): Specify a right_pattern delimiter
        obj (object): Reference a string or a list of strings
        ignorecase (bool, optional): Allows the string search to be case-sensitive or case-insensitive. Defaults to True.

    Returns:
        object: Returns the substring or list of substrings between the two delimiters
    """
    import re

    if ignorecase:
        match_syntax = re.compile(left_pattern + r"(.*?)" + right_pattern, re.IGNORECASE)
    else:
        match_syntax = re.compile(left_pattern + r"(.*?)" + right_pattern)

    if isinstance(obj, str):
        result = re.findall(match_syntax, obj)
    elif isinstance(obj, list):
        result = [refindall_content_between_patterns(e) for e in obj]

    return result

# %%
#######################################
def replace_numbers_reversed(obj: str or list):
    """Takes a group of string digits and reverses their order in place.

    Examples:
        >>> replace_numbers_reversed('1984')\n
        '4891'

        >>> from pprint import pprint

        >>> list1 = ['353',
        ...  '1618285621506',
        ...  '182711621994',
        ...  '1984',
        ...  '688',
        ...  '4991999',
        ...  '185235691716215851336',
        ...  '14363109411127',
        ...  '14113473',
        ...  '278']

        >>> test = replace_numbers_reversed(list1)
        >>> pprint(test)\n
        ['353',\n
        '6051265828161',\n
        '499126117281',\n
        '4891',\n
        '886',\n
        '9991994',\n
        '633158512617196532581',\n
        '72111490136341',\n
        '37431141',\n
        '872']

    Args:
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a string with reversed digits, or a list of strings with reversed digits
    """
    import re

    if isinstance(obj, str):
        result = re.sub(r"\d+", lambda x: x.group(0)[::-1], obj)
    elif isinstance(obj, list):
        result = [replace_numbers_reversed(e) for e in obj]

    return result

# %%
#######################################
def notlike(matchlist: list, array: list, andop=False):
    """Returns a list of non-matches in the given array by excluding each object that contains one of the values in the matchlist parameter.

    Examples:
        >>> subdir_list = ['get_random.py',
        ...  'day6_15_payload-by-port.py',
        ...  'worksheet_get_exif.py',
        ...  'worksheet_get_random.py',
        ...  'day6_19_browser-snob.py',
        ...  'day6_12_letterpassword.py',
        ...  'day6_21_exif-tag.py',
        ...  'day6_17_subprocess_ssh.py',
        ...  'day6_16._just_use_split.py']

        >>> notlike('day6',subdir_list)\n
        ['get_random.py', 'worksheet_get_exif.py', 'worksheet_get_random.py']
        >>>
        >>> notlike(['exif','_1'],subdir_list)\n
        ['get_random.py', 'worksheet_get_random.py']

    Args:
        matchlist (list): Submit one or many substrings to exclude
        array (list): This is the list that we want to filter
        andop (bool, optional): This will determine if the matchlist criteria is an "And Operation" or an "Or Operation. Defaults to False (which is the "Or Operation").  Only applies when multiple arguments are used for the "matchlist" parameter

    Returns:
        list: Returns a result list derived after the matchlist exclusions have been made

    References:
        https://stackoverflow.com/questions/469913/regular-expressions-is-there-an-and-operator
        https://stackoverflow.com/questions/3041320/regex-and-operator
        https://stackoverflow.com/questions/717644/regular-expression-that-doesnt-contain-certain-string
    """
    import re

    if isinstance(matchlist, str):
        # matchlist is a single string object
        thecompile = re.compile(rf"^(?!.*{matchlist}).*$")
        result_list = [x for x in array if re.findall(thecompile, x)]
        return result_list
    else:
        if andop:
            # We will be doing an "AND" match or an "And" "Operation"
            match_string = r"(?!.*?" + r".*?)(?!.*?".join(matchlist) + r".*?)"
            # e.g. for the above... ['6_19','6_21','6_24'] turns to: '(?!.*?6_19.*?)(?!.*?6_21.*?)(?!.*?6_24.*?)'
            thecompile = re.compile(rf"^{match_string}.*$")
            # equivalent to: '^(?!.*?6_19.*?)(?!.*?6_21.*?)(?!.*?6_24.*?).*$'
            result_list = [x for x in array if re.findall(thecompile, x)]
            return result_list
        else:
            # We will be doing an "OR" match
            match_string = r"(?!.*" + r"|.*".join(matchlist) + ")"
            # e.g. for the above... ['6_19','6_21','6_24'] turns to: '(?!.*6_19|.*6_21|.*6_24)'
            thecompile = re.compile(rf"^{match_string}.*$")
            # equivalent to: '^(?!.*6_19|.*6_21|.*6_24).*$'
            result_list = [x for x in array if re.findall(thecompile, x)]
            return result_list

# %%
#######################################
def like(matchlist: list, array: list, andop=False):
    """Returns a list of matches in the given array by doing a comparison of each object with the values given to the matchlist parameter.

    Examples:
        >>> subdir_list = ['get_random.py',
        ...  'day6_15_payload-by-port.py',
        ...  'worksheet_get_exif.py',
        ...  'worksheet_get_random.py',
        ...  'day6_19_browser-snob.py',
        ...  'day6_12_letterpassword.py',
        ...  'day6_21_exif-tag.py',
        ...  'day6_17_subprocess_ssh.py',
        ...  'day6_16._just_use_split.py']

        >>> like('day', subdir_list)\n
        ['day6_15_payload-by-port.py', 'day6_19_browser-snob.py', 'day6_12_letterpassword.py', 'day6_21_exif-tag.py', 'day6_17_subprocess_ssh.py', 'day6_16._just_use_split.py']

        >>> like(['get','exif'], subdir_list)\n
        ['get_random.py', 'worksheet_get_exif.py', 'worksheet_get_random.py', 'day6_21_exif-tag.py']

        >>> like(['get','exif'], subdir_list, andop=True)\n
        ['worksheet_get_exif.py']

    Args:
        matchlist (list): Submit one or many substrings to match against
        array (list): This is the list that we want to filter
        andop (bool, optional): This will determine if the matchlist criteria is an "And Operation" or an "Or Operation. Defaults to False (which is the "Or Operation").  Only applies when multiple arguments are used for the "matchlist" parameter

    Returns:
        list: Returns a list of matches

    References:
        https://stackoverflow.com/questions/469913/regular-expressions-is-there-an-and-operator
        https://stackoverflow.com/questions/3041320/regex-and-operator
        https://stackoverflow.com/questions/717644/regular-expression-that-doesnt-contain-certain-string
    """
    import re

    if isinstance(matchlist, str):
        # matchlist is a single string object
        thecompile = re.compile(rf"^(?=.*{matchlist}).*$")
        result_list = [x for x in array if re.findall(thecompile, x)]
        return result_list
    else:
        if andop:
            # We will be doing an "AND" match or an "And" "Operation"
            match_string = r"(?=.*?" + r".*?)(?=.*?".join(matchlist) + r".*?)"
            # e.g. for the above... ['6_19','6_21','6_24'] turns to: '(?=.*?6_19.*?)(?=.*?6_21.*?)(?=.*?6_24.*?)'
            thecompile = re.compile(rf"^{match_string}.*$")
            # equivalent to: '^(?=.*?6_19.*?)(?=.*?6_21.*?)(?=.*?6_24.*?).*$'
            result_list = [x for x in array if re.findall(thecompile, x)]
            return result_list
        else:
            # We will be doing an "OR" match
            match_string = r"(?=.*" + r"|.*".join(matchlist) + ")"
            # e.g. for the above... ['6_19','6_21','6_24'] turns to: '(?=.*6_19|.*6_21|.*6_24)'
            thecompile = re.compile(rf"^{match_string}.*$")
            # equivalent to: '^(?=.*6_19|.*6_21|.*6_24).*$'
            result_list = [x for x in array if re.findall(thecompile, x)]
            return result_list

# %%
#######################################
def refindall_border_demo():
    import re

    example1 = "987!5887315075505 963273979167!1792 424 8829428 758423813480156538725 80338918230792#82063912 *891"
    example2 = "823!03270182 997 868!465#891*0105#46535832231!296!2364#1903 406333702!355536717 1204!827205710879978416468!3357 *711"

    print(
        r'For the first example I will take the string and isolate each sequence of 3 digits surrounded by a "border character" or "\b"',
        "\n",
    )
    print(f"Example1 String: {example1}\n")

    # Here we are specifying each group of 3 digits surrounded by a "border character" or "\b"
    match_syntax1 = re.compile(r"\b\d{3}\b")
    print(f"Using the match syntax: {match_syntax1}")

    result1 = re.findall(match_syntax1, example1)
    print(f"Result for Example #1: {result1}")
    # Output:   Result for Example #1: ['987', '424', '891']

    print("\n\n")

    print(
        r'For the second example I will take the string and isolate each sequence of 4 digits surrounded by a "border character" or "\b"',
        "\n",
    )
    print(f"Example2 String: {example2}\n")

    # Here we are specifying each group of 4 digits surrounded by a "border character" or "\b"
    match_syntax2 = re.compile(r"\b\d{4}\b")
    print(f"Using the match syntax: {match_syntax2}")

    result2 = re.findall(match_syntax2, example2)
    print(f"Result for Example #2: {result2}")
    # Output:   Result for Example #2: ['0105', '2364', '1903', '1204', '3357']

