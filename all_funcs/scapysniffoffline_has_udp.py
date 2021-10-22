# %%
#######################################
def scapysniffoffline_has_udp(pcap_file: str):
    """Executes a print() of the Source IP addresses for each UDP packet that is found.

    Example:
        >>> scapysniffoffline_has_udp('temp.pcap')\n
        UDP packet sent from 49.22.3.9\n
        UDP packet sent from 49.22.3.9\n

    Args:
        pcap_file (str): Reference a .pcap file
    """
    def scapyfilterer(packetin):
        return packetin.haslayer('UDP')
    def scapyprocessor(packetin):
        print('UDP packet sent from', packetin['IP'].src)
    sniff(offline=pcap_file, prn=scapyprocessor, lfilter=scapyfilterer)

