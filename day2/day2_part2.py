#  --- Day 2: 1202 Program Alarm ---
#  On the way to your gravity assist around the Moon, your ship computer beeps angrily about 
#  a "1202 program alarm". On the radio, an Elf is already explaining how to handle the situation: 
#   "Don't worry, that's perfectly norma--" The ship computer bursts into flames.
#  
#  You notify the Elves that the computer's magic smoke seems to have escaped. 
#  "That computer ran Intcode programs like the gravity assist program it was working on; surely 
#  there are enough spare parts up there to build a new Intcode computer!"
#  
#  An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, 
#  start by looking at the first integer (called position 0). Here, you will find an opcode - 
#  either 1, 2, or 99. The opcode indicates what to do; for example, 99 means that the program is 
#  finished and should immediately halt. Encountering an unknown opcode means something went wrong.
#  
#  Opcode 1 adds together numbers read from two positions and stores the result in a third position. 
#  The three integers immediately after the opcode tell you these three positions - 
#  the first two indicate the positions from which you should read the input values, 
#  and the third indicates the position at which the output should be stored.
#  
#  For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 
#  10 and 20, add those values, and then overwrite the value at position 30 with their sum.
#  
#  Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. 
#  Again, the three integers after the opcode indicate where the inputs and outputs are, not their 
#  values.
#  
#  Once you're done processing an opcode, move to the next one by stepping forward 4 positions.
#  
#  For example, suppose you have the following program:
#  
#  1,9,10,3,2,3,11,0,99,30,40,50
#  For the purposes of illustration, here is the same program split into multiple lines:
#  
#  1,9,10,3,
#  2,3,11,0,
#  99,
#  30,40,50
#  The first four integers, 1,9,10,3, are at positions 0, 1, 2, and 3. Together, they represent 
#  the first opcode (1, addition), the positions of the two inputs (9 and 10), and the position of 
#  the output (3). To handle this opcode, you first need to get the values at the input positions: 
#  position 9 contains 30, and position 10 contains 40. Add these numbers together to get 70. 
#  Then, store this value at the output position; here, the output position (3) is at position 3, 
#  so it overwrites itself. Afterward, the program looks like this:
#  
#  1,9,10,70,
#  2,3,11,0,
#  99,
#  30,40,50
#  Step forward 4 positions to reach the next opcode, 2. This opcode works just like the previous, 
#  but it multiplies instead of adding. The inputs are at positions 3 and 11; these positions 
#  contain 70 and 50 respectively. Multiplying these produces 3500; this is stored at position 0:
#  
#  3500,9,10,70,
#  2,3,11,0,
#  99,
#  30,40,50
#  Stepping forward 4 more positions arrives at opcode 99, halting the program.
#  
#  Here are the initial and final states of a few more small programs:
#  
#  1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
#  2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
#  2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
#  1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
#  Once you have a working computer, the first step is to restore the gravity 
#  assist program (your puzzle input) to the "1202 program alarm" state it had just 
#  before the last computer caught fire. To do this, before running the program, 
#  replace position 1 with the value 12 and replace position 2 with the value 2. 
#  What value is left at position 0 after the program halts?
#

#
#  Right, so we probably want an array which is big enough to hold everything..
#  but later on we might want subroutines and higher memory areas so perhaps we need something
#  which handles arbitrary index values instead of offsets, although they have to behave like offsets 
#  so initially I'm going with a dictionary of int->int memory_position->value.
#
#  That should give us decent flexibility albeit at a memory and execution speed cost
#

#
#  this lot should probably be a class
#
core_memory = {}

def store_value(memory_position, new_value):
    global core_memory
    core_memory[int(memory_position)] = int(new_value) 

def load_memory(memory_contents, start_offset=0):
    """
    Take a comma separated list of memory values and store them into the machine memory 
    """
    global core_memory 
    individual_values = memory_contents.split(',')
    for location, value in enumerate(individual_values, start=start_offset):
        store_value(location, value)

def has_value(memory_position):
    global core_memory
    return memory_position in core_memory

def read_value(memory_position, default_value=None):
    global core_memory
    memory_position = int(memory_position)
    if memory_position in core_memory:
        result = core_memory[memory_position]
    else:
        if default_value == None:
            raise ValueError(f"Memory location {memory_position} requested but has never been set")
        else:
            result = default_value
    return result 

def dump_memory():
    global core_memory 
    max_memory_position = max(core_memory.keys())
    print(f"Maximum stored memory location is {max_memory_position}")
    # loop through each 4 locations, printing is anything is available in that row, default being 0 
    for starting_position in range(0, max_memory_position + 4, 4):
        # have any of the locations got a value to show ?
        row_has_value = has_value(starting_position) or has_value(starting_position + 1) or has_value(starting_position + 2) or has_value(starting_position + 3)
        if(row_has_value):
            opcode = read_value(starting_position, 0)
            src_addr1 = read_value(starting_position + 1, 0)
            src_addr2 = read_value(starting_position + 2, 0)
            dst_addr = read_value(starting_position + 3, 0)
            print(f"{starting_position}: {opcode} {src_addr1} {src_addr2} {dst_addr}")


