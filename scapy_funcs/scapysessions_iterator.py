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

