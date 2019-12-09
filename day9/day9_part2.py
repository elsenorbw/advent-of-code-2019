#  --- Day 9: Sensor Boost ---
#  You've just said goodbye to the rebooted rover and left Mars when you receive a faint distress 
#  signal coming from the asteroid belt. It must be the Ceres monitoring station!
#  
#  In order to lock on to the signal, you'll need to boost your sensors. The Elves send up the latest 
#  BOOST program - Basic Operation Of System Test.
#  
#  While BOOST (your puzzle input) is capable of boosting your sensors, for tenuous safety reasons, 
#  it refuses to do so until the computer it runs on passes some checks to demonstrate it is a complete 
#  Intcode computer.
#  
#  Your existing Intcode computer is missing one key feature: it needs support for parameters in relative 
#  mode.
#  
#  Parameters in mode 2, relative mode, behave very similarly to parameters in position mode: 
#  the parameter is interpreted as a position. Like position mode, parameters in relative mode 
#  can be read from or written to.
#  
#  The important difference is that relative mode parameters don't count from address 0. Instead, 
#  they count from a value called the relative base. The relative base starts at 0.
#  
#  The address a relative mode parameter refers to is itself plus the current relative base. When 
#  the relative base is 0, relative mode parameters and position mode parameters with the same value 
#  refer to the same address.
#  
#  For example, given a relative base of 50, a relative mode parameter of -7 refers to memory 
#  address 50 + -7 = 43.
#  
#  The relative base is modified with the relative base offset instruction:
#  
#  Opcode 9 adjusts the relative base by the value of its only parameter. The relative base increases 
#  (or decreases, if the value is negative) by the value of the parameter.
#  For example, if the relative base is 2000, then after the instruction 109,19, the relative base 
#  would be 2019. If the next instruction were 204,-34, then the value at address 1985 would be 
#  output.
#  
#  Your Intcode computer will also need a few other capabilities:
#  
#  The computer's available memory should be much larger than the initial program. Memory beyond 
#  the initial program starts with the value 0 and can be read or written like any other memory. 
#  (It is invalid to try to access memory at a negative address, though.)
#  The computer should have support for large numbers. Some instructions near the beginning of the 
#  BOOST program will verify this capability.
#  Here are some example programs that use these features:
#  
#  109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 takes no input and produces a copy 
#  of itself as output.
#  1102,34915192,34915192,7,4,7,99,0 should output a 16-digit number.
#  104,1125899906842624,99 should output the large number in the middle.
#  The BOOST program will ask for a single input; run it in test mode by providing it the value 1. 
#  It will perform a series of checks on each opcode, output any opcodes (and the associated parameter 
#  modes) that seem to be functioning incorrectly, and finally output a BOOST keycode.
#  
#  Once your Intcode computer is fully functional, the BOOST program should report no malfunctioning 
#  opcodes when run in test mode; it should only output a single value, the BOOST keycode. What 
#  BOOST keycode does it produce?
#
# 
# Your puzzle answer was 2955820355.
# 
# The first half of this puzzle is complete! It provides one gold star: *
# 
# --- Part Two ---
# You now have a complete Intcode computer.
# 
# Finally, you can lock on to the Ceres distress signal! You just need to boost your sensors using the 
# BOOST program.
# 
# The program runs in sensor boost mode by providing the input instruction the value 2. Once run, it 
# will boost the sensors automatically, but it might take a few seconds to complete the operation on 
# slower hardware. In sensor boost mode, the program will output a single value: the coordinates of 
# the distress signal.
# 
# Run the BOOST program in sensor boost mode. What are the coordinates of the distress signal?
# 
#   
import sys 
sys.path.append("c:\\development\\advent-of-code-2019")
from compute_engine.engine import ComputeEngine

test_copy_self = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
test_16_digits = "1102,34915192,34915192,7,4,7,99,0"
test_large_number = "104,1125899906842624,99"

