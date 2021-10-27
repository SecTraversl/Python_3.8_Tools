# %%
#######################################
def scapyconvert_packet_timestamp(the_packet: scapy.layers.l2.Ether):
    """For a given packet, takes the packet.time timestamp and converts it to a human readable string in the form: '%Y-%m-%d %H:%M:%S.%f'

    Examples:
    >>> somepcap = rdpcap('one.pcap')
    >>> somepcap\n
    <one.pcap: TCP:1 UDP:0 ICMP:0 Other:0>
    >>> somepcap[0]\n
    <Ether  'dst=12:2a:ed:f3:9d:ab src=36:fa:5b:2d:a6:7f' type=IPv4 |<IP  version=4 ihl=5 tos=0x8 len=164 id=60884 flags=DF frag=0 ttl=64 proto=tcp chksum=0x28e8 'src=66.12.1.192 dst=44.64.3.56' |<TCP  sport=ssh dport=1046 seq=2569990924 ack=4067611282 dataofs=5 reserved=0 flags=PA window=9617 chksum=0x2426 urgptr=0 |<Raw  load='?\\xa7\\x9eB!>p\\x9aS\\xf2bK\\xe7)\x14\\xe2\\xff*WK\\xfcC\\x98\\xf6J\x04\x14\\x94\x08\\xaa\\xf3\\xa2l\x19I\\x854\\x93F\\xe9\\x98\\xecܞ\\xfet|^,\x1f\\xce\\xf8R\\xbf\\x8d\x16\\xa8\tfF\x07\x07\\x93(\\x880\\xcb\\xda-R\\xbcLt\\xfaF\\x92i>\\x99 \\xb1\\xc6I\\xc5OY\\xf0\\x85\\xb8\x0f/L\\xc0\\x88`\tY\\xb5\\xb7\\xec!\x1c\x7f\\x96\\x8b\\xcf陧\\xee\\xa9uw\\x9d\x05\\xae\\xe3\\x84IK\\x8dn>b' |>>>>

    >>> somepcap[0].time\n
    Decimal('1629217872.080297')

    >>> scapyconvert_packet_timestamp(somepcap[0])\n
    '2021-08-17 09:31:12.080297'

    References:
        # This was where we retrieved the proper syntax for the code:
        https://stackoverflow.com/questions/33812737/getting-time-from-scapy-packet

    Args:
        the_packet (scapy.layers.l2.Ether): Reference a specific packet within a scapy.plist.PacketList object

    Returns:
        [str]: Returns a human-readable string of the date/time of the packet
    """
    from datetime import datetime
#
    the_packet_time = float(the_packet.time)
    human_readable_timestamp = datetime.fromtimestamp(the_packet_time).strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )
    return human_readable_timestamp

