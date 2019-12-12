#  --- Day 11: Space Police ---
#  On the way to Jupiter, you're pulled over by the Space Police.
#  
#  "Attention, unmarked spacecraft! You are in violation of Space Law! All spacecraft must have a clearly visible registration identifier! You have 24 hours to comply or be sent to Space Jail!"
#  
#  Not wanting to be sent to Space Jail, you radio back to the Elves on Earth for help. Although it takes almost three hours for their reply signal to reach you, they send instructions for how to power up the emergency hull painting robot and even provide a small Intcode program (your puzzle input) that will cause it to paint your ship appropriately.
#  
#  There's just one problem: you don't have an emergency hull painting robot.
#  
#  You'll need to build a new emergency hull painting robot. The robot needs to be able to move around on the grid of square panels on the side of your ship, detect the color of its current panel, and paint its current panel black or white. (All of the panels are currently black.)
#  
#  The Intcode program will serve as the brain of the robot. The program uses input instructions to access the robot's camera: provide 0 if the robot is over a black panel or 1 if the robot is over a white panel. Then, the program will output two values:
#  
#  First, it will output a value indicating the color to paint the panel the robot is over: 0 means to paint the panel black, and 1 means to paint the panel white.
#  Second, it will output a value indicating the direction the robot should turn: 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
#  After the robot turns, it should always move forward exactly one panel. The robot starts facing up.
#  
#  The robot will continue running for a while like this and halt when it is finished drawing. Do not restart the Intcode computer inside the robot during this process.
#  
#  For example, suppose the robot is about to start running. Drawing black panels as ., white panels as #, and the robot pointing the direction it is facing (< ^ > v), the initial state and region near the robot looks like this:
#  
#  .....
#  .....
#  ..^..
#  .....
#  .....
#  The panel under the robot (not visible here because a ^ is shown instead) is also black, and so any input instructions at this point should be provided 0. Suppose the robot eventually outputs 1 (paint white) and then 0 (turn left). After taking these actions and moving forward one panel, the region now looks like this:
#  
#  .....
#  .....
#  .<#..
#  .....
#  .....
#  Input instructions should still be provided 0. Next, the robot might output 0 (paint black) and then 0 (turn left):
#  
#  .....
#  .....
#  ..#..
#  .v...
#  .....
#  After more outputs (1,0, 1,0):
#  
#  .....
#  .....
#  ..^..
#  .##..
#  .....
#  The robot is now back where it started, but because it is now on a white panel, input instructions should be provided 1. After several more outputs (0,1, 1,0, 1,0), the area looks like this:
#  
#  .....
#  ..<#.
#  ...#.
#  .##..
#  .....
#  Before you deploy the robot, you should probably have an estimate of the area it will cover: specifically, you need to know the number of panels it paints at least once, regardless of color. In the example above, the robot painted 6 panels at least once. (It painted its starting panel twice, but that panel is still only counted once; it also never painted the panel it ended on.)
#  
#  Build a new emergency hull painting robot and run the Intcode program on it. How many panels does it paint at least once?
#  
#  To begin, get your puzzle input.
#  
# Your puzzle answer was 1883.
# 
# The first half of this puzzle is complete! It provides one gold star: *
# 
# --- Part Two ---
# You're not sure what it's trying to paint, but it's definitely not a registration identifier. 
# The Space Police are getting impatient.
# 
# Checking your external ship cameras again, you notice a white panel marked "emergency hull painting 
# robot starting panel". The rest of the panels are still black, but it looks like the robot was 
# expecting to start on a white panel, not a black one.
# 
# Based on the Space Law Space Brochure that the Space Police attached to one of your windows, 
# a valid registration identifier is always eight capital letters. After starting the robot on 
# a single white panel instead, what registration identifier does it paint on your hull?
#

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

TURN_LEFT = 0
TURN_RIGHT = 1

BLACK = 0
WHITE = 1

PAINTING = 1001
MOVING = 1002

# find out about constants, and static class member functions 

def storage_key_for(x, y):
    return (x, y)