puzzle_input = "1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,3,0,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,35,1,1010,1102,1,33,1013,1101,0,715,1022,1102,1,20,1004,1102,1,24,1012,1101,36,0,1005,1101,0,655,1024,1102,32,1,1014,1101,0,499,1026,1102,1,242,1029,1101,0,25,1002,1101,0,27,1017,1101,708,0,1023,1101,0,21,1016,1101,0,28,1000,1101,0,492,1027,1102,34,1,1015,1102,29,1,1007,1102,247,1,1028,1101,0,39,1011,1102,1,31,1018,1102,1,0,1020,1102,1,37,1006,1101,1,0,1021,1102,26,1,1009,1102,1,38,1008,1101,30,0,1019,1102,1,23,1001,1102,650,1,1025,1101,22,0,1003,109,7,2101,0,-7,63,1008,63,29,63,1005,63,205,1001,64,1,64,1105,1,207,4,187,1002,64,2,64,109,-1,1202,-1,1,63,1008,63,35,63,1005,63,227,1106,0,233,4,213,1001,64,1,64,1002,64,2,64,109,17,2106,0,5,4,239,1105,1,251,1001,64,1,64,1002,64,2,64,109,-1,21108,40,39,-4,1005,1018,271,1001,64,1,64,1106,0,273,4,257,1002,64,2,64,109,-9,1206,8,285,1106,0,291,4,279,1001,64,1,64,1002,64,2,64,109,-13,2108,27,0,63,1005,63,307,1106,0,313,4,297,1001,64,1,64,1002,64,2,64,109,11,2101,0,-5,63,1008,63,37,63,1005,63,339,4,319,1001,64,1,64,1105,1,339,1002,64,2,64,109,13,21101,41,0,-9,1008,1015,41,63,1005,63,365,4,345,1001,64,1,64,1106,0,365,1002,64,2,64,109,-14,1201,-6,0,63,1008,63,22,63,1005,63,385,1106,0,391,4,371,1001,64,1,64,1002,64,2,64,109,-10,1202,3,1,63,1008,63,22,63,1005,63,417,4,397,1001,64,1,64,1105,1,417,1002,64,2,64,109,6,1207,-3,21,63,1005,63,437,1001,64,1,64,1105,1,439,4,423,1002,64,2,64,109,16,21107,42,41,-8,1005,1014,455,1105,1,461,4,445,1001,64,1,64,1002,64,2,64,109,-28,2107,24,7,63,1005,63,481,1001,64,1,64,1106,0,483,4,467,1002,64,2,64,109,33,2106,0,0,1001,64,1,64,1106,0,501,4,489,1002,64,2,64,109,-18,2108,38,-1,63,1005,63,519,4,507,1105,1,523,1001,64,1,64,1002,64,2,64,109,-3,1208,-4,25,63,1005,63,545,4,529,1001,64,1,64,1106,0,545,1002,64,2,64,109,12,21102,43,1,-8,1008,1010,43,63,1005,63,571,4,551,1001,64,1,64,1106,0,571,1002,64,2,64,109,-1,1207,-8,27,63,1005,63,593,4,577,1001,64,1,64,1106,0,593,1002,64,2,64,109,-7,21101,44,0,8,1008,1018,42,63,1005,63,617,1001,64,1,64,1105,1,619,4,599,1002,64,2,64,109,-4,1208,-1,39,63,1005,63,639,1001,64,1,64,1105,1,641,4,625,1002,64,2,64,109,13,2105,1,5,4,647,1106,0,659,1001,64,1,64,1002,64,2,64,109,4,1206,-3,673,4,665,1106,0,677,1001,64,1,64,1002,64,2,64,109,-22,21108,45,45,10,1005,1011,699,4,683,1001,64,1,64,1105,1,699,1002,64,2,64,109,29,2105,1,-7,1001,64,1,64,1105,1,717,4,705,1002,64,2,64,109,-19,21107,46,47,5,1005,1016,739,4,723,1001,64,1,64,1106,0,739,1002,64,2,64,109,-8,2102,1,2,63,1008,63,33,63,1005,63,763,1001,64,1,64,1106,0,765,4,745,1002,64,2,64,109,1,1201,-2,0,63,1008,63,25,63,1005,63,791,4,771,1001,64,1,64,1105,1,791,1002,64,2,64,109,16,1205,0,803,1105,1,809,4,797,1001,64,1,64,1002,64,2,64,109,-8,1205,9,827,4,815,1001,64,1,64,1106,0,827,1002,64,2,64,109,-4,2102,1,-3,63,1008,63,36,63,1005,63,853,4,833,1001,64,1,64,1106,0,853,1002,64,2,64,109,17,21102,47,1,-6,1008,1019,50,63,1005,63,877,1001,64,1,64,1105,1,879,4,859,1002,64,2,64,109,-29,2107,22,5,63,1005,63,897,4,885,1106,0,901,1001,64,1,64,4,64,99,21102,27,1,1,21101,0,915,0,1106,0,922,21201,1,25338,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1105,1,922,22102,1,1,-1,21201,-2,-3,1,21102,957,1,0,1106,0,922,22201,1,-1,-2,1105,1,968,21202,-2,1,-2,109,-3,2106,0,0"


c = ComputeEngine()
c.load_memory(puzzle_input)
c.load_data([2])
c.run(False)
c.dump_memory()


