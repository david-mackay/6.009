junctions = {'0-0', '0-1', '0-2', '0-3', '0-4', '0-5', '0-6', '0-7', '0-8', '0-9', '1-0', '1-1', '1-2', '1-3', '1-4', '1-5', '1-6', '1-7', '1-8', '1-9', '10-0', '10-1', '10-2', '10-3', '10-4', '10-5', '10-6', '10-7', '10-8', '10-9', '2-0', '2-1', '2-2', '2-3', '2-4', '2-5', '2-6', '2-7', '2-8', '2-9', '3-0', '3-1', '3-2', '3-3', '3-4', '3-5', '3-6', '3-7', '3-8', '3-9', '4-0', '4-1', '4-2', '4-3', '4-4', '4-5', '4-6', '4-7', '4-8', '4-9', '5-0', '5-1', '5-2', '5-3', '5-4', '5-5', '5-6', '5-7', '5-8', '5-9', '6-0', '6-1', '6-2', '6-3', '6-4', '6-5', '6-6', '6-7', '6-8', '6-9', '7-0', '7-1', '7-2', '7-3', '7-4', '7-5', '7-6', '7-7', '7-8', '7-9', '8-0', '8-1', '8-2', '8-3', '8-4', '8-5', '8-6', '8-7', '8-8', '8-9', '9-0', '9-1', '9-2', '9-3', '9-4', '9-5', '9-6', '9-7', '9-8', '9-9'}

