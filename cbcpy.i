%module cbcpy
%{
#include "CbcModel.hpp"
#include "CbcStrategy.hpp"
#include "OsiSolverInterface.hpp"
#include "OsiClpSolverInterface.hpp"
%}
%ignore OsiSolverInterfaceCommonUnitTest;
%ignore OsiSolverInterfaceMpsUnitTest;
%ignore OsiClpSolverInterfaceUnitTest;
%include "carrays.i"
%array_class(double, doubleArray);
%include "CbcModel.hpp"
%include "CbcStrategy.hpp"
%include "OsiSolverInterface.hpp"
%include "OsiClpSolverInterface.hpp"