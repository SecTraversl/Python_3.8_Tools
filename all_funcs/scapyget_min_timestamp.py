# %%
#######################################
def scapyget_min_timestamp(packet_list: scapy.plist.PacketList):
    smallest_timestamp_in_packetlist = min([pack.time for pack in packet_list])
    return smallest_timestamp_in_packetlist

