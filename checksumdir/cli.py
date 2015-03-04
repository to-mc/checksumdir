#!/usr/bin/env python
"""
Function for deterministically creating a single hash for a directory of files,
taking into account only file contents and not filenames.

Usage:

$ dirhash('/path/to/directory', 'md5')

"""


import argparse
from checksumdir import dirhash


def main():
    parser = argparse.ArgumentParser(description='Create hash for directory')
    parser.add_argument('directory', help='Directory to create hash value of')
    parser.add_argument('-a', '--algorithm', choices=('md5', 'sha1', 'sha256',
                                                      'sha512'), default='md5')

    args = parser.parse_args()
    print(dirhash(args.directory, args.algorithm))

if __name__ == '__main__':
    main()