# %%
#######################################
def replace_ipaddress_randomly(obj: str or list):
    """Takes a given string or a list of strings and replaces each IP Address with a randomly generated substitution.

    Examples:
        >>> example\n
        'client 210.52.249.246#19232,client 55.156.45.4#33065,client 189.43.24.227#37534,client 239.68.189.30#30097,client 103.209.157.229#48600,client 162.155.156.194#35500,client 21.186.183.234#34398,client 195.112.201.182#14423,client 229.109.221.127#46930,client 100.70.77.31#13513'

        >>> replace_ipaddress_randomly(example)\n
        'client 184.42.243.125#19232,client 74.230.98.2#33065,client 203.10.69.128#37534,client 176.29.181.74#30097,client 145.234.153.143#48600,client 193.224.213.148#35500,client 77.214.218.163#34398,client 150.197.184.211#14423,client 245.175.122.227#46930,client 125.68.48.34#13513'

        >>> iplist = [
        ...     "210.52.249.246",
        ...     "55.156.45.4",
        ...     "189.43.24.227",
        ...     "239.68.189.30",
        ...     "103.209.157.229",
        ...     "162.155.156.194",
        ...     "21.186.183.234",
        ...     "195.112.201.182",
        ...     "229.109.221.127",
        ...     "100.70.77.31",
        ... ]

        >>> replace_ipaddress_randomly(iplist)\n
        ['242.21.117.149', '24.248.33.9', '199.62.94.229', '197.96.239.66', '132.221.212.220', '182.243.176.207', '52.124.125.221', '170.198.120.180', '242.183.115.107', '117.24.83.16']

    References:
        IP Address reg ex matching syntax retrieved from:
        https://www.regular-expressions.info/ip.html

    Args:
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a string or list of strings with replaced IP Addresses.
    """
    import re
    import random

    # Syntax retrieved from: https://www.regular-expressions.info/ip.html
    match_syntax = re.compile(
        r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        + r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        + r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."
        + r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b"
    )

    single_digits = [str(e) for e in range(1, 10)]
    double_digits = [str(e) for e in range(10, 100)]
    triple_digits = [str(e) for e in range(100, 256)]

    if isinstance(obj, str):
        find_results = re.findall(match_syntax, obj)
        find_replace_list = []

        for ipaddress_sections in find_results:

            orig_ip = ".".join(ipaddress_sections)
            replacement_octets = []

            for octet in ipaddress_sections:
                temp_octet = ""
                if len(octet) == 1:
                    temp_octet = random.choice(single_digits)
                    replacement_octets.append(temp_octet)
                elif len(octet) == 2:
                    temp_octet = random.choice(double_digits)
                    replacement_octets.append(temp_octet)
                elif len(octet) == 3:
                    temp_octet = random.choice(triple_digits)
                    replacement_octets.append(temp_octet)

                replacement_ip = ".".join(replacement_octets)

            find_replace_list.append((orig_ip, replacement_ip))

        # This replacement will replace a particular IP with the same substitution throughout the string
        # Use .replace(match, replacement, 1) if you want a random replacement for each occurrence of a given IP address
        for replacement in find_replace_list:
            obj = re.sub(replacement[0], replacement[1], obj)

        result = obj

    elif isinstance(obj, list):
        result = [replace_ipaddress_randomly(e) for e in obj]

    return result

