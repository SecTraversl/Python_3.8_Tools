# %%
#######################################
def ungzip_file(thepath: str, out_filename=None):
    import gzip

    if out_filename:
        pass
    else:
        out_filename = thepath.replace(".gz", "")

    with gzip.open(thepath, "rt") as f_in, open(out_filename, "w") as f_out:
        f_out.writelines(f_in)

