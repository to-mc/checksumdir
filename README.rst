***********
Checksumdir
***********

This is a simple module to create a single hash for a directory of files,
taking into account only file contents, ignoring any metadata such as file name.

=====
Usage
=====

.. code-block:: python

    from checksumdir import hashdir

    directory = '/path/to/directory/'
    md5hash = hashdir(directory, 'md5')
    sha1hash = hashdir(directory, 'sha1')


Or to use the CLI:

.. code-block:: bash

    # Defaults to md5
    $ checksumdir /path/to/directory

    # Create sha1 hash
    $ checksumdir -a sha1 /path/to/directory