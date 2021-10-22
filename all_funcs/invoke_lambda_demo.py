# %%
#######################################
def invoke_lambda_demo(*args):
    """Demo of a stand-alone way of using lambda

    Examples:
        >>> invoke_lambda_demo(10, 25, 'blah')\n
        Here is what is happening:
        (lambda x: x + x)(item)

        [20, 50, 'blahblah']

    Returns:
        object: Returns double of the given argument.
    """
    print("Here is what is happening:")
    print("  (lambda x: x + x)(item)")
    print("")
    results = []
    for item in args:
        results.append((lambda x: x + x)(item))
    return results

