# %%
#######################################
def refindall_ssn(obj: str or list):
    """Takes a string or list of strings and pulls out possible Social Security Numbers (SSNs) within the string.

    Examples:
        >>> ##### EXAMPLE 1 #####
        >>> ssn_list = [
        ...     "131-77-1772",
        ...     "189 58 6514",
        ...     "285552842",
        ...     "396668332",
        ...     "343524281",
        ...     "683 96 1179",
        ...     "993 89 8127",
        ...     "331 65 0902",
        ...     "104-53-7752",
        ...     "626 22 7897",
        ...     "481-56-5808",
        ...     "772 97 1352",
        ...     "235734843",
        ... ]

        >>> refindall_ssn(ssn_list)
        ['131-77-1772', '189-58-6514', '285-55-2842', '396-66-8332', '343-52-4281', '683-96-1179', '993-89-8127', '331-65-0902', '104-53-7752', '626-22-7897', '481-56-5808', '772-97-1352', '235-73-4843']

        >>> ##### EXAMPLE 2 #####
        >>> newdata = "hKedOp M341-31-3346I BlA uNACVG bJzH-o FdkVhlRlkFgAj489 33 0132ho-jUO gdUjp HNVWXUrIkJJ-MzY966678227-hoMa cdhgoAI UONbfjgQWrAP-FsoWT-t522489534sARAtvH-ENXMPazpPY yhwt -m002857865GLm fWX-DYt-Lhqyhj679 13 8344pNmUrXJdGg V eINyF mG-rIs592 76 1624iH j OyPr QbuchOEiPycnC y hGmIJ757 84 6898bBvQDisd-a F c-R-nVm835-16-6964bCLxlBNjTaFgQMQvXrCl434 96 6239MxKZ ThyaFE-CBvBQnEMznbZCxbp928-36-4379mDIb jl sNkdCgPUxgpnypCAeywuD907 82 1576TPMLyYnhrDTqJLzpClNtGUxZIET825216383wllgM q"

        >>> refindall_ssn(newdata)\n
        ['341-31-3346', '489-33-0132', '966-67-8227', '522-48-9534', '002-85-7865', '679-13-8344', '592-76-1624', '757-84-6898', '835-16-6964', '434-96-6239', '928-36-4379', '907-82-1576', '825-21-6383']

    Args:
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a list of SSNs found within the string
    """
    import re

    if isinstance(obj, str):
        match_syntax = re.compile(r"(\d{3})[\s-]?(\d\d)[\s-]?(\d{4})")
        result = re.findall(match_syntax, obj)
        final = ["-".join(e) for e in result]
    elif isinstance(obj, list):
        final = []
        for item in obj:
            match_syntax = re.compile(r"(\d{3})[\s-]?(\d\d)[\s-]?(\d{4})")
            result = re.findall(match_syntax, item)
            final.extend(["-".join(e) for e in result])
    return final