class HullPaintingModule:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.painted_spots = {}
        self.facing = UP
        self.mode = PAINTING 

    def __repr__(self):
        return f"<HullPainter(x={self.x}, y={self.y}, facing={self.facing}, mode={self.mode}, painted={len(self.painted_spots.keys())})>"

    def show_canvas(self):
        """ print out the painted grid """
        # find the minimum and maximum x and y values
        min_x = None 
        min_y = None
        max_x = None 
        max_y = None  
        for x,y in self.painted_spots.keys():
            if min_x is None or x < min_x:
                min_x = x 
            if max_x is None or x > max_x:
                max_x = x
            if min_y is None or y < min_y:
                min_y = y 
            if max_y is None or y > max_y:
                max_y = y 

        print(f"canvas is ({min_x},{min_y})-({max_x}, {max_y})")

        for this_line in range(min_y, max_y + 1):
            s = ''
            for this_x in range(min_x, max_x + 1):
                key = storage_key_for(this_x, this_line)
                colour = BLACK 
                if key in self.painted_spots:
                    colour = self.painted_spots[key]
                if WHITE == colour:
                    s += '#'
                else:
                    s += ' '
            print(s)

    def receive_output(self, output_value):
        """
        Intcode computer interface - receives the output value
        in this case it is a two part process, the first output indicates a colour to paint 
        the second output value indicates a rotate and then move 
        """
        print("Got some output {output_value}")
        if PAINTING == self.mode:
            # paint this square, move next 
            self.paint(output_value)
            self.mode = MOVING
        elif MOVING == self.mode:
            self.turn_and_move(output_value)
            self.mode = PAINTING
        else:
            print(f"You have made a programming mistake Williams.. mode is somehow {self.mode}")
            raise ValueError(f"mode value is impossible - {self.mode}") 

    def paint(self, colour):
        """
        Paint the current location the colour provided
        """
        key = storage_key_for(self.x, self.y)
        self.painted_spots[key] = colour 


    def turn(self, turn_value, turn_count = 1):
        """
        Rotate the facing value in the specified direction x times 
        """
        if TURN_LEFT == turn_value:
            self.facing -= turn_count
            while self.facing < 0:
                self.facing += 4
        elif TURN_RIGHT == turn_value:
            self.facing += turn_count
            self.facing %= 4 
        else:
            raise ValueError(f"Invalid turn value of {turn_value}")

    def move(self, step_count):
        """
        Move the specified number of spaces forward 
        """
        if UP == self.facing:
            self.y -= step_count
        elif DOWN == self.facing:
            self.y += step_count
        elif RIGHT == self.facing:
            self.x += step_count
        elif LEFT == self.facing:
            self.x -= step_count
        else:
            raise ValueError(f"Invalid facing value when it was time to move - {self.facing}")

    def turn_and_move(self, turn_value):
        """
        Turn either left or right and then move one space forward
        """
        self.turn(turn_value)
        self.move(1)


    def provide_input(self):
        """
        Intcode computer interface - provides an input value to the computer
        in this case, the colour of the current location
        """
        result = BLACK 
        key = storage_key_for(self.x, self.y)
        if key in self.painted_spots:
            result = self.painted_spots[key]
        return result 
        

# quick object test to see how to implement the next thing 
def test_objects():
    my_obj = HullPaintingModule()
    second_reference = my_obj
    print(f"myobj is {my_obj}, second_reference is {second_reference}")

    test_value = my_obj.provide_input()
    print(f"test_value is {test_value}")

    # let's paint a thing 
    second_reference.receive_output(1)
    print(f"myobj is {my_obj}, second_reference is {second_reference}")

# ok - everything looks like it works - time to plug this into the Intcode and see what happens 

import sys 
sys.path.append("c:\\development\\advent-of-code-2019")
from compute_engine.engine import ComputeEngine

program_code = '3,8,1005,8,301,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,28,1006,0,98,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,54,2,1001,6,10,1,108,1,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,84,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,105,1006,0,94,2,7,20,10,2,5,7,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,139,1006,0,58,2,1003,16,10,1,6,10,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,172,2,107,12,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,197,1006,0,34,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,223,1006,0,62,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,248,1,7,7,10,1006,0,64,2,1008,5,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,280,101,1,9,9,1007,9,997,10,1005,10,15,99,109,623,104,0,104,1,21102,1,387508351636,1,21101,318,0,0,1106,0,422,21102,1,838480007948,1,21101,0,329,0,1106,0,422,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,235190525123,1,21101,0,376,0,1105,1,422,21101,0,106505084123,1,21101,0,387,0,1106,0,422,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,838324605292,1,21102,1,410,0,1105,1,422,21102,709496668940,1,1,21102,421,1,0,1105,1,422,99,109,2,22101,0,-1,1,21102,1,40,2,21101,0,453,3,21102,443,1,0,1106,0,486,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,448,449,464,4,0,1001,448,1,448,108,4,448,10,1006,10,480,1102,1,0,448,109,-2,2106,0,0,0,109,4,2101,0,-1,485,1207,-3,0,10,1006,10,503,21102,0,1,-3,22102,1,-3,1,21201,-2,0,2,21101,1,0,3,21102,1,522,0,1106,0,527,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,550,2207,-4,-2,10,1006,10,550,21202,-4,1,-4,1106,0,618,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,569,1,0,1106,0,527,21202,1,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,588,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,610,22101,0,-1,1,21101,0,610,0,106,0,485,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0'

painter = HullPaintingModule()
# start on a white square
painter.paint(WHITE)

c = ComputeEngine(program_code)
c.attach_input_device(painter)
c.attach_output_device(painter)
c.run(False)
#c.dump_memory()

print(f"After painting the ship : {painter}")
painter.show_canvas()


