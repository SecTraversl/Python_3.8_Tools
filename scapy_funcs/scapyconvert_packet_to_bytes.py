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

