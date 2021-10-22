# %%
#######################################
def scapy_orderby_seqnum(packet_list: scapy.plist.PacketList):
    tcp_only_packetlist = PacketList([ pckt for pckt in packet_list if pckt.haslayer('TCP') ])
    seq_num_sorted = sorted(tcp_only_packetlist, key=lambda x: x.seq)
    return PacketList(seq_num_sorted)

