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

def mode_string(x):
    """ return an indicator value for a positional integer """
    modes = ['pos', 'imd', 'rel']
    return modes[x]

def get_absolute_destination(compute_engine, idx, arguments, parameter_modes):
    """
    Used for destination handling - is the addressing mode used relative ?
    """
    result = arguments[idx]
    # If this is relational then we need to translate using the compute engine current setting 
    if idx < len(parameter_modes):
        if 2 == parameter_modes[idx]:
            result += compute_engine.get_current_relative_base()
    return result

def get_parameter(compute_engine, idx, arguments, parameter_modes):
    """
    Return the specified parameter value - if the corresponding parameter_mode is a value
    """
    position_mode = False  # 0 or missing 
    relative_mode = False  # 2 
    immediate_mode = False  # 1 

    # determine which of these values is appropriate 
    mode_value = 0 
    if idx < len(parameter_modes):
        mode_value = parameter_modes[idx]
    
    # interpret the value 
    if 0 == mode_value:
        position_mode = True 
    elif 1 == mode_value:
        immediate_mode = True 
    elif 2 == mode_value:
        relative_mode = True 
    else:
        raise ValueError(f"Invalid mode value {mode_value} encountered")

    # and do the actual work - get the value 

    if position_mode:
        result = compute_engine.peek(arguments[idx])
    elif relative_mode:
        result = compute_engine.peek_relative(arguments[idx])
    elif immediate_mode:
        # Immediate mode - just return the value
        result = arguments[idx]
    else:
        raise ValueError(f"logic error in the get_parameter - you have a code bug.")

    #print(f"{idx} of {arguments} ({parameter_modes}) -> {result}")
    return result

def operation_add(compute_engine, arguments, parameter_modes = []):
    """ Perform an addition operation, takes 3 operands, src_addr_1, src_addr_2, dest_addr """
    val1 = get_parameter(compute_engine, 0, arguments, parameter_modes)
    val2 = get_parameter(compute_engine, 1, arguments, parameter_modes)
    dest = get_absolute_destination(compute_engine, 2, arguments, parameter_modes)
    result = val1 + val2
    compute_engine.poke(dest, result)
    return True

def operation_multiply(compute_engine, arguments, parameter_modes = []):
    """ Perform a multiplication operation, takes 3 operands, src_addr_1, src_addr_2, dest_addr """
    val1 = get_parameter(compute_engine, 0, arguments, parameter_modes)
    val2 = get_parameter(compute_engine, 1, arguments, parameter_modes)
    dest = get_absolute_destination(compute_engine, 2, arguments, parameter_modes)
    result = val1 * val2
    compute_engine.poke(dest, result)
    #print(f"MUL: {val1} * {val2} = {result}")
    return True

def operation_input(compute_engine, arguments, parameter_modes = []):
    """ Read a value from the data input and store it in the dest_addr """
    dest = get_absolute_destination(compute_engine, 0, arguments, parameter_modes)
    result = compute_engine.read()
    compute_engine.poke(dest, result)
    #print(f"INP: {result} stored at address {arguments[0]}")
    return True

def operation_output(compute_engine, arguments, parameter_modes = []):
    """ Output the value at the address src1 """
    val = get_parameter(compute_engine, 0, arguments, parameter_modes)
    compute_engine.output(val)
    return True

def operation_exit(compute_engine, arguments, parameter_modes = []):
    """ Essentially a no-op """
    return False

def operation_jumpnonzero(compute_engine, arguments, parameter_modes = []):
    """ If the first value is non-zero, the next instruction will be the value from the second parameter """
    test_val = get_parameter(compute_engine, 0, arguments, parameter_modes)
    if 0 != test_val:
        dest = get_parameter(compute_engine, 1, arguments, parameter_modes)
        print(f"jumping to {dest} because {test_val} is non-zero")
        compute_engine.jump_to(dest)
    return True 


def operation_jumpzero(compute_engine, arguments, parameter_modes = []):
    """ If the first value is zero, the next instruction will be the value from the second parameter """
    test_val = get_parameter(compute_engine, 0, arguments, parameter_modes)
    if 0 == test_val:
        dest = get_parameter(compute_engine, 1, arguments, parameter_modes)
        print(f"jumping to {dest} because {test_val} is zero")
        compute_engine.jump_to(dest)
    return True 

def operation_storelessthan(compute_engine, arguments, parameter_modes = []):
    """ if the first parameter is less than the second parameter, 
        it stores 1 in the position given by the third parameter. 
        Otherwise, it stores 0 """
    val1 = get_parameter(compute_engine, 0, arguments, parameter_modes)
    val2 = get_parameter(compute_engine, 1, arguments, parameter_modes)
    dest = get_absolute_destination(compute_engine, 2, arguments, parameter_modes)
    if val1 < val2:
        result = 1
    else:
        result = 0
    compute_engine.poke(dest, result)
    return True

