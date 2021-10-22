# %%
#######################################
def deep_copy(obj_to_copy: object):
    """Returns a copy.deepcopy() of the given object.

    Example:
        >>> frag3_pcap = rdpcap('fragments3.pcap')
        >>> frag3_pcap\n
        <fragments3.pcap: TCP:15 UDP:0 ICMP:0 Other:114>
        >>> id(frag3_pcap)\n
        140567994637504

        >>> frag3_pcap_copy = deep_copy(frag3_pcap)
        >>> frag3_pcap_copy\n
        <fragments3.pcap: TCP:15 UDP:0 ICMP:0 Other:114>
        >>> id(frag3_pcap_copy)\n
        140568023743440

    Reference:
        https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy

    Args:
        obj_to_copy (object): Reference an existing object

    Returns:
        object: Returns a deepcopy of the given object
    """
    from copy import deepcopy
    return deepcopy(obj_to_copy)

