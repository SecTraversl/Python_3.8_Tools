# %%
#######################################
def remove_falsey_values_in_array(lst: list):
    """Removes falsey values such as 0, '', False, None from the list.

    Examples:
        >>> list_with_falsey = [0, 1, False, 2, '', ' ', 3, 'a', 's', 34, None]\n

        >>> remove_falsey_values_in_array(list_with_falsey)\n
        [1, 2, ' ', 3, 'a', 's', 34]

        >>> filter(bool, list_with_falsey)\n
        <filter object at 0x7f8d02efbd90>

        >>> list( filter(bool, list_with_falsey) )\n
        [1, 2, ' ', 3, 'a', 's', 34]
    """
    return list(filter(bool, lst))

