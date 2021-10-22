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

