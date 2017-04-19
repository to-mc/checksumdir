***********
Checksumdir
***********

A simple module for creating a single hash for a directory of files, with file contents;
ignoring any metadata such as file name.  Options exist to also exclude specific files
or files with specific extensions.

=====
Usage
=====

.. code-block:: python

    from checksumdir import dirhash

    directory  = '/path/to/directory/'
    md5hash    = dirhash(directory, 'md5')
    sha1hash   = dirhash(directory, 'sha1', excluded_files=['package.json'])
    sha256hash = dirhash(directory, 'sha256', excluded_extensions=['pyc'])


Or to use the CLI:

.. code-block:: bash

    # Defaults to md5.
    $ checksumdir /path/to/directory

    # Create sha1 hash:
    $ checksumdir -a sha1 /path/to/directory

    # Exclude files:
    $ checksumdir -e <files> /path/to/directory

    # Exclude files with specific extensions:
    $ checksumdir -x <extensions> /path/to/directory

    # Follow soft links:
    $ checksumdir --follow-links /path/to/directory