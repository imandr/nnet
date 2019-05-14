import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), "r").read()

def get_version():
    g = {}
    exec(open(os.path.join("nnet", "Version.py"), "r").read(), g)
    return g["Version"]


setup(
    name = "nnet",
    version = get_version(),
    author = "Igor Mandrichenko",
    author_email = "igorvm@gmail.com",
    description = ("Simple machine learning framework"),
    license = "BSD 3-clause",
    keywords = "machine learning",
    url = "https://github.com/imandr/NNET",
    packages=['nnet'],
    long_description=read('README.md'),
    classifiers=[
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
    ]
)