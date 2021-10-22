# %%
#######################################
def access_nested_dict(thedict: dict):
    """Demo of how to access a nested dictionary with a two dictionary comprehensions

    Examples:
        >>> a_dictionary = {
        ...     "1-2017": {
        ...         "Win7": "0.47",
        ...         "Vista": "0.2",
        ...         "NT*": "0.09",
        ...         "WinXP": "0.06",
        ...         "Linux": "0.17",
        ...         "Mac": "0.04",
        ...         "Mobile": "0.26",
        ...     },
        ...     "2-2017": {
        ...         "Win7": "0.48",
        ...         "Vista": "0.28",
        ...         "NT*": "0.07",
        ...         "WinXP": "0.09",
        ...         "Linux": "0.16",
        ...         "Mac": "0.03",
        ...         "Mobile": "0.27",
        ...     },
        ...     "3-2017": {
        ...         "Win7": "0.41",
        ...         "Vista": "0.25",
        ...         "NT*": "0.05",
        ...         "WinXP": "0.05",
        ...         "Linux": "0.1",
        ...         "Mac": "0.04",
        ...         "Mobile": "0.27",
        ...     },
        ... }

        >>> access_nested_dict(a_dictionary)\n
        {'1-2017': {('NT*', '0.09'), ('Vista', '0.2'), ('WinXP', '0.06')},
        '2-2017': {('NT*', '0.07'), ('Vista', '0.28'), ('WinXP', '0.09')},
        '3-2017': {('NT*', '0.05'), ('Vista', '0.25'), ('WinXP', '0.05')}}

    References:
        https://stackoverflow.com/questions/17915117/nested-dictionary-comprehension-python
    """
    comprehension = {
        outer_k: {
            (inner_k, inner_v)
            for inner_k, inner_v in outer_v.items()
            if inner_k in ["Vista", "NT*", "WinXP"]
        }
        for outer_k, outer_v in thedict.items()
    }
    return comprehension

