# %%
#######################################
def get_etc_shadow_salt(string: str):
    """Returns the salt found within the line retreived from the /etc/shadow file

    Examples:
        >>> line_from_etc_shadow = 'root:$1$umqC71l2$370xDLmeGD9m4aF/ciIlC.:14425:0:99999:7:::'\n
        >>> get_etc_shadow_salt(line_from_etc_shadow)\n
        'umqC71l2'

    References:
        https://linuxize.com/post/etc-shadow-file/
    """
    (
        username,
        hash_string,
        last_pw_change,
        min_pw_age,
        max_pw_age,
        warn_period,
        exp_date,
    ) = string.split(":")[:-2]
    if "$" in hash_string:
        algorithm, salt, thehash = hash_string.split("$")[1:]
        return salt

    else:
        return "There is no $ in the hash_string value."

