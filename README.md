# cbcpy

Native Python interface for Coin-or Branch and Cut Solver ([Cbc](https://github.com/coin-or/Cbc)).

# Description

This project provide the build mechanism to automatically generate the wrapper code between Cbc c++ code and python using [SWIG](http://www.swig.org/).

This project was develop as part of the CBC Coin-or Sprint Aug 2019.

Binaries for the following platform are pre-compiled:
* linux x86_64 / python 2.7
* linux x86_64 / python 3.5
* linux x86_64 / python 3.6
* linux x86_64 / python 3.7
* win32 / python 2.7

**Linux i386 is not supported.**

NOTICE Adding more platform is in progress.

# Installation

Pre-compiled python packages are deployed to [cbcpy Pypi repositories](https://pypi.org/cbcpy).
To install `cbcpy` you should make use of `pip` command line:

    pip install cbcpy
    
The packages include pre-compiled version of Cbc.


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