wires = {'battery': ('5-5', '5-4'), ('0-0', '0-1'): ('0-0', '0-1'), ('0-0', '1-0'): ('0-0', '1-0'), ('0-1', '0-2'): ('0-1', '0-2'), ('0-1', '1-1'): ('0-1', '1-1'), ('0-2', '0-3'): ('0-2', '0-3'), ('0-2', '1-2'): ('0-2', '1-2'), ('0-3', '0-4'): ('0-3', '0-4'), ('0-3', '1-3'): ('0-3', '1-3'), ('0-4', '0-5'): ('0-4', '0-5'), ('0-4', '1-4'): ('0-4', '1-4'), ('0-5', '0-6'): ('0-5', '0-6'), ('0-5', '1-5'): ('0-5', '1-5'), ('0-6', '0-7'): ('0-6', '0-7'), ('0-6', '1-6'): ('0-6', '1-6'), ('0-7', '0-8'): ('0-7', '0-8'), ('0-7', '1-7'): ('0-7', '1-7'), ('0-8', '0-9'): ('0-8', '0-9'), ('0-8', '1-8'): ('0-8', '1-8'), ('0-9', '1-9'): ('0-9', '1-9'), ('1-0', '1-1'): ('1-0', '1-1'), ('1-0', '2-0'): ('1-0', '2-0'), ('1-1', '1-2'): ('1-1', '1-2'), ('1-1', '2-1'): ('1-1', '2-1'), ('1-2', '1-3'): ('1-2', '1-3'), ('1-2', '2-2'): ('1-2', '2-2'), ('1-3', '1-4'): ('1-3', '1-4'), ('1-3', '2-3'): ('1-3', '2-3'), ('1-4', '1-5'): ('1-4', '1-5'), ('1-4', '2-4'): ('1-4', '2-4'), ('1-5', '1-6'): ('1-5', '1-6'), ('1-5', '2-5'): ('1-5', '2-5'), ('1-6', '1-7'): ('1-6', '1-7'), ('1-6', '2-6'): ('1-6', '2-6'), ('1-7', '1-8'): ('1-7', '1-8'), ('1-7', '2-7'): ('1-7', '2-7'), ('1-8', '1-9'): ('1-8', '1-9'), ('1-8', '2-8'): ('1-8', '2-8'), ('1-9', '2-9'): ('1-9', '2-9'), ('10-0', '10-1'): ('10-0', '10-1'), ('10-1', '10-2'): ('10-1', '10-2'), ('10-2', '10-3'): ('10-2', '10-3'), ('10-3', '10-4'): ('10-3', '10-4'), ('10-4', '10-5'): ('10-4', '10-5'), ('10-5', '10-6'): ('10-5', '10-6'), ('10-6', '10-7'): ('10-6', '10-7'), ('10-7', '10-8'): ('10-7', '10-8'), ('10-8', '10-9'): ('10-8', '10-9'), ('2-0', '2-1'): ('2-0', '2-1'), ('2-0', '3-0'): ('2-0', '3-0'), ('2-1', '2-2'): ('2-1', '2-2'), ('2-1', '3-1'): ('2-1', '3-1'), ('2-2', '2-3'): ('2-2', '2-3'), ('2-2', '3-2'): ('2-2', '3-2'), ('2-3', '2-4'): ('2-3', '2-4'), ('2-3', '3-3'): ('2-3', '3-3'), ('2-4', '2-5'): ('2-4', '2-5'), ('2-4', '3-4'): ('2-4', '3-4'), ('2-5', '2-6'): ('2-5', '2-6'), ('2-5', '3-5'): ('2-5', '3-5'), ('2-6', '2-7'): ('2-6', '2-7'), ('2-6', '3-6'): ('2-6', '3-6'), ('2-7', '2-8'): ('2-7', '2-8'), ('2-7', '3-7'): ('2-7', '3-7'), ('2-8', '2-9'): ('2-8', '2-9'), ('2-8', '3-8'): ('2-8', '3-8'), ('2-9', '3-9'): ('2-9', '3-9'), ('3-0', '3-1'): ('3-0', '3-1'), ('3-0', '4-0'): ('3-0', '4-0'), ('3-1', '3-2'): ('3-1', '3-2'), ('3-1', '4-1'): ('3-1', '4-1'), ('3-2', '3-3'): ('3-2', '3-3'), ('3-2', '4-2'): ('3-2', '4-2'), ('3-3', '3-4'): ('3-3', '3-4'), ('3-3', '4-3'): ('3-3', '4-3'), ('3-4', '3-5'): ('3-4', '3-5'), ('3-4', '4-4'): ('3-4', '4-4'), ('3-5', '3-6'): ('3-5', '3-6'), ('3-5', '4-5'): ('3-5', '4-5'), ('3-6', '3-7'): ('3-6', '3-7'), ('3-6', '4-6'): ('3-6', '4-6'), ('3-7', '3-8'): ('3-7', '3-8'), ('3-7', '4-7'): ('3-7', '4-7'), ('3-8', '3-9'): ('3-8', '3-9'), ('3-8', '4-8'): ('3-8', '4-8'), ('3-9', '4-9'): ('3-9', '4-9'), ('4-0', '4-1'): ('4-0', '4-1'), ('4-0', '5-0'): ('4-0', '5-0'), ('4-1', '4-2'): ('4-1', '4-2'), ('4-1', '5-1'): ('4-1', '5-1'), ('4-2', '4-3'): ('4-2', '4-3'), ('4-2', '5-2'): ('4-2', '5-2'), ('4-3', '4-4'): ('4-3', '4-4'), ('4-3', '5-3'): ('4-3', '5-3'), ('4-4', '4-5'): ('4-4', '4-5'), ('4-4', '5-4'): ('4-4', '5-4'), ('4-5', '4-6'): ('4-5', '4-6'), ('4-5', '5-5'): ('4-5', '5-5'), ('4-6', '4-7'): ('4-6', '4-7'), ('4-6', '5-6'): ('4-6', '5-6'), ('4-7', '4-8'): ('4-7', '4-8'), ('4-7', '5-7'): ('4-7', '5-7'), ('4-8', '4-9'): ('4-8', '4-9'), ('4-8', '5-8'): ('4-8', '5-8'), ('4-9', '5-9'): ('4-9', '5-9'), ('5-0', '5-1'): ('5-0', '5-1'), ('5-0', '6-0'): ('5-0', '6-0'), ('5-1', '5-2'): ('5-1', '5-2'), ('5-1', '6-1'): ('5-1', '6-1'), ('5-2', '5-3'): ('5-2', '5-3'), ('5-2', '6-2'): ('5-2', '6-2'), ('5-3', '5-4'): ('5-3', '5-4'), ('5-3', '6-3'): ('5-3', '6-3'), ('5-4', '5-5'): ('5-4', '5-5'), ('5-4', '6-4'): ('5-4', '6-4'), ('5-5', '5-6'): ('5-5', '5-6'), ('5-5', '6-5'): ('5-5', '6-5'), ('5-6', '5-7'): ('5-6', '5-7'), ('5-6', '6-6'): ('5-6', '6-6'), ('5-7', '5-8'): ('5-7', '5-8'), ('5-7', '6-7'): ('5-7', '6-7'), ('5-8', '5-9'): ('5-8', '5-9'), ('5-8', '6-8'): ('5-8', '6-8'), ('5-9', '6-9'): ('5-9', '6-9'), ('6-0', '6-1'): ('6-0', '6-1'), ('6-0', '7-0'): ('6-0', '7-0'), ('6-1', '6-2'): ('6-1', '6-2'), ('6-1', '7-1'): ('6-1', '7-1'), ('6-2', '6-3'): ('6-2', '6-3'), ('6-2', '7-2'): ('6-2', '7-2'), ('6-3', '6-4'): ('6-3', '6-4'), ('6-3', '7-3'): ('6-3', '7-3'), ('6-4', '6-5'): ('6-4', '6-5'), ('6-4', '7-4'): ('6-4', '7-4'), ('6-5', '6-6'): ('6-5', '6-6'), ('6-5', '7-5'): ('6-5', '7-5'), ('6-6', '6-7'): ('6-6', '6-7'), ('6-6', '7-6'): ('6-6', '7-6'), ('6-7', '6-8'): ('6-7', '6-8'), ('6-7', '7-7'): ('6-7', '7-7'), ('6-8', '6-9'): ('6-8', '6-9'), ('6-8', '7-8'): ('6-8', '7-8'), ('6-9', '7-9'): ('6-9', '7-9'), ('7-0', '7-1'): ('7-0', '7-1'), ('7-0', '8-0'): ('7-0', '8-0'), ('7-1', '7-2'): ('7-1', '7-2'), ('7-1', '8-1'): ('7-1', '8-1'), ('7-2', '7-3'): ('7-2', '7-3'), ('7-2', '8-2'): ('7-2', '8-2'), ('7-3', '7-4'): ('7-3', '7-4'), ('7-3', '8-3'): ('7-3', '8-3'), ('7-4', '7-5'): ('7-4', '7-5'), ('7-4', '8-4'): ('7-4', '8-4'), ('7-5', '7-6'): ('7-5', '7-6'), ('7-5', '8-5'): ('7-5', '8-5'), ('7-6', '7-7'): ('7-6', '7-7'), ('7-6', '8-6'): ('7-6', '8-6'), ('7-7', '7-8'): ('7-7', '7-8'), ('7-7', '8-7'): ('7-7', '8-7'), ('7-8', '7-9'): ('7-8', '7-9'), ('7-8', '8-8'): ('7-8', '8-8'), ('7-9', '8-9'): ('7-9', '8-9'), ('8-0', '8-1'): ('8-0', '8-1'), ('8-0', '9-0'): ('8-0', '9-0'), ('8-1', '8-2'): ('8-1', '8-2'), ('8-1', '9-1'): ('8-1', '9-1'), ('8-2', '8-3'): ('8-2', '8-3'), ('8-2', '9-2'): ('8-2', '9-2'), ('8-3', '8-4'): ('8-3', '8-4'), ('8-3', '9-3'): ('8-3', '9-3'), ('8-4', '8-5'): ('8-4', '8-5'), ('8-4', '9-4'): ('8-4', '9-4'), ('8-5', '8-6'): ('8-5', '8-6'), ('8-5', '9-5'): ('8-5', '9-5'), ('8-6', '8-7'): ('8-6', '8-7'), ('8-6', '9-6'): ('8-6', '9-6'), ('8-7', '8-8'): ('8-7', '8-8'), ('8-7', '9-7'): ('8-7', '9-7'), ('8-8', '8-9'): ('8-8', '8-9'), ('8-8', '9-8'): ('8-8', '9-8'), ('8-9', '9-9'): ('8-9', '9-9'), ('9-0', '10-0'): ('9-0', '10-0'), ('9-0', '9-1'): ('9-0', '9-1'), ('9-1', '10-1'): ('9-1', '10-1'), ('9-1', '9-2'): ('9-1', '9-2'), ('9-2', '10-2'): ('9-2', '10-2'), ('9-2', '9-3'): ('9-2', '9-3'), ('9-3', '10-3'): ('9-3', '10-3'), ('9-3', '9-4'): ('9-3', '9-4'), ('9-4', '10-4'): ('9-4', '10-4'), ('9-4', '9-5'): ('9-4', '9-5'), ('9-5', '10-5'): ('9-5', '10-5'), ('9-5', '9-6'): ('9-5', '9-6'), ('9-6', '10-6'): ('9-6', '10-6'), ('9-6', '9-7'): ('9-6', '9-7'), ('9-7', '10-7'): ('9-7', '10-7'), ('9-7', '9-8'): ('9-7', '9-8'), ('9-8', '10-8'): ('9-8', '10-8'), ('9-8', '9-9'): ('9-8', '9-9'), ('9-9', '10-9'): ('9-9', '10-9')}

