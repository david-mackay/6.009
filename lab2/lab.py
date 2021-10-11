# NO IMPORTS ALLOWED!

import json

def did_x_and_y_act_together(data, actor_id_1, actor_id_2):
    for item in data:
        if actor_id_1 == item[0] and actor_id_2 == item[1]:
            return (True)
        if actor_id_1 == item[1] and actor_id_2 == item[0]:
            return(True)            
        else:
            continue
    return (False)

def get_actor_id_from_name(name):
    with open('resources/names.json') as f:
        names = json.load(f)
    return (names[name])

def get_actor_name_from_id(idnumber):
    with open('resources/names.json')as f:
        names = json.load(f)
    for i in names:
        if names[i] == idnumber:
            return(i)
def get_actors_with_bacon_number(data, n, visited = None, dic = None):
    if dic is None:
        
        dic = {}
        for row in data:
            if row[0] in dic:
                dic[row[0]].add(row[1])
            else:
                dic[row[0]] = set()
                dic[row[0]].add(row[1])
            if row[1] in dic:
                dic[row[1]].add(row[0])
            else:
                dic[row[1]] = set()
                dic[row[1]].add(row[0])
                
    if visited is None:
        visited = set()
        
    if n == 0:
        visited.update({4724})
        return {4724}
    else:
        bacon2 = set()
        val = get_actors_with_bacon_number(data, n-1, visited, dic)
        if val == set():
            return val
        for actor in val:
#            print('for loop start')
            bacon2.update(dic[actor])

        
        ans = bacon2.difference(visited)

        visited.update(bacon2)

    return(ans)
        


def get_bacon_path(data, actor_id):
    return(get_path(data, 4724, actor_id))

def get_path(data, actor_id_1, actor_id_2):
    dic = {}
    for row in data:
        if row[0] in dic:
            dic[row[0]].add(row[1])
        else:
            dic[row[0]] = set()
            dic[row[0]].add(row[1])
        if row[1] in dic:
            dic[row[1]].add(row[0])
        else:
            dic[row[1]] = set()
            dic[row[1]].add(row[0])
    
    list_of_paths = []
    list_of_paths.append([actor_id_1])
    found = set()
    count= 0
    while actor_id_2 not in found and count < len(list_of_paths):
        current_path = list_of_paths[count]
        for actor in dic[current_path[-1]]:
            if actor not in found:            
                x = current_path.copy()
                x.append(actor)
                list_of_paths.append(x)
                found.add(actor)
            if actor == actor_id_2:
                return(x)        
        count +=1
    return(None)

def get_movies(data, path):
    dic = {}
    for row in data:
        actor_pair = (row[0], row[1])
        actor_pair2 = (row[1], row[2])
        dic[actor_pair] = row[2]
        dic[actor_pair2] = row[2]
    list_of_movies = []
    for i in range(len(path)):
        if i == 0:
            continue
        actors = (path[i], path[i-1])
        actors2 = (path[i-1], path[i])
        if actors in dic:
            list_of_movies.append(dic[actors])
        else:
            list_of_movies.append(dic[actors2])
    return(list_of_movies)
    
def movies_to_name(movieids):
    with open('resources/movies.json')as f:
        names = json.load(f)
    for i in names:
        if names[i] == movieids:
            return(i)
if __name__ == '__main__':
    filename ='resources/large.json'
    with open(filename, 'r') as f:
        smalldb = json.load(f)
    moviename = 'resources/movies.json'
    with open(moviename, 'r') as d:
        movies = json.load(d)
#    print(smalldb)
#    y = (get_actors_with_bacon_number(smalldb, 6))
#    print(y)
#    print(list(map(get_actor_name_from_id, [4724, 4610, 102429, 31155, 105288, 1134971])))
#    print(get_actor_id_from_name('Eugene Byrd'))
#    print(get_path(smalldb, 1395659, 342))
#    print(did_x_and_y_act_together(smalldb, get_actor_id_from_name('Dominique Ducos'), get_actor_id_from_name('Andre Wilms')))
#    print(did_x_and_y_act_together(smalldb, get_actor_id_from_name('Jan Malmsjo'), get_actor_id_from_name('Kevin Bacon')))
    
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    pass
