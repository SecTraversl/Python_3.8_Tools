# %%
#######################################
def scapyremove_duplicate_and_badsum_packets(packet_list: scapy.plist.PacketList):
    """Takes a given PacketList, evaluates each packet, looks for TCP packets that have bad checksums and the TCP packets that have duplicate sequence numbers, and omits the bad checksum and duplicate TCP packets from the returned PacketList.  This tool is simply a combination of "scapyremove_bad_checksum_packets" and then "scapyremove_duplicate_packets".
    
    Examples:
        >>> from pprint import pprint
        
        >>> frag3_pcap = rdpcap('fragments3.pcap')\n
        >>> frag3_pcap_badsum_removed = scapyremove_bad_checksum_packets(frag3_pcap)\n
        >>> frag3_pcap_badsum_duplicates_removed = scapyremove_duplicate_packets(frag3_pcap_badsum_removed)\n

        >>> frag3_pcap_badsum_removed\n
        <PacketList: TCP:9 UDP:0 ICMP:0 Other:114>
        >>> frag3_pcap_badsum_duplicates_removed\n
        <PacketList: TCP:6 UDP:0 ICMP:0 Other:114>

        >>> pprint([p[TCP].seq for p in frag3_pcap_badsum_removed if p.haslayer(TCP)])\n
        [1611997371,\n
        703601939,\n
        1611997372,\n
        703601940,\n
        703601940,\n
        1611997826,\n
        703601940,\n
        703601940,\n
        1611997827]\n
        
        >>> pprint([p[TCP].seq for p in frag3_pcap_badsum_duplicates_removed if p.haslayer(TCP)])\n
        [1611997371, 703601939, 1611997372, 1611997826, 703601940, 1611997827]\n

        >>> pprint([scapy_convert_time(p) for p in frag3_pcap_badsum_removed if p.haslayer(TCP)])\n
        ['2012-05-01 02:37:47.858950',\n
        '2012-05-01 02:37:47.859186',\n
        '2012-05-01 02:37:47.859270',\n
        '2012-05-01 02:37:47.859354',\n
        '2012-05-01 02:37:47.866939',\n
        '2012-05-01 02:37:51.519281',\n
        '2012-05-01 02:37:51.519904',\n
        '2012-05-01 02:37:51.520007',\n
        '2012-05-01 02:37:51.520196']\n
        
        >>> pprint([scapy_convert_time(p) for p in frag3_pcap_badsum_duplicates_removed if p.haslayer(TCP)])\n
        ['2012-05-01 02:37:47.858950',\n
        '2012-05-01 02:37:47.859186',\n
        '2012-05-01 02:37:47.859270',\n
        '2012-05-01 02:37:51.519281',\n
        '2012-05-01 02:37:51.520007',\n
        '2012-05-01 02:37:51.520196']\n

    Args:
        packet_list (scapy.plist.PacketList): Reference a given PacketList object
        
    Returns:
        scapy.plist.PacketList: Returns a PacketList object
    """    
    my_packet_list = packet_list
#    
    def scapyremove_bad_checksum_packets(packet_list: scapy.plist.PacketList):
#        
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
#    
#
    def scapyremove_duplicate_packets(packet_list: scapy.plist.PacketList):
#    
        temp_dict = {}
        non_tcp_packets = []
#        
        for pckt in packet_list:
            if pckt.haslayer(TCP):
                temp_dict[pckt[TCP].seq] = pckt
            else:
                non_tcp_packets.append(pckt)
#            
        deduplicated_tcp_packets = list(temp_dict.values())
#        
        rejoin_deduplicated = non_tcp_packets + deduplicated_tcp_packets
        packetlist_obj = PacketList(rejoin_deduplicated)
        time_sorted_deduplicated_array = sorted(packetlist_obj, key=lambda x: x.time)
#        
        return PacketList(time_sorted_deduplicated_array)
#
#
    packet_list_no_bad_checksum = scapyremove_bad_checksum_packets(my_packet_list)
#    
    packet_list_deduped_no_badsum = scapyremove_duplicate_packets(packet_list_no_bad_checksum)
#    
    return packet_list_deduped_no_badsum

