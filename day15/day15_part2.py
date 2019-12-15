#  --- Day 15: Oxygen System ---
#  Out here in deep space, many things can go wrong. Fortunately, many of those things have indicator lights. Unfortunately, one of those lights is lit: the oxygen system for part of the ship has failed!
#  
#  According to the readouts, the oxygen system must have failed days ago after a rupture in oxygen tank two; that section of the ship was automatically sealed once oxygen levels went dangerously low. A single remotely-operated repair droid is your only option for fixing the oxygen system.
#  
#  The Elves' care package included an Intcode program (your puzzle input) that you can use to remotely control the repair droid. By running that program, you can direct the repair droid to the oxygen system and fix the problem.
#  
#  The remote control program executes the following steps in a loop forever:
#  
#  Accept a movement command via an input instruction.
#  Send the movement command to the repair droid.
#  Wait for the repair droid to finish the movement operation.
#  Report on the status of the repair droid via an output instruction.
#  Only four movement commands are understood: north (1), south (2), west (3), and east (4). 
#  Any other command is invalid. The movements differ in direction, but not in distance: in a 
#  long enough east-west hallway, a series of commands like 4,4,4,4,3,3,3,3 would leave the repair 
#  droid back where it started.
#  
#  The repair droid can reply with any of the following status codes:
#  
#  0: The repair droid hit a wall. Its position has not changed.
#  1: The repair droid has moved one step in the requested direction.
#  2: The repair droid has moved one step in the requested direction; its new position is the location 
#  of the oxygen system.
#  You don't know anything about the area around the repair droid, but you can figure it out by watching 
#  the status codes.
#  
#  For example, we can draw the area using D for the droid, # for walls, . for locations the droid can 
#  traverse, and empty space for unexplored locations. Then, the initial state looks like this:
#  
#        
#        
#     D  
#        
#        
#  To make the droid go north, send it 1. If it replies with 0, you know that location is a 
#  wall and that the droid didn't move:
#  
#        
#     #  
#     D  
#        
#        
#  To move east, send 4; a reply of 1 means the movement was successful:
#  
#        
#     #  
#     .D 
#        
#        
#  Then, perhaps attempts to move north (1), south (2), and east (4) are all met with replies of 0:
#  
#        
#     ## 
#     .D#
#      # 
#        
#  Now, you know the repair droid is in a dead end. Backtrack with 3 (which you already 
#  know will get a reply of 1 because you already know that location is open):
#  
#        
#     ## 
#     D.#
#      # 
#        
#  Then, perhaps west (3) gets a reply of 0, south (2) gets a reply of 1, south again (2) gets a reply 
#  of 0, and then west (3) gets a reply of 2:
#  
#        
#     ## 
#    #..#
#    D.# 
#     #  
#  Now, because of the reply of 2, you know you've found the oxygen system! In this example, 
#  it was only 2 moves away from the repair droid's starting position.
#  
#  What is the fewest number of movement commands required to move the repair droid from its 
#  starting position to the location of the oxygen system?
#  
#  To begin, get your puzzle input.
#
#  Your puzzle answer was 272.
#  
#  The first half of this puzzle is complete! It provides one gold star: *
#  
#  --- Part Two ---
#  You quickly repair the oxygen system; oxygen gradually fills the area.
#  
#  Oxygen starts in the location containing the repaired oxygen system. It takes one minute for oxygen 
#  to spread to all open locations that are adjacent to a location that already contains oxygen. 
#  Diagonal locations are not adjacent.
#  
#  In the example above, suppose you've used the droid to explore the area fully and have the following 
#  map (where locations that currently contain oxygen are marked O):
#  
#   ##   
#  #..## 
#  #.#..#
#  #.O.# 
#   ###  
#  Initially, the only location which contains oxygen is the location of the repaired oxygen system. 
#  However, after one minute, the oxygen spreads to all open (.) locations that are adjacent to a location 
#  containing oxygen:
#  
#   ##   
#  #..## 
#  #.#..#
#  #OOO# 
#   ###  
#  After a total of two minutes, the map looks like this:
#  
#   ##   
#  #..## 
#  #O#O.#
#  #OOO# 
#   ###  
#  After a total of three minutes:
#  
#   ##   
#  #O.## 
#  #O#OO#
#  #OOO# 
#   ###  
#  And finally, the whole region is full of oxygen after a total of four minutes:
#  
#   ##   
#  #OO## 
#  #O#OO#
#  #OOO# 
#   ###  
#  So, in this example, all locations contain oxygen after 4 minutes.
#  
#  Use the repair droid to get a complete map of the area. How many minutes will it take to fill with 
#  oxygen?
#  
#  Although it hasn't changed, you can still get your puzzle input.




# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



TILE_SPACE = 1001
TILE_WALL = 1002
TILE_TARGET = 1003

class LocationInfo:
    def __init__(self, tile_type, x, y, distance):
        self.tile_type = tile_type 
        self.x = x 
        self.y = y 
        self.distance = distance 
        self.oxygen = False
        self.filling = False
        if TILE_TARGET == tile_type:
            self.oxygen = True
    
    def __repr__(self):
        s = f"<LocationInfo {self.x},{self.y} = {self.tile_type} (distance = {self.distance})>"
        return s

    def set_oxygen(self):
        self.oxygen = True
        self.filling = False

    def has_oxygen(self):
        return self.oxygen

    def set_filling(self):
        self.filling = True 

    def is_filling(self):
        return self.filling

    def is_empty(self):
        return TILE_SPACE == self.tile_type

    def get_map_character(self):
        result = '?'
        if TILE_SPACE == self.tile_type:
            result = '.'
            if self.oxygen:
                result = 'O'
        elif TILE_WALL == self.tile_type:
            result = '#'
        elif TILE_TARGET == self.tile_type:
            result = '*'
        return result


MOVE_FAILED = 0
MOVE_WORKED = 1
MOVE_TARGET = 2

MOVE_NORTH = 1
MOVE_SOUTH = 2
MOVE_EAST = 4
MOVE_WEST = 3

