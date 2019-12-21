#  --- Day 19: Tractor Beam ---
#  Unsure of the state of Santa's ship, you borrowed the tractor beam technology from Triton. 
#  Time to test it out.
#  
#  When you're safely away from anything else, you activate the tractor beam, but nothing happens. 
#  It's hard to tell whether it's working if there's nothing to use it on. Fortunately, your ship's 
#  drone system can be configured to deploy a drone to specific coordinates and then check whether it's 
#  being pulled. There's even an Intcode program (your puzzle input) that gives you access to the drone 
#  system.
#  
#  The program uses two input instructions to request the X and Y position to which the drone should be 
#  deployed. Negative numbers are invalid and will confuse the drone; all numbers should be zero or positive.
#  
#  Then, the program will output whether the drone is stationary (0) or being pulled by something (1). 
#  For example, the coordinate X=0, Y=0 is directly in front of the tractor beam emitter, so the drone control 
#  program will always report 1 at that location.
#  
#  To better understand the tractor beam, it is important to get a good picture of the beam itself. 
#  For example, suppose you scan the 10x10 grid of points closest to the emitter:
#  
#         X
#    0->      9
#   0#.........
#   |.#........
#   v..##......
#    ...###....
#    ....###...
#  Y .....####.
#    ......####
#    ......####
#    .......###
#   9........##
#  In this example, the number of points affected by the tractor beam in the 10x10 area closest to the 
#  emitter is 27.
#  
#  However, you'll need to scan a larger area to understand the shape of the beam. How many points are 
#  affected by the tractor beam in the 50x50 area closest to the emitter? 
#  (For each of X and Y, this will be 0 through 49.)
#  
#  To begin, get your puzzle input.
#  
#  



import sys 
sys.path.append("c:\\development\\advent-of-code-2019")
from compute_engine.engine import ComputeEngine

puzzle_program = '109,424,203,1,21101,0,11,0,1105,1,282,21101,18,0,0,1105,1,259,1202,1,1,221,203,1,21102,1,31,0,1106,0,282,21102,38,1,0,1106,0,259,21002,23,1,2,22102,1,1,3,21102,1,1,1,21102,1,57,0,1105,1,303,2102,1,1,222,20101,0,221,3,21001,221,0,2,21102,259,1,1,21102,1,80,0,1106,0,225,21102,62,1,2,21101,91,0,0,1105,1,303,2101,0,1,223,21001,222,0,4,21101,0,259,3,21101,0,225,2,21101,0,225,1,21101,0,118,0,1105,1,225,20102,1,222,3,21101,94,0,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1105,1,259,1202,1,1,223,20101,0,221,4,21001,222,0,3,21102,17,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,105,1,109,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21101,214,0,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22102,1,-3,1,22101,0,-2,2,21201,-1,0,3,21102,1,250,0,1106,0,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21101,343,0,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22102,1,-4,1,21102,384,1,0,1105,1,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2105,1,0'

# build a solver 
field = dict()

total = 0
for y in range(50):
    s = ''
    for x in range(50):
        input = [x, y]
        c = ComputeEngine(puzzle_program)
        c.add_data(input)
        c.run(False, False)
        #print(f"Produced: {c.get_output()}")
        result = c.get_output(0)
        field[(x,y)] = result 
        s += str(result)
        total += result 
    print(s)

print(f"Total:{total}")