resistances = {'battery': 0, ('0-0', '0-1'): 200, ('0-0', '1-0'): 200, ('0-1', '0-2'): 200, ('0-1', '1-1'): 200, ('0-2', '0-3'): 200, ('0-2', '1-2'): 200, ('0-3', '0-4'): 200, ('0-3', '1-3'): 200, ('0-4', '0-5'): 200, ('0-4', '1-4'): 200, ('0-5', '0-6'): 200, ('0-5', '1-5'): 200, ('0-6', '0-7'): 200, ('0-6', '1-6'): 200, ('0-7', '0-8'): 200, ('0-7', '1-7'): 200, ('0-8', '0-9'): 200, ('0-8', '1-8'): 200, ('0-9', '1-9'): 200, ('1-0', '1-1'): 200, ('1-0', '2-0'): 200, ('1-1', '1-2'): 200, ('1-1', '2-1'): 200, ('1-2', '1-3'): 200, ('1-2', '2-2'): 200, ('1-3', '1-4'): 200, ('1-3', '2-3'): 200, ('1-4', '1-5'): 200, ('1-4', '2-4'): 200, ('1-5', '1-6'): 200, ('1-5', '2-5'): 200, ('1-6', '1-7'): 200, ('1-6', '2-6'): 200, ('1-7', '1-8'): 200, ('1-7', '2-7'): 200, ('1-8', '1-9'): 200, ('1-8', '2-8'): 200, ('1-9', '2-9'): 200, ('10-0', '10-1'): 200, ('10-1', '10-2'): 200, ('10-2', '10-3'): 200, ('10-3', '10-4'): 200, ('10-4', '10-5'): 200, ('10-5', '10-6'): 200, ('10-6', '10-7'): 200, ('10-7', '10-8'): 200, ('10-8', '10-9'): 200, ('2-0', '2-1'): 200, ('2-0', '3-0'): 200, ('2-1', '2-2'): 200, ('2-1', '3-1'): 200, ('2-2', '2-3'): 200, ('2-2', '3-2'): 200, ('2-3', '2-4'): 200, ('2-3', '3-3'): 200, ('2-4', '2-5'): 200, ('2-4', '3-4'): 200, ('2-5', '2-6'): 200, ('2-5', '3-5'): 200, ('2-6', '2-7'): 200, ('2-6', '3-6'): 200, ('2-7', '2-8'): 200, ('2-7', '3-7'): 200, ('2-8', '2-9'): 200, ('2-8', '3-8'): 200, ('2-9', '3-9'): 200, ('3-0', '3-1'): 200, ('3-0', '4-0'): 200, ('3-1', '3-2'): 200, ('3-1', '4-1'): 200, ('3-2', '3-3'): 200, ('3-2', '4-2'): 200, ('3-3', '3-4'): 200, ('3-3', '4-3'): 200, ('3-4', '3-5'): 200, ('3-4', '4-4'): 200, ('3-5', '3-6'): 200, ('3-5', '4-5'): 200, ('3-6', '3-7'): 200, ('3-6', '4-6'): 200, ('3-7', '3-8'): 200, ('3-7', '4-7'): 200, ('3-8', '3-9'): 200, ('3-8', '4-8'): 200, ('3-9', '4-9'): 200, ('4-0', '4-1'): 200, ('4-0', '5-0'): 200, ('4-1', '4-2'): 200, ('4-1', '5-1'): 200, ('4-2', '4-3'): 200, ('4-2', '5-2'): 200, ('4-3', '4-4'): 200, ('4-3', '5-3'): 200, ('4-4', '4-5'): 200, ('4-4', '5-4'): 200, ('4-5', '4-6'): 200, ('4-5', '5-5'): 200, ('4-6', '4-7'): 200, ('4-6', '5-6'): 200, ('4-7', '4-8'): 200, ('4-7', '5-7'): 200, ('4-8', '4-9'): 200, ('4-8', '5-8'): 200, ('4-9', '5-9'): 200, ('5-0', '5-1'): 200, ('5-0', '6-0'): 200, ('5-1', '5-2'): 200, ('5-1', '6-1'): 200, ('5-2', '5-3'): 200, ('5-2', '6-2'): 200, ('5-3', '5-4'): 200, ('5-3', '6-3'): 200, ('5-4', '5-5'): 200, ('5-4', '6-4'): 200, ('5-5', '5-6'): 200, ('5-5', '6-5'): 200, ('5-6', '5-7'): 200, ('5-6', '6-6'): 200, ('5-7', '5-8'): 200, ('5-7', '6-7'): 200, ('5-8', '5-9'): 200, ('5-8', '6-8'): 200, ('5-9', '6-9'): 200, ('6-0', '6-1'): 200, ('6-0', '7-0'): 200, ('6-1', '6-2'): 200, ('6-1', '7-1'): 200, ('6-2', '6-3'): 200, ('6-2', '7-2'): 200, ('6-3', '6-4'): 200, ('6-3', '7-3'): 200, ('6-4', '6-5'): 200, ('6-4', '7-4'): 200, ('6-5', '6-6'): 200, ('6-5', '7-5'): 200, ('6-6', '6-7'): 200, ('6-6', '7-6'): 200, ('6-7', '6-8'): 200, ('6-7', '7-7'): 200, ('6-8', '6-9'): 200, ('6-8', '7-8'): 200, ('6-9', '7-9'): 200, ('7-0', '7-1'): 200, ('7-0', '8-0'): 200, ('7-1', '7-2'): 200, ('7-1', '8-1'): 200, ('7-2', '7-3'): 200, ('7-2', '8-2'): 200, ('7-3', '7-4'): 200, ('7-3', '8-3'): 200, ('7-4', '7-5'): 200, ('7-4', '8-4'): 200, ('7-5', '7-6'): 200, ('7-5', '8-5'): 200, ('7-6', '7-7'): 200, ('7-6', '8-6'): 200, ('7-7', '7-8'): 200, ('7-7', '8-7'): 200, ('7-8', '7-9'): 200, ('7-8', '8-8'): 200, ('7-9', '8-9'): 200, ('8-0', '8-1'): 200, ('8-0', '9-0'): 200, ('8-1', '8-2'): 200, ('8-1', '9-1'): 200, ('8-2', '8-3'): 200, ('8-2', '9-2'): 200, ('8-3', '8-4'): 200, ('8-3', '9-3'): 200, ('8-4', '8-5'): 200, ('8-4', '9-4'): 200, ('8-5', '8-6'): 200, ('8-5', '9-5'): 200, ('8-6', '8-7'): 200, ('8-6', '9-6'): 200, ('8-7', '8-8'): 200, ('8-7', '9-7'): 200, ('8-8', '8-9'): 200, ('8-8', '9-8'): 200, ('8-9', '9-9'): 200, ('9-0', '10-0'): 200, ('9-0', '9-1'): 200, ('9-1', '10-1'): 200, ('9-1', '9-2'): 200, ('9-2', '10-2'): 200, ('9-2', '9-3'): 200, ('9-3', '10-3'): 200, ('9-3', '9-4'): 200, ('9-4', '10-4'): 200, ('9-4', '9-5'): 200, ('9-5', '10-5'): 200, ('9-5', '9-6'): 200, ('9-6', '10-6'): 200, ('9-6', '9-7'): 200, ('9-7', '10-7'): 200, ('9-7', '9-8'): 200, ('9-8', '10-8'): 200, ('9-8', '9-9'): 200, ('9-9', '10-9'): 200}