class MazeSolver:
    def __init__(self):
        self.current_x = 0
        self.current_y = 0
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0 
        self.maze = dict()
        self.add_tile(0, 0, TILE_SPACE, 0)
        self.history = []
        self.backtracking = False

    def add_tile(self, x, y, tile_type, distance_from_start):
        #print(f"Adding a tile at {x},{y} distance={distance_from_start}")
        if TILE_TARGET == tile_type:
            print(f"****************** Target at {x},{y} distance={distance_from_start}")
            #self.print_map(False)
            #sleep(60)
        self.maze[(x, y)] = LocationInfo(tile_type, x, y, distance_from_start)
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x 
        if y < self.min_y:
            self.min_y = y 
        if y > self.max_y:
            self.max_y = y 

    def print_map(self, show_current_location=True):
        """
        Draw the current map as we know it 
        """
        print("Map:")
        for y in range(self.min_y, self.max_y + 1):
            s = ''
            for x in range(self.min_x, self.max_x + 1):
                c = ' '
                if show_current_location and self.current_x == x and self.current_y == y:
                    c = 'R'
                elif (x, y) in self.maze:
                    c = self.maze[(x, y)].get_map_character()
                s += c
            print(s)
        print("\n")
        #print(f"History: {self.history}")
        #print("\n")


    def has_oxygen(self, x, y):
        result = False
        if (x,y) in self.maze:
            result = self.maze[(x,y)].has_oxygen()
        return result

    def has_nearby_oxygen(self, x, y):
        """
        Returns True if one of the orthagonal squares has oxygen 
        """
        return self.has_oxygen(x - 1, y) or self.has_oxygen(x + 1, y) or self.has_oxygen(x, y - 1) or self.has_oxygen(x, y + 1)

    def oxygen_flood(self):
        """
        Flood the maze with oxygen moving at one square per minute 
        """
        # the oxygen square is already set so we can just crack on..
        minute = 0
        no_oxygen_count = 999
        while 0 != no_oxygen_count and minute < 30000:
            no_oxygen_count = 0
            for x in range(self.min_x, self.max_x + 1):
                for y in range(self.min_y, self.max_y + 1):
                    # is this an empty square 
                    if (x, y) in self.maze and self.maze[(x, y)].is_empty():
                        # ok, do we have oxygen ?
                        if not self.maze[(x,y)].has_oxygen():
                            # but should it fill this time ?
                            if self.has_nearby_oxygen(x, y):
                                self.maze[(x,y)].set_filling()
                            else:
                                no_oxygen_count += 1
            # ok - so we're done, now fill the filling spaces 
            for key in self.maze.keys():
                if self.maze[key].is_filling():
                    self.maze[key].set_oxygen()

            # and print the thing
            #clear() 
            minute += 1
            print(f"Minute {minute}, {no_oxygen_count} spaces remain to be filled")
            self.print_map(False)
            #sleep(0.1)
                        

    def receive_output(self, output_value):
        """
        Intcode computer interface - receives the output value
        in this case it is a three part process, x, y, tile  
        """
        #clear()
        # we have the move result 
        distance = self.maze[(self.current_x, self.current_y)].distance
        if MOVE_FAILED == output_value:
            self.add_tile(self.target_x, self.target_y, TILE_WALL, distance + 1)
            #print(f"OW! a wall at {self.target_x}, {self.target_y}")
            # we don't update the current location here
        elif MOVE_WORKED == output_value or MOVE_TARGET == output_value:
            if not self.backtracking:
                tile = TILE_SPACE
                if MOVE_TARGET == output_value:
                    tile = TILE_TARGET
                self.add_tile(self.target_x, self.target_y, tile, distance + 1)
                self.history.append((self.current_x, self.current_y))
            self.current_x = self.target_x
            self.current_y = self.target_y 
            #print(f"YAY, moved to {self.target_x}, {self.target_y}")
            if MOVE_TARGET == output_value:                
                print(f"Found the thing at {self.target_x}, {self.target_y}")
        else:
            raise ValueError(f"received a move result of {output_value} ?!?!?")

        #self.print_map()
        #sleep(0.1)

    def provide_input(self):
        """
        Provide the relevant movement value based on current location
        """
        result = -1
        self.backtracking = False
        # if we have something to explore then let's explore 
        x = self.current_x 
        y = self.current_y 
        # have we explored North ?
        if (x, y - 1) not in self.maze:
            # we haven't 
            self.target_x = x
            self.target_y = y - 1
            result = MOVE_NORTH
            #print("going NORTH")
        elif (x + 1, y) not in self.maze:
            self.target_x = x + 1
            self.target_y = y 
            result = MOVE_EAST
            #print("going EAST")
        elif (x, y + 1) not in self.maze:
            self.target_x = x
            self.target_y = y + 1 
            result = MOVE_SOUTH
            #print("going SOUTH")
        elif (x - 1, y) not in self.maze:
            self.target_x = x - 1
            self.target_y = y 
            result = MOVE_WEST
            #print("go WEST!")
        # ok - everything is explored, head back where we came from 
        else:
            #print("Explored everything boss, going back")
            if 0 == len(self.history):
                print("Map is discovered, oxygen flood time.")
                self.print_map()
                self.print_map(False)
                self.oxygen_flood()
                exit(1)
            else:
                self.backtracking = True 
                target_xy = self.history[-1]
                self.history = self.history[:-1]
                self.target_x = target_xy[0]
                self.target_y = target_xy[1]
                if y > self.target_y:
                    # we need to move North 
                    result = MOVE_NORTH
                    #print("going back North")
                elif y < self.target_y:
                    # or south 
                    result = MOVE_SOUTH
                    #print("going back South")
                elif x > self.target_x:
                    result = MOVE_WEST
                    #print("Go WEST!!! (back west that is)")
                else:
                    result = MOVE_EAST
                    #print("Going home east")

        #sleep(2)
        return result 

    

import sys 
sys.path.append("c:\\development\\advent-of-code-2019")
from compute_engine.engine import ComputeEngine