def reset_memory():
    global core_memory
    core_memory = {}

#  now the execution logic 
clock = 0
instruction_pointer = 0
OP_ADD = 1
OP_MUL = 2
OP_DON = 99

def dump_processor_state():
    global clock
    global instruction_pointer
    print(f"Clock {clock}  instruction_pointer {instruction_pointer}")

def valid_opcode(opcode):
    return opcode in [OP_ADD, OP_MUL, OP_DON]

def reset_machine():
    global clock 
    global instruction_pointer
    clock = 0
    instruction_pointer = 0

def step():
    global clock
    global instruction_pointer
    clock += 1
    opcode = read_value(instruction_pointer)
    # should stop early on terminate or invalid opcode here 
    if(OP_DON == opcode):
        #print("Program end")
        return False
    if not valid_opcode(opcode):
        print(f"Invalid opcode {opcode} at location {instruction_pointer}")
        raise ValueError(f"Invalid opcode {opcode}")
    src_addr1 = read_value(instruction_pointer + 1)
    src_addr2 = read_value(instruction_pointer + 2)
    dst_addr = read_value(instruction_pointer + 3)
    # get the actual values for the inputs
    val_1 = read_value(src_addr1)
    val_2 = read_value(src_addr2)
    # perform the operation
    if(OP_ADD == opcode): 
        result = val_1 + val_2
        store_value(dst_addr, result)
    elif(OP_MUL == opcode):
        result = val_1 * val_2
        store_value(dst_addr, result)
    else:
        print(f"Unknown Opcode {opcode}")
    instruction_pointer += 4
    return True


#  test the memory logic 
store_value(0, 101)
store_value(1, 80)
store_value(2, 90)
store_value(10, 1024)
store_value(3, 99) 
store_value(1, 77)
dump_memory()
print(f"position 1 has {read_value(1)}")
print(f"position 2 has {read_value(2)}")
print(f"position 3 has {read_value(3)}")
print(f"position 4,999 has {read_value(4, 999)}")
try:
  print(f"position 5 has {read_value(5)}")
except:
  print("that threw - as expected")

# run through the example program from the description 
reset_memory()
program_input = '1,9,10,3,2,3,11,0,99,30,40,50'
load_memory(program_input)
dump_memory()
# looks ok, time to execute the program 
reset_machine()
while(step()):
    dump_processor_state()
    dump_memory()

#
#  Actual part 1 puzzle..
#
puzzle_input = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,1,23,6,27,1,6,27,31,1,13,31,35,1,13,35,39,1,39,13,43,2,43,9,47,2,6,47,51,1,51,9,55,1,55,9,59,1,59,6,63,1,9,63,67,2,67,10,71,2,71,13,75,1,10,75,79,2,10,79,83,1,83,6,87,2,87,10,91,1,91,6,95,1,95,13,99,1,99,13,103,2,103,9,107,2,107,10,111,1,5,111,115,2,115,9,119,1,5,119,123,1,123,9,127,1,127,2,131,1,5,131,0,99,2,0,14,0'
reset_memory()
reset_machine()
load_memory(puzzle_input)
dump_memory()
# To do this, before running the program, 
#  replace position 1 with the value 12 and replace position 2 with the value 2. 
#  What value is left at position 0 after the program halts?
store_value(1, 12)
store_value(2, 2)
dump_memory()
while(step()):
    dump_processor_state()
    dump_memory()


#
# Part 2
#
#  "With terminology out of the way, we're ready to proceed. To complete the gravity assist, 
#  you need to determine what pair of inputs produces the output 19690720."
#  
#  The inputs should still be provided to the program by replacing the values at addresses 1 and 2, 
#  just like before. In this program, the value placed in address 1 is called the noun, and the value 
#  placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, 
#  inclusive.
#  
#  Once the program has halted, its output is available at address 0, also just like before. Each 
#  time you try a pair of inputs, make sure you first reset the computer's memory to the values in 
#  the program (your puzzle input) - in other words, don't reuse memory from a previous attempt.
#  
#  Find the input noun and verb that cause the program to produce the output 19690720. 
#  What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)
#

# ok, so the stupid way is just to execute across the whole problem space : 
# score one for stupid in this case 
# 
target = 19690720

for noun in range(100):
    for verb in range(100):
        # reset the machine 
        reset_memory()
        reset_machine()
        load_memory(puzzle_input)
        store_value(1, noun)
        store_value(2, verb)
        while(step()):
            pass
            #dump_processor_state()
            #dump_memory()
        result = read_value(0)
        print(f"{noun},{verb}={result}")
        if result == target:
            print("Found it !")
            exit(1)










