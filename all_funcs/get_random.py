# %%
#######################################
def get_random(array=None):
    """The 'get_random' function returns a random list of integers of a random length for the list.

    Examples:
        >>> get_random()\n
        [29, 5, 22, 100, 74, 15, 7, 50, 52, 18, 26, 54, 37, 21, 42, 46, 39, 62, 5, 41, 67, 25, 26, 72, 89, 19]
        >>> get_random()\n
        [28, 87, 92, 87, 18, 24, 49, 90, 9, 37, 75, 43, 36, 92, 82]

        >>> list1\n
        ['353', '1618285621506', '182711621994', '1984', '688', '4991999', '185235691716215851336', '14363109411127', '14113473', '278']

        >>> get_random(list1)\n
        '185235691716215851336'

    References:
        https://www.geeksforgeeks.org/python-select-random-value-from-a-list/

    Returns:
        list: Returns a randomly sized list of random integers.
    """
    import random

    if array:
        # If an array was submitted to the function, get a random value from it
        return random.choice(array)
    else:
        # Here we  create a list of up to 30 elements in size
        size_of_list = random.choice(range(1, 30))
        # The elements will be integers ranging from 1 to 100
        lst = list(range(1, 101))
        # From the "lst" of numbers 1 - 100, there will be multiple random choices, the quantity of which is based off of the number given to "k="
        random_list_of_ints = random.choices(lst, k=size_of_list)
        return random_list_of_ints

