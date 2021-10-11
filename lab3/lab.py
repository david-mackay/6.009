"""6.009 Lab 3 -- Circuit Solver."""

# NO IMPORTS ALLOWED!

# Uncomment below and comment/rename the solveLinear defined in this file to
# use the sample solveLinear function.
# Remember to comment it out before submitting!
#
#from solve_linear_sample import solveLinear

def substituteEquation(equation, substitutedVariable, substitutionEquation):
    """
        Note that implementing this function is optional. You might want to
        consider implementing it to break up your code into more managable
        chunks.
        
        Given:
            equation: An equation represented by a dictionary that maps the
                      variables or 1 to its coefficient in the equation.
                      E.g. {1: 2, 'x': 2, 'y': 3} represents 2 + 2x + 3y = 0.
            substitutedVariable: The variable to be substituted out of the
                                 equation.
            substitutionEquation: The substitution equation represented as a
                                  dictionary.
        Return:
            finalEquation: A dictionary representing the resulting equation
                           after the substitution is performed. 
    """
#    print(equation)
#    print(substitutionEquation)
    if substitutedVariable not in equation.keys():
        return equation
    
    sub_var_coefficient = substitutionEquation[substitutedVariable]
    coeff = equation[substitutedVariable]

    for i in substitutionEquation.keys():
        substitutionEquation[i] = substitutionEquation[i]/(sub_var_coefficient)
#    print(substitutionEquation)
    for i in substitutionEquation.keys() :

        if i not in equation.keys():
            equation[i] = 0
        equation[i] += -coeff*substitutionEquation[i]
        if equation[i] == 0:
            del equation[i]
    return equation
    

def solveLinear(variables, equations):
    """
        Given:
            variables: A set of strings or tuples representing the independent
                       variables. E.g. {'x', 'y', 'z'}
            equations: A list of linear equations where each equation is
                       represented as a dictionary. Each dictionary maps the
                       variables or 1 to its coefficient in the equation.
                       E.g. {1: 2, 'x': 2, 'y': 3} represents 2 + 2x + 3y = 0.
                       Note that all variables may not appear in all of the
                       equations. Moreover, you may assume that the equations
                       are independent.
        Return:
            result: A dictionary mapping each variable to the numerical value
            that solves the system of equations. Assume that there is exactly
            one solution. Some inaccuracy as typical from floating point
            computations will be acceptable.
    """

    solved = {}
        
    #if equation has a variable and 1's value
    if len(equations) == 1:
        final_eq = equations[0]
        ans = -final_eq[1]
        for var in final_eq:
            if var != 1:
                solved[var] = ans/final_eq[var]
                return(solved)
                
                
    current_len = len(equations[0])
    shortest_eq = equations[0]
    
    
    
    for i in (equations): #find shortest equation in O(n)
        if len(i) < current_len:
            current_len = len(i)
            shortest_eq = i
#            equations.remove(i)
#    copy_of_eq = shortest_eq.copy()
    high_val = 0
    for i in shortest_eq.keys():
        if i == 1:
            continue
        else:
            if abs(shortest_eq[i]) > high_val:
                high_val = abs(shortest_eq[i])
                subVar = i  #find variable in shortest eq with highest coeff that isnt one gang
    equations.remove(shortest_eq)
    variables.remove(subVar)
    for n, eq in enumerate(equations): #substitute variable into all the equations
        if subVar in eq.keys():
            new_eq = substituteEquation(eq, subVar, shortest_eq)
            equations[n] = new_eq
            
    solved = solveLinear(variables, equations)
    if 1 not in shortest_eq.keys():
        shortest_eq[1] = 0
    for i in shortest_eq:
        if i in solved.keys():
            shortest_eq[1] +=shortest_eq[i]*solved[i]
    solved[subVar] = -shortest_eq[1]/shortest_eq[subVar]
            
    

    
    return solved
    
    
    
    
#    while len(equations) != 1:
        
            
            
        

