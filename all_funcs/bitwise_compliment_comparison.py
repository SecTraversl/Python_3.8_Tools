# %%
#######################################
def bitwise_compliment_comparison(num: int):
    """Prints a comparison table of the number, its complement (the num * -1), and the

    Args:
        num (int): [description]

    Returns:
        [type]: [description]
    """
    from pprint import pprint

    dict1 = {}
    dict1["num_orig"] = (num, format(num, "08b"))
    dict1["num_neg"] = (num * -1, format(num * -1, "08b"))
    dict1["bitcomp"] = (~num, format(~num, "08b"))
    pprint(list(dict1.items()))

