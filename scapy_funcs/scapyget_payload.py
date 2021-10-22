# %%
#######################################
def scapyget_payload(packet_list: scapy.plist.PacketList):
    payload_only_list = [pack.load for pack in packet_list if pack.haslayer("Raw")]
    combined_byte_strings = b"".join(payload_only_list)
    convert_to_strings = combined_byte_strings.decode()
    return convert_to_strings

