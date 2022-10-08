"""
Function for deterministically creating a single hash for a directory of files,
taking into account only file contents and not filenames.

Usage:

from checksumdir import dirhash

dirhash('/path/to/directory', 'md5')

"""

import hashlib
import logging
import os
import re

import pkg_resources

__version__ = pkg_resources.require("checksumdir")[0].version

HASH_FUNCS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}

_LOGGER = logging.Logger(__name__)


def dirhash(
        dirname,
        hash_method="md5",
        excluded_files=None,
        excluded_extensions=None,
        excluded_dirs=None,
        ignore_hidden=False,
        follow_links=False,
        include_paths=False,
        debug=False,
):
    """

    :param dirname: Need to be an absolute path
    :param hash_method: Supported methods are [md5,sha1,sha256,sha512]
    :param excluded_files:
    :param excluded_extensions:
    :param excluded_dirs:
    :param ignore_hidden:
    :param follow_links:
    :param include_paths:
    :param debug:
    :return:
    """
    hash_func = HASH_FUNCS.get(hash_method)
    if not hash_func:
        raise NotImplementedError("{} not implemented.".format(hash_method))

    if not excluded_files:
        excluded_files = []

    if not excluded_extensions:
        excluded_extensions = []

    if not excluded_dirs:
        excluded_dirs = []

    if not os.path.isdir(dirname):
        raise TypeError("{} is not a directory.".format(dirname))

    hash_values = []
    for root, dirs, files in os.walk(dirname, topdown=True, followlinks=follow_links):
        if ignore_hidden and re.search(r"/\.", root):
            continue

        # Check the directory name against the excluded dirs
        if os.path.split(root)[1] in excluded_dirs:
            if debug:
                _LOGGER.info(f"Skipping root {root} as in -> {excluded_dirs}")
            continue
        sorted_files = sorted(files)

        if debug:
            _LOGGER.info(f"Processing root: {root} files: {sorted_files} dirs: {dirs}")

        for fname in sorted_files:
            if ignore_hidden and fname.startswith("."):
                continue

            if fname.split(".")[-1:][0] in excluded_extensions:
                continue

            if fname in excluded_files:
                continue

            hash_value = _filehash(os.path.join(root, fname), hash_func)
            hash_values.append(hash_value)
            if include_paths:
                hasher = hash_func()
                # get the resulting relative path into array of elements
                path_list = os.path.relpath(os.path.join(root, fname)).split(os.sep)
                # compute the hash on joined list, removes all os specific separators
                hasher.update(''.join(path_list).encode('utf-8'))
                hash_values.append(hasher.hexdigest())

    return _reduce_hash(hash_values, hash_func)


def _filehash(filepath, hashfunc):
    hasher = hashfunc()
    blocksize = 64 * 1024

    if not os.path.exists(filepath):
        return hasher.hexdigest()

    with open(filepath, "rb") as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def _reduce_hash(hashlist, hashfunc):
    hasher = hashfunc()
    for hashvalue in sorted(hashlist):
        hasher.update(hashvalue.encode("utf-8"))
    return hasher.hexdigest()
