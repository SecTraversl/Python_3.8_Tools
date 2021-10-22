# %%
#######################################
def scapy_list_protocol(proto=(Ether, Dot1Q, ARP, IP, ICMP, TCP, UDP, Raw)[0]):
    """Lists field information for a given protocol.

Examples:
    >>> ##### EXAMPLE 1 #####
    >>> scapy_list_protocol()
    Displaying field info for protocol: <class 'scapy.layers.l2.Ether'>

    dst        : DestMACField                        = ('None')
    src        : SourceMACField                      = ('None')
    type       : XShortEnumField                     = ('36864')
    
    >>> ##### EXAMPLE 2 #####
    >>> scapy_list_protocol(proto=ARP)
    Displaying field info for protocol: <class 'scapy.layers.l2.ARP'>

    hwtype     : XShortField                         = ('1')
    ptype      : XShortEnumField                     = ('2048')
    hwlen      : FieldLenField                       = ('None')
    plen       : FieldLenField                       = ('None')
    op         : ShortEnumField                      = ('1')
    hwsrc      : MultipleTypeField (SourceMACField, StrFixedLenField) = ('None')
    psrc       : MultipleTypeField (SourceIPField, SourceIP6Field, StrFixedLenField) = ('None')
    hwdst      : MultipleTypeField (MACField, StrFixedLenField) = ('None')
    pdst       : MultipleTypeField (IPField, IP6Field, StrFixedLenField) = ('None')

    Args:
        proto (class, optional): Reference a scapy protocol class.  To see all options use ls(). Defaults to Ether - (Ether, Dot1Q, ARP, IP, ICMP, TCP, UDP, Raw)[0].
    """
    # print(ls(proto))
    print(f"Displaying field info for protocol: {proto}")
    print('')
    ls(proto)
    
    