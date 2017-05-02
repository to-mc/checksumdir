from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="checksumdir",
    version="1.1.4",
    packages=['checksumdir'],
    entry_points={
        'console_scripts': ['checksumdir=checksumdir.cli:main'],
    },
    author="Tom McCarthy, M. Niedzielski",
    author_email="tmac.se@gmail.com, mark@x-powered-by.info",
    description="Compute a single hash of the file contents of a directory.",
    long_description=read('README.rst'),
    license="MIT",
    keywords="hash checksum md5 directory",
    url="http://github.com/cakepietoast/checksumdir",
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        ],
)
