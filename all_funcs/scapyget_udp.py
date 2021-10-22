# %%
#######################################
# THIS IS NOT THE SAME AS:  my_pcap.getlayer(UDP)
def scapyget_udp(packet_list: scapy.plist.PacketList):
    result_list = [ pckt for pckt in packet_list if pckt.haslayer('UDP')]
    return PacketList(result_list)