def operation_storeequal(compute_engine, arguments, parameter_modes = []):
    """ if the first parameter is equal to the second parameter, 
        it stores 1 in the position given by the third parameter. 
        Otherwise, it stores 0 """
    val1 = get_parameter(compute_engine, 0, arguments, parameter_modes)
    val2 = get_parameter(compute_engine, 1, arguments, parameter_modes)
    dest = get_absolute_destination(compute_engine, 2, arguments, parameter_modes)
    if val1 == val2:
        result = 1
    else:
        result = 0
    compute_engine.poke(dest, result)
    return True

def operation_changerelbase(compute_engine, arguments, parameter_modes = []):
    """ Modify the compute-engine's relative base by the value of our only parameter """
    val1 = get_parameter(compute_engine, 0, arguments, parameter_modes)
    compute_engine.modify_relative_base(val1)
    return True

class OperationInfo:
    def __init__(self, name, argument_count, func, desc):
        self.name = name
        self.argument_count = argument_count
        self.func = func
        self.description = desc

    def __repr__(self):
        return f"{self.name} ({self.argument_count} args)"

opcodes = {
    1: OperationInfo("ADD", 3, operation_add, "Add a+b, store in c"),
    2: OperationInfo("MUL", 3, operation_multiply, "Multiply a*b, store in c"),
    3: OperationInfo("INP", 1, operation_input, "Get one input value and store in a"),
    4: OperationInfo("OUT", 1, operation_output, "Output a"),
    5: OperationInfo("JNZ", 2, operation_jumpnonzero, "Jump to b if a is non-zero"),
    6: OperationInfo("JPZ", 2, operation_jumpzero, "Jump to b if a is zero"),
    7: OperationInfo("SLT", 3, operation_storelessthan, "Store 1/0 in c depending on whether a > b"),
    8: OperationInfo("SEQ", 3, operation_storeequal, "Store 1/0 in c depending on whether a == b"),
    9: OperationInfo("REL", 1, operation_changerelbase, "Change the relative base by a"),
    99: OperationInfo("END", 0, operation_exit, "Exit the program")
}

def get_opcode_info(opcode):
    """ Return the information block for the given opcode """
    result = None
    if opcode in opcodes:
        result = opcodes[opcode]
    return result



def valid_opcode(opcode):
    """ Is the opcode passed a valid opcode """
    return opcode in opcodes

def opcode_split(opcode, parameter_modes_size = 16):
    """
      Takes an input value opcode and returns the actual opcode (smallest two digits)
      and the parameter modes array for the higher order bits 
    """
    parameter_list = []
    actual_opcode = opcode % 100
    parameter_modes = int(opcode / 100)
    #print(f"Actual opcode: {actual_opcode}")
    #print(f"Param Modes: {parameter_modes}")
    store_idx = 0
    while(0 != parameter_modes):
        #
        #  Peel off this parameter and put it into the result in the right place
        #
        this_mode = parameter_modes % 10
        parameter_modes = int(parameter_modes / 10)
        parameter_list.append(this_mode)
        # next 
        store_idx += 1

    #print(f"final list is : {parameter_list}")
    return actual_opcode, parameter_list


