"""
Function for deterministically creating a single hash for a directory of files,
taking into account only file contents and not filenames.

Usage:

from checksumdir import dirhash

dirhash('/path/to/directory', 'md5')

"""

import os
import hashlib
import re
from joblib import Parallel, delayed

import pkg_resources

__version__ = pkg_resources.require("checksumdir")[0].version

HASH_FUNCS = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
    'sha512': hashlib.sha512
}


def dirhash(dirname, hashfunc='md5', excluded_files=None, ignore_hidden=False, followlinks=False, parallel=False):
    hash_func = HASH_FUNCS.get(hashfunc)
    if not hash_func:
        raise NotImplementedError('{} not implemented.'.format(hashfunc))

    if not excluded_files:
        excluded_files = []

    if not os.path.isdir(dirname):
        raise TypeError('{} is not a directory.'.format(dirname))
    fileslist = []
    for root, dirs, files in os.walk(dirname, topdown=True, followlinks=followlinks):
        if ignore_hidden:
            if not re.search(r'/\.', root):
                fileslist.extend([os.path.join(root, f) for f in files if not
                                   f.startswith('.') and not re.search(r'/\.', f)
                                   and f not in excluded_files])
        else:
            fileslist.extend([os.path.join(root, f) for f in files if f not in excluded_files])

    if parallel:
        hashvalues = Parallel(n_jobs=100, prefer='threads')(delayed(_filehash)(f, hash_func) for f in fileslist)
    else:
        hashvalues = [_filehash(f, hash_func) for f in fileslist]

    return _reduce_hash(hashvalues, hash_func)


def _filehash(filepath, hashfunc):
    hasher = hashfunc()
    blocksize = 64 * 1024
    try:
        with open(filepath, 'rb') as fp:
            while True:
                data = fp.read(blocksize)
                if not data:
                    break
                hasher.update(data)
    except:
        pass
        #"The file %s no longer exists."%filepath

    return hasher.hexdigest()


def _reduce_hash(hashlist, hashfunc):
    hasher = hashfunc()
    for hashvalue in sorted(hashlist):
        hasher.update(hashvalue.encode('utf-8'))
    return hasher.hexdigest()
