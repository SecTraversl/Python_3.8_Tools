# %%
#######################################
def sort_by_multiple_indexes(lst: list, *index_nums: int, reverse=False):
    """With a two dimensional array, returns the rows sorted by one or more column index numbers.

    Example:
        >>> mylst = []
            # create the table (name, age, job)
        >>> mylst.append(["Nick", 30, "Doctor"])
        >>> mylst.append(["John",  8, "Student"])
        >>> mylst.append(["Paul", 22, "Car Dealer"])
        >>> mylst.append(["Mark", 66, "Retired"])
        >>> mylst.append(['Yolo', 22, 'Student'])
        >>> mylst.append(['Mark', 66, 'Doctor'])

        # Sort by the "Name"
        >>> sort_by_multiple_indexes(mylst, 0)\n
        [['John', 8, 'Student'], ['Mark', 66, 'Retired'], ['Mark', 66, 'Doctor'], ['Nick', 30, 'Doctor'], ['Paul', 22, 'Car Dealer'], ['Yolo', 22, 'Student']]

        # Sort by the "Name", then the "Job"
        >>> sort_by_multiple_indexes(mylst, 0,2)\n
        [['John', 8, 'Student'], ['Mark', 66, 'Doctor'], ['Mark', 66, 'Retired'], ['Nick', 30, 'Doctor'], ['Paul', 22, 'Car Dealer'], ['Yolo', 22, 'Student']]

        # Sort by the "Job"
        >>> sort_by_multiple_indexes(mylst, 2)\n
        [['Paul', 22, 'Car Dealer'], ['Nick', 30, 'Doctor'], ['Mark', 66, 'Doctor'], ['Mark', 66, 'Retired'], ['John', 8, 'Student'], ['Yolo', 22, 'Student']]

        # Sort by the "Job", then the "Age"
        >>> sort_by_multiple_indexes(mylst, 2,1)\n
        [['Paul', 22, 'Car Dealer'], ['Nick', 30, 'Doctor'], ['Mark', 66, 'Doctor'], ['Mark', 66, 'Retired'], ['John', 8, 'Student'], ['Yolo', 22, 'Student']]

        # Sort by age in descending order
        >>> sort_by_multiple_indexes(mylst, 1, reverse=True)\n
        [['Mark', 66, 'Retired'], ['Mark', 66, 'Doctor'], ['Nick', 30, 'Doctor'], ['Paul', 22, 'Car Dealer'], ['Yolo', 22, 'Student'], ['John', 8, 'Student']]

    References:
        https://stackoverflow.com/questions/18595686/how-do-operator-itemgetter-and-sort-work
        https://docs.python.org/3/library/operator.html#operator.itemgetter
    """
    import operator

    if reverse:
        return sorted(lst, key=operator.itemgetter(*index_nums), reverse=True)
    else:
        return sorted(lst, key=operator.itemgetter(*index_nums))