class ComputeEngine:
    def __init__(self, memory = None, data = None):
        self.reset()
        if memory is not None:
            self.load_memory(memory)
        if data is not None:
            self.load_data(data)

    def __repr__(self):
        return f"IntCode(clock={self.clock} *data={self.data_pointer} *instruction={self.instruction_pointer}"

    def clear_memory(self):
        """ Clear down the main storage of the machine """
        self.core_memory = {}
        self.data = []
        self.data_pointer = 0
        self.output_buffer = []

    def reset(self, clear_memory = True):
        """ Reset the machine to a clean state, optionally preserving the current memory """
        self.clock = 0
        self.instruction_pointer = 0
        self.relative_base = 0
        self.inhibit_increment = False
        if clear_memory:
            self.clear_memory()

    def set_relative_base(self, new_relative_base):
        """ Update the relative base to be an explicit value """
        self.relative_base = new_relative_base

    def modify_relative_base(self, modification):
        """ Change the relative base by the value passed """
        self.relative_base += modification

    def get_current_relative_base(self):
        return self.relative_base

    def read(self):
        """ Read the next value from the data """
        if self.data_pointer < len(self.data):
            result = self.data[self.data_pointer]
            self.data_pointer += 1
        else:
            raise ValueError("read operation that has run out of data")
        return result

    def output(self, val):
        """ Output a value, print it and add it to the output buffer """
        #print(f"OUTPUT: {val}")
        self.output_buffer.append(val)

    def jump_to(self, location):
        """ Set the next instruction address """
        self.instruction_pointer = location
        self.inhibit_increment = True

    def poke(self, memory_position, new_value):
        """ Store a given value in the provided memory address """
        new_value = int(new_value)
        self.core_memory[int(memory_position)] = new_value 
        return new_value

    # Default value is now 0, according to day 9 pt 1
    def peek(self, memory_position, default_value = 0):
        """ Obtain a value from a specified memory address, optional default value if not. """
        memory_position = int(memory_position)
        if memory_position in self.core_memory:
            result = self.core_memory[memory_position]
        else:
            if default_value == None:
                raise ValueError(f"Memory location {memory_position} requested but has never been set")
            else:
                result = default_value
        return result 

    def peek_relative(self, memory_position, default_value = None):
        """ peek functionality but relative to the relative_base value """
        return self.peek(self.relative_base + memory_position, default_value)

    def populated(self, memory_position):
        """ Return True if the memory_location specified has a populated value """
        return int(memory_position) in self.core_memory

    def load_data(self, data_array):
        """
        Load the data input values for later consumption
        """
        self.data = [*data_array]
        self.data_pointer = 0

    def add_data(self, data_array):
        """
        Add additional data to the data input, this doesn't need to reset the data pointer
        """
        self.data.extend([*data_array])

    def load_memory(self, memory_contents, start_offset=0):
        """
        Take a comma separated list of memory values and store them into the machine memory 
        """
        if isinstance(memory_contents, list):
            individual_values = [int(x) for x in memory_contents]
        else:
            individual_values = memory_contents.split(',')
        for location, value in enumerate(individual_values, start=start_offset):
            self.poke(location, value)

    def dump_memory(self):
        """
        Output a nicely formatted display of the current memory, clock and instruction pointer
        """
        max_memory_position = max(self.core_memory.keys())
        # starting at the beginning, process each of the locations with the correct number of arguments
        # loop through each 4 locations, printing is anything is available in that row, default being 0 
        print(f"Clock {self.clock:04}  instruction_pointer:{self.instruction_pointer:08}")
        print(f"Data: {self.data[self.data_pointer:]}  Output: {self.output_buffer}")
        this_location = 0
        while(this_location <= max_memory_position):
            # Is this location a valid operation ?
            raw_opcode = self.peek(this_location, -42)
            opcode, parameter_modes = opcode_split(raw_opcode)
            if valid_opcode(opcode):
                # 
                #  Ok, get the relevant information about this opcode
                #
                opcode_info = get_opcode_info(opcode)
                #print(f"Getting {opcode_info}")
                arguments = [self.peek(this_location + i + 1, -42) for i in range(opcode_info.argument_count)]
                formatted_arguments = [f"{i:02}" for i in arguments]
                formatted_argument_list = " ".join(formatted_arguments)
                current_instruction_marker = ' '
                if this_location == self.instruction_pointer:
                    current_instruction_marker = '*'
                this_line = f"{current_instruction_marker} {this_location:08} {raw_opcode:05} {opcode_info.name} {formatted_argument_list}"
                print(this_line)
                this_location += 1 + opcode_info.argument_count;
            else:
                data_size = 4
                display_data = [f"{self.peek(this_location + i, 0):02}" if self.populated(this_location + i) else '??' for i in range(data_size)]  
                this_line = f"  {this_location:08} {display_data}"
                print(this_line)
                this_location += data_size
        print("")


    def step(self, debug_step = True):
        """
        Execute the next instruction, returning True if the program should continue or False if it should end  
        """
        self.clock += 1
        raw_opcode = self.peek(self.instruction_pointer)
        opcode, parameter_modes = opcode_split(raw_opcode)
        opcode_info = get_opcode_info(opcode)
        # get the correct number of arguments 
        arguments = [self.peek(self.instruction_pointer + i + 1) for i in range(opcode_info.argument_count)]

        # debug if necessary 
        if debug_step:
            #params = [f"{x} " for x in arguments]
            #modes = [f"{mode_string(x) for x in parameter_modes}"]
            s = f"{opcode_info.name} {raw_opcode} {arguments} {parameter_modes}"
            print(s)

        # call the function with the execution 
        result = opcode_info.func(self, arguments, parameter_modes)
        # increment the instruction counter unless we jumped 
        if self.inhibit_increment:
            self.inhibit_increment = False
        else:
            self.instruction_pointer += 1 + opcode_info.argument_count

        # and we're done
        return result 

    def run(self, debug_output = False):
        """
        Execute the program until the end, optionally debugging every step
        """
        if debug_output:
            self.dump_memory()
        while(self.step()):
            if debug_output:
                self.dump_memory()
        if debug_output:
            self.dump_memory()

    def _getoutputlength(self):
        return len(self.output_buffer)

    def run_to_output(self, debug_output = False):
        """
        Execute the program until the end or the next output instruction has been executed, 
        optionally debugging every step
        """
        result = None
        if(debug_output):
            self.dump_memory()
        starting_output_length = self._getoutputlength()
        while(self.step() and self._getoutputlength() == starting_output_length):
            if debug_output:
                self.dump_memory()
        if self._getoutputlength() != starting_output_length:
            result = self.output_buffer[-1]
        return result

