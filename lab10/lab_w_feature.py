"""6.009 Fall 2019 Lab 10 -- 6.009 Zoo"""

from math import ceil
from math import acos
# NO OTHER IMPORTS ALLOWED!

class Constants:
    """
    A collection of game-specific constants.

    You can experiment with tweaking these constants, but
    remember to revert the changes when running the test suite!
    """
    # width and height of keepers
    KEEPER_WIDTH = 30
    KEEPER_HEIGHT = 30

    # width and height of animals
    ANIMAL_WIDTH = 30
    ANIMAL_HEIGHT = 30

    # width and height of food
    FOOD_WIDTH = 10
    FOOD_HEIGHT = 10

    # width and height of rocks
    ROCK_WIDTH = 50
    ROCK_HEIGHT = 50

    # thickness of the path
    PATH_THICKNESS = 30

    CRAZY_NAP_LENGTH = 125

    CRAZY_ENDURANCE = 6

    TRAINEE_THRESHOLD = 3

    TEXTURES = {
        'rock': '1f5ff',
        'animal': '1f418',
        'SpeedyZookeeper': '1f472',
        'ThriftyZookeeper': '1f46e',
        'CheeryZookeeper': '1f477',
        'food': '1f34e',
        'Demon': '1f479',
        'VHS': '1f4fc',
        'TraineeZookeeper': '1f476',
        'CrazyZookeeper': '1f61c',
        'SleepingZookeeper': '1f634'
    }

    FORMATION_INFO = {'SpeedyZookeeper':
                       {'price': 9,
                        'interval': 55,
                        'throw_speed_mag': 20},
                      'ThriftyZookeeper':
                       {'price': 7,
                        'interval': 45,
                        'throw_speed_mag': 7},
                      'CheeryZookeeper':
                       {'price': 10,
                        'interval': 35,
                        'throw_speed_mag': 2}, 

                      'TraineeZookeeper':
                       {'price': 4,
                        'interval': 65,
                        'throw_speed_mag': 1},
                      'CrazyZookeeper':
                        {'price': 11,
                         'interval': 10,
                         'throw_speed_mag': 13},

                      'Demon': 
                       {'width': 50,
                        'height': 50,
                        'radius': 75,
                        'multiplier': 2,
                        'price': 8},
                      'VHS':
                       {'width': 30,
                        'height': 30,
                        'radius': 75, 
                        'multiplier': 0.5,
                        'price': 5}}

# New spec for timestep(self, mouse):
# 
# (0. Do not take any action if the player is already defeated.)
#  1. Compute the new speed of animals based on the presence of nearby VHS cassettes or demons.
#  2. Compute any changes in formation locations and remove any off-board formations.
#  3. Handle any food-animal collisions, and remove the fed animals and the eaten food.
#  4. Upgrade trainee zookeeper if needed.
#  5. Throw new food if possible.
#  6. Spawn a new animal from the path's start if needed.
#  7. Handle mouse input, which is the integer tuple coordinate of a player's click, the string 
#     label of a particular particular zookeeper type, `'Demon'`, `'VHS'`, or `None`.
#  8. Redeem one dollar per animal fed this timestep.
#  9. Check for the losing condition.

################################################################################
##  Copy and paste your code from lab9 below EXCEPT for the Constants class.  ##
##  The Constants class above contains the changes needed for the lab.        ##
################################################################################


def get_corners(center, size):
    
    x_min = center[0] - size[0]//2
    x_max = center[0] + size[0]//2
    y_min = center[1] - size[1]//2 
    y_max = center[1] + size[1]//2
    return ((x_min, y_min), (x_max, y_max))

def collide(corners_small, corners_large):
    """
    takes corner tuples that represent the opposite corners and checks if they overlap.

    """
    food_x_min = corners_small[0][0]
    food_x_max = corners_small[1][0]
    biggs_x_min = corners_large[0][0]
    biggs_x_max = corners_large[1][0]
    food_y_min = corners_small[0][1]
    food_y_max = corners_small[1][1]
    biggs_y_min = corners_large[0][1]
    biggs_y_max = corners_large[1][1]
    if biggs_x_min < food_x_min < biggs_x_max or biggs_x_min < food_x_max < biggs_x_max:
        if biggs_y_min < food_y_min < biggs_y_max or biggs_y_min < food_y_max < biggs_y_max:
            return True
    return False
