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

libraries = ['CbcSolver', 'Cbc', 'Cgl', 'OsiClp', 'OsiCbc', 'Osi', 'Clp', 'CoinUtils']
if os.name == 'nt':
    libraries = ['lib' + name for name in libraries]

setup(
    name='cbcpy',
    version="2.10.3-1",
    description='Coin-or CBC native interface for Python',
    author='Patrik Dufresne',
    author_email='info@patrikdufresne.com',
    url='https://git.patrikdufresne.com/pdsl/cbcpy',
    license="",
    ext_modules=[Extension(
        '_cbcpy',
        ['cbcpy.i'],
        swig_opts=['-modern'],
        libraries=libraries)],
    py_modules=['cbcpy'],
)
