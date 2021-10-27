#######################################
####### SPECIFIC USE CASE FUNCS #######
#######################################

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

# %%
#######################################
def get_etc_shadow_algorithm(string: str):
    """Returns the salt found within the line retreived from the /etc/shadow file

    Examples:
        >>> line_from_etc_shadow = 'root:$1$umqC71l2$370xDLmeGD9m4aF/ciIlC.:14425:0:99999:7:::'\n
        >>> get_etc_shadow_algorithm(line_from_etc_shadow)\n
        'MD5'

        >>> another_line = 'user:0.7QYSH8yshtus8d:18233:0:99999:7:::'\n
        >>> get_etc_shadow_algorithm(another_line)\n
        'There is no $ in the hash_string value.'

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
        hash_alg_lookup_table = {
            "1": "MD5",
            "2a": "Blowfish",
            "2y": "EksBlowfish",
            "5": "SHA-256",
            "6": "SHA-512",
        }
        algorithm_name = hash_alg_lookup_table.get(algorithm, "Unknown")
        return algorithm_name

    else:
        return "There is no $ in the hash_string value."