def dot_product(v1,v2):
    return v1[0] * v2[0] + v1[1]*v2[1]
def angle(v1, v2):
    dot = dot_product(v1, v2)
    mag1 = mag(v1)
    mag2 = mag(v2)
    arg = dot/(mag1 * mag2)
    return acos(arg)
def mag(vector):

    return (vector[0]**2 + vector[1]**2)**0.5

class NotEnoughMoneyError(Exception):
    """A custom exception to be used when insufficient funds are available
    to hire new zookeepers. You may leave this class as is."""
    pass


class Game:
    def __init__(self, game_info):
        """Initializes the game.

        `game_info` is a dictionary formatted in the following manner:
          { 'width': The width of the game grid, in an integer (i.e. number of pixels).
            'height': The height of the game grid, in an integer (i.e. number of pixels).
            'rocks': The set of tuple rock coordinates.
            'path_corners': An ordered list of coordinate tuples. The first
                            coordinate is the starting point of the path, the
                            last point is the end point (both of which lie on
                            the edges of the gameboard), and the other points
                            are corner ("turning") points on the path.
            'money': The money balance with which the player begins.
            'spawn_interval': The interval (in timesteps) for spawning animals
                              to the game.
            'animal_speed': The magnitude of the speed at which the animals move
                            along the path, in units of grid distance traversed
                            per timestep.
            'num_allowed_unfed': The number of animals allowed to finish the
                                 path unfed before the player loses.
          }
        """
        self.game_info = game_info
        self.width = game_info['width']
        self.height = game_info['height']
        self.status = 'ongoing'
        self.corners = game_info['path_corners']
        self.start = game_info['path_corners'][0]
        self.end = game_info['path_corners'][-1]
        self.money = game_info['money']
        self.formations_data = []
        self.formations = []
        #rock_coords = list(self.game_info["rocks"])
        self.unremoveable_locs = set()
        self.add_rocks(list(self.game_info["rocks"]))
        self.num_allowed_unfed = game_info['num_allowed_unfed']
        self.time = -1
        corners = self.corners
        path = self.get_path(corners)
        self.path = path
        self.keeper_selected = None #-> to know to take the next mouseclick as a location
        self.invalid_locations = set()
        self.find_invalid_locations(self.formations)
        self.awaiting_aim = None
        self.buffed = {}
        

    def get_path(self, corners):
        path = []
        for i in range(len(corners)-1):
            x = corners[i][0]
            y = corners[i][1]
            next_corner = corners[i+1]
            if x == next_corner[0]:
                if y> next_corner[1]:
                    current_path = [(x, j) for j in range(y, next_corner[1], -1)] #vertical upwards path
                else:
                    current_path = [(x, j) for j in range(y, next_corner[1])] #vertical downward path
                path += current_path
            if y == next_corner[1]: 
                if x> next_corner[0]:
                    current_path = [(j, y) for j in range(x, next_corner[0], -1)] #horizontal westward path
                else:
                    current_path = [(j, y) for j in range(x, next_corner[0])]
                path += current_path
        path.append(corners[-1])
        return path
    
    def add_rocks(self, rock_coords):
        for coord in rock_coords: #adds all rocks from game_info to formations
            texture = Constants.TEXTURES['rock']
            size = (Constants.ROCK_WIDTH, Constants.ROCK_HEIGHT)
            form = Rock(texture, coord, size, 0)
            self.formations.append(form)
            self.formations_data.append(form.dic)   
            self.unremoveable_locs.add(form.loc)
    
    
    def isvalid(self, corner, centre):
        for location in self.get_invalid_locations(): #checks non path formations
            if collide(corner, location):
                return False
        for point in self.path:
            if point == centre:
                return False
            corners = get_corners(point, (Constants.PATH_THICKNESS, Constants.PATH_THICKNESS)) #checks path
            if collide(corner, corners):
                return False
        return True



    def find_invalid_locations(self, coords):
        for form in coords: #calculates invalid_locations that stay constant, will be updates as zookeepers are placed.
            center= form.loc
            x_min = center[0] - form.size[0]//2
            x_max = center[0] + form.size[0]//2
            y_min = center[1] - form.size[1]//2 
            y_max = center[1] + form.size[1]//2 
            self.invalid_locations.add(((x_min, y_min), (x_max, y_max)))
    def get_invalid_locations(self):
        return list(self.invalid_locations)
    def add_invalid_locations(self, coord, size):
        center = coord
        x_min = center[0] - size[0]//2
        x_max = center[0] + size[0]//2
        y_min = center[1] - size[1]//2 
        y_max = center[1] + size[1]//2
        self.invalid_locations.add(((x_min, y_min), (x_max, y_max))) 

    
    def render(self):
        """Renders the game in a form that can be parsed by the UI.

        Returns a dictionary of the following form:
          { 'formations': A list of dictionaries in any order, each one
                          representing a formation. The list should contain 
                          the formations of all animals, zookeepers, rocks, 
                          and food. Each dictionary has the key/value pairs:
                             'loc': (x, y), 
                             'texture': texture, 
                             'size': (width, height)
                          where `(x, y)` is the center coordinate of the 
                          formation, `texture` is its texture, and `width` 
                          and `height` are its dimensions. Zookeeper
                          formations have an additional key, 'aim_dir',
                          which is None if the keeper has not been aimed, or a 
                          tuple `(aim_x, aim_y)` representing a unit vector 
                          pointing in the aimed direction.
            'money': The amount of money the player has available.
            'status': The current state of the game which can be 'ongoing' or 'defeat'.
            'num_allowed_remaining': The number of animals which are still
                                     allowed to exit the board before the game
                                     status is `'defeat'`.
          }
        """
        num_allowed_remaining = self.num_allowed_unfed

        ans = {'formations': self.formations_data, 'money': self.money, 'status': self.status, 'num_allowed_remaining': num_allowed_remaining}
        return ans

    def timestep(self, mouse=None):
        """Simulates the evolution of the game by one timestep.

        In this order:
            (0. Do not take any action if the player is already defeated.)
            1. Compute any changes in formation locations, then remove any
                off-board formations.
            2. Handle any food-animal collisions, and remove the fed animals
                and eaten food.
            3. Throw new food if possible.
            4. Spawn a new animal from the path's start if needed.
            5. Handle mouse input, which is the integer coordinate of a player's
               click, the string label of a particular zookeeper type, or `None`.
            6. Redeem one unit money per animal fed this timestep.
            7. Check for the losing condition to update the game status if needed.
        """
        if self.status == 'defeat':
            return
        if self.status == 'ongoing':
            self.time += 1
            removal_forms = set() #in this list we will mark formations for DEATH
            keepers = []
            animals = []
            food = []
            upgraded_keepers = []
            for i, animal in enumerate(self.formations): #HERE I MOVE ALL THE FORMATIONS. I USE A RENEWED REMOVAL LIST EACH TIMESTEP WHICH IS WHY I DO NOT MAKE NEW METHODS                                        # FOR MOVEMENT AND REMOVAL.
                if animal.type == 'animal' and animal.loc in self.buffed.keys():

                    animal.vel *= (self.buffed[animal.loc])
                    animal.vel = ceil(animal.vel)
                    
                elif animal.type == 'animal':
                  animal.vel = self.game_info['animal_speed']
                animal.move(self.path)
                if animal.type == 'animal':
                  animal.vel = self.game_info['animal_speed']
                new = animal.update()
                position = new['loc']
                if position[0]<0 or position[1] <0 or position[0] > self.width or position[1] > self.height: #off the map
                    removal_forms.add(animal)
                elif animal.type == 'animal': #puts all the animals in a list 
                    animals.append(animal)
                self.formations_data[i] = new
 
                if animal.type == 'keeper' and animal.aim_dir: #making sure keeper can see
                    keepers.append(animal) #puts all the keepers in a list
                if animal.type == 'food':
                    food.append(animal) #puts all foods in a list

            if self.time%self.game_info['spawn_interval'] == 0: #WE SPAWN AFTER MOVEMENETS ARE MADE BECAUSE NEWBORNS DONT MOVE IN THE SAME TIMESTEP
                new_animal = Animal(Constants.TEXTURES['animal'], self.start, (Constants.ANIMAL_WIDTH, Constants.ANIMAL_HEIGHT), self.game_info['animal_speed'], 0)
                self.formations.append(new_animal)
                self.formations_data.append(new_animal.dic)     
            
            
            for f in food:
                for a in animals:

                    if collide(f.get_corners(), a.get_corners()):
                        removal_forms.add(f)
                        if a.type == 'animal':
                            a.fed = True
                            removal_forms.add(a)


            for form in removal_forms:
                old = form.update()
                if form.type == 'animal' and form.fed:
                    self.money +=1
                elif form.type == 'animal' and not form.fed:
                    self.num_allowed_unfed -=1
                if form.type == 'food':
                  form.thrown_by.threshold -= 1
                  if form.thrown_by.threshold <= 0:
                      upgraded_keepers.append(form.thrown_by)
                self.formations.remove(form)
                self.formations_data.remove(old)
            for keeper in upgraded_keepers:
              keeper.upgrade_keeper(self.time-1)
              i = self.formations.index(keeper)
              self.formations_data[i] = keeper.update()

  
            for keeper in keepers:
              if keeper.keeper == 'SleepingZookeeper':
                keeper.nap -=1
                if keeper.nap == 0:
                  i = self.formations.index(keeper)
                  keeper.keeper = 'CrazyZookeeper'
                  keeper.texture = Constants.TEXTURES['CrazyZookeeper']
                  keeper.nap = Constants.CRAZY_NAP_LENGTH
                  keeper.throws = Constants.CRAZY_ENDURANCE
                  
                  self.formations_data[i] = keeper.update()
                continue      
              if (self.time-keeper.time)%keeper.interval == 1: #keeper can throw food, check if keeper can see animal

                  origin = keeper.loc
                  ray = keeper.aim_dir
                  for animal in animals:
                      lines = animal.get_borders()

                      if keeper.can_see(lines, origin, ray):

                          new_food = Food(Constants.TEXTURES['food'], keeper.loc, (Constants.FOOD_WIDTH, Constants.FOOD_HEIGHT), keeper.throw_speed, keeper.aim_dir, keeper)
                          self.formations.append(new_food)
                          self.formations_data.append(new_food.update())
                          if keeper.keeper == 'CrazyZookeeper':
                            keeper.throws -=1
                            if keeper.throws == 0:
                              keeper.keeper = 'SleepingZookeeper'
                              keeper.texture = Constants.TEXTURES['SleepingZookeeper']
                              i = self.formations.index(keeper)
                              self.formations_data[i] = keeper.update()
                          break
            


            keeper = self.keeper_selected #handling mouse input
            if keeper != None:#applies keepers or buffs
              if type(mouse) == tuple:            
                if keeper == 'Demon' or keeper == 'VHS':
                    if self.money < Constants.FORMATION_INFO[keeper]['price']:
                        raise NotEnoughMoneyError

                    coords = mouse
                    size = (Constants.FORMATION_INFO[keeper]['width'],Constants.FORMATION_INFO[keeper]['height'])
                    corners =get_corners(coords, size)

                    if self.isvalid(corners, coords) and coords not in self.unremoveable_locs:
                        new_buff = Buff(Constants.TEXTURES[keeper], coords, size, 0, Constants.FORMATION_INFO[keeper]['radius'], Constants.FORMATION_INFO[keeper]['multiplier'])
                        buffed_locations = new_buff.get_buffed_locations(self.path)
                    # if len(buffed_locations) != 0:
                        #print(mouse, self.money)
                        self.formations.append(new_buff)
                        self.formations_data.append(new_buff.update())
                        self.money -= Constants.FORMATION_INFO[keeper]['price']
                        self.add_invalid_locations(new_buff.loc, new_buff.size)
                        self.unremoveable_locs.add(new_buff.loc)
                        self.keeper_selected = None

                        
                        for local in buffed_locations:
                            if local in self.buffed:
                                self.buffed[local]*= new_buff.multiplier
                            else:
                                self.buffed[local] = new_buff.multiplier
                elif type(mouse) == tuple and self.awaiting_aim == None:
                    if self.money < Constants.FORMATION_INFO[keeper]['price']:
                        raise NotEnoughMoneyError
                    coords = mouse
                    size = (Constants.KEEPER_WIDTH, Constants.KEEPER_HEIGHT)
                    corners = get_corners(coords, size)
                    if self.isvalid(corners, coords):

                        new_keeper = Zookeeper(Constants.TEXTURES[keeper], coords, (Constants.KEEPER_WIDTH, Constants.KEEPER_HEIGHT), 0, self.time, keeper)

                        self.formations.append(new_keeper)
                        self.formations_data.append(new_keeper.update())
                        self.money -= new_keeper.price

                        self.add_invalid_locations(new_keeper.loc, new_keeper.size)
                        self.unremoveable_locs.add(new_keeper.loc)

                        self.awaiting_aim = new_keeper

                if type(mouse) == tuple and self.awaiting_aim != None:
                                      
                    selected = self.awaiting_aim
                    i = self.formations.index(selected)
                    selected.set_aim_dir(mouse)
                    if selected.aim_dir:

                        self.formations_data[i] = selected.update()
                        self.awaiting_aim = None
                        self.keeper_selected = None

            if type(mouse) == str:
                self.keeper_selected = mouse

            if self.num_allowed_unfed <0:
                self.status = 'defeat'
                return




