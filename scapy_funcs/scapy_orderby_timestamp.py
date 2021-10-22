# %%
#######################################
def scapy_orderby_timestamp(packet_list: scapy.plist.PacketList):
    time_sorted = sorted(packet_list, key=lambda x: x.time)
    return PacketList(time_sorted)

