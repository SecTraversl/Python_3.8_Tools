# %%
#######################################
def refindall_ipaddress(obj: str or list):
    """Takes a given string or list of strings and returns the IP Addresses in the string.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> myexample = "client 218.19.144.132#19232,client 53.173.21.9#33065,client 132.72.64.130#37534,client 220.65.223.96#30097,client 109.136.221.226#48600,client 165.224.250.158#35500,client 42.187.220.133#34398,client 234.181.156.136#14423,client 248.189.187.101#46930,client 201.75.90.98#13513"

        >>> refindall_ipaddress(myexample)\n
        ['218.19.144.132', '53.173.21.9', '132.72.64.130', '220.65.223.96', '109.136.221.226', '165.224.250.158', '42.187.220.133', '234.181.156.136', '248.189.187.101', '201.75.90.98']

        >>> ##### EXAMPLE 2 #####
        >>> mylist = [
        ...     "IP at some time: 216.90.223.255",
        ...     "Here is another ... 60.231.93.2",
        ...     "178.83.41.251, and this one too",
        ...     "More 105.45.185.55 to come soon",
        ...     "For the win, 101.184.120.113",
        ...     "199.227.198.206 -- looks promising",
        ...     "Possible bogey _ 10.164.142.233",
        ...     "190.253.191.105; coming in with artillery",
        ...     "fast and high 165.179.143.113",
        ...     "one final go +249.64.38.17",
        ... ]

        >>> refindall_ipaddress(mylist)\n
        [['216.90.223.255'], ['60.231.93.2'], ['178.83.41.251'], ['105.45.185.55'], ['101.184.120.113'], ['199.227.198.206'], ['10.164.142.233'], ['190.253.191.105'], ['165.179.143.113'], ['249.64.38.17']]

    References:
        IP Address reg ex matching syntax retrieved from:
        https://www.regular-expressions.info/ip.html

    Args:
        obj (object): Reference a string or list of strings.

    Returns:
        list: Returns a list of strings containing the matched IP Addresses
    """
    import re

    # Syntax retrieved from: https://www.regular-expressions.info/ip.html
    match_syntax = re.compile(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}"
        + r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b"
    )

    if isinstance(obj, str):
        result = re.findall(match_syntax, obj)
    elif isinstance(obj, list):
        result = [refindall_ipaddress(e) for e in obj]

    return result

