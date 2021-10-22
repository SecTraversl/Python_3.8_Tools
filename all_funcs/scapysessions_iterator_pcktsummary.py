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

