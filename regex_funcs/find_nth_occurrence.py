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

