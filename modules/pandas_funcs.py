#######################################
############ PANDAS FUNCS #############
#######################################

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

# %%
#######################################
def get_group_members(group_name=None):
    """Returns a DataFrame containing the local computer's groups, GID, and group members.

    Examples:
        >>> get_group_members()\n
                           0  1     2                  3\n
        0               root  x     0                 []\n
        1             daemon  x     1                 []\n
        2                bin  x     2                 []\n
        3                sys  x     3                 []\n
        4                adm  x     4  [syslog, pengwin]\n
        ..               ... ..   ...                ...\n
        71  systemd-coredump  x   999                 []\n
        72           pengwin  x  1000                 []\n
        73           lightdm  x   133                 []\n
        74     nopasswdlogin  x   134                 []\n
        75          testuser  x  1001                 []\n

    Args:
        group_name (str, optional): Reference the name of a particular group. Defaults to None.

    Returns:
        pandas.core.frame.DataFrame: Returns a pandas DataFrame with the group information.
    """
    import grp
    import pandas as pd

    all_groups = grp.getgrall()
    df = pd.DataFrame(all_groups)
    return df

