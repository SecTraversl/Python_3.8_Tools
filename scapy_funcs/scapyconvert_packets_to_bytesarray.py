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

