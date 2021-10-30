# %%
#######################################
def scapyget_hexraw(packet_list: scapy.plist.PacketList):
    """Prints a summary view of the packets, including sections of the upper layers payload.

    Example:
        >>> ncat_pcap = rdpcap('ncat.pcap')\n
        >>> scapyget_hexraw(ncat_pcap)\n
        0000 12:23:47.642055 Ether / IP / TCP 127.0.0.1:52253 > 127.0.0.1:9898 S\n
        0001 12:23:47.642067 Ether / IP / TCP 127.0.0.1:9898 > 127.0.0.1:52253 SA\n
        0002 12:23:47.642083 Ether / IP / TCP 127.0.0.1:52253 > 127.0.0.1:9898 A\n
        0003 12:23:50.163506 Ether / IP / TCP 127.0.0.1:52253 > 127.0.0.1:9898 PA / Raw\n
        0000  48 65 6C 6C 6F 0A                                Hello.\n
        0004 12:23:50.163534 Ether / IP / TCP 127.0.0.1:9898 > 127.0.0.1:52253 A\n
        0005 12:23:53.305331 Ether / IP / TCP 127.0.0.1:52253 > 127.0.0.1:9898 PA / Raw\n
        0000  48 6F 77 61 72 65 79 6F 75 0A                    Howareyou.\n
        0006 12:23:53.305357 Ether / IP / TCP 127.0.0.1:9898 > 127.0.0.1:52253 A\n
        0007 12:23:57.918808 Ether / IP / TCP 127.0.0.1:52253 > 127.0.0.1:9898 PA / Raw\n
        0000  68 61 76 65 79 6F 75 62 65 65 6E 61 6C 72 69 67  haveyoubeenalrig\n
        0010  68 74 0A                                         ht.\n

    Args:
        packet_list (scapy.plist.PacketList): Reference an existing scapy PacketList object
    """
    return packet_list.hexraw()

