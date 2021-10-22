# %%
#######################################
def scapyrdpcap_tcp_payloads(pcap_file: str):
    def scapy_orderby_seqnum(packet_list: scapy.plist.PacketList):
        tcp_only_packetlist = PacketList([ pckt for pckt in packet_list if pckt.haslayer('TCP') ])
        seq_num_sorted = sorted(tcp_only_packetlist, key=lambda x: x.seq)
        return PacketList(seq_num_sorted)
#
    def scapyget_payload(packet_list: scapy.plist.PacketList):
        payload_only_list = [pack.load for pack in packet_list if pack.haslayer("Raw")]
        combined_byte_strings = b"".join(payload_only_list)
        convert_to_strings = combined_byte_strings.decode()
        return convert_to_strings
#    
    def main():
        full_pcap_packet_list = rdpcap(pcap_file)
        payload_array = []
        for sess_key in full_pcap_packet_list.sessions().keys():
            orderedby_seqnum = scapy_orderby_seqnum(full_pcap_packet_list.sessions()[sess_key])
            # print( scapyget_payload(orderedby_seqnum) )
            payload_array.append( scapyget_payload(orderedby_seqnum) )
        # print(''.join(payload_array))
        return payload_array
#        
    finalresults = main()
    return finalresults