class Formation:
    """
    texture:
    """
    def __init__(self, texture, loc, size, vel):
        self.type = None
        self.texture = texture
        self.loc = loc
        self.size = size
        self.vel = vel
        self.is_keeper = False
        self.dic = {
            'loc' : self.loc,
            'texture' : self.texture,
            'size': self.size
        }


    def update(self):
        necessary_vals = {'loc' : self.loc, 'texture' : self.texture, 'size': self.size}
        return necessary_vals
    def get_corners(self):
        center = self.loc
        x_min = center[0] - self.size[0]//2
        x_max = center[0] + self.size[0]//2
        y_min = center[1] - self.size[1]//2 
        y_max = center[1] + self.size[1]//2
        return ((x_min, y_min), (x_max, y_max))

    def get_borders(self):
        center = self.loc
        x_min = center[0] - self.size[0]//2
        x_max = center[0] + self.size[0]//2
        y_min = center[1] - self.size[1]//2 
        y_max = center[1] + self.size[1]//2
        return [((x_min, y_min),(x_max, y_min)),((x_min, y_max),(x_max, y_max)),((x_min, y_min),(x_min, y_max)),((x_max, y_min),(x_max, y_max))]

class Animal(Formation):
    """
    In addition to formation attributes, initializes:
    fed: default False
    vel: tuple representing (x_velocity, y_velocity)


    #######################################
    ANIMALS CHECK FOR FOOD:
    IF ANIMAL IS FED; FOR THAT TIMESTEP, REMOVE ANIMAL AND FOOD.

    FOOD REMOVAL MUST BE:
    IF ANIMAL FED:
        REMOVE FOOD


    IF FOOD OUTSIDE BOUNDARIES:
        REMOVE FOOD
        
    """

    def __init__(self, texture, loc, size, vel, curr):
        
        self.fed = False
        self.curr = curr #maintain its position on the path
        super().__init__(Constants.TEXTURES['animal'], loc, (Constants.ANIMAL_WIDTH, Constants.ANIMAL_HEIGHT), vel)
        self.type = 'animal'
    
    def move(self, path):
        self.curr = self.curr + self.vel
        try:
            self.loc = path[self.curr]
        except: #end of path reached
            x = path[-1][0]+1 
            y = path[-1][1]+1
            self.loc = (x, y)
    
