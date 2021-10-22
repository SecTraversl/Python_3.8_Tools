# %%
#######################################
def sort_by_multiple_indexes_granular_reverse(lst: list, reverse_age_not_job=False):
    """Demo of how to reverse one column but ensuring the other column is not reversed during the sort

    Examples:
        >>> mylst = [['Nick', 30, 'Doctor'], ['John', 8, 'Student'], ['Paul', 22, 'Car Dealer'], ['Mark', 66, 'Retired'], ['Yolo', 22, 'Student'], ['Mark', 66, 'Doctor']]\n

        >>> sort_by_multiple_indexes_granular_reverse(mylst)\n
        [['Mark', 66, 'Retired'], ['Mark', 66, 'Doctor'], ['Nick', 30, 'Doctor'], ['Paul', 22, 'Car Dealer'], ['Yolo', 22, 'Student'], ['John', 8, 'Student']]

        >>> sort_by_multiple_indexes_granular_reverse(mylst, reverse_age_not_job=True)\n
        [['Mark', 66, 'Doctor'], ['Mark', 66, 'Retired'], ['Nick', 30, 'Doctor'], ['Paul', 22, 'Car Dealer'], ['Yolo', 22, 'Student'], ['John', 8, 'Student']]

    References:
        https://stackoverflow.com/questions/14466068/sort-a-list-of-tuples-by-second-value-reverse-true-and-then-by-key-reverse-fal
        https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work
    """
    # Reverse by age, do not reverse by job title
    if reverse_age_not_job:
        return sorted(lst, key=lambda x: (-x[1], x[2]))
    else:
        # Reverse by age
        return sorted(lst, key=lambda x: (-x[1]))

