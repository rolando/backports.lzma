#!/usr/bin/python -u
#
# Python Bindings for XY/LZMA backported from Python 3.3.0
#
# This file copyright (c) 2012 Peter Cock, p.j.a.cock@googlemail.com
# See other files for separate copyright notices.

import sys, os
from warnings import warn

from distutils import log
from distutils.command.build_ext import build_ext
from distutils.core import setup
from distutils.extension import Extension

packages = ["backports.lzma"]
home = os.path.expanduser("~")
extens = [Extension('backports/lzma/_lzma',
                    ['backports/lzma/_lzmamodule.c'],
                    libraries = ['lzma'],
                    include_dirs = [os.path.join(home, 'include')],
                    library_dirs = [os.path.join(home, 'lib')]
                    )]

descr = "Backport of Python 3.3's 'lzma' modoule for XY/LZMA compressed files."
long_descr = """This is a backport of the 'lzma' module included in Python 3.3 or later
by Nadeem Vawda and Per Oyvind Karlsen, which provides a Python wrapper for ZY Utils
(aka LZMA Utils v2) by Igor Pavlov.

In order to compile this, you will need to install XY Utils from http://tukaani.org/xz/
"""

setup(
    name = "backports.lzma",
    version = "0.0.1",
    description = descr,
    author = "Peter Cock, based on work by Nadeem Vawda and Per Oyvind Karlsen",
    author_email = "p.j.a.cock@googlemail.com",
    license='PSF license',
    keywords = "xy lzma compression decompression",
    long_description = long_descr,
    classifiers = [
        #'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: PSF license',
        #'Operating System :: OS Independent',
    ],
    packages = packages,
    ext_modules = extens,
    cmdclass = {
        'build_ext': build_ext,
    },
)