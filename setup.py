from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="checksumdir",
    version="1.0.5",
    packages=['checksumdir'],
    entry_points={
        'console_scripts': ['checksumdir=checksumdir.cli:main'],
    },
    author="Tom McCarthy",
    author_email="tmac.se@gmail.com",
    description="Simple package to compute a single deterministic hash of the "
                "file contents of a directory.",
    long_description=read('README.rst'),
    license="MIT",
    keywords="hash checksum md5 directory",
    url="http://github.com/cakepietoast/checksumdir",
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        ],
)
