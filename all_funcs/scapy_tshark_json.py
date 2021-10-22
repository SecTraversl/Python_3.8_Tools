# %%
#######################################
def scapy_tshark_json(packet_list: scapy.plist.PacketList):
    """Pretty prints the packet fields for a given scapy PacketList object.  Uses the tshark binary, the json python library, and pprint.

    Example:
        >>> udp_pcap = rdpcap('udp.pcap')\n
        >>> scapy_tshark_json(udp_pcap)\n
        [{'_index': 'packets-2021-08-17',
        '_score': None,
        '_source': {'layers': {'data': {'data.data': '01:00:00:00', 'data.len': '4'},
                                'eth': {'eth.dst': '07:00:6b:09:e1:e2',
                                        'eth.dst_tree': {'eth.addr': '07:00:6b:09:e1:e2',
                                                        'eth.addr.oui': '65630',
                                                        'eth.addr_resolved': 'IPv4mcast_09:e1:e2',
                                                        'eth.dst.ig': '1',
                                                        'eth.dst.lg': '0',
                                                        'eth.dst.oui': '65630',
                                                        'eth.dst_resolved': 'IPv4mcast_09:e1:e2',
                                                        'eth.ig': '1',
                                                        'eth.lg': '0'}
                                                        ... ]

    Reference:
        https://scapy.readthedocs.io/en/latest/api/scapy.utils.html#scapy.utils.tcpdump

    Args:
        packet_list (scapy.plist.PacketList): Rerence an existing PacketList object
    """
    import json
    from pprint import pprint
    json_data = json.loads(tcpdump(packet_list, IP(), prog=conf.prog.tshark, args=["-T", "json"], getfd=True))
    pprint(json_data)

