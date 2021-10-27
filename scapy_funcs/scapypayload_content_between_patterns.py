# %%
#######################################
def scapypayload_content_between_patterns(packet_list: scapy.plist.PacketList, left_pattern: str, right_pattern: str, return_packetlist=False, ignorecase=True):
    import re
    
    def scapypayload_contains_pattern(packet_list: scapy.plist.PacketList, thepattern: str, return_packetlist=False, ignorecase=True):
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
    
    initial_results = scapypayload_contains_pattern(packet_list, left_pattern)
    
    # Specifying case-sensitive or case-insensitive matching, along with the pattern to match
    if ignorecase:
        match_syntax = re.compile(left_pattern + r'(.*?)' + right_pattern, re.IGNORECASE)
    else:
        match_syntax = re.compile(left_pattern + r'(.*?)' + right_pattern)
    
    # For each item find the matches of the Reg Ex compiled pattern above
    keep_list = []
    [keep_list.extend(re.findall(match_syntax, theresults)) for theresults in initial_results]

    # Otherwise, the payload of each packet is decoded as a single string and returned in a list
    results = keep_list
    
    return results

