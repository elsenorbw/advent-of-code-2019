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
#  Your puzzle answer was 223.
#  
#  The first half of this puzzle is complete! It provides one gold star: *
#  
#  --- Part Two ---
#  You aren't sure how large Santa's ship is. You aren't even sure if you'll need to use this thing 
#  on Santa's ship, but it doesn't hurt to be prepared. You figure Santa's ship might fit in a 100x100 
#  square.
#  
#  The beam gets wider as it travels away from the emitter; you'll need to be a minimum distance away to 
#  fit a square of that size into the beam fully. (Don't rotate the square; it should be aligned to the 
#  same axes as the drone grid.)
#  
#  For example, suppose you have the following tractor beam readings:
#  
#  #.......................................
#  .#......................................
#  ..##....................................
#  ...###..................................
#  ....###.................................
#  .....####...............................
#  ......#####.............................
#  ......######............................
#  .......#######..........................
#  ........########........................
#  .........#########......................
#  ..........#########.....................
#  ...........##########...................
#  ...........############.................
#  ............############................
#  .............#############..............
#  ..............##############............
#  ...............###############..........
#  ................###############.........
#  ................#################.......
#  .................########OOOOOOOOOO.....
#  ..................#######OOOOOOOOOO#....
#  ...................######OOOOOOOOOO###..
#  ....................#####OOOOOOOOOO#####
#  .....................####OOOOOOOOOO#####
#  .....................####OOOOOOOOOO#####
#  ......................###OOOOOOOOOO#####
#  .......................##OOOOOOOOOO#####
#  ........................#OOOOOOOOOO#####
#  .........................OOOOOOOOOO#####
#  ..........................##############
#  ..........................##############
#  ...........................#############
#  ............................############
#  .............................###########
#  In this example, the 10x10 square closest to the emitter that fits entirely within the tractor beam has 
#  been marked O. Within it, the point closest to the emitter (the only highlighted O) is at X=25, Y=20.
#  
#  Find the 100x100 square closest to the emitter that fits entirely within the tractor beam; within that 
#  square, find the point closest to the emitter. What value do you get if you take that point's X coordinate, 
#  multiply it by 10000, then add the point's Y coordinate? (In the example above, this would be 250020.)
#




import sys 
sys.path.append("c:\\development\\advent-of-code-2019")
from compute_engine.engine import ComputeEngine

puzzle_program = '109,424,203,1,21101,0,11,0,1105,1,282,21101,18,0,0,1105,1,259,1202,1,1,221,203,1,21102,1,31,0,1106,0,282,21102,38,1,0,1106,0,259,21002,23,1,2,22102,1,1,3,21102,1,1,1,21102,1,57,0,1105,1,303,2102,1,1,222,20101,0,221,3,21001,221,0,2,21102,259,1,1,21102,1,80,0,1106,0,225,21102,62,1,2,21101,91,0,0,1105,1,303,2101,0,1,223,21001,222,0,4,21101,0,259,3,21101,0,225,2,21101,0,225,1,21101,0,118,0,1105,1,225,20102,1,222,3,21101,94,0,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1105,1,259,1202,1,1,223,20101,0,221,4,21001,222,0,3,21102,17,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,105,1,109,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21101,214,0,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22102,1,-3,1,22101,0,-2,2,21201,-1,0,3,21102,1,250,0,1106,0,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21101,343,0,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22102,1,-4,1,21102,384,1,0,1105,1,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2105,1,0'

# build a solver 
widths = dict()

total = 0
for y in range(365, 1500):
    s = ''
    start_x = None
    stop_x = None
    solid_total = 0
    for x in range(y, y + 500):
        input = [x, y]
        c = ComputeEngine(puzzle_program)
        c.add_data(input)
        c.run(False, False)
        #print(f"Produced: {c.get_output()}")
        result = c.get_output(0)
        if 1 == result:
            if start_x is None: 
                start_x = x
        else:
            if stop_x is None and start_x is not None:
                stop_x = x - 1 # the last digit is behind us..
                solid_total = stop_x - start_x
                break
    print(f"y:{y} solid from {start_x} - {stop_x} for {solid_total}")
    widths[y] = (start_x, stop_x)
    # ok, so the question is, does a grid of 100x100 starting in this row fit into the rows above ?
    # so the final end width of the furthest left point is 99 units further right than the start_x 
    shortest_final_x = start_x + 99
    print(f"The earliest set of 100 on row {y} is {start_x} - {shortest_final_x}")
    # do we have a value for 99 lines earlier ? if not we're wasting our time
    if y - 99 in widths:
        previous_start_x, previous_stop_x = widths[y - 99]
        print(f"The row 99 before this went from {previous_start_x} to {previous_stop_x}")
        if shortest_final_x <= previous_stop_x:
            print("Bingo!")
            exit(9)



print(f"Total:{total}")

# result is : 
#y:860 solid from 948 - 1183 for 235
#The earliest set of 100 on row 860 is 948 - 1047
#The row 99 before this went from 839 to 1047
#Bingo!

# therefore the x where the thing starts is 839
# and the y is 860 - 99 = 761
# so x * 10000 + y = 
# 8390000 + 761 = 8390761
# which is too low apparently..
# man I suck :)
# ok, let's draw the area..
# no wait... x = 948 not 761, it's the X from the bottom row that matters
# so 9480000 + 761 = 9480761
# and there we go - moron but winning.


