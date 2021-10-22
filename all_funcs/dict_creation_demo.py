# %%
#######################################
def dict_creation_demo():
    print(
        "We can convert a list of tuples into Dictionary Items: dict( [('key1','val1'), ('key2', 'val2')] "
    )
    was_tuple = dict([("key1", "val1"), ("key2", "val2")])
    print(f"This was a list of Tuples: {was_tuple}\n")
    print(
        "We can convert a list of lists into Dictionary Items: dict( [['key1','val1'], ['key2', 'val2']] "
    )
    was_list = dict([["key1", "val1"], ["key2", "val2"]])
    print(f"This was a list of Lists: {was_list} ")

