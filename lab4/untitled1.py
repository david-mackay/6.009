# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 12:16:24 2019

@author: david
"""

rule1 = [[['adam', True], ['karl', True], ['pete', True],
          ['duane', True], ['tim', True]]]

rule2 = [[('adam', False), ('karl', False)],
         [('adam', False), ('pete', False)],
         [('adam', False), ('duane', False)],
         [('adam', False), ('tim', False)],
         [('karl', False), ('pete', False)],
         [('karl', False), ('duane', False)],
         [('karl', False), ('tim', False)],
         [('pete', False), ('duane', False)],
         [('pete', False), ('tim', False)],
         [('duane', False), ('tim', False)]]


rule3 = [[('chocolate', False), ('vanilla', False), ('pickles', False)],
         [('chocolate', True), ('vanilla', True)],
         [('chocolate', True), ('pickles', True)],
         [('vanilla', True), ('pickles', True)]]

rule4 = [[['adam', False], ['pickles', True]],
         [['adam', False], ['chocolate', False]],
         [['adam', False], ['vanilla', False]]]

rule5 = [[['pete', False], ['duane', True]],
         [['duane', False], ['pete', True]]]

rule6 = [[('karl', False), ('chocolate', True)],
         [('karl', False), ('vanilla', True)],
         [('karl', False), ('pickles', True)]]

rules = rule1 + rule2 + rule3 + rule4 + rule5 + rule6

print(rules)