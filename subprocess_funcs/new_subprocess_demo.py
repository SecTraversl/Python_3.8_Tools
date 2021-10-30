# %%
#######################################
def new_subprocess_demo():
    """Here we demonstrate using subprocess to create a child Python process which calls the print() function within that child process.  The output from the print() function is returned as a string by subprocess.

    Example:
        >>> new_subprocess_demo()\n
        'Hello, Guru\\nhow are you?\\n'

    Returns:
        str: Returns a string
    """
    import subprocess
    prochandle = subprocess.Popen("python3 -I -c 'print(\"Hello, Guru\");print(\"how are you?\")'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output,error = prochandle.communicate()
    return output.decode()

