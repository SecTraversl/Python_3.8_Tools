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

