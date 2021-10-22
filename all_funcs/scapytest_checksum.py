# %%
#######################################
def scapytest_checksum(packet_list: scapy.plist.PacketList):
    """For each TCP packet, does a comparison of the current checksum with the correct checksum and returns a tuple of the results where the tuple contents are: (packet_checksum, the_correct_checksum, comparison_results).

    Example:
        >>> frag3_pcap = rdpcap('fragments3.pcap')\n
        >>> thechecksums = [p[TCP].chksum for p in frag3_pcap if p.haslayer(TCP)]
        >>> thechecksums\n
        [49411, 14704, 30718, 46868, 47051, 22598, 13794, 46597, 30297, 45517, 45664, 45663, 20079, 45480, 13135]
        
        >>> from pprint import pprint\n
        >>> results = scapytest_checksum(frag3_pcap)
        >>> pprint(results)\n
        [(49411, 49411, True),\n
        (14704, 28667, False),\n
        (30718, 30718, True),\n
        (46868, 46868, True),\n
        (47051, 47051, True),\n
        (22598, 56833, False),\n
        (13794, 46860, False),\n
        (46597, 46597, True),\n
        (30297, 43252, False),\n
        (45517, 45517, True),\n
        (45664, 45664, True),\n
        (45663, 45663, True),\n
        (20079, 21368, False),\n
        (45480, 45480, True),\n
        (13135, 7058, False)]\n
        >>> thechecksums\n
        [49411, 14704, 30718, 46868, 47051, 22598, 13794, 46597, 30297, 45517, 45664, 45663, 20079, 45480, 13135]
        >>> [p[TCP].chksum for p in frag3_pcap if p.haslayer(TCP)]\n
        [49411, 14704, 30718, 46868, 47051, 22598, 13794, 46597, 30297, 45517, 45664, 45663, 20079, 45480, 13135]

    Args:
        packet_list (scapy.plist.PacketList): Reference an existing PacketList object

    Returns:
        tuple: Returns a tuple of the results
    """
    from copy import deepcopy
    
    def verify_checksum(packet):
        orig_checksum = packet['TCP'].chksum
        del packet['TCP'].chksum
        packet = IP(bytes(packet[IP]))
        recalc_checksum = packet['TCP'].chksum
        comparison = orig_checksum == recalc_checksum
        return (orig_checksum, recalc_checksum, comparison)
        
    temp_copy = deepcopy(packet_list)
    temp_copy = PacketList([p for p in temp_copy if p.haslayer(TCP)])
    
    results_array = []
    
    for eachpacket in temp_copy:
        results_array.append(verify_checksum(eachpacket))
    
    return results_array

