[![Linux Build Status](https://git.patrikdufresne.com/pdsl/cbcpy/badges/master/pipeline.svg)](https://git.patrikdufresne.com/pdsl/cbcpy/pipelines)

[![Windows Build status](https://ci.appveyor.com/api/projects/status/whyjc5s9vpulkno6?svg=true)](https://ci.appveyor.com/project/ikus060/cbcpy)

# cbcpy

Native Python interface for Coin-or Branch and Cut Solver ([Cbc](https://github.com/coin-or/Cbc)).

# Description

This project provide the build mechanism to automatically generate the wrapper code between Cbc C++ code and Python using [SWIG](http://www.swig.org/).

This project was develop as part of the CBC Coin-or Sprint Aug 2019.

Binaries for the following platform are pre-compiled and available on [pypi](https://pypi.org/project/cbcpy/).
* linux x86_64 / python 2.7
* linux x86_64 / python 3.5
* linux x86_64 / python 3.6
* linux x86_64 / python 3.7
* win x86 / python 2.7
* win x86 / python 3.5
* win x86 / python 3.6
* win x86 / python 3.7
* win x86_64 / python 3.5
* win x86_64 / python 3.6
* win x86_64 / python 3.7

Linux x86 is not supported.

# Installation

Pre-compiled python packages are deployed to [cbcpy Pypi repositories](https://pypi.org/cbcpy).
To install `cbcpy` you should make use of `pip` command line:

    pip install cbcpy
    
The packages include pre-compiled version of Cbc.

**For Windows: You must install [Visual C++ Redistributable for VS2015](https://www.microsoft.com/en-us/download/details.aspx?id=52685)**

# Usage

Here a minimalistic python script making use of `cbcpy`.
You may download `p0033.mps` from [here](https://raw.githubusercontent.com/coin-or/yaposib/master/examples/p0033.mps).

    import cbcpy as cbc
    solver1 = cbc.OsiClpSolverInterface()
    solver1.readMps("p0033.mps")
    model = cbc.CbcModel(solver1)
    model.branchAndBound()
    numberColumns = model.solver().getNumCols()
    p_solution = model.solver().getColSolution()
    solution = cbc.doubleArray_frompointer(p_solution)
    
    for i in range(numberColumns):
      value = solution[i]
      print("%s has value %s" % (i, value))
      
# Documentation

Original documentation from Cbc project is available in python using the `help()` function.

    # python
    Python 2.7.16 (default, Jul 13 2019, 16:01:51) 
    [GCC 8.3.0] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import cbcpy
    >>> help(cbcpy)
    Help on module cbcpy:
    
# Troubleshooting

## The specified module could not be found.
```
>>> import cbcpy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Python37-32\lib\site-packages\cbcpy.py", line 15, in <module>
    import _cbcpy
ImportError: DLL load failed: The specified module could not be found.
```
This error might occur on Windows platform when the file `msvcp140.dll` cannot
be found. You must install [Visual C++ Redistributable for VS2015](https://www.microsoft.com/en-us/download/details.aspx?id=52685).
For 32-bit download "vc_redist.x86.exe" file and for 64-bit download "vc_redist.x64.exe" file.

# Support

To get community help for cbcpy, you may send email to the [Cbc mailing list](https://list.coin-or.org/mailman/listinfo/cbc).

You may also get paid support by contacting [Patrik Dufresne Service Logiciel](http://www.patrikdufresne.com/en/support/#form).