class Rock(Formation):
    def __init__(self, texture, loc, size, vel, ):
        super().__init__(Constants.TEXTURES['rock'], loc, (Constants.ROCK_WIDTH, Constants.ROCK_HEIGHT), vel)
        self.type = 'rock'
    
    
    def move(self, path):
        pass

class Zookeeper(Formation): #record time of creation for food throwing interval
    def __init__(self, texture, loc, size, vel, time, keeper_type):
        
        self.interval = Constants.FORMATION_INFO[keeper_type]['interval']
        self.price = Constants.FORMATION_INFO[keeper_type]['price']
        self.throw_speed = Constants.FORMATION_INFO[keeper_type]['throw_speed_mag']
        self.time = time
        self.aim_dir = None

        super().__init__(texture, loc, size, vel, )
        self.type = 'keeper'
        self.keeper = keeper_type
        if self.keeper == 'TraineeZookeeper':
          self.threshold = Constants.TRAINEE_THRESHOLD
          self.upgrade = 'SpeedyZookeeper'
        else:
          self.threshold = float('inf')
        if self.keeper == 'CrazyZookeeper':
          self.throws = Constants.CRAZY_ENDURANCE
        else:
          self.throws = float('inf')
        self.nap = Constants.CRAZY_NAP_LENGTH
        # if self.keeper == 'SleepingZookeeper':
        #   self.nap = Constants.CRAZY_NAP_LENGTH
        # else:
        #   self.nap = float('inf')


    def can_see(self, line_segments, origin, ray):
        """
        Line segments: list of 4 line segments: [((x1, y1),(x2, y2)),((x1, y1),(x3, y3)),((x2, y2),(x4, y4)),((x3, y3),(x4, y4))]
        Origin: point from which ray originates
        Ray: vector from origin

        """
        for segment in line_segments:
            v1 = (segment[0][0] - origin[0], segment[0][1] - origin[1])
            v2 =(segment[1][0] - origin[0], segment[1][1] - origin[1])
            angle_1 = angle(v1, v2)
            angle_1ray =  angle(v1, ray)
            angle_ray2 = angle(ray, v2)
            rhs = angle_1ray + angle_ray2
            if abs(rhs - angle_1) < 0.001:
                return True
        return False
    def upgrade_keeper(self, time):

      keep_aim = self.aim_dir

      self.__init__(Constants.TEXTURES[self.upgrade], self.loc, (Constants.KEEPER_WIDTH, Constants.KEEPER_HEIGHT), 0, time, self.upgrade) 
      self.aim_dir = keep_aim

    def move(self, path):
        pass

    def set_aim_dir(self, coord):
        if coord == self.loc:
            return
        v = (coord[0] - self.loc[0], (coord[1] - self.loc[1]))


        unit = (v[0]/mag(v),v[1]/mag(v))

        self.aim_dir = unit

    def update(self):
        necessary_vals = {'loc' : self.loc, 'texture' : self.texture, 'size': self.size, 'aim_dir': self.aim_dir}
        return necessary_vals

