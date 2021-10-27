def scapyremove_bad_checksum_packets(packet_list: scapy.plist.PacketList):
    """Takes a given PacketList, evaluates each packet, looks for TCP packets that have a bad checksum, and omits the TCP packets with the bad checksum from the returned PacketList.

    Example:
        >>> from pprint import pprint\n
        >>> frag3_pcap = rdpcap('fragments3.pcap')\n
        >>> testresults = scapytest_checksum( frag3_pcap )\n
        
        >>> pprint(testresults)\n
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
        
        >>> [print(e) for e in testresults if e[2] == False][-1]\n
        (14704, 28667, False)
        (22598, 56833, False)
        (13794, 46860, False)
        (30297, 43252, False)
        (20079, 21368, False)
        (13135, 7058, False)
        
        >>> [e for e in testresults if e[2] == False].__len__()\n
        6
        >>> new_frag3 = scapyremove_bad_checksum_packets(frag3_pcap)\n
        >>> frag3_pcap.__len__()\n
        129
        >>> new_frag3.__len__()\n
        123
        
    References:
        https://stackoverflow.com/questions/6665844/comparing-tcp-checksums-with-scapy
        https://www.sans.org/cyber-security-courses/automating-information-security-with-python/

    Args:
        packet_list (scapy.plist.PacketList): Reference a given PacketList object
        
    Returns:
        scapy.plist.PacketList: Returns a PacketList object
    """
    def return_good_checksum_packets_only(packet):
        from copy import deepcopy
#        
        temp_packet = deepcopy(packet)
        orig_checksum = temp_packet['TCP'].chksum
        del temp_packet['TCP'].chksum
        temp_packet = IP(bytes(temp_packet[IP]))
        recalc_checksum = temp_packet['TCP'].chksum
        comparison = orig_checksum == recalc_checksum
        if comparison:
            return packet
#            
    final_packet_array = []
#            
    for eachpacket in packet_list:
        if eachpacket.haslayer('TCP'):
            temp_results = return_good_checksum_packets_only(eachpacket)
            if temp_results:
                final_packet_array.append( eachpacket )
        else:
            final_packet_array.append( eachpacket )
#            
    return PacketList(final_packet_array)

