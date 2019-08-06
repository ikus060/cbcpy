#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Coin-or CBC native interface for Python
# Copyright (C) 2019 Patrik Dufresne Service Logiciel inc.
#
# TODO Add the right license.

try:
    from setuptools import setup, Extension
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, Extension

setup(
    name='cbcpy',
    use_scm_version=True,
    description='Coin-or CBC native interface for Python',
    author='Patrik Dufresne',
    author_email='info@patrikdufresne.com',
    url='https://git.patrikdufresne.com/pdsl/cbcpy',
    license="GPLv3",
    ext_modules=[Extension('_cbcpy', ['cbcpy.i'], swig_opts=['-modern', '-I../include'])],
    py_modules=['cbcpy'],
    setup_requires=[
        "setuptools_scm",
    ],
)
