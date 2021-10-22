# %%
#######################################
def get_emojis():
    """Retrieves hundreds of emoji glyphs derived from the UTF-8 character table.

    Examples:
        >>> moji = get_emojis()\n
        >>> moji[1540:1547]\n
        '🤠 🤡 🤢 🤣'
    """
    emoji_list_1 = [chr(i) for i in range(127744, 127994)]
    emoji_list_2 = [chr(e) for e in range(128000, 128501)]
    remove_list_for_list_3 = [
        129394,
        129399,
        129400,
        129401,
        129443,
        129444,
        129451,
        129452,
        129453,
        129483,
        129484,
    ]
    emoji_list_3 = [
        chr(e) for e in range(129293, 129536) if e not in remove_list_for_list_3
    ]

    agg_list = emoji_list_1 + emoji_list_2 + emoji_list_3
    one_space_sep_string = " ".join(agg_list)
    return one_space_sep_string

