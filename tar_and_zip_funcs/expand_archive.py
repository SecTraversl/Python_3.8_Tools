# %%
# #######################################
def expand_archive(
    thepath: str,
    extract_dir=None,
    arch_format=("auto", "bztar", "gztar", "tar", "xztar", "zip")[0],
):
    """Extracts the contents of a given archive

    Examples:
        >>> ls(names=True)\n
        ['worksheet_dir.tar', 'worksheet_dir.tar.gz']

        >>> expand_archive('worksheet_dir.tar.gz','worksheet_dir')\n

        >>> ls(names=True)\n
        ['worksheet_dir', 'worksheet_dir.tar', 'worksheet_dir.tar.gz']

        >>> ls('worksheet_dir',names=True)\n
        ['__pycache__', 'worksheet_match_str_len_with_padding.py', 'worksheet_name_eq_main_demo.py', 'worksheet_pathlib.py', 'worksheet_sets.py', 'worksheet_where_like.py', 'worksheet_xor_strings.py']

    References:
        Using sys.exit() to exit a function if a certain condition occurs
        https://stackoverflow.com/questions/6190776/what-is-the-best-way-to-exit-a-function-which-has-no-return-value-in-python-be

        shutil Archive operations
        https://docs.python.org/3/library/shutil.html#archiving-operations

        Using shutil.make_archive()
        https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory-in-python

        Using shutil.unpack_archive()
        https://stackoverflow.com/questions/3451111/unzipping-files-in-python

        Diff between tar and zip
        https://stackoverflow.com/questions/10540935/what-is-the-difference-between-tar-and-zip

        Diff between .tar, .gz, .zip, .tar.gz
        https://www.quora.com/What-is-the-difference-between-tar-gz-zip-and-tar-gz-in-Linux?share=1

        Other...
        https://stackoverflow.com/questions/3874837/how-do-i-compress-a-folder-with-the-python-gzip-module


    Args:
        thepath (str): Specify the archive you want to expand
        extract_dir (str, optional): Specify the directory to extract the files to. Defaults to None, which means that all archive contents will be extracted to the current working directory
        arch_format (str, optional): If your archive does not end with a known-extension you will want to specify the type of archive format the file is. Defaults to "auto" - meaning that the default expects the archive to end in a well-known extension - ("auto", "bztar", "gztar", "tar", "xztar", "zip")[0].

    """
    import pathlib
    import shutil

    # import sys

    path_obj = pathlib.Path(thepath).resolve()
    # shutil.get_archive_formats()
    # shutil.get_unpack_formats()
    archive_lookup_table = {
        "auto": ["use the built-in process for unpack_archive"],
        "bztar": [".tar.bz2", ".tbz2"],
        "gztar": [".tar.gz", ".tgz"],
        "tar": [".tar"],
        "xztar": [".tar.xz", ".txz"],
        "zip": [".zip"],
    }
    if arch_format == "auto":
        default_behavior = True
    elif arch_format in archive_lookup_table:
        # extension = archive_lookup_table.get(arch_format)
        archive_type = arch_format
    else:
        print(
            'The "arch_format" must be one of the following: ("bztar", "gztar", "tar", "xztar", "zip")'
        )
        return None
        # sys.exit(
        #     'The "arch_format" must be one of the following: ("bztar", "gztar", "tar", "xztar", "zip")'
        # )
    if extract_dir:
        pass
    else:
        extract_dir = "."
    if default_behavior:
        shutil.unpack_archive(path_obj, extract_dir)
    else:
        shutil.unpack_archive(path_obj, extract_dir, archive_type)

