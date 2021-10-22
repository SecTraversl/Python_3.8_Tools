# %%
#######################################
def compress_archive(
    thepath: str,
    arch_format=("bztar", "gztar", "tar", "xztar", "zip")[1],
    arch_name=None,
):
    """Creates an archive of a given directory.

    Examples:
        >>> [e for e in ls(names=True) if e.startswith('work')]\n
        ['worksheet_dir']
        >>> compress_archive('worksheet_dir')\n
        >>> [e for e in ls(names=True) if e.startswith('work')]\n
        ['worksheet_dir', 'worksheet_dir.tar.gz']
        >>> compress_archive('worksheet_dir','tar')\n
        >>> [e for e in ls(names=True) if e.startswith('work')]\n
        ['worksheet_dir', 'worksheet_dir.tar', 'worksheet_dir.tar.gz'

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
        thepath (str): Reference the directory you want to archive
        arch_format (str, optional): Use this to specify what archive format to use. Defaults to 'gztar' or .tar.gz as shown here - ("bztar", "gztar", "tar", "xztar", "zip")[1].
        arch_name (str, optional): Use this if you want a different name than what what is produced by "shutil.make_archive()". Defaults to None.
    """
    import pathlib
    import shutil

    # import sys

    path_obj = pathlib.Path(thepath).resolve()

    # shutil.get_archive_formats()
    # shutil.get_unpack_formats()
    archive_lookup_table = {
        "bztar": [".tar.bz2", ".tbz2"],
        "gztar": [".tar.gz", ".tgz"],
        "tar": [".tar"],
        "xztar": [".tar.xz", ".txz"],
        "zip": [".zip"],
    }

    if arch_format in archive_lookup_table:
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

    if arch_name:
        pass
    else:
        # arch_name = pathlib.Path(path_obj.name + extension)
        arch_name = path_obj

    # shutil.make_archive(path_obj, extension, arch_name)
    shutil.make_archive(arch_name, archive_type, path_obj)

