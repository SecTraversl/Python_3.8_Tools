#######################################
########### PCAP FUNCTIONS ############
#######################################
# %%
#######################################
from scapy.all import *


# %%
#######################################
def scapy_order_by_seqnum(packet_list: scapy.all.PacketList):
    return sorted(packet_list, key=lambda x: x.seq)


# %%
#######################################
def scapy_get_min_timestamp(packet_list: scapy.all.PacketList):
    smallest_timestamp_in_packetlist = min([pack.time for pack in packet_list])
    return smallest_timestamp_in_packetlist


# %%
#######################################
def scapy_reassemble_payload(packet_list: scapy.all.PacketList):
    payload_only_list = [pack.load for pack in packet_list if pack.haslayer("Raw")]
    combined_byte_strings = b"".join(payload_only_list)
    convert_to_strings = combined_byte_strings.decode()
    return convert_to_strings


# %%
#######################################
