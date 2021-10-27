# %%
#######################################
def get_random(thelist: list, samplesize=10):
    import random
    
    results_list = random.choices(thelist, k=samplesize)
    return results_list

