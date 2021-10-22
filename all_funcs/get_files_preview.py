# %%
#######################################
def get_files_preview(thepath=".", preview_size=40):
    """Returns a tuple containing the file name and the first 40 characters of the file for each file in a given directory. Includes gzip files. Excludes .tar files.

    Examples:
        >>> from pprint import pprint\n

        >>> pprint( previewgzipfiles() )\n
        [('misc_funcs.py', '#######################################\\n'),\n
        ('repl_tricks.py', '# %%\\n###################################'),\n
        ('test_text.txt.gz', "ok\\nso here is some\\n'blah blah'\\nWe are pl"),\n
        ('all_funcs.py', '#######################################\\n'),\n
        ('system_funcs.py', '#######################################\\n'),\n
        ('two_dimension_funcs.py', '#######################################\\n'),\n
        ('test_text.txt', "ok\\nso here is some\\n'blah blah'\\nWe are pl"),\n
        ('string_funcs.py', '#######################################\\n'),\n
        ('regex_funcs.py', '#######################################\\n'),\n
        ('lambda_and_map_examples.py', ''),\n
        ('array_funcs.py', '#######################################\\n'),\n
        ('specific_use_case_funcs.py', '#######################################\\n'),\n
        ('dict_funcs.py', '#######################################\\n'),\n
        ('file_folder_funcs.py', '#######################################\\n'),\n
        ('test.txt', "ok\\nso here is some\\n'blah blah'\\nWe are pl"),\n
        ('notes.py', '# %%\\n###################################'),\n
        ('conversion_encoding_bytes_chr_funcs.py',\n
        '#######################################\\n'),\n
        ('test_copy.txt', "ok\\nso here is some\\n'blah blah'\\nWe are pl")]

    Args:
        thepath (str, optional): Specify the directory. Defaults to ".".
        preview_size (int, optional): Specify the number of characters to preview. Defaults to 40.

    Returns:
        list: Returns a list of tuples where the 1st element is the file name, and the 2nd element is the first 40 characters of the file
    """
    import pathlib
    import gzip

    path_obj = pathlib.Path(thepath).resolve()
    results_preview = []
    for file in path_obj.glob("*"):
        if file.is_file() and ".tar" not in file.name:
            if file.name.endswith(".gz"):
                with gzip.open(file, "rt") as f:
                    preview = f.read()[:preview_size]
                results_preview.append((file.name, preview))
            else:
                results_preview.append((file.name, file.read_text()[:preview_size]))

    return results_preview


previewfiles = get_files_preview

