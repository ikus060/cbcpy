#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Coin-or CBC native interface for Python
# Coin-or CBC native interface for Python
# Copyright (C) 2019 Patrik Dufresne Service Logiciel <info@patrikdufresne.com>
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
import os
try:
    from setuptools import setup, Extension
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, Extension

# Configure the SWIG build
CBC_DIR = os.environ.get('CBC_DIR', './Cbc')
if not os.path.isdir(CBC_DIR):
  print('CBC_DIR environment variable must be a directory: ' + CBC_DIR)

include_dirs = [os.path.join(CBC_DIR, 'include/coin')]
library_dirs = [os.path.join(CBC_DIR, 'lib')]
libraries = ['CbcSolver', 'Cbc', 'Cgl', 'OsiClp', 'OsiCbc', 'Osi', 'Clp', 'CoinUtils']
if os.name == 'nt':
    extra_objects = []
    libraries = ['lib' + name for name in libraries]
else:
    extra_objects = ['%s/lib%s.a' % (library_dirs[0], l) for l in libraries]
    libraries = []
swig_opts=['-c++','-doxygen']
swig_opts.extend(['-I%s' % i for i in include_dirs])

# Define project description
project_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(project_dir, 'README.md')) as f:
    long_description = f.read()

setup(
    name='cbcpy',
    version="2.10.3-2",
    description='Coin-or CBC native interface for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Patrik Dufresne',
    author_email='info@patrikdufresne.com',
    url='https://git.patrikdufresne.com/pdsl/cbcpy',
    license="",
    ext_modules=[Extension(
        '_cbcpy',
        ['cbcpy.i'],
        swig_opts=swig_opts,
        include_dirs=include_dirs,
        library_dirs=library_dirs,
        libraries=libraries,
        extra_objects=extra_objects)],
    py_modules=['cbcpy'],
)