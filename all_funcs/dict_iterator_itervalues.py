# %%
#######################################
def dict_iterator_itervalues(thedict: dict):
    """Iterates over the values in a given dictionary and further loops over the values.
    
    Example:
        >>> sessions_pcap = rdpcap('sessions.pcap')\n
        >>> dict_iterator_itervalues( sessions_pcap.sessions() )\n
        (0, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=52 id=37579 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3bb8 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470518139 ack=626548773 dataofs=8 reserved=0 flags=FA window=229 chksum=0x6c67 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264020, 910859633))] |>>>)\n
        (1, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=89 id=37576 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3b96 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470517854 ack=626548773 dataofs=8 reserved=0 flags=PA window=229 chksum=0x302c urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264018, 910859633))] |<Raw  load='			of virtually every computer crime' |>>>>)\n
        (2, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=85 id=37566 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3ba4 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470517611 ack=626548773 dataofs=8 reserved=0 flags=PA window=229 chksum=0xd944 urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264018, 910859633))] |<Raw  load='			security number, you pay your' |>>>>)\n
        (3, <Ether  dst=00:25:00:4a:2c:85 src=00:0c:29:f0:c5:c4 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=109 id=37556 flags=DF frag=0 ttl=64 proto=tcp chksum=0x3b96 src=253.48.53.56 dst=186.71.51.27 |<TCP  sport=58662 dport=8000 seq=470517283 ack=626548773 dataofs=8 reserved=0 flags=PA window=229 chksum=0xb42a urgptr=0 options=[('NOP', None), ('NOP', None), ('Timestamp', (205264016, 910859633))] |<Raw  load='He opens the file.  Paper rattle marks the silence as he' |>>>>)

    Args:
        thedict (dict): Reference an existing dict object.
    """
    counter = 0
    for eachkey in thedict.keys():  
        for val in thedict[eachkey]:
            print( (counter, val ) )
            counter += 1 