class Buff(Formation):
  def __init__(self, texture, loc, size, vel, radius, multiplier):
      self.texture = texture
      self.loc = loc
      self.size = size
      self.vel = vel
      self.radius = radius
      self.multiplier = multiplier
      self.type = 'buff'

  def get_buffed_locations(self, path):
      locations = {(x, y) for (x, y) in path if ((x - self.loc[0])**2 + (y - self.loc[1])**2 < self.radius**2)} #checks the path coords
      return locations
  def move(self, path):
      pass

class Demon(Buff):
  def __init__(self, texture, loc, size, vel, radius, multiplier):
      super().__init__(texture, loc, size, vel, radius, multiplier)
  
  def move(self, path):
      pass
class CheeryZookeeper(Zookeeper):
    def __init__(self, texture, loc, size, vel, ):
        super().__init__(Constants.TEXTURES['CheeryZookeeper'], loc, (Constants.KEEPER_WIDTH, Constants.KEEPER_HEIGHT), vel, )

class SpeedyZookeeper(Zookeeper):
    def __init__(self, texture, loc,size, vel, ):
        super().__init__(Constants.TEXTURES['SpeedyZookeeper'], loc, (Constants.KEEPER_WIDTH, Constants.KEEPER_HEIGHT), vel, )

class ThriftyZookeeper(Zookeeper):
    def __init__(self, texture, loc,size, vel, ):
        super().__init__(Constants.TEXTURES['ThiftyZookeeper'], loc, (Constants.KEEPER_WIDTH, Constants.KEEPER_HEIGHT), vel, )

class Food(Formation):
    def __init__(self, texture, loc, size, vel, trajectory, keeper ):   
        self.trajectory = trajectory
        self.thrown_by = keeper
        super().__init__(Constants.TEXTURES['food'], loc, (Constants.FOOD_WIDTH, Constants.FOOD_HEIGHT), vel)
        self.type = 'food'
    def move(self, _):
        x = self.loc[0] + (self.trajectory[0]*self.vel)
        y = self.loc[1] + (self.trajectory[1]*self.vel)
        self.loc = (x, y)



if __name__ == '__main__':
    pass