#
#  quick testing 
#


if __name__ == "__main__":
    c = ComputeEngine()
    # c.load_memory("1, 9, 10, 11, 2, 9, 10, 12, 99, 10, 42")
    # c.run(True)
    # 
    # c.reset()
    # c.load_memory("101, 42, 0, 6, 99")
    # c.run(True)
    # 
    # c.reset()
    # c.load_memory("1002,4,3,4,33")
    # c.run(True)

    c.reset()
    #c.load_memory("3, 0, 3, 1, 104, 50, 4, 0, 4, 1, 4, 2, 99")
    #c.load_memory([1108, 88, 88, 8, 99, 99])
    c.load_memory([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
    c.load_data([9])
    c.run(True)


##  test the memory logic 
#store_value(0, 101)
#store_value(1, 80)
#store_value(2, 90)
#store_value(10, 1024)
#store_value(3, 99) 
#store_value(1, 77)
#dump_memory()
#print(f"position 1 has {read_value(1)}")
#print(f"position 2 has {read_value(2)}")
#print(f"position 3 has {read_value(3)}")
#print(f"position 4,999 has {read_value(4, 999)}")
#try:
#  print(f"position 5 has {read_value(5)}")
#except:
#  print("that threw - as expected")
#
## run through the example program from the description 
#reset_memory()
#program_input = '1,9,10,3,2,3,11,0,99,30,40,50'
#load_memory(program_input)
#dump_memory()
## looks ok, time to execute the program 
#reset_machine()
#while(step()):
#    dump_processor_state()
#    dump_memory()
#
##
##  Actual part 1 puzzle..
##
#puzzle_input = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,1,23,6,27,1,6,27,31,1,13,31,35,1,13,35,39,1,39,13,43,2,43,9,47,2,6,47,51,1,51,9,55,1,55,9,59,1,59,6,63,1,9,63,67,2,67,10,71,2,71,13,75,1,10,75,79,2,10,79,83,1,83,6,87,2,87,10,91,1,91,6,95,1,95,13,99,1,99,13,103,2,103,9,107,2,107,10,111,1,5,111,115,2,115,9,119,1,5,119,123,1,123,9,127,1,127,2,131,1,5,131,0,99,2,0,14,0'
#reset_memory()
#reset_machine()
#load_memory(puzzle_input)
#dump_memory()
## To do this, before running the program, 
##  replace position 1 with the value 12 and replace position 2 with the value 2. 
##  What value is left at position 0 after the program halts?
#store_value(1, 12)
#store_value(2, 2)
#dump_memory()
#while(step()):
#    dump_processor_state()
#    dump_memory()
#
#
##
## Part 2
##
##  "With terminology out of the way, we're ready to proceed. To complete the gravity assist, 
##  you need to determine what pair of inputs produces the output 19690720."
##  
##  The inputs should still be provided to the program by replacing the values at addresses 1 and 2, 
##  just like before. In this program, the value placed in address 1 is called the noun, and the value 
##  placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, 
##  inclusive.
##  
##  Once the program has halted, its output is available at address 0, also just like before. Each 
##  time you try a pair of inputs, make sure you first reset the computer's memory to the values in 
##  the program (your puzzle input) - in other words, don't reuse memory from a previous attempt.
##  
##  Find the input noun and verb that cause the program to produce the output 19690720. 
##  What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)
##
#
## ok, so the stupid way is just to execute across the whole problem space : 
## score one for stupid in this case 
## 
#target = 19690720
#
#for noun in range(100):
#    for verb in range(100):
#        # reset the machine 
#        reset_memory()
#        reset_machine()
#        load_memory(puzzle_input)
#        store_value(1, noun)
#        store_value(2, verb)
#        while(step()):
#            pass
#            #dump_processor_state()
#            #dump_memory()
#        result = read_value(0)
#        print(f"{noun},{verb}={result}")
#        if result == target:
#            print("Found it !")
#            exit(1)
#
#