def solveCircuit(junctions, wires, resistances, voltages):
    """
        Given:
            junctions:  A set of junctions. Each junction is labeled by a string
                        or a tuple.
            wires:      A dictionary mapping a unique wire ID (a string or tuple)
                        to a tuple of two elements representing the starting and
                        ending junctions of the wire, respectively. The set of
                        wire IDs is disjoint from the set of junction labels.
                        Note that although electricity can flow in either
                        directions, each wire between a pair of junctions will
                        appear exactly once in the list. Moreover, the starting
                        and ending junctions are distinct.
            resistances:A dictionary mapping each unique wire ID to a numeric
                        value representing the magnitude of the resistance of
                        the wire in Ohms. This dictionary has the same set of
                        keys as the wires dictionary.
            voltages:   A dictionary mapping each unique wire ID to a numeric
                        value representing the voltage (EMF or potential
                        difference) of the battery connected along the wire in 
                        Volts. The positive terminal of the battery is next to
                        the ending junction (as defined in the wires dictionary)
                        if the voltage is positive whereas it is next to the 
                        starting junction otherwise. This dictionary also has
                        the same set of keys as the wires dictionary.
        Return:
            result: A dictionary mapping the label of each wire to the current
                    it carries. The labels must be the keys in the wires
                    dictionary and the current should be considered positive if
                    it is flowing from the starting junction to the ending
                    junction as specified in the wires dictionary.
    """
    raise NotImplementedError

def findMaximumDeviationJunction(junctions, wires, resistances, voltages, currents):
    """
        Note that this part is completely optional and would not contribute to your grade.
        
        Given:
            junctions:  A set of junctions. Each junction is labeled by a
                        string or a tuple.
            wires:      A dictionary mapping a unique wire ID (a string or tuple)
                        to a tuple of two elements representing the starting and
                        ending junctions of the wire respectively. The set of
                        wire IDs is disjoint from the set of junction labels.
                        Note that although electricity can flow in either
                        direction, each wire between a pair of junctions will
                        appear exactly once in the list. Moreover, the starting
                        and ending junctions are distinct.
            resistances:A dictionary mapping each unique wire ID to a numeric
                        value representing the magnitude of the resistance of
                        the wire in Ohms. This dictionary has the same set of
                        keys as the wires dictionary.
            voltages:   A dictionary mapping each unique wire ID to a numeric
                        value representing the voltage (EMF or potential
                        difference) of the battery connected along the wire in
                        Volts. The positive terminal of the battery is next to
                        the ending junction (as defined in the wires dictionary)
                        if the voltage is positive whereas it is next to the
                        starting junction otherwise. This dictionary also has 
                        the same set of keys as the wires dictionary.
            currents:   A dictionary mapping each unique wire ID to a numeric
                        value representing the indicated current flowing along
                        the wire. The format is identical to that of the output 
                        of the previous function. Note that the values will not
                        necessarily be correct.
        Return:
            result: A junction with the maximum deviation from current
                    conservation. Note that any junction with maximal deviation
                    will be accepted.
    """
    raise NotImplementedError

def findMaximumDeviationLoop(junctions, wires, resistances, voltages, currents):
    """
        Note that this part is completely optional and would not contribute to your grade.
        
        Given:
            junctions:  A set of junctions. Each junction is labeled by a string
                        or a tuple.
            wires:      A dictionary mapping a unique wire ID (a string or tuple)
                        to a tuple of two elements representing the starting and
                        ending junctions of the wire respectively. The set of
                        wire IDs is disjoint from the set of junction labels.
                        Note that although electricity can flow in either
                        directions, each wire between a pair of junctions will
                        appear exactly once in the list. Moreover, the starting
                        and ending junctions are distinct.
            resistances:A dictionary mapping each unique wire ID to a numeric
                        value representing the magnitude of the resistance of 
                        the wire in Ohms. This dictionary has the same set of
                        keys as the wires dictionary.
            voltages:   A dictionary mapping each unique wire ID to a numeric
                        value representing the voltage (EMF or potential
                        difference) of the battery connected along the wire in
                        Volts. The positive terminal of the battery is next to
                        the ending junction (as defined in the wires dictionary)
                        if the voltage is positive whereas it is next to the 
                        starting junction otherwise. This dictionary also has
                        the same set of keys as the wires dictionary.
            currents:   A dictionary mapping each unique wire ID to a numeric
                        value representing the indicated current flowing along
                        the wire. The format is identical to that of the output
                        of the previous function. Note that the values will not
                        necessarily be correct.
        Return:
            result: A list of wires IDs representing the edges along a loop with
                    maximal (additive) deviation from Kirchoff's loop law.
                    The wires should be in order along the cycle but the
                    starting node and the direction may be arbitrary.
    """
    raise NotImplementedError

if __name__ == '__main__':
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used for testing.
    print(substituteEquation({'x': -1, 'y': 3}, 'y', {'x': 1, 'y': 2, 1: 11}))
    pass
