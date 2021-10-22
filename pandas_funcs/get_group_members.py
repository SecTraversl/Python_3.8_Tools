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

