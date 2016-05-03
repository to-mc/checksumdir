#!/usr/bin/env python
"""
Function for deterministically generating a single hash for a directory of files,
taking into account only file contents and not filenames.

Usage:

$ dirhash('/path/to/directory', 'md5')

"""


import argparse
import checksumdir

VERSION = checksumdir.__version__


def main():
    parser = argparse.ArgumentParser(description='Determine the hash for directory.')
    parser.add_argument('-v', '--version', action='version',
                        version='checksumdir %s' % VERSION)
    parser.add_argument('directory', help='Directory for which to generate hash.')
    parser.add_argument('-a', '--algorithm', choices=('md5', 'sha1', 'sha256',
                                                      'sha512'), default='md5')
    parser.add_argument('-e', '--excluded-files', nargs='+',
                        help='List of excluded files.')
    parser.add_argument('-x', '--excluded-extensions', nargs='+',
                        help='List of excluded file extensions.')

    args = parser.parse_args()
    print(checksumdir.dirhash(args.directory, args.algorithm,
                              args.excluded_files))

if __name__ == '__main__':
    main()
