#######################################
############# SCAPY FUNCS #############
#######################################

from scapy.all import *

# %%
#######################################
def scapyget_tcp_port(packet_list: scapy.plist.PacketList, port: int, sport=False, dport=False, notin=False):
    if notin:
        if sport and dport:
            print("The defaults of this tool will search for the given port in both the [TCP].sport and the [TCP].dport fields.  If you only want to search for 'sport' field OR the 'dport' field use, sport=True or dport=True, respectively (but don't turn them both on).")
        elif sport:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('TCP') and ( (pckt['TCP'].sport != port) ) ]
        elif dport:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('TCP') and ( (pckt['TCP'].dport != port) ) ]
        else:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('TCP') and ( (pckt['TCP'].sport != port) and (pckt['TCP'].dport != port) ) ]
    else:
        if sport and dport:
            print("The defaults of this tool will search for the given port in both the [TCP].sport and the [TCP].dport fields.  If you only want to search for 'sport' field OR the 'dport' field use, sport=True or dport=True, respectively (but don't turn them both on).")
        elif sport:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('TCP') and ( (pckt['TCP'].sport == port) ) ]
        elif dport:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('TCP') and ( (pckt['TCP'].dport == port) ) ]
        else:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('TCP') and ( (pckt['TCP'].sport == port) or (pckt['TCP'].dport == port) ) ]
#            
    return PacketList(result_list)

