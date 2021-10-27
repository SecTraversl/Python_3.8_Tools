# %%
#######################################
def scapypayload_contains_pattern(packet_list: scapy.plist.PacketList, thepattern: str, return_packetlist=False, ignorecase=True):
    """For each packet in a given PacketList, if the packet has a Raw layer, this function will look for the given pattern, and will return those payloads containing the pattern (or the full packet if 'return_packetlist = True').

    Examples:
        >>> ##### EXAMPLE 1 #####\n
        >>> web_pcap = rdpcap('web.pcap')\n
        >>> scapypayload_contains_pattern(web_pcap, 'push%20green%20button')\n
        ['POST /hitchhikers-guide-game/hhguide HTTP/1.1\\r\\nHost: talkback.live.bbc.co.uk\\r\\nUser-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:32.0) Gecko/20100101 Firefox/32.0\\r\\nAccept: text/xml\\r\\nAccept-Language: en-US,en;q=0.5\\r\\nAccept-Encoding: gzip, deflate\\r\\nContent-Type: text/xml; charset=UTF-8\\r\\nReferer: hxxp://play.bbc.co.uk/play/pen/g38lb8zppy\\r\\nContent-Length: 825\\r\\nOrigin: hxxp://play.bbc.co.uk\\r\\nConnection: keep-alive\\r\\nPragma: no-cache\\r\\nCache-Control: no-cache\\r\\n\\r\\n<zclient><command>push%20green%20button</command><sessionid>42==</sessionid><version>0.08</version></zclient>']

        >>> ##### EXAMPLE 2 #####\n
        >>> mypacketlist = scapypayload_contains_pattern(web_pcap, 'push%20green%20button', return_packetlist=True)\n
        >>> mypacketlist\n
        <PacketList: TCP:1 UDP:0 ICMP:0 Other:0>
        >>> mypacketlist[0].summary()\n
        'Ether / IP / TCP 74.2.7.198:48905 > 245.64.204.201:http PA / Raw'

    Args:
        packet_list (scapy.plist.PacketList): Reference an exsiting PacketList object
        thepattern (str): Reference a pattern you want to match
        return_packetlist (bool, optional): If you want the full packet with the pattern found in the payload, set this to True. Defaults to False.
        ignorecase (bool, optional): If you want to have a case-sensitive pattern match set this to. Defaults to True.

    Returns:
        object: Returns a list of strings with the matching payloads by default. If 'return_packetlist = True' then a PacketList of packets with the matching payloads is returned.
    """
    import re
    
    # Converting the string pattern to bytes for proper pattern matching of the payload in the packets
    thepattern_bytes = thepattern.encode()
    
    # Specifying case-sensitive or case-insensitive matching, along with the pattern to match
    if ignorecase:
        match_syntax = re.compile(thepattern_bytes, re.IGNORECASE)
    else:
        match_syntax = re.compile(thepattern_bytes)
    
    # For each packet, where the packet has a Raw layer (i.e. the payload exists), get the packets w/ payload that match our pattern within the payload
    keep_list = [p for p in packet_list if p.haslayer(Raw) and re.findall(match_syntax, p.load)]
    
    # If the option of 'return_packetlist' = True, then this function returns the complete list of packets as a PacketList object
    if return_packetlist:
        results = PacketList(keep_list)
    else:
        # Otherwise, the payload of each packet is decoded as a single string and returned in a list
        results = [pl.load.decode() for pl in keep_list]
    
    return results

