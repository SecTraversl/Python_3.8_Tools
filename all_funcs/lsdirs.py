# %%
#######################################
def lsdirs(thepath='.', recurse=False):
    import pathlib
    
    path_obj = pathlib.Path(thepath).resolve()
    
    if recurse:
        results = [e.as_posix() for e in path_obj.rglob('*') if e.is_dir()]
    else:
        results = [e.name for e in path_obj.glob('*') if e.is_dir()]
    return results

