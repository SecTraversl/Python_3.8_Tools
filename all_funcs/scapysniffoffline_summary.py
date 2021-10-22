# %%
#######################################
def scapysniffoffline_summary(pcap_file: str):
    """Prints the summary of each packet in the given .pcap file

    Example:
        >>> scapysniffoffline_summary('temp.pcap')\n
        Ether / IP / TCP 48.11.3.131:ssh > 79.54.2.80:1046 PA / Raw\n
        Ether / IP / TCP 79.54.2.80:1046 > 48.11.3.131:ssh A / Padding\n
        Ether / IP / TCP 48.11.3.131:ssh > 79.54.2.80:1046 PA / Raw\n
        Ether / IP / TCP 79.54.2.80:1046 > 48.11.3.131:ssh PA / Raw\n
        Ether / IP / TCP 48.11.3.131:ssh > 79.54.2.80:1046 PA / Raw\n
        Ether / IP / TCP 79.54.2.80:1046 > 48.11.3.131:ssh A / Padding\n

    Reference:
        https://www.oreilly.com/library/view/mastering-python-for/9781788992510/9b8dcad2-ba6c-410d-93ff-c098ffaffe20.xhtml

    Args:
        pcap_file (str): Reference the path of the .pcap file
    """
    sniff(offline=pcap_file, prn=lambda x:x.summary())

