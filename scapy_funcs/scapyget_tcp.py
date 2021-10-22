# %%
#######################################
# THIS IS NOT THE SAME AS:  my_pcap.getlayer(TCP)
def scapyget_tcp(packet_list: scapy.plist.PacketList):
    result_list = [ pckt for pckt in packet_list if pckt.haslayer('TCP')]
    return PacketList(result_list)

