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

