# %%
#######################################
def replace_numbers_reversed(obj: str or list):
    """Takes a group of string digits and reverses their order in place.

    Examples:
        >>> replace_numbers_reversed('1984')\n
        '4891'

        >>> from pprint import pprint

        >>> list1 = ['353',
        ...  '1618285621506',
        ...  '182711621994',
        ...  '1984',
        ...  '688',
        ...  '4991999',
        ...  '185235691716215851336',
        ...  '14363109411127',
        ...  '14113473',
        ...  '278']

        >>> test = replace_numbers_reversed(list1)
        >>> pprint(test)\n
        ['353',\n
        '6051265828161',\n
        '499126117281',\n
        '4891',\n
        '886',\n
        '9991994',\n
        '633158512617196532581',\n
        '72111490136341',\n
        '37431141',\n
        '872']

    Args:
        obj (object): Reference a string or a list of strings

    Returns:
        object: Returns a string with reversed digits, or a list of strings with reversed digits
    """
    import re

    if isinstance(obj, str):
        result = re.sub(r"\d+", lambda x: x.group(0)[::-1], obj)
    elif isinstance(obj, list):
        result = [replace_numbers_reversed(e) for e in obj]

    return result

