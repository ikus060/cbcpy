# cbcpy

Native Python interface for Coin-or Branch and Cut Solver ([Cbc](https://github.com/coin-or/Cbc)).

# Description

This project provide the build mechanism to automatically generate the wrapper code betweeb Cbc c++ code and python using [SWIG](http://www.swig.org/).

# Build

This project was develop as part of the CBC Coin-or Sprint Aug 2019.

# Installation

Python packages are deployed to [cbcpy Pypi repositories](https://pypi.org/cbcpy).

Binaries for the following platform are pre-compiled:
* linux x86_64 / python 2.7
* linux x86_64 / python 3.5
* linux x86_64 / python 3.6
* linux x86_64 / python 3.7
* win32 / python 2.7

To install `cbcpy` you should make use of `pip` command line:

    pip install cbcpy
    
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