# %%
#######################################
def scapyremove_duplicate_packets(packet_list: scapy.plist.PacketList):
    """Takes a given PacketList, evaluates each packet, looks for TCP packets that have duplicate sequence numbers, and omits the TCP packets with the duplicate sequence numbers from the returned PacketList.
    
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

# %%
#######################################
def scapysniffoffline_summary(pcap_file: str):
    """Prints the summary of each packet in the given .pcap file

    Example:
        >>> scapysniffoffline_summary('temp.pcap')\n
        Ether / IP / TCP 48.11.3.131:ssh > 79.54.2.80:1046 PA / Raw\n
        Ether / IP / TCP 79.54.2.80:1046 > 48.11.3.131:ssh A / Padding\n
        Ether / IP / TCP 48.11.3.131:ssh > 79.54.2.80:1046 PA / Raw\n
        Ether / IP / TCP 79.54.2.80:1046 > 48.11.3.131:ssh PA / Raw\n
        Ether / IP / TCP 48.11.3.131:ssh > 79.54.2.80:1046 PA / Raw\n
        Ether / IP / TCP 79.54.2.80:1046 > 48.11.3.131:ssh A / Padding\n

    Reference:
        https://www.oreilly.com/library/view/mastering-python-for/9781788992510/9b8dcad2-ba6c-410d-93ff-c098ffaffe20.xhtml

    Args:
        pcap_file (str): Reference the path of the .pcap file
    """
    sniff(offline=pcap_file, prn=lambda x:x.summary())

# %%
#######################################
def scapy_orderby_seqnum(packet_list: scapy.plist.PacketList):
    tcp_only_packetlist = PacketList([ pckt for pckt in packet_list if pckt.haslayer('TCP') ])
    seq_num_sorted = sorted(tcp_only_packetlist, key=lambda x: x.seq)
    return PacketList(seq_num_sorted)

# %%
#######################################
def scapyget_udp_port(packet_list: scapy.plist.PacketList, port: int, sport=False, dport=False, notin=False):
    if notin:
        if sport and dport:
            print("The defaults of this tool will search for the given port in both the [UDP].sport and the [UDP].dport fields.  If you only want to search for 'sport' field OR the 'dport' field use, sport=True or dport=True, respectively (but don't turn them both on).")
        elif sport:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('UDP') and ( (pckt['UDP'].sport != port) ) ]
        elif dport:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('UDP') and ( (pckt['UDP'].dport != port) ) ]
        else:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('UDP') and ( (pckt['UDP'].sport != port) and (pckt['UDP'].dport != port) ) ]
    else:
        if sport and dport:
            print("The defaults of this tool will search for the given port in both the [UDP].sport and the [UDP].dport fields.  If you only want to search for 'sport' field OR the 'dport' field use, sport=True or dport=True, respectively (but don't turn them both on).")
        elif sport:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('UDP') and ( (pckt['UDP'].sport == port) ) ]
        elif dport:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('UDP') and ( (pckt['UDP'].dport == port) ) ]
        else:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('UDP') and ( (pckt['UDP'].sport == port) or (pckt['UDP'].dport == port) ) ]
#            
    return PacketList(result_list)

# %%
#######################################
def scapysniffoffline_has_udp(pcap_file: str):
    """Executes a print() of the Source IP addresses for each UDP packet that is found.

    Example:
        >>> scapysniffoffline_has_udp('temp.pcap')\n
        UDP packet sent from 49.22.3.9\n
        UDP packet sent from 49.22.3.9\n

    Args:
        pcap_file (str): Reference a .pcap file
    """
    def scapyfilterer(packetin):
        return packetin.haslayer('UDP')
    def scapyprocessor(packetin):
        print('UDP packet sent from', packetin['IP'].src)
    sniff(offline=pcap_file, prn=scapyprocessor, lfilter=scapyfilterer)

# %%
#######################################
def scapypayload_contains_pattern(packet_list: scapy.plist.PacketList, thepattern: str, return_packetlist=False, ignorecase=True):
    """For each packet in a given PacketList, if the packet has a Raw layer, this function will look for the given pattern, and will return those payloads containing the pattern (or the full packet if 'return_packetlist = True').

    Examples:
        >>> ##### EXAMPLE 1 #####\n
        >>> web_pcap = rdpcap('web.pcap')\n
        >>> scapypayload_contains_pattern(web_pcap, 'push%20green%20button')\n
        ['POST /hitchhikers-guide-game/hhguide HTTP/1.1\\r\\nHost: talkback.live.bbc.co.uk\\r\\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:32.0) Gecko/20100101 Firefox/32.0\\r\\nAccept: text/xml\\r\\nAccept-Language: en-US,en;q=0.5\\r\\nAccept-Encoding: gzip, deflate\\r\\nContent-Type: text/xml; charset=UTF-8\\r\\nReferer: hxxp://play.bbc.co.uk/play/pen/g38lb8zppy\\r\\nContent-Length: 825\\r\\nOrigin: hxxp://play.bbc.co.uk\\r\\nConnection: keep-alive\\r\\nPragma: no-cache\\r\\nCache-Control: no-cache\\r\\n\\r\\n<zclient><command>push%20green%20button</command><sessionid>42==</sessionid><version>0.08</version></zclient>']

        >>> ##### EXAMPLE 2 #####\n
        >>> mypacketlist = scapypayload_contains_pattern(web_pcap, 'push%20green%20button', return_packetlist=True)\n
        >>> mypacketlist\n
        <PacketList: TCP:1 UDP:0 ICMP:0 Other:0>
        >>> mypacketlist[0].summary()\n
        'Ether / IP / TCP 74.2.7.198:48905 > 245.64.204.201:http PA / Raw'

    Args:
        packet_list (scapy.plist.PacketList): Reference an exsiting PacketList object
        thepattern (str): Reference a pattern you want to match
        return_packetlist (bool, optional): If you want the full packet with the pattern found in the payload, set this to True. Defaults to False.
        ignorecase (bool, optional): If you want to have a case-sensitive pattern match set this to. Defaults to True.

    Returns:
        object: Returns a list of strings with the matching payloads by default. If 'return_packetlist = True' then a PacketList of packets with the matching payloads is returned.
    """
    import re
    
    # Converting the string pattern to bytes for proper pattern matching of the payload in the packets
    thepattern_bytes = thepattern.encode()
    
    # Specifying case-sensitive or case-insensitive matching, along with the pattern to match
    if ignorecase:
        match_syntax = re.compile(thepattern_bytes, re.IGNORECASE)
    else:
        match_syntax = re.compile(thepattern_bytes)
    
    # For each packet, where the packet has a Raw layer (i.e. the payload exists), get the packets w/ payload that match our pattern within the payload
    keep_list = [p for p in packet_list if p.haslayer(Raw) and re.findall(match_syntax, p.load)]
    
    # If the option of 'return_packetlist' = True, then this function returns the complete list of packets as a PacketList object
    if return_packetlist:
        results = PacketList(keep_list)
    else:
        # Otherwise, the payload of each packet is decoded as a single string and returned in a list
        results = [pl.load.decode() for pl in keep_list]
    
    return results

# %%
#######################################
def scapypayload_joinall(packet_list: scapy.plist.PacketList):
    allpayloads_onestring = b''.join([ p.load for p in packet_list if p.haslayer(Raw) ])
    return allpayloads_onestring

# %%
#######################################
def scapyrdpcap_tcp_payloads(pcap_file: str):
    def scapy_orderby_seqnum(packet_list: scapy.plist.PacketList):
        tcp_only_packetlist = PacketList([ pckt for pckt in packet_list if pckt.haslayer('TCP') ])
        seq_num_sorted = sorted(tcp_only_packetlist, key=lambda x: x.seq)
        return PacketList(seq_num_sorted)
#
    def scapyget_payload(packet_list: scapy.plist.PacketList):
        payload_only_list = [pack.load for pack in packet_list if pack.haslayer("Raw")]
        combined_byte_strings = b"".join(payload_only_list)
        convert_to_strings = combined_byte_strings.decode()
        return convert_to_strings
#    
    def main():
        full_pcap_packet_list = rdpcap(pcap_file)
        payload_array = []
        for sess_key in full_pcap_packet_list.sessions().keys():
            orderedby_seqnum = scapy_orderby_seqnum(full_pcap_packet_list.sessions()[sess_key])
            # print( scapyget_payload(orderedby_seqnum) )
            payload_array.append( scapyget_payload(orderedby_seqnum) )
        # print(''.join(payload_array))
        return payload_array
#        
    finalresults = main()
    return finalresults

# %%
#######################################
# THIS IS NOT THE SAME AS:  my_pcap.getlayer(UDP)
def scapyget_udp(packet_list: scapy.plist.PacketList):
    result_list = [ pckt for pckt in packet_list if pckt.haslayer('UDP')]
    return PacketList(result_list)

# %%
#######################################
def scapyget_ip_address(packet_list: scapy.plist.PacketList, ip: str, dst=False, src=False, notin=False):
    """Takes a given PacketList and a partial/full string of an ip address and returns each packet that contains that ip address (or that DOES NOT contain that ip address if the notin=True switch is turned on).

    Example:
        >>> temp_pcap = rdpcap('temp.pcap')\n
        >>> example = scapyget_ip_address(temp_pcap, '185.34.210')\n
        >>> example\n
        <PacketList: TCP:0 UDP:1 ICMP:0 Other:0>
        >>> example[0]\n
        <Ether  dst=b4:38:91:24:c9:d9 src=a8:81:71:e3:22:61 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=32 id=52361 flags=DF frag=0 ttl=1 proto=udp chksum=0xf6a1 src=66.17.1.2 dst=185.34.210.1 |<UDP  sport=58429 dport=10001 len=12 chksum=0x3ce5 |<Raw  load='\x01\x00\x00\x00' |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>>>

    Args:
        packet_list (scapy.plist.PacketList): Reference a PacketList
        ip (str): Reference an ip address
        dst (bool, optional): If you want to only search the [IP].dst field, set dst=True. Defaults to False.
        src (bool, optional): If you want to only search the [IP].src field, set src=True. Defaults to False.
        notin (bool, optional): If you want to get every packet that DOES NOT contain a given ip address, set notin=True. Defaults to False.

    Returns:
        scapy.plist.PacketList: Returns a PacketList of the matching packets.
    """
    if notin:
        if dst and src:
            print("The defaults of this tool will search for the given ip address in both the [IP].dst and the [IP].src fields.  If you only want to search for 'dst' field OR the 'src' field use, dst=True or src=True, respectively (but don't turn them both on).")
        elif dst:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('IP') and ( (ip not in pckt['IP'].dst) ) ]
        elif src:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('IP') and ( (ip not in pckt['IP'].src) ) ]
        else:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('IP') and ( (ip not in pckt['IP'].src) and (ip not in pckt['IP'].dst) ) ]
    else:
        if dst and src:
            print("The defaults of this tool will search for the given ip address in both the [IP].dst and the [IP].src fields.  If you only want to search for 'dst' field OR the 'src' field use, dst=True or src=True, respectively (but don't turn them both on).")
        elif dst:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('IP') and ( (ip in pckt['IP'].dst) ) ]
        elif src:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('IP') and ( (ip in pckt['IP'].src) ) ]
        else:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('IP') and ( (ip in pckt['IP'].src) or (ip in pckt['IP'].dst) ) ]
#
    return PacketList(result_list)

# %%
#######################################
def scapyconvert_packet_to_bytes(the_packet: scapy.layers.l2.Ether):
    """Takes a packet and returns the 'bytes' string conversion of it.
    
    Example:
        >>> ncat_pcap = rdpcap('ncat.pcap')\n
        >>> ncat_pcap[0]\n
        <Ether  dst=00:00:00:00:00:00 src=00:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=60 id=59088 flags=DF frag=0 ttl=64 proto=tcp chksum=0x55e9 src=127.0.0.1 dst=127.0.0.1 |<TCP  sport=52253 dport=9898 seq=904206629 ack=0 dataofs=10 reserved=0 flags=S window=43690 chksum=0xfe30 urgptr=0 options=[('MSS', 65495), ('SAckOK', b''), ('Timestamp', (47382517, 0)), ('NOP', None), ('WScale', 7)] |>>>
        >>> single_packet_as_bytes = scapyconvert_packet_to_bytes(ncat_pcap[0])
        >>> single_packet_as_bytes\n
        b'\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x08\\x00E\\x00\\x00<\\xe6\\xd0@\\x00@\\x06U\\xe9\\x7f\\x00\\x00\\x01\\x7f\\x00\\x00\\x01\\xcc\\x1d&\\xaa5\\xe5\\x19%\\x00\\x00\\x00\\x00\\xa0\\x02\\xaa\\xaa\\xfe0\\x00\\x00\\x02\\x04\\xff\\xd7\\x04\\x02\\x08\n\\x02\\xd2\\xff\\xf5\\x00\\x00\\x00\\x00\\x01\\x03\\x03\\x07'

    Args:
        the_packet (scapy.layers.l2.Ether): Reference an existing scapy Ether packet

    Returns:
        bytes: Returns a 'bytes' string.
    """
    bytes_string = the_packet.__bytes__()
    return bytes_string

# %%
#######################################
def scapyget_port(packet_list: scapy.plist.PacketList, port: int, sport=False, dport=False, notin=False):
    if notin:
        if sport and dport:
            print("The defaults of this tool will search for the given port in both the [TCP/UDP].sport and the [TCP/UDP].dport fields.  If you only want to search for 'sport' field OR the 'dport' field use, sport=True or dport=True, respectively (but don't turn them both on).")
        elif sport:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and pckt['TCP'].sport != port ) or ( pckt.haslayer('UDP') and pckt['UDP'].sport != port ) ]
        elif dport:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and pckt['TCP'].dport != port ) or ( pckt.haslayer('UDP') and pckt['UDP'].dport != port ) ]
        else:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and ( pckt['TCP'].sport != port and pckt['TCP'].dport != port ) ) or ( pckt.haslayer('UDP') and ( pckt['UDP'].sport != port and pckt['UDP'].dport != port ) ) ]
    else:
        if sport and dport:
            print("The defaults of this tool will search for the given port in both the [TCP/UDP].sport and the [TCP/UDP].dport fields.  If you only want to search for 'sport' field OR the 'dport' field use, sport=True or dport=True, respectively (but don't turn them both on).")
        elif sport:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and pckt['TCP'].sport == port ) or ( pckt.haslayer('UDP') and pckt['UDP'].sport == port ) ]
        elif dport:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and pckt['TCP'].dport == port ) or ( pckt.haslayer('UDP') and pckt['UDP'].dport == port ) ]
        else:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and ( pckt['TCP'].sport == port or pckt['TCP'].dport == port ) ) or ( pckt.haslayer('UDP') and ( pckt['UDP'].sport == port or pckt['UDP'].dport == port ) ) ]
#            
    return PacketList(result_list)

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

# %%
#######################################
def scapyconvert_packet_timestamp(the_packet: scapy.layers.l2.Ether):
    """For a given packet, takes the packet.time timestamp and converts it to a human readable string in the form: '%Y-%m-%d %H:%M:%S.%f'

    Examples:
    >>> somepcap = rdpcap('one.pcap')
    >>> somepcap\n
    <one.pcap: TCP:1 UDP:0 ICMP:0 Other:0>
    >>> somepcap[0]\n
    <Ether  'dst=12:2a:ed:f3:9d:ab src=36:fa:5b:2d:a6:7f' type=IPv4 |<IP  version=4 ihl=5 tos=0x8 len=164 id=60884 flags=DF frag=0 ttl=64 proto=tcp chksum=0x28e8 'src=66.12.1.192 dst=44.64.3.56' |<TCP  sport=ssh dport=1046 seq=2569990924 ack=4067611282 dataofs=5 reserved=0 flags=PA window=9617 chksum=0x2426 urgptr=0 |<Raw  load='?\\xa7\\x9eB!>p\\x9aS\\xf2bK\\xe7)\x14\\xe2\\xff*WK\\xfcC\\x98\\xf6J\x04\x14\\x94\x08\\xaa\\xf3\\xa2l\x19I\\x854\\x93F\\xe9\\x98\\xecܞ\\xfet|^,\x1f\\xce\\xf8R\\xbf\\x8d\x16\\xa8\tfF\x07\x07\\x93(\\x880\\xcb\\xda-R\\xbcLt\\xfaF\\x92i>\\x99 \\xb1\\xc6I\\xc5OY\\xf0\\x85\\xb8\x0f/L\\xc0\\x88`\tY\\xb5\\xb7\\xec!\x1c\x7f\\x96\\x8b\\xcf陧\\xee\\xa9uw\\x9d\x05\\xae\\xe3\\x84IK\\x8dn>b' |>>>>

    >>> somepcap[0].time\n
    Decimal('1629217872.080297')

    >>> scapyconvert_packet_timestamp(somepcap[0])\n
    '2021-08-17 09:31:12.080297'

    References:
        # This was where we retrieved the proper syntax for the code:
        https://stackoverflow.com/questions/33812737/getting-time-from-scapy-packet

    Args:
        the_packet (scapy.layers.l2.Ether): Reference a specific packet within a scapy.plist.PacketList object

    Returns:
        [str]: Returns a human-readable string of the date/time of the packet
    """
    from datetime import datetime
#
    the_packet_time = float(the_packet.time)
    human_readable_timestamp = datetime.fromtimestamp(the_packet_time).strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )
    return human_readable_timestamp

# %%
#######################################
def scapyconvert_bytes_to_packet(bytes_string: bytes):
    """Takes a 'bytes' string that was previously a packet, and reverts that 'bytes' string back to a scapy Ether packet.
    
    Example:
        >>> ncat_pcap = rdpcap('ncat.pcap')\n
        >>> ncat_pcap[0]\n
        <Ether  dst=00:00:00:00:00:00 src=00:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=60 id=59088 flags=DF frag=0 ttl=64 proto=tcp chksum=0x55e9 src=127.0.0.1 dst=127.0.0.1 |<TCP  sport=52253 dport=9898 seq=904206629 ack=0 dataofs=10 reserved=0 flags=S window=43690 chksum=0xfe30 urgptr=0 options=[('MSS', 65495), ('SAckOK', b''), ('Timestamp', (47382517, 0)), ('NOP', None), ('WScale', 7)] |>>>
        >>> single_packet_as_bytes = scapyconvert_packet_to_bytes(ncat_pcap[0])
        >>> single_packet_as_bytes\n
        b'\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x08\\x00E\\x00\\x00<\\xe6\\xd0@\\x00@\\x06U\\xe9\\x7f\\x00\\x00\\x01\\x7f\\x00\\x00\\x01\\xcc\\x1d&\\xaa5\\xe5\\x19%\\x00\\x00\\x00\\x00\\xa0\\x02\\xaa\\xaa\\xfe0\\x00\\x00\\x02\\x04\\xff\\xd7\\x04\\x02\\x08\n\\x02\\xd2\\xff\\xf5\\x00\\x00\\x00\\x00\\x01\\x03\\x03\\x07'

        >>> a_packet_again = scapyconvert_bytes_to_packet(single_packet_as_bytes)\n
        >>> a_packet_again.time\n
        1635296905.106703

    Args:
        bytes_string (bytes): Reference a 'bytes' string that was previously a packet.

    Returns:
        scapy.layers.l2.Ether: Returns a scapy Ether packet object
    """
    thepacket = Ether(bytes_string)
    return thepacket

# %%
#######################################
def scapysessions_overview_print(packet_list: scapy.plist.PacketList):
    """Prints the session (Follow the Stream) overview information found in a scapy PacketList.

    Example:
        >>> temp_pcap = rdpcap('temp.pcap')\n
        >>> temp_pcap\n
        <temp.pcap: TCP:113 UDP:2 ICMP:0 Other:3>

        >>> scapysessions_overview(temp_pcap)\n
        ('TCP 27.72.5.247:22 > 84.67.6.14:1046', <PacketList: TCP:53 UDP:0 ICMP:0 Other:0>)
        ('TCP 84.67.6.14:1046 > 27.72.5.247:22', <PacketList: TCP:60 UDP:0 ICMP:0 Other:0>)
        ('UDP 89.56.3.8:58429 > 105.83.183.4:10001', <PacketList: TCP:0 UDP:1 ICMP:0 Other:0>)
        ('UDP 89.56.3.8:58429 > 108.114.197.208:10001', <PacketList: TCP:0 UDP:1 ICMP:0 Other:0>)
        ('Other', <PacketList: TCP:0 UDP:0 ICMP:0 Other:3>)

    Args:
        packet_list (scapy.plist.PacketList): Reference an existing PacketList object.
    """
    [print(sess) for sess in list(packet_list.sessions().items())][-1]

# %%
#######################################
def scapy_tshark_json(packet_list: scapy.plist.PacketList):
    """Pretty prints the packet fields for a given scapy PacketList object.  Uses the tshark binary, the json python library, and pprint.

    Example:
        >>> udp_pcap = rdpcap('udp.pcap')\n
        >>> scapy_tshark_json(udp_pcap)\n
        [{'_index': 'packets-2021-08-17',
        '_score': None,
        '_source': {'layers': {'data': {'data.data': '01:00:00:00', 'data.len': '4'},
                                'eth': {'eth.dst': '07:00:6b:09:e1:e2',
                                        'eth.dst_tree': {'eth.addr': '07:00:6b:09:e1:e2',
                                                        'eth.addr.oui': '65630',
                                                        'eth.addr_resolved': 'IPv4mcast_09:e1:e2',
                                                        'eth.dst.ig': '1',
                                                        'eth.dst.lg': '0',
                                                        'eth.dst.oui': '65630',
                                                        'eth.dst_resolved': 'IPv4mcast_09:e1:e2',
                                                        'eth.ig': '1',
                                                        'eth.lg': '0'}
                                                        ... ]

    Reference:
        https://scapy.readthedocs.io/en/latest/api/scapy.utils.html#scapy.utils.tcpdump

    Args:
        packet_list (scapy.plist.PacketList): Rerence an existing PacketList object
    """
    import json
    from pprint import pprint
    json_data = json.loads(tcpdump(packet_list, IP(), prog=conf.prog.tshark, args=["-T", "json"], getfd=True))
    pprint(json_data)

# %%
#######################################
# THIS IS NOT THE SAME AS:  my_pcap.getlayer(TCP)
def scapyget_tcp(packet_list: scapy.plist.PacketList):
    result_list = [ pckt for pckt in packet_list if pckt.haslayer('TCP')]
    return PacketList(result_list)

# %%
#######################################
def scapyget_payload(packet_list: scapy.plist.PacketList):
    payload_only_list = [pack.load for pack in packet_list if pack.haslayer("Raw")]
    combined_byte_strings = b"".join(payload_only_list)
    convert_to_strings = combined_byte_strings.decode()
    return convert_to_strings

# %%
#######################################
def scapy_list_protocol(proto=(Ether, Dot1Q, ARP, IP, ICMP, TCP, UDP, Raw)[0]):
    """Lists field information for a given protocol.

Examples:
    >>> ##### EXAMPLE 1 #####
    >>> scapy_list_protocol()
    Displaying field info for protocol: <class 'scapy.layers.l2.Ether'>

    dst        : DestMACField                        = ('None')
    src        : SourceMACField                      = ('None')
    type       : XShortEnumField                     = ('36864')
    
    >>> ##### EXAMPLE 2 #####
    >>> scapy_list_protocol(proto=ARP)
    Displaying field info for protocol: <class 'scapy.layers.l2.ARP'>

    hwtype     : XShortField                         = ('1')
    ptype      : XShortEnumField                     = ('2048')
    hwlen      : FieldLenField                       = ('None')
    plen       : FieldLenField                       = ('None')
    op         : ShortEnumField                      = ('1')
    hwsrc      : MultipleTypeField (SourceMACField, StrFixedLenField) = ('None')
    psrc       : MultipleTypeField (SourceIPField, SourceIP6Field, StrFixedLenField) = ('None')
    hwdst      : MultipleTypeField (MACField, StrFixedLenField) = ('None')
    pdst       : MultipleTypeField (IPField, IP6Field, StrFixedLenField) = ('None')

    Args:
        proto (class, optional): Reference a scapy protocol class.  To see all options use ls(). Defaults to Ether - (Ether, Dot1Q, ARP, IP, ICMP, TCP, UDP, Raw)[0].
    """
    # print(ls(proto))
    print(f"Displaying field info for protocol: {proto}")
    print('')
    ls(proto)
    
    # %%
#######################################
def scapy_tcpdump(packet_list: scapy.plist.PacketList):
    """Basic usage of tcpdump with scapy. Returns the tcdump output in an array.

    Example:
        >>> udp_pcap = rdpcap('udp.pcap')\n
        >>> scapy_tcpdump(udp_pcap)\n
        reading from file -, link-type EN10MB (Ethernet)\n
        ['09:08:15.572656 IP 100.19.239.1.58429 > 100.19.239.8.10001: UDP, length 4', '09:08:15.575544 IP 100.19.239.1.58429 > 255.255.255.255.10001: UDP, length 4']

    Args:
        packet_list (scapy.plist.PacketList): Reference an existing PacketList object

    Returns:
        list: Returns a list of the tcpdump packet output
    """
    bytes_string = tcpdump(packet_list, IP())
    array_of_packets = bytes_string.decode().splitlines()
    return array_of_packets

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

# %%
#######################################
def scapyconvert_packets_to_bytesarray(packet_list: scapy.plist.PacketList):
    """For each packet in a given PacketList, converts that packet to a 'bytes' string.  Returns a list of these 'bytes' strings.

Example:
    >>> ncat_pcap = rdpcap('ncat.pcap')\n
    >>> ncat_pcap[0]\n
    <Ether  dst=00:00:00:00:00:00 src=00:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=60 id=59088 flags=DF frag=0 ttl=64 proto=tcp chksum=0x55e9 src=127.0.0.1 dst=127.0.0.1 |<TCP  sport=52253 dport=9898 seq=904206629 ack=0 dataofs=10 reserved=0 flags=S window=43690 chksum=0xfe30 urgptr=0 options=[('MSS', 65495), ('SAckOK', b''), ('Timestamp', (47382517, 0)), ('NOP', None), ('WScale', 7)] |>>>
    >>> bytes_array = scapyconvert_packets_to_bytesarray(ncat_pcap)\n
    >>> bytes_array[0]\n
    b'\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x08\\x00E\\x00\\x00<\\xe6\\xd0@\\x00@\\x06U\\xe9\\x7f\\x00\\x00\\x01\\x7f\\x00\\x00\\x01\\xcc\\x1d&\\xaa5\\xe5\\x19%\\x00\\x00\\x00\\x00\\xa0\\x02\\xaa\\xaa\\xfe0\\x00\\x00\\x02\\x04\\xff\\xd7\\x04\\x02\\x08\n\\x02\\xd2\\xff\\xf5\\x00\\x00\\x00\\x00\\x01\\x03\\x03\\x07'

    Args:
        packet_list (scapy.plist.PacketList): Reference an existing PacketList object

    Returns:
        list: Returns a list of bytes strings
    """
    bytes_array = [p.__bytes__() for p in packet_list]
    return bytes_array

# %%
#######################################
from scapy.all import *# %%
#######################################
def scapyget_min_timestamp(packet_list: scapy.plist.PacketList):
    smallest_timestamp_in_packetlist = min([pack.time for pack in packet_list])
    return smallest_timestamp_in_packetlist

# %%
#######################################
def scapyconvert_bytesarray_to_packets(bytes_array: list):
    """For each 'bytes' string that was previously a packet, reverts that 'bytes' string to a packet as part of a reconstituted PacketList .

Example:
    >>> ncat_pcap = rdpcap('ncat.pcap')\n
    >>> ncat_pcap[0]\n
    <Ether  dst=00:00:00:00:00:00 src=00:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=60 id=59088 flags=DF frag=0 ttl=64 proto=tcp chksum=0x55e9 src=127.0.0.1 dst=127.0.0.1 |<TCP  sport=52253 dport=9898 seq=904206629 ack=0 dataofs=10 reserved=0 flags=S window=43690 chksum=0xfe30 urgptr=0 options=[('MSS', 65495), ('SAckOK', b''), ('Timestamp', (47382517, 0)), ('NOP', None), ('WScale', 7)] |>>>
    >>> bytes_array = scapyconvert_packets_to_bytesarray(ncat_pcap)\n
    >>> bytes_array[0]\n
    b'\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x08\\x00E\\x00\\x00<\\xe6\\xd0@\\x00@\\x06U\\xe9\\x7f\\x00\\x00\\x01\\x7f\\x00\\x00\\x01\\xcc\\x1d&\\xaa5\\xe5\\x19%\\x00\\x00\\x00\\x00\\xa0\\x02\\xaa\\xaa\\xfe0\\x00\\x00\\x02\\x04\\xff\\xd7\\x04\\x02\\x08\n\\x02\\xd2\\xff\\xf5\\x00\\x00\\x00\\x00\\x01\\x03\\x03\\x07'
    
    >>> packet_list = scapyconvert_bytesarray_to_packets(bytes_array)\n
    >>> packet_list[5]\n
    <Ether  dst=00:00:00:00:00:00 src=00:00:00:00:00:00 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=62 id=59091 flags=DF frag=0 ttl=64 proto=tcp chksum=0x55e4 src=127.0.0.1 dst=127.0.0.1 |<TCP  sport=52253 dport=9898 seq=904206636 ack=248088723 dataofs=8 reserved=0 flags=PA window=342 chksum=0xfe32 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (47383933, 47383148))] |<Raw  load='Howareyou\\n' |>>>>
    >>> packet_list[5].time\n
    1635294905.032475
    >>> packet_list[5].load\n
    b'Howareyou\\n'

    Args:
        bytes_array (list): Reference an existing list of bytes strings (that were previously packets)

    Returns:
        scapy.plist.PacketList: Returns a PacketList object.
    """
    packet_list_array = [Ether(e) for e in bytes_array]
    packet_list = PacketList(packet_list_array)
    return packet_list

# %%
#######################################
def scapysessions_overview(packet_list: scapy.plist.PacketList):
    """Returns a list of tuples with the session (Follow the Stream) overview information found in a scapy PacketList.

    Example:
        >>> temp_pcap = rdpcap('temp.pcap')\n
        >>> temp_pcap\n
        <temp.pcap: TCP:113 UDP:2 ICMP:0 Other:3>
        
        >>> scapysessions_overview(temp_pcap)\n        
        [('TCP 27.72.5.247:22 > 84.67.6.14:1046', <PacketList: TCP:53 UDP:0 ICMP:0 Other:0>), ('TCP 84.67.6.14:1046 > 27.72.5.247:22', <PacketList: TCP:60 UDP:0 ICMP:0 Other:0>), ('UDP 89.56.3.8:58429 > 105.83.183.4:10001', <PacketList: TCP:0 UDP:1 ICMP:0 Other:0>), ('UDP 89.56.3.8:58429 > 108.114.197.208:10001', <PacketList: TCP:0 UDP:1 ICMP:0 Other:0>), ('Other', <PacketList: TCP:0 UDP:0 ICMP:0 Other:3>)]

    Args:
        packet_list (scapy.plist.PacketList): Reference an existing PacketList object.

    Returns:
        list: Returns the key and value summary from the sessions() method in a tuple.
    """
    session_overview_list = [sess for sess in list(packet_list.sessions().items())]
    return session_overview_list

# %%
#######################################
def scapypayload_content_between_patterns(packet_list: scapy.plist.PacketList, left_pattern: str, right_pattern: str, return_packetlist=False, ignorecase=True):
    import re
    
    def scapypayload_contains_pattern(packet_list: scapy.plist.PacketList, thepattern: str, return_packetlist=False, ignorecase=True):
        import re
        
        # Converting the string pattern to bytes for proper pattern matching of the payload in the packets
        thepattern_bytes = thepattern.encode()
        
        # Specifying case-sensitive or case-insensitive matching, along with the pattern to match
        if ignorecase:
            match_syntax = re.compile(thepattern_bytes, re.IGNORECASE)
        else:
            match_syntax = re.compile(thepattern_bytes)
        
        # For each packet, where the packet has a Raw layer (i.e. the payload exists), get the packets w/ payload that match our pattern within the payload
        keep_list = [p for p in packet_list if p.haslayer(Raw) and re.findall(match_syntax, p.load)]
        
        # If the option of 'return_packetlist' = True, then this function returns the complete list of packets as a PacketList object
        if return_packetlist:
            results = PacketList(keep_list)
        else:
            # Otherwise, the payload of each packet is decoded as a single string and returned in a list
            results = [pl.load.decode() for pl in keep_list]
        
        return results
    
    initial_results = scapypayload_contains_pattern(packet_list, left_pattern)
    
    # Specifying case-sensitive or case-insensitive matching, along with the pattern to match
    if ignorecase:
        match_syntax = re.compile(left_pattern + r'(.*?)' + right_pattern, re.IGNORECASE)
    else:
        match_syntax = re.compile(left_pattern + r'(.*?)' + right_pattern)
    
    # For each item find the matches of the Reg Ex compiled pattern above
    keep_list = []
    [keep_list.extend(re.findall(match_syntax, theresults)) for theresults in initial_results]

    # Otherwise, the payload of each packet is decoded as a single string and returned in a list
    results = keep_list
    
    return results

# %%
#######################################
def scapypcapreader_mac_address(pcap_file: str, mac: str, dst=False, src=False, notin=False):
    """Takes a given .pcap file and a partial/full string of a mac address (in the form aa:bb:cc:dd:11:22:33:44) and returns each packet that contains that mac address (or that DOES NOT contain that mac address if the notin=True switch is turned on).

    Example:
        >>> example = scapypcapreader_mac_address('temp.pcap', '64:5a', notin=True)\n
        >>> example\n
        <PacketList: TCP:0 UDP:2 ICMP:0 Other:0>
        >>> example[0]\n
        <Ether  dst=c2:a2:14:31:61:19 src=4c:22:51:3f:8a:72 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=32 id=52361 flags=DF frag=0 ttl=1 proto=udp chksum=0xf6a1 src=66.17.1.2 dst=185.34.210.1 |<UDP  sport=58429 dport=10001 len=12 chksum=0x3ce5 |<Raw  load='\x01\x00\x00\x00' |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>>>

    Args:
        pcap_file (str): Reference a .pcap file
        mac (str): Reference a mac address
        dst (bool, optional): If you want to only search the [Ether].dst field, set dst=True. Defaults to False.
        src (bool, optional): If you want to only search the [Ether].src field, set src=True. Defaults to False.
        notin (bool, optional): If you want to get every packet that DOES NOT contain a given mac address, set notin=True. Defaults to False.

    Returns:
        scapy.plist.PacketList: Returns a PacketList of the matching packets.
    """
    import pathlib
#    
    path_obj = pathlib.Path(pcap_file).resolve().as_posix()
    pcap_reader = PcapReader(path_obj)
#    
    if notin:
        if dst and src:
            print("The defaults of this tool will search for the given mac address in both the [Ether].dst and the [Ether].src fields.  If you only want to search for 'dst' field OR the 'src' field use, dst=True or src=True, respectively (but don't turn them both on).")
        elif dst:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('Ether') and ( (mac not in pckt['Ether'].dst) ) ]
        elif src:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('Ether') and ( (mac not in pckt['Ether'].src) ) ]
        else:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('Ether') and ( (mac not in pckt['Ether'].src) and (mac not in pckt['Ether'].dst) ) ]
    else:
        if dst and src:
            print("The defaults of this tool will search for the given mac address in both the [Ether].dst and the [Ether].src fields.  If you only want to search for 'dst' field OR the 'src' field use, dst=True or src=True, respectively (but don't turn them both on).")
        elif dst:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('Ether') and ( (mac in pckt['Ether'].dst) ) ]
        elif src:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('Ether') and ( (mac in pckt['Ether'].src) ) ]
        else:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('Ether') and ( (mac in pckt['Ether'].src) or (mac in pckt['Ether'].dst) ) ]
#
    return PacketList(result_list)

# %%
#######################################
def scapyget_mac_address(packet_list: scapy.plist.PacketList, mac: str, dst=False, src=False, notin=False):
    """Takes a given PacketList and a partial/full string of a mac address (in the form aa:bb:cc:dd:11:22:33:44) and returns each packet that contains that mac address (or that DOES NOT contain that mac address if the notin=True switch is turned on).

    Example:
        >>> from scapy.all import *\n
        >>> my_packetlist = rdpcap('temp.pcap')\n
        >>> example = scapyget_mac_address(my_packetlist, '64:5a', notin=True)\n
        >>> example\n
        <PacketList: TCP:0 UDP:2 ICMP:0 Other:0>
        >>> example[0]\n
        <Ether  dst=c2:a2:14:31:61:19 src=4c:22:51:3f:8a:72 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=32 id=52361 flags=DF frag=0 ttl=1 proto=udp chksum=0xf6a1 src=66.17.1.2 dst=185.34.210.1 |<UDP  sport=58429 dport=10001 len=12 chksum=0x3ce5 |<Raw  load='\x01\x00\x00\x00' |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>>>


    Args:
        packet_list (scapy.plist.PacketList): Reference a PacketList
        mac (str): Reference a mac address
        dst (bool, optional): If you want to only search the [Ether].dst field, set dst=True. Defaults to False.
        src (bool, optional): If you want to only search the [Ether].src field, set src=True. Defaults to False.
        notin (bool, optional): If you want to get every packet that DOES NOT contain a given mac address, set notin=True. Defaults to False.

    Returns:
        scapy.plist.PacketList: Returns a PacketList of the matching packets.
    """
    if notin:
        if dst and src:
            print("The defaults of this tool will search for the given mac address in both the [Ether].dst and the [Ether].src fields.  If you only want to search for 'dst' field OR the 'src' field use, dst=True or src=True, respectively (but don't turn them both on).")
        elif dst:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('Ether') and ( (mac not in pckt['Ether'].dst) ) ]
        elif src:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('Ether') and ( (mac not in pckt['Ether'].src) ) ]
        else:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('Ether') and ( (mac not in pckt['Ether'].src) and (mac not in pckt['Ether'].dst) ) ]
    else:
        if dst and src:
            print("The defaults of this tool will search for the given mac address in both the [Ether].dst and the [Ether].src fields.  If you only want to search for 'dst' field OR the 'src' field use, dst=True or src=True, respectively (but don't turn them both on).")
        elif dst:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('Ether') and ( (mac in pckt['Ether'].dst) ) ]
        elif src:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('Ether') and ( (mac in pckt['Ether'].src) ) ]
        else:
            result_list = [ pckt for pckt in packet_list if pckt.haslayer('Ether') and ( (mac in pckt['Ether'].src) or (mac in pckt['Ether'].dst) ) ]
#
    return PacketList(result_list)

# %%
#######################################
def scapypcapreader_ip_address(pcap_file: str, ip: str, dst=False, src=False, notin=False):
    """Takes a given .pcap file and a partial/full string of an ip address and returns each packet that contains that ip address (or that DOES NOT contain that ip address if the notin=True switch is turned on).

    Example:
        >>> example = scapypcapreader_ip_address('temp.pcap', '185.34.210')\n
        >>> example\n
        <PacketList: TCP:0 UDP:1 ICMP:0 Other:0>
        >>> example[0]\n
        <Ether  dst=b4:38:91:24:c9:d9 src=a8:81:71:e3:22:61 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=32 id=52361 flags=DF frag=0 ttl=1 proto=udp chksum=0xf6a1 src=66.17.1.2 dst=185.34.210.1 |<UDP  sport=58429 dport=10001 len=12 chksum=0x3ce5 |<Raw  load='\x01\x00\x00\x00' |<Padding  load='\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>>>

    Args:
        pcap_file (str): Reference a .pcap file
        ip (str): Reference an ip address
        dst (bool, optional): If you want to only search the [IP].dst field, set dst=True. Defaults to False.
        src (bool, optional): If you want to only search the [IP].src field, set src=True. Defaults to False.
        notin (bool, optional): If you want to get every packet that DOES NOT contain a given ip address, set notin=True. Defaults to False.

    Returns:
        scapy.plist.PacketList: Returns a PacketList of the matching packets.
    """
    import pathlib
#    
    path_obj = pathlib.Path(pcap_file).resolve().as_posix()
    pcap_reader = PcapReader(path_obj)
#    
    if notin:
        if dst and src:
            print("The defaults of this tool will search for the given ip address in both the [IP].dst and the [IP].src fields.  If you only want to search for 'dst' field OR the 'src' field use, dst=True or src=True, respectively (but don't turn them both on).")
        elif dst:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('IP') and ( (ip not in pckt['IP'].dst) ) ]
        elif src:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('IP') and ( (ip not in pckt['IP'].src) ) ]
        else:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('IP') and ( (ip not in pckt['IP'].src) and (ip not in pckt['IP'].dst) ) ]
    else:
        if dst and src:
            print("The defaults of this tool will search for the given ip address in both the [IP].dst and the [IP].src fields.  If you only want to search for 'dst' field OR the 'src' field use, dst=True or src=True, respectively (but don't turn them both on).")
        elif dst:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('IP') and ( (ip in pckt['IP'].dst) ) ]
        elif src:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('IP') and ( (ip in pckt['IP'].src) ) ]
        else:
            result_list = [ pckt for pckt in pcap_reader if pckt.haslayer('IP') and ( (ip in pckt['IP'].src) or (ip in pckt['IP'].dst) ) ]
#
    return PacketList(result_list)

# %%
#######################################
def scapysessions_iterator(packet_list: scapy.plist.PacketList):
    """Iterates over each session (Follow the Stream) in a scapy PacketList.

    Example:
        >>> sessions_pcap = rdpcap('sessions.pcap')\n
        >>> scapysessions_iterator(sessions_pcap)\n
        <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>
        <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>
        <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>
        <PacketList: TCP:27 UDP:0 ICMP:0 Other:0>

    Args:
        packet_list (scapy.plist.PacketList): Reference an existing PacketList object
    """
    for sess_key in packet_list.sessions().keys():
        session_packet_list = packet_list.sessions()[sess_key]
        print(session_packet_list)

# %%
#######################################
def scapy_orderby_timestamp(packet_list: scapy.plist.PacketList):
    time_sorted = sorted(packet_list, key=lambda x: x.time)
    return PacketList(time_sorted)

# %%
#######################################
def scapysessions_iterator_pcktsummary(packet_list: scapy.plist.PacketList):
    """Iterates over each session (Follow the Stream) in a scapy PacketList and prints the summary of each packet for each session.

    Example:
        >>> sessions_pcap = rdpcap('sessions.pcap')\n
        >>> scapysessions_iterator_pcktsummary(sessions_pcap)\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 FA\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 S\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 A\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 A\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n
        Ether / IP / TCP 172.20.10.14:58662 > 172.20.10.10:8000 PA / Raw\n

    Args:
        packet_list (scapy.plist.PacketList): Reference an existing PacketList object.
    """
    for sess_key in packet_list.sessions().keys():
        session_packet_list = packet_list.sessions()[sess_key]
        [print(pckt.summary()) for pckt in session_packet_list]

