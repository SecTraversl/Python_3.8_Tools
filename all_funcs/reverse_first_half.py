# %%
#######################################
def reverse_first_half(string: str):
    """Reverse the first half of a given string.

    Examples:
        >>> reverse_first_half('sandwich')\n
        'dnaswich'
    """
    halfway_point = len(string) // 2
    first_half_reversed = string[:halfway_point][::-1]
    last_half = string[halfway_point:]
    return first_half_reversed + last_half

