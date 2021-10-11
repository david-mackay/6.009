junctions = {'0-1', '1-1', 'A', 'B'}

wires = {'battery': ('B', 'A'), ('0-1', '1-1'): ('0-1', '1-1'), ('0-1', 'B'): ('0-1', 'B'), ('1-1', 'B'): ('1-1', 'B'), ('A', '0-1'): ('A', '0-1'), ('A', '1-1'): ('A', '1-1')}

resistances = {'battery': 0, ('0-1', '1-1'): 86.75195391727786, ('0-1', 'B'): 2, ('1-1', 'B'): 4, ('A', '0-1'): 1, ('A', '1-1'): 2}

voltages = {'battery': 6, ('0-1', '1-1'): 0, ('0-1', 'B'): 0, ('1-1', 'B'): 0, ('A', '0-1'): 0, ('A', '1-1'): 0}

currents = {'battery': 2.49, ('0-1', '1-1'): -0.5, ('0-1', 'B'): 2.86, ('1-1', 'B'): 0.8, ('A', '0-1'): 1.76, ('A', '1-1'): 1.42}

deviations = {'battery': 6.0, ('0-1', '1-1'): 43.37597695863893, ('0-1', 'B'): -5.72, ('1-1', 'B'): -3.2, ('A', '0-1'): -1.76, ('A', '1-1'): -2.84}

soln = -45.93597695863893
