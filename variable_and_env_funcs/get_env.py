# %%
#######################################
def get_env(env_var=None):
    """Returns the value of a given environment variable, or if no argument is given returns all environment variables and their values.

    Args:
        env_var (str, optional): Reference an environment variable. Defaults to None.

    Returns:
        str: Returns the string value of a given environment variable
    """
    import os
    
    if env_var:
        return os.environ.get(env_var)
    else:
        return os.environ

