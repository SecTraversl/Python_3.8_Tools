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