voltages = {'battery': 1000, ('0-0', '0-1'): 0, ('0-0', '1-0'): 0, ('0-1', '0-2'): 0, ('0-1', '1-1'): 0, ('0-2', '0-3'): 0, ('0-2', '1-2'): 0, ('0-3', '0-4'): 0, ('0-3', '1-3'): 0, ('0-4', '0-5'): 0, ('0-4', '1-4'): 0, ('0-5', '0-6'): 0, ('0-5', '1-5'): 0, ('0-6', '0-7'): 0, ('0-6', '1-6'): 0, ('0-7', '0-8'): 0, ('0-7', '1-7'): 0, ('0-8', '0-9'): 0, ('0-8', '1-8'): 0, ('0-9', '1-9'): 0, ('1-0', '1-1'): 0, ('1-0', '2-0'): 0, ('1-1', '1-2'): 0, ('1-1', '2-1'): 0, ('1-2', '1-3'): 0, ('1-2', '2-2'): 0, ('1-3', '1-4'): 0, ('1-3', '2-3'): 0, ('1-4', '1-5'): 0, ('1-4', '2-4'): 0, ('1-5', '1-6'): 0, ('1-5', '2-5'): 0, ('1-6', '1-7'): 0, ('1-6', '2-6'): 0, ('1-7', '1-8'): 0, ('1-7', '2-7'): 0, ('1-8', '1-9'): 0, ('1-8', '2-8'): 0, ('1-9', '2-9'): 0, ('10-0', '10-1'): 0, ('10-1', '10-2'): 0, ('10-2', '10-3'): 0, ('10-3', '10-4'): 0, ('10-4', '10-5'): 0, ('10-5', '10-6'): 0, ('10-6', '10-7'): 0, ('10-7', '10-8'): 0, ('10-8', '10-9'): 0, ('2-0', '2-1'): 0, ('2-0', '3-0'): 0, ('2-1', '2-2'): 0, ('2-1', '3-1'): 0, ('2-2', '2-3'): 0, ('2-2', '3-2'): 0, ('2-3', '2-4'): 0, ('2-3', '3-3'): 0, ('2-4', '2-5'): 0, ('2-4', '3-4'): 0, ('2-5', '2-6'): 0, ('2-5', '3-5'): 0, ('2-6', '2-7'): 0, ('2-6', '3-6'): 0, ('2-7', '2-8'): 0, ('2-7', '3-7'): 0, ('2-8', '2-9'): 0, ('2-8', '3-8'): 0, ('2-9', '3-9'): 0, ('3-0', '3-1'): 0, ('3-0', '4-0'): 0, ('3-1', '3-2'): 0, ('3-1', '4-1'): 0, ('3-2', '3-3'): 0, ('3-2', '4-2'): 0, ('3-3', '3-4'): 0, ('3-3', '4-3'): 0, ('3-4', '3-5'): 0, ('3-4', '4-4'): 0, ('3-5', '3-6'): 0, ('3-5', '4-5'): 0, ('3-6', '3-7'): 0, ('3-6', '4-6'): 0, ('3-7', '3-8'): 0, ('3-7', '4-7'): 0, ('3-8', '3-9'): 0, ('3-8', '4-8'): 0, ('3-9', '4-9'): 0, ('4-0', '4-1'): 0, ('4-0', '5-0'): 0, ('4-1', '4-2'): 0, ('4-1', '5-1'): 0, ('4-2', '4-3'): 0, ('4-2', '5-2'): 0, ('4-3', '4-4'): 0, ('4-3', '5-3'): 0, ('4-4', '4-5'): 0, ('4-4', '5-4'): 0, ('4-5', '4-6'): 0, ('4-5', '5-5'): 0, ('4-6', '4-7'): 0, ('4-6', '5-6'): 0, ('4-7', '4-8'): 0, ('4-7', '5-7'): 0, ('4-8', '4-9'): 0, ('4-8', '5-8'): 0, ('4-9', '5-9'): 0, ('5-0', '5-1'): 0, ('5-0', '6-0'): 0, ('5-1', '5-2'): 0, ('5-1', '6-1'): 0, ('5-2', '5-3'): 0, ('5-2', '6-2'): 0, ('5-3', '5-4'): 0, ('5-3', '6-3'): 0, ('5-4', '5-5'): 0, ('5-4', '6-4'): 0, ('5-5', '5-6'): 0, ('5-5', '6-5'): 0, ('5-6', '5-7'): 0, ('5-6', '6-6'): 0, ('5-7', '5-8'): 0, ('5-7', '6-7'): 0, ('5-8', '5-9'): 0, ('5-8', '6-8'): 0, ('5-9', '6-9'): 0, ('6-0', '6-1'): 0, ('6-0', '7-0'): 0, ('6-1', '6-2'): 0, ('6-1', '7-1'): 0, ('6-2', '6-3'): 0, ('6-2', '7-2'): 0, ('6-3', '6-4'): 0, ('6-3', '7-3'): 0, ('6-4', '6-5'): 0, ('6-4', '7-4'): 0, ('6-5', '6-6'): 0, ('6-5', '7-5'): 0, ('6-6', '6-7'): 0, ('6-6', '7-6'): 0, ('6-7', '6-8'): 0, ('6-7', '7-7'): 0, ('6-8', '6-9'): 0, ('6-8', '7-8'): 0, ('6-9', '7-9'): 0, ('7-0', '7-1'): 0, ('7-0', '8-0'): 0, ('7-1', '7-2'): 0, ('7-1', '8-1'): 0, ('7-2', '7-3'): 0, ('7-2', '8-2'): 0, ('7-3', '7-4'): 0, ('7-3', '8-3'): 0, ('7-4', '7-5'): 0, ('7-4', '8-4'): 0, ('7-5', '7-6'): 0, ('7-5', '8-5'): 0, ('7-6', '7-7'): 0, ('7-6', '8-6'): 0, ('7-7', '7-8'): 0, ('7-7', '8-7'): 0, ('7-8', '7-9'): 0, ('7-8', '8-8'): 0, ('7-9', '8-9'): 0, ('8-0', '8-1'): 0, ('8-0', '9-0'): 0, ('8-1', '8-2'): 0, ('8-1', '9-1'): 0, ('8-2', '8-3'): 0, ('8-2', '9-2'): 0, ('8-3', '8-4'): 0, ('8-3', '9-3'): 0, ('8-4', '8-5'): 0, ('8-4', '9-4'): 0, ('8-5', '8-6'): 0, ('8-5', '9-5'): 0, ('8-6', '8-7'): 0, ('8-6', '9-6'): 0, ('8-7', '8-8'): 0, ('8-7', '9-7'): 0, ('8-8', '8-9'): 0, ('8-8', '9-8'): 0, ('8-9', '9-9'): 0, ('9-0', '10-0'): 0, ('9-0', '9-1'): 0, ('9-1', '10-1'): 0, ('9-1', '9-2'): 0, ('9-2', '10-2'): 0, ('9-2', '9-3'): 0, ('9-3', '10-3'): 0, ('9-3', '9-4'): 0, ('9-4', '10-4'): 0, ('9-4', '9-5'): 0, ('9-5', '10-5'): 0, ('9-5', '9-6'): 0, ('9-6', '10-6'): 0, ('9-6', '9-7'): 0, ('9-7', '10-7'): 0, ('9-7', '9-8'): 0, ('9-8', '10-8'): 0, ('9-8', '9-9'): 0, ('9-9', '10-9'): 0}

