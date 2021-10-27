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

