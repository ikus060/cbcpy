import cbc
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