puzzle_program = '3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1002,1034,1,1039,101,0,1036,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,1002,1034,1,1039,101,0,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1105,1,124,1001,1034,-1,1039,1008,1036,0,1041,101,0,1035,1040,101,0,1038,1043,1002,1037,1,1042,1105,1,124,1001,1034,1,1039,1008,1036,0,1041,1002,1035,1,1040,102,1,1038,1043,1002,1037,1,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,39,1032,1006,1032,165,1008,1040,39,1032,1006,1032,165,1101,0,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,74,1044,1106,0,224,1101,0,0,1044,1106,0,224,1006,1044,247,102,1,1039,1034,102,1,1040,1035,1002,1041,1,1036,1002,1043,1,1038,1002,1042,1,1037,4,1044,1105,1,0,15,82,44,17,88,23,99,42,83,68,98,44,75,66,15,14,89,20,34,89,18,1,84,70,84,69,55,89,65,10,76,63,83,20,80,60,48,47,98,65,82,84,68,89,52,76,63,86,61,75,4,52,82,79,24,28,93,94,95,40,66,76,81,50,31,94,81,54,19,91,92,61,18,28,79,77,43,69,19,5,87,35,14,23,94,10,76,32,73,90,20,86,67,90,80,8,86,25,89,89,26,48,37,81,49,25,87,92,17,46,84,96,95,60,79,52,19,13,93,30,93,99,17,13,89,96,36,93,81,89,18,2,97,42,45,63,86,20,26,76,97,29,75,56,7,97,93,2,78,9,79,8,57,84,38,80,53,98,89,34,71,85,17,96,50,31,93,64,7,81,72,85,32,83,31,99,69,90,88,33,88,81,41,80,46,47,93,75,34,95,8,98,24,7,76,77,17,23,95,72,82,98,24,91,95,50,38,92,91,32,95,40,77,80,84,82,7,90,23,13,92,40,82,37,80,56,24,79,99,64,90,55,58,46,33,4,88,92,7,84,19,45,16,75,94,40,93,21,87,94,79,39,83,52,92,14,21,77,82,5,84,85,48,75,19,26,91,28,99,87,81,86,24,53,98,52,25,2,75,39,82,24,51,77,47,92,53,94,27,34,85,22,25,36,92,79,29,2,10,19,95,13,96,82,56,99,3,91,62,99,43,49,7,91,96,77,89,7,99,86,24,92,57,24,49,3,96,77,35,75,11,86,21,1,82,67,84,90,75,96,9,83,1,47,78,7,98,30,11,88,52,78,58,98,47,90,46,78,14,77,88,3,97,87,70,75,24,98,5,80,87,93,95,22,37,59,85,23,41,89,91,9,7,90,61,3,95,96,92,25,57,47,38,88,14,15,84,31,79,20,79,77,22,33,90,70,89,78,51,24,93,81,21,79,82,17,75,88,78,26,87,24,38,96,50,81,6,46,93,39,91,92,81,39,91,5,79,58,9,87,50,83,63,87,2,29,92,37,81,55,59,99,91,35,9,96,18,82,66,4,89,44,87,92,6,79,88,9,9,63,88,71,77,91,35,29,87,87,51,20,94,19,57,93,72,89,4,77,10,87,20,67,80,79,71,1,75,28,87,88,87,55,37,80,85,5,55,5,97,12,62,88,82,27,6,99,93,42,91,16,75,80,6,20,96,6,84,6,46,84,23,92,93,32,90,79,3,54,7,97,92,92,33,79,9,5,10,90,76,19,76,1,85,83,58,2,91,83,77,59,63,89,26,97,67,96,52,88,62,65,23,91,94,51,31,80,24,5,72,40,81,9,85,79,12,98,44,45,81,25,30,60,5,76,92,62,18,32,78,25,16,76,97,18,96,39,96,60,78,78,47,99,48,82,98,57,96,98,73,89,18,12,91,8,66,85,57,94,22,76,88,98,39,58,96,91,61,98,89,7,77,91,13,96,20,86,2,88,91,27,75,32,29,79,51,81,4,86,10,37,79,84,67,49,75,20,94,91,23,33,92,38,91,37,76,79,55,91,43,80,25,98,77,91,88,44,15,97,45,3,86,73,87,30,91,62,80,80,16,85,54,88,54,75,88,65,18,85,22,90,79,36,10,77,86,65,30,38,85,3,90,44,48,75,81,80,32,59,90,91,41,95,72,79,11,66,26,96,20,4,68,88,23,95,31,98,12,98,56,94,95,80,68,78,39,79,93,85,55,96,4,77,14,80,46,95,84,84,6,93,35,95,46,85,92,81,69,85,92,87,0,0,21,21,1,10,1,0,0,0,0,0,0'

# build a solver 
solver = MazeSolver()

# build the computer and attach the screen
c = ComputeEngine(puzzle_program)
# attach the controls
c.attach_output_device(solver)
c.attach_input_device(solver)
c.run(False, False)