soln = {'battery': 9.90619606169875, ('0-0', '0-1'): 0.025786753996051744, ('0-0', '1-0'): -0.025786753996051744, ('0-1', '0-2'): 0.05461105844007207, ('0-1', '1-1'): -0.02882430444402033, ('0-2', '0-3'): 0.08702523625623072, ('0-2', '1-2'): -0.03241417781615894, ('0-3', '0-4'): 0.11761365548141427, ('0-3', '1-3'): -0.030588419225183544, ('0-4', '0-5'): 0.13249334072025648, ('0-4', '1-4'): -0.0148796852388422, ('0-5', '0-6'): 0.11761365548141431, ('0-5', '1-5'): 0.014879685238842172, ('0-6', '0-7'): 0.08702523625623083, ('0-6', '1-6'): 0.030588419225183475, ('0-7', '0-8'): 0.05461105844007195, ('0-7', '1-7'): 0.032414177816158886, ('0-8', '0-9'): 0.025786753996051567, ('0-8', '1-8'): 0.028824304444020364, ('0-9', '1-9'): 0.025786753996051567, ('1-0', '1-1'): 0.02274920354808259, ('1-0', '2-0'): -0.04853595754413433, ('1-1', '1-2'): 0.05102118506793318, ('1-1', '2-1'): -0.05709628596387077, ('1-2', '1-3'): 0.0888509948472067, ('1-2', '2-2'): -0.0702439875954316, ('1-3', '1-4'): 0.13332238946775563, ('1-3', '2-3'): -0.07505981384573204, ('1-4', '1-5'): 0.16225271119794057, ('1-4', '2-4'): -0.04381000696902639, ('1-5', '1-6'): 0.13332238946775563, ('1-5', '2-5'): 0.043810006969026885, ('1-6', '1-7'): 0.0888509948472064, ('1-6', '2-6'): 0.07505981384573274, ('1-7', '1-8'): 0.0510211850679333, ('1-7', '2-7'): 0.07024398759543209, ('1-8', '1-9'): 0.02274920354808281, ('1-8', '2-8'): 0.057096285963870876, ('1-9', '2-9'): 0.04853595754413438, ('10-0', '10-1'): 0.025786753996051605, ('10-1', '10-2'): 0.05461105844007179, ('10-2', '10-3'): 0.08702523625623074, ('10-3', '10-4'): 0.117613655481414, ('10-4', '10-5'): 0.13249334072025598, ('10-5', '10-6'): 0.11761365548141406, ('10-6', '10-7'): 0.08702523625623065, ('10-7', '10-8'): 0.05461105844007186, ('10-8', '10-9'): 0.025786753996051574, ('2-0', '2-1'): 0.014188875128346155, ('2-0', '3-0'): -0.06272483267248048, ('2-1', '2-2'): 0.03787348343637234, ('2-1', '3-1'): -0.08078089427189653, ('2-2', '2-3'): 0.08403516859690625, ('2-2', '3-2'): -0.11640567275596553, ('2-3', '2-4'): 0.16457219634446127, ('2-3', '3-3'): -0.1555968415932864, ('2-4', '2-5'): 0.24987272513599387, ('2-4', '3-4'): -0.12911053576055898, ('2-5', '2-6'): 0.16457219634446146, ('2-5', '3-5'): 0.12911053576055956, ('2-6', '2-7'): 0.08403516859690577, ('2-6', '3-6'): 0.1555968415932884, ('2-7', '2-8'): 0.03787348343637209, ('2-7', '3-7'): 0.11640567275596585, ('2-8', '2-9'): 0.014188875128346322, ('2-8', '3-8'): 0.08078089427189665, ('2-9', '3-9'): 0.06272483267248072, ('3-0', '3-1'): -0.0038671864710698857, ('3-0', '4-0'): -0.058857646201411595, ('3-1', '3-2'): 0.002248704952303342, ('3-1', '4-1'): -0.08689678569526961, ('3-2', '3-3'): 0.04484399975958539, ('3-2', '4-2'): -0.15900096756324672, ('3-3', '3-4'): 0.1910585021771888, ('3-3', '4-3'): -0.3018113440108898, ('3-4', '3-5'): 0.5080937966571124, ('3-4', '4-4'): -0.4461458302404823, ('3-5', '3-6'): 0.1910585021771903, ('3-5', '4-5'): 0.4461458302404816, ('3-6', '3-7'): 0.044843999759583204, ('3-6', '4-6'): 0.3018113440108876, ('3-7', '3-8'): 0.0022487049523029212, ('3-7', '4-7'): 0.15900096756324614, ('3-8', '3-9'): -0.003867186471069646, ('3-8', '4-8'): 0.08689678569526915, ('3-9', '4-9'): 0.058857646201411075, ('4-0', '4-1'): -0.0319063259649279, ('4-0', '5-0'): -0.026951320236483695, ('4-1', '4-2'): -0.06985547691567376, ('4-1', '5-1'): -0.048947634744523044, ('4-2', '4-3'): -0.09796637668805772, ('4-2', '5-2'): -0.1308900677908629, ('4-3', '4-4'): 0.046724015947596204, ('4-3', '5-3'): -0.44650173664654264, ('4-4', '4-5'): 1.4003854571380765, ('4-4', '5-4'): -1.799807271430962, ('4-5', '4-6'): 0.046724015947596204, ('4-5', '5-5'): 1.7998072714309614, ('4-6', '4-7'): -0.09796637668805822, ('4-6', '5-6'): 0.446501736646542, ('4-7', '4-8'): -0.06985547691567412, ('4-7', '5-7'): 0.130890067790862, ('4-8', '4-9'): -0.03190632596492773, ('4-8', '5-8'): 0.048947634744522794, ('4-9', '5-9'): 0.026951320236483348, ('5-0', '5-1'): -0.05390264047296739, ('5-0', '6-0'): 0.026951320236483695, ('5-1', '5-2'): -0.15179790996201362, ('5-1', '6-1'): 0.04894763474452333, ('5-2', '5-3'): -0.41357804554373745, ('5-2', '6-2'): 0.13089006779086332, ('5-3', '5-4'): -1.3065815188368233, ('5-3', '6-3'): 0.4465017366465432, ('5-4', '5-5'): 5.0, ('5-4', '6-4'): 1.799807271430962, ('5-5', '5-6'): -1.306581518836823, ('5-5', '6-5'): -1.799807271430962, ('5-6', '5-7'): -0.4135780455437382, ('5-6', '6-6'): -0.4465017366465433, ('5-7', '5-8'): -0.15179790996201334, ('5-7', '6-7'): -0.13089006779086293, ('5-8', '5-9'): -0.05390264047296716, ('5-8', '6-8'): -0.04894763474452342, ('5-9', '6-9'): -0.026951320236483837, ('6-0', '6-1'): -0.0319063259649279, ('6-0', '7-0'): 0.058857646201411595, ('6-1', '6-2'): -0.06985547691567362, ('6-1', '7-1'): 0.08689678569526961, ('6-2', '6-3'): -0.09796637668805758, ('6-2', '7-2'): 0.15900096756324658, ('6-3', '6-4'): 0.046724015947595635, ('6-3', '7-3'): 0.3018113440108894, ('6-4', '6-5'): 1.4003854571380756, ('6-4', '7-4'): 0.446145830240482, ('6-5', '6-6'): 0.046724015947595635, ('6-5', '7-5'): -0.4461458302404823, ('6-6', '6-7'): -0.09796637668805783, ('6-6', '7-6'): -0.30181134401088977, ('6-7', '6-8'): -0.06985547691567381, ('6-7', '7-7'): -0.159000967563247, ('6-8', '6-9'): -0.03190632596492762, ('6-8', '7-8'): -0.08689678569526961, ('6-9', '7-9'): -0.05885764620141146, ('7-0', '7-1'): -0.003867186471069456, ('7-0', '8-0'): 0.06272483267248105, ('7-1', '7-2'): 0.002248704952303342, ('7-1', '8-1'): 0.08078089427189682, ('7-2', '7-3'): 0.044843999759585244, ('7-2', '8-2'): 0.11640567275596539, ('7-3', '7-4'): 0.19105850217718826, ('7-3', '8-3'): 0.15559684159328654, ('7-4', '7-5'): 0.5080937966571113, ('7-4', '8-4'): 0.12911053576055906, ('7-5', '7-6'): 0.19105850217718817, ('7-5', '8-5'): -0.12911053576055917, ('7-6', '7-7'): 0.04484399975958497, ('7-6', '8-6'): -0.15559684159328668, ('7-7', '7-8'): 0.002248704952303546, ('7-7', '8-7'): -0.11640567275596556, ('7-8', '7-9'): -0.0038671864710694147, ('7-8', '8-8'): -0.08078089427189672, ('7-9', '8-9'): -0.06272483267248086, ('8-0', '8-1'): 0.014188875128346573, ('8-0', '9-0'): 0.04853595754413448, ('8-1', '8-2'): 0.03787348343637191, ('8-1', '9-1'): 0.057096285963871056, ('8-2', '8-3'): 0.0840351685969064, ('8-2', '9-2'): 0.07024398759543232, ('8-3', '8-4'): 0.16457219634446077, ('8-3', '9-3'): 0.07505981384573204, ('8-4', '8-5'): 0.24987272513599307, ('8-4', '9-4'): 0.04381000696902653, ('8-5', '8-6'): 0.1645721963444607, ('8-5', '9-5'): -0.0438100069690266, ('8-6', '8-7'): 0.08403516859690609, ('8-6', '9-6'): -0.07505981384573202, ('8-7', '8-8'): 0.03787348343637238, ('8-7', '9-7'): -0.07024398759543177, ('8-8', '8-9'): 0.01418887512834645, ('8-8', '9-8'): -0.057096285963870806, ('8-9', '9-9'): -0.04853595754413441, ('9-0', '10-0'): 0.025786753996051605, ('9-0', '9-1'): 0.022749203548082873, ('9-1', '10-1'): 0.02882430444402033, ('9-1', '9-2'): 0.05102118506793318, ('9-2', '10-2'): 0.03241417781615894, ('9-2', '9-3'): 0.08885099484720613, ('9-3', '10-3'): 0.03058841922518326, ('9-3', '9-4'): 0.13332238946775526, ('9-4', '10-4'): 0.014879685238842057, ('9-4', '9-5'): 0.16225271119793994, ('9-5', '10-5'): -0.014879685238841915, ('9-5', '9-6'): 0.13332238946775526, ('9-6', '10-6'): -0.030588419225183117, ('9-6', '9-7'): 0.08885099484720634, ('9-7', '10-7'): -0.032414177816158796, ('9-7', '9-8'): 0.05102118506793335, ('9-8', '10-8'): -0.02882430444402029, ('9-8', '9-9'): 0.02274920354808285, ('9-9', '10-9'): -0.025786753996051574}
