from setuptools import setup
import os
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from setuptools import setup, find_packages


try:
    from pypandoc import convert

    def read_md(f):
        return convert(f, 'rst')

except ImportError:
    convert = None
    print(
        "warning: pypandoc module not found, could not convert Markdown to RST"
    )

    def read_md(f):
        return open(f, 'r').read()

README = os.path.join(os.path.dirname(__file__), 'README.md')




def get_version(version_tuple):
    # additional handling of a,b,rc tags, this can
    # be simpler depending on your versioning scheme
    if not isinstance(version_tuple[-1], int):
        return '.'.join(
            map(str, version_tuple[:-1])
        ) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))

# path to the packages __init__ module in project
# source tree
init = os.path.join(
    os.path.dirname(__file__), 'study\LearningCythonProgramming', '__init__.py'
)
version_line = list(
    filter(lambda l: l.startswith('VERSION'), open(init))
)[0]

# VERSION is a tuple so we need to eval its line of code.
# We could simply import it from the package but we
# cannot be sure that this package is importable before
# finishing its installation
VERSION = get_version(eval(version_line.split('=')[-1]))




setup(
    namespace_packages=['study'],
    name='study.ExpertPythonProgramming2ndEdition',
    keywords =['ExpertPythonProgramming2ndEdition'],
    description=' book study',
    long_description=read_md(README),
    version=VERSION,
    packages=find_packages(),
    classifiers = [],
)