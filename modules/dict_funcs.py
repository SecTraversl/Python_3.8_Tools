#######################################
############# DICT FUNCS ##############
#######################################

# %%
#######################################
def dict_merge(dict1: dict, dict2: dict):
    """Merges two dictionaries into one.

    Examples:
        >>> x = {'a': 1, 'b': 2}\n
        >>> y = {'b': 3, 'c': 4}\n
        >>> dict_merge(x, y)\n
        {'a': 1, 'b': 3, 'c': 4}

    References:
        https://www.youtube.com/watch?v=Duexw08KaC8
    """
    return {**dict1, **dict2}

# %%
#######################################
def dict_to_tuple_list(thedict: dict):
    """Takes a Dictionary and converts the .items() into a list of tuples.

    Examples:
    >>> my_dict = {'item1': 'I am a raptor', 'item2': 'eat everything', 'item3': 'Till the appearance of man'}
    >>> my_dict.items()\n
    dict_items([('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')])
    >>> dict_to_tuple_list(my_dict)\n
    [('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')]
    >>> # This has the same effect #
    >>> list(my_dict.items())\n
    [('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')]

    Args:
        thedict (dict): Reference the dictionary

    Returns:
        list: Returns a list of tuples from the .items() method
    """
    my_tuple_list = [(k, v) for k, v in thedict.items()]
    # same as: # list(thedict.items())
    return my_tuple_list

# %%
#######################################
def dict_creation_demo():
    print(
        "We can convert a list of tuples into Dictionary Items: dict( [('key1','val1'), ('key2', 'val2')] "
    )
    was_tuple = dict([("key1", "val1"), ("key2", "val2")])
    print(f"This was a list of Tuples: {was_tuple}\n")
    print(
        "We can convert a list of lists into Dictionary Items: dict( [['key1','val1'], ['key2', 'val2']] "
    )
    was_list = dict([["key1", "val1"], ["key2", "val2"]])
    print(f"This was a list of Lists: {was_list} ")

# %%
#######################################
def access_nested_dict(thedict: dict):
    """Demo of how to access a nested dictionary with a two dictionary comprehensions

    Examples:
        >>> a_dictionary = {
        ...     "1-2017": {
        ...         "Win7": "0.47",
        ...         "Vista": "0.2",
        ...         "NT*": "0.09",
        ...         "WinXP": "0.06",
        ...         "Linux": "0.17",
        ...         "Mac": "0.04",
        ...         "Mobile": "0.26",
        ...     },
        ...     "2-2017": {
        ...         "Win7": "0.48",
        ...         "Vista": "0.28",
        ...         "NT*": "0.07",
        ...         "WinXP": "0.09",
        ...         "Linux": "0.16",
        ...         "Mac": "0.03",
        ...         "Mobile": "0.27",
        ...     },
        ...     "3-2017": {
        ...         "Win7": "0.41",
        ...         "Vista": "0.25",
        ...         "NT*": "0.05",
        ...         "WinXP": "0.05",
        ...         "Linux": "0.1",
        ...         "Mac": "0.04",
        ...         "Mobile": "0.27",
        ...     },
        ... }

        >>> access_nested_dict(a_dictionary)\n
        {'1-2017': {('NT*', '0.09'), ('Vista', '0.2'), ('WinXP', '0.06')},
        '2-2017': {('NT*', '0.07'), ('Vista', '0.28'), ('WinXP', '0.09')},
        '3-2017': {('NT*', '0.05'), ('Vista', '0.25'), ('WinXP', '0.05')}}

    References:
        https://stackoverflow.com/questions/17915117/nested-dictionary-comprehension-python
    """
    comprehension = {
        outer_k: {
            (inner_k, inner_v)
            for inner_k, inner_v in outer_v.items()
            if inner_k in ["Vista", "NT*", "WinXP"]
        }
        for outer_k, outer_v in thedict.items()
    }
    return comprehension

# %%
#######################################
def dict_iterator(thedict: dict):
    """Iterates over the values in a given dictionary.

    Example:
        >>> sessions_pcap = rdpcap('sessions.pcap')\n
        >>> dict_iterator( sessions_pcap.sessions() )\n
        (0, <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>)
        (1, <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>)
        (2, <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>)
        (3, <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>)

    Args:
        thedict (dict): Reference an existing dict object
    """
    counter = 0
    for eachkey in thedict.keys():
        print( (counter, thedict[eachkey]) )
        counter += 1

# %%
#######################################
def sort_dict_by_key(dict1: dict, reverse=False):
    """For a given dictionary, returns a sorted list of tuples for each item based on the value.

    Examples:
        >>> employees = {'Alice' : 100000,
        ...              'Bob' : 99817,
        ...              'Carol' : 122908,
        ...              'Frank' : 88123,
        ...              'Eve' : 93121}

        >>> sort_dict_by_key(employees)\n
        [('Alice', 100000), ('Bob', 99817), ('Carol', 122908), ('Eve', 93121), ('Frank', 88123)]
        >>>
        >>> sort_dict_by_key(employees, reverse=True)\n
        [('Frank', 88123), ('Eve', 93121), ('Carol', 122908), ('Bob', 99817), ('Alice', 100000)]
    """
    if reverse:
        return sorted(dict1.items(), reverse=True)
    else:
        return sorted(dict1.items())

# %%
#######################################
def dict_from_two_lists(keys: list, values: list):
    """Creates a dictionary from a list of keys and a list of values.

    Examples:
        >>> keys = ('bztar', 'gztar', 'tar', 'xztar', 'zip')\n
        >>> values = ('.tbz2', '.tgz', '.tar', '.txz', '.zip')\n
        >>> newdict = dict_from_two_lists(keys, values)\n
        >>> pprint(newdict)\n
        {'bztar': '.tbz2',
        'gztar': '.tgz',
        'tar': '.tar',
        'xztar': '.txz',
        'zip': '.zip'}

    Args:
        keys (list): Reference the keys list
        values (list): Reference the values list

    Returns:
        dict: Returns a dictionary
    """
    result = {k: v for k, v in zip(keys, values)}
    return result

# %%
#######################################
def dict_from_tuple_list(tuple_list: list):
    """Creates a dictionary from a list of 2-element tuples, where each tuple is in the format of (key, value).

    Examples:
        >>> tuple_list = [('item1', 'I am a raptor'), ('item2', 'eat everything'), ('item3', 'Till the appearance of man')]\n
        >>> dict_from_tuple_list(tuple_list)\n
        {'item1': 'I am a raptor', 'item2': 'eat everything', 'item3': 'Till the appearance of man'}
    """
    result = {k: v for k, v in tuple_list}
    return result

# %%
#######################################
def sort_dict_by_value(dict1: dict, reverse=False):
    """For a given dictionary, returns a sorted list of tuples for each item based on the value.

    Examples:
        >>> employees = {'Alice' : 100000,
        ...              'Bob' : 99817,
        ...              'Carol' : 122908,
        ...              'Frank' : 88123,
        ...              'Eve' : 93121}

        >>> sort_dict_by_value(employees)\n
        [('Frank', 88123), ('Eve', 93121), ('Bob', 99817), ('Alice', 100000), ('Carol', 122908)]

        >>> sort_dict_by_value(employees, reverse=True)\n
        [('Carol', 122908), ('Alice', 100000), ('Bob', 99817), ('Eve', 93121), ('Frank', 88123)]

    References:
        https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value?page=1&tab=votes#tab-top
    """
    if reverse:
        return sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    else:
        return sorted(dict1.items(), key=lambda x: x[1])

# %%
#######################################
def sort_dict_by_value_itemgetter(dict1: dict, reverse=False):
    """For a given dictionary, returns a sorted list of tuples for each item based on the value.

    Examples:
        >>> employees = {'Alice' : 100000, 'Bob' : 99817, 'Carol' : 122908, 'Frank' : 88123, 'Eve' : 93121}\n
        >>> sort_dict_by_value_itemgetter(employees)\n
        [('Frank', 88123), ('Eve', 93121), ('Bob', 99817), ('Alice', 100000), ('Carol', 122908)]

        >>> sort_dict_by_value_itemgetter(employees, reverse=True)\n
        [('Carol', 122908), ('Alice', 100000), ('Bob', 99817), ('Eve', 93121), ('Frank', 88123)]

    References:
        https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value?page=1&tab=votes#tab-top
        https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work
    """
    import operator

    if reverse:
        return sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)
    else:
        return sorted(dict1.items(), key=operator.itemgetter(1))

# %%
#######################################
def dict_iterator_itervalues(thedict: dict):
    """Iterates over the values in a given dictionary and further loops over the values.
    
    Example:
        >>> sessions_pcap = rdpcap('sessions.pcap')\n
        >>> dict_iterator_itervalues( sessions_pcap.sessions() )\n
        (0, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=52 id=37579 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3bb8 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470518139 ack=626548773 dataofs=8 reserved=0 flags=FA window=229 chksum=0x6c67 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264020, 910859633))] |>>>)\n
        (1, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=89 id=37576 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3b96 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470517854 ack=626548773 dataofs=8 reserved=0 flags=PA window=229 chksum=0x302c urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264018, 910859633))] |<Raw  load='			of virtually every computer crime' |>>>>)\n
        (2, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=85 id=37566 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3ba4 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470517611 ack=626548773 dataofs=8 reserved=0 flags=PA window=229 chksum=0xd944 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264018, 910859633))] |<Raw  load='			security number, you pay your' |>>>>)\n
        (3, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=109 id=37556 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3b96 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470517283 ack=626548773 dataofs=8 reserved=0 flags=PA window=229 chksum=0xb42a urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264016, 910859633))] |<Raw  load='He opens the file.  Paper rattle marks the silence as he' |>>>>)

    Args:
        thedict (dict): Reference an existing dict object.
    """
    counter = 0
    for eachkey in thedict.keys():  
        for val in thedict[eachkey]:
            print( (counter, val ) )
            counter += 1 

