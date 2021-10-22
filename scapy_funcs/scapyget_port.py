# %%
#######################################
def scapyget_port(packet_list: scapy.plist.PacketList, port: int, sport=False, dport=False, notin=False):
    if notin:
        if sport and dport:
            print("The defaults of this tool will search for the given port in both the [TCP/UDP].sport and the [TCP/UDP].dport fields.  If you only want to search for 'sport' field OR the 'dport' field use, sport=True or dport=True, respectively (but don't turn them both on).")
        elif sport:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and pckt['TCP'].sport != port ) or ( pckt.haslayer('UDP') and pckt['UDP'].sport != port ) ]
        elif dport:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and pckt['TCP'].dport != port ) or ( pckt.haslayer('UDP') and pckt['UDP'].dport != port ) ]
        else:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and ( pckt['TCP'].sport != port and pckt['TCP'].dport != port ) ) or ( pckt.haslayer('UDP') and ( pckt['UDP'].sport != port and pckt['UDP'].dport != port ) ) ]
    else:
        if sport and dport:
            print("The defaults of this tool will search for the given port in both the [TCP/UDP].sport and the [TCP/UDP].dport fields.  If you only want to search for 'sport' field OR the 'dport' field use, sport=True or dport=True, respectively (but don't turn them both on).")
        elif sport:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and pckt['TCP'].sport == port ) or ( pckt.haslayer('UDP') and pckt['UDP'].sport == port ) ]
        elif dport:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and pckt['TCP'].dport == port ) or ( pckt.haslayer('UDP') and pckt['UDP'].dport == port ) ]
        else:
            result_list = [ pckt for pckt in packet_list if ( pckt.haslayer('TCP') and ( pckt['TCP'].sport == port or pckt['TCP'].dport == port ) ) or ( pckt.haslayer('UDP') and ( pckt['UDP'].sport == port or pckt['UDP'].dport == port ) ) ]
#            
    return PacketList(result_list)

