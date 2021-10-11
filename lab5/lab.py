"""6.009 Lab 5 -- Don't Turn Left!"""

# NO ADDITIONAL IMPORTS

def shortest_path(edges, start, end):
    """
    Finds a shortest path from start to end using the provided edges

    Args:
        edges: a list of dictionaries, where each dictionary has two items. 
            These items have keys `"start"` and `"end"` and values that are 
            tuples (two integers), to specify grid locations.
        start: a tuple representing our initial location.
        end: a tuple representing the target location.

    Returns:
        A list containing the edges taken in the resulting path if one exists, 
            None if there is no path

        formatted as:
            [{"start":(x1,y1), "end":(x2,y2)}, {"start":(x2,y2), "end":(x3,y3)}]
    """

    adj_dic = adj(edges)

    visited = set()
    if start == end:
        return
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            if node not in adj_dic.keys():
                continue
            neighbours = adj_dic[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == end:
                    final_ans = []
                    for n, node in enumerate(new_path):
                        if n<(len(new_path)-1):
                            final_ans.append({"start" : node, "end": new_path[n+1]})
                    return final_ans
            visited.add(node)
    return None
        
def cross_product(v1, v2):
    ans = (v1[0] *v2[1]) - (v1[1] * v2[0])
    return(ans)

def dot_product(v1, v2):
    ans = (v1[0]*v2[0]) +(v1[1]*v2[1])
    return (ans)
def direction(v1,v2):
    """
    Returns type of turn 2 vectors make.
    """
    if cross_product(v1,v2) < 0:
        return "left"
    if cross_product(v1,v2) > 0:
        return "right"
    if cross_product(v1,v2) == 0:
        if dot_product(v1,v2) < 0:
            return "u-turn"
        else:
            return "straight"
    else:
        return "straight"
def vec(tup1, tup2):
    """
    Turns 2 points into their vector
    """
    ans = (tup2[0] - tup1[0], tup2[1] - tup1[1])
    return(ans)
def adj(edges):
    """
    Takes edges and converts into an adjacent dictionary
    Returns dictionary mapping each possible starting point to all possible end points.
    """
    adj_dic = {}
    for edge in edges:
        edge_start = edge["start"]
        if edge_start not in adj_dic.keys():
            adj_dic[edge_start] = set()
            adj_dic[edge_start].add(edge["end"])
        else:
            adj_dic[edge_start].add(edge["end"])

    return adj_dic
def shortest_path_no_lefts(edges, start, end):
    
    """
    Finds a shortest path without any left turns that goes
        from start to end using the provided edges. 
        (reversing turns are also not allowed)

    Args:
        edges: a list of dictionaries, where each dictionary has two items. 
            These items have keys `"start"` and `"end"` and values that are 
            tuples (two integers), to specify grid locations.
        start: a tuple representing our initial location.
        end: a tuple representing the target location.

    Returns:
        A list containing the edges taken in the resulting path if one exists, 
            None if there is no path

        formatted as:
            [{"start":(x1,y1), "end":(x2,y2)}, {"start":(x2,y2), "end":(x3,y3)}]
    """
    adj_dic = adj(edges)


    H_naught = {}
    for edge in edges:
        transition = (edge["start"], edge["end"])
        vector = vec(edge["start"], edge["end"])
        H_naught[transition] = vector
    
    Transitions ={}
    
    for val in H_naught:
        v1 = H_naught[val]
        i = val[1]
        if i not in adj_dic.keys():
            continue
        for turn in adj_dic[i]:
            v2 = H_naught[(i,turn)]

            if direction(v1,v2) != "left" and direction (v1,v2) != "u-turn":
                if val not in Transitions.keys():
                    Transitions[val] = set()
                Transitions[val].add((i,turn)) #possible remove brackets
        # H_naught = dictionary of every possible transition vector
        #Transitions is all valid Transitions
    visited = set()
    if start == end:
        return

    beginning = []
    for star in Transitions:
        if star[0] == start:
            beginning.append([star])
    queue = beginning

    while queue:

        

        path = queue.pop(0)

        node = path[-1]

        if node not in visited:
            if node not in Transitions.keys():
                continue
            neighbours = Transitions[node]


            for neighbour in neighbours:

                new_path = list(path)

                new_path.append(neighbour)
            

                queue.append(new_path)

                if neighbour[1] == end:
                    final_ans = []
                    for n, node in enumerate(new_path):
                        final_ans.append({"start" : node[0], "end": node[1]})
                    
                    return(final_ans)
            visited.add(node)
    return None



    

def shortest_path_k_lefts(edges, start, end, k):
    """
    Finds a shortest path with no more than k left turns that 
        goes from start to end using the provided edges.
        (reversing turns are also not allowed)

    Args:
        edges: a list of dictionaries, where each dictionary has two items. 
            These items have keys `"start"` and `"end"` and values that are 
            tuples (two integers), to specify grid locations.
        start: a tuple representing our initial location.
        end: a tuple representing the target location.
        k: the max number of allowed left turns.

    Returns:
        A list containing the edges taken in the resulting path if one exists, 
            None if there is no path

        formatted as:
            [{"start":(x1,y1), "end":(x2,y2)}, {"start":(x2,y2), "end":(x3,y3)}]
    """
    adj_dic = adj(edges)
    H_naught = {}
    for edge in edges:
        transition = (edge["start"], edge["end"])
        vector = vec(edge["start"], edge["end"])
        H_naught[transition] = vector
    
    Transitions ={}
    
    for val in H_naught:
        v1 = H_naught[val]
        i = val[1]
        if i not in adj_dic.keys():
            continue
        for turn in adj_dic[i]:
            v2 = H_naught[(i,turn)]

            if direction(v1,v2) != "u-turn":
                if val not in Transitions.keys():
                    Transitions[val] = set()
                Transitions[val].add(((i,turn), (direction(v1,v2))))
    print(Transitions) #possible remove brackets
    



if __name__ == "__main__":
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used for testing.
    print(shortest_path_k_lefts(
      [
        {"start":(1,1), "end":(1,0)},
        {"start":(1,2), "end":(1,1)},
        {"start":(3,0), "end":(2,0)},
        {"start":(1,4), "end":(2,3)},
        {"start":(1,4), "end":(1,3)},
        {"start":(1,3), "end":(2,3)},
        {"start":(2,3), "end":(3,3)},
        {"start":(2,3), "end":(2,2)},
        {"start":(2,4), "end":(2,3)},
        {"start":(2,2), "end":(3,2)},
        {"start":(3,0), "end":(4,0)},
        {"start":(3,1), "end":(3,0)},
        {"start":(3,1), "end":(2,1)},
        {"start":(3,2), "end":(3,1)},
        {"start":(3,2), "end":(4,2)},
        {"start":(3,3), "end":(3,2)},
        {"start":(3,3), "end":(4,4)},
        {"start":(4,0), "end":(4,1)},
        {"start":(4,1), "end":(3,1)},
        {"start":(4,4), "end":(3,4)},
        {"start":(3,4), "end":(3,3)},
        {"start":(3,4), "end":(2,4)},
      ],
      (1,4),
      (2,1),
      1,
    ))
    print(dot_product((0,-1),(0,-1)))


    


