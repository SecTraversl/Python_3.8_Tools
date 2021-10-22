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

