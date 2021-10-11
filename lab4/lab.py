"""6.009 Lab 4 -- Boolean satisfiability solving"""

import sys
sys.setrecursionlimit(10000)
# NO ADDITIONAL IMPORTS

def newform(formula,x, y):


    newformula = []
    
    for literal in formula:
        if (x, y) in literal: #literal = [('c', True),('c', True)]
            continue
        if [x,y] in literal:
            continue
        if [x, not y] in literal:
            z= literal.copy()
            z.remove([x, not y])
            newformula.append(z)
            continue
        if (x, not y) in literal:
            z = literal.copy()
            
            z.remove((x, not y))
            newformula.append(z)
            continue
        newformula.append(literal)
    print('old formula = ', formula)
    print('new formula = ', newformula)
    return newformula
def satisfying_assignment(formula, ans = None):
    """
    Find a satisfying assignment for a given CNF formula.
    Returns that assignment if one exists, or None otherwise.

    >>> satisfying_assignment([])
    {}
    >>> x = satisfying_assignment([[('a', True), ('b', False), ('c', True)]])
    >>> x.get('a', None) is True or x.get('b', None) is False or x.get('c', None) is True
    True
    >>> satisfying_assignment([[('a', True)], [('a', False)]])
    """
   
    
    noneval = 0
    if formula == []:
        return ans  
    newformula = formula.copy()
    if ans == None:
        ans = {}
        for literal in formula:
            for b in literal:
                ans.update({b[0]: None})
    for literal in formula:
        if len(literal) == 1:
            i =literal[0][0]
            j = literal[0][1]                   
            newformula = newform(newformula, i, j)
            ans.update({i: j})
            
    

        
    for empty in newformula:
        if empty == []:
            return
    for val in ans:
        x= None
        if ans[val] == None:
            x = (val)
            noneval+=1
            break
    
    if x == None:
        return ans
    attempt_dict = ans.copy()

    attempt_dict2 = ans.copy()

    f1 = newform(newformula, x, True)
    attempt_dict.update({x: True})
    attempt = satisfying_assignment(f1, attempt_dict)    
    if attempt == None:
#        print('attempt 1 is none')
        f2 = newform(newformula, x, False)
        attempt_dict2.update({x: False})
        attempt = satisfying_assignment(f2, attempt_dict2)
        if attempt == None:
#            print('attempt is none')
            return

    return attempt



def boolify_scheduling_problem(student_preferences, session_capacities):
    """
    Convert a quiz-room-scheduling problem into a Boolean formula.

    student_preferences: a dictionary mapping a student name (string) to a set
                         of session names (strings) that work for that student
    session_capacities: a dictionary mapping each session name to a positive
                        integer for how many students can fit in that session

    Returns: a CNF formula encoding the scheduling problem, as per the
             lab write-up
    We assume no student or session names contain underscores.
    """
    raise NotImplementedError


if __name__ == '__main__':
    import doctest
#    _doctest_flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
#    print(doctest.testmod(optionflags=_doctest_flags))
    formula = [
    [('a', True), ('b', True), ('c', True)],
    [('a', False), ('f', True)],
    [('d', False), ('e', True), ('a', True), ('g', True)],
    [('h', False), ('c', True), ('a', False)],[('a', True)],
]
#    formula2 = [[('a', True)],[('a', False)]]
    print(satisfying_assignment(formula))
    