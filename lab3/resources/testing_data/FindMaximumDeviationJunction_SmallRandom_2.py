junctions = {'X_0', 'X_1', 'X_10', 'X_11', 'X_12', 'X_13', 'X_14', 'X_2', 'X_3', 'X_4', 'X_5', 'X_6', 'X_7', 'X_8', 'X_9'}

wires = {'W_0': ('X_6', 'X_5'), 'W_1': ('X_14', 'X_6'), 'W_10': ('X_1', 'X_14'), 'W_11': ('X_2', 'X_0'), 'W_12': ('X_0', 'X_9'), 'W_13': ('X_12', 'X_13'), 'W_14': ('X_1', 'X_10'), 'W_15': ('X_10', 'X_7'), 'W_16': ('X_1', 'X_2'), 'W_17': ('X_8', 'X_11'), 'W_18': ('X_0', 'X_10'), 'W_19': ('X_12', 'X_1'), 'W_2': ('X_8', 'X_4'), 'W_20': ('X_10', 'X_13'), 'W_21': ('X_10', 'X_11'), 'W_22': ('X_10', 'X_11'), 'W_23': ('X_6', 'X_9'), 'W_24': ('X_6', 'X_5'), 'W_25': ('X_6', 'X_12'), 'W_26': ('X_4', 'X_8'), 'W_27': ('X_4', 'X_6'), 'W_28': ('X_14', 'X_9'), 'W_29': ('X_12', 'X_7'), 'W_3': ('X_9', 'X_0'), 'W_30': ('X_2', 'X_3'), 'W_31': ('X_10', 'X_3'), 'W_32': ('X_2', 'X_7'), 'W_33': ('X_10', 'X_11'), 'W_34': ('X_9', 'X_11'), 'W_35': ('X_7', 'X_6'), 'W_36': ('X_13', 'X_5'), 'W_37': ('X_2', 'X_10'), 'W_38': ('X_14', 'X_2'), 'W_39': ('X_1', 'X_0'), 'W_4': ('X_13', 'X_0'), 'W_5': ('X_2', 'X_11'), 'W_6': ('X_11', 'X_9'), 'W_7': ('X_9', 'X_0'), 'W_8': ('X_11', 'X_3'), 'W_9': ('X_7', 'X_2')}

resistances = {'W_0': 3.0764726767942765, 'W_1': 6.201451227573388, 'W_10': 2.2922971338008606, 'W_11': 3.3990567465141566, 'W_12': 6.200098139336808, 'W_13': 1.5165168994124727, 'W_14': 1.841676880901457, 'W_15': 8.735506046961397, 'W_16': 1.7008026400637255, 'W_17': 3.517714067236224, 'W_18': 5.173739737993735, 'W_19': 7.445832739445319, 'W_2': 4.4518965755974556, 'W_20': 8.665380654948395, 'W_21': 2.1488978047178495, 'W_22': 7.746559200941368, 'W_23': 8.635626933688648, 'W_24': 7.60079169375345, 'W_25': 5.050134545169273, 'W_26': 2.9037918549890045, 'W_27': 9.077046493712222, 'W_28': 4.418313570982671, 'W_29': 7.5881537700083594, 'W_3': 8.030886107993403, 'W_30': 1.2792171018564655, 'W_31': 1.5792933098223392, 'W_32': 3.96163129879294, 'W_33': 2.066644977058509, 'W_34': 7.417422993014345, 'W_35': 9.736177609930156, 'W_36': 1.2685947463455585, 'W_37': 2.377560925609529, 'W_38': 4.701192539552342, 'W_39': 5.58814956991717, 'W_4': 4.954550598109068, 'W_5': 3.8699575551420224, 'W_6': 6.254086036499532, 'W_7': 4.89337678106148, 'W_8': 1.6544572378407556, 'W_9': 5.997159287553807}

voltages = {'W_0': 166.87068758982105, 'W_1': 690.4425246579519, 'W_10': 900.9264016451308, 'W_11': 226.0921355432273, 'W_12': 435.4620035133699, 'W_13': 400.05327936829394, 'W_14': 22.480245498392165, 'W_15': 231.17289351406026, 'W_16': 945.7871417588295, 'W_17': 29.064544129909606, 'W_18': 177.15312040353723, 'W_19': 720.5317616583505, 'W_2': 731.892582420186, 'W_20': 838.9496174694592, 'W_21': 889.1784587341893, 'W_22': 609.4474351289491, 'W_23': 961.7160593892622, 'W_24': 680.2736120470798, 'W_25': 967.6628056009808, 'W_26': 686.4436581402605, 'W_27': 326.41333771575944, 'W_28': 885.2332119006467, 'W_29': 215.1020781741893, 'W_3': 661.9193913850642, 'W_30': 181.44492838767212, 'W_31': 237.9709015942901, 'W_32': 229.14529827849245, 'W_33': 997.5251030533773, 'W_34': 553.0016417265789, 'W_35': 893.8263872021296, 'W_36': 589.9244562594675, 'W_37': 518.7316689718597, 'W_38': 972.703055925091, 'W_39': 595.6355549247917, 'W_4': 155.89437137304637, 'W_5': 258.25561252236764, 'W_6': 120.69890436179918, 'W_7': 282.5542105377079, 'W_8': 360.845479902683, 'W_9': 19.519275044231133}

currents = {'W_0': -128.4294451948666, 'W_1': 61.12155549507807, 'W_10': 255.63065889973223, 'W_11': 19.266861687541894, 'W_12': 54.36973139617783, 'W_13': 65.9991175044442, 'W_14': -222.76608600817264, 'W_15': 6.126516605195285, 'W_16': 164.45785812232512, 'W_17': -40.82561428501076, 'W_18': 110.4110292126046, 'W_19': 156.07883456137554, 'W_2': 208.93833953128023, 'W_20': 61.169119802460706, 'W_21': 130.48575151355294, 'W_22': 0.08642822598078198, 'W_23': 76.78427544439565, 'W_24': 15.563279482665012, 'W_25': 228.18995462188707, 'W_26': 168.10224830101953, 'W_27': 40.82561428501076, 'W_28': 62.28560420164205, 'W_29': 6.112002556067268, 'W_3': 94.66996720025884, 'W_30': -86.4893589870608, 'W_31': -182.04565233117074, 'W_32': 71.92371061589441, 'W_33': 188.10545285186387, 'W_34': 58.85035887503282, 'W_35': 90.16120827506465, 'W_36': 112.86616571220158, 'W_37': 316.31518905927925, 'W_38': 132.18203098873693, 'W_39': -41.33177059139571, 'W_4': 14.302071594703223, 'W_5': -30.28336483158527, 'W_6': 37.92441287781149, 'W_7': 77.83526416182357, 'W_8': 268.49459947202286, 'W_9': -6.028357305850602}

soln = {'X_2'}

