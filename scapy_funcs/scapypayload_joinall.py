# %%
#######################################
def scapypayload_joinall(packet_list: scapy.plist.PacketList):
    allpayloads_onestring = b''.join([ p.load for p in packet_list if p.haslayer(Raw) ])
    return allpayloads_onestring

