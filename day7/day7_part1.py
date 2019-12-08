#  --- Day 7: Amplification Circuit ---
#  Based on the navigational maps, you're going to need to send more power to your ship's thrusters to reach Santa in time. To do this, you'll need to configure a series of amplifiers already installed on the ship.
#  
#  There are five amplifiers connected in series; each one receives an input signal and produces an output signal. They are connected such that the first amplifier's output leads to the second amplifier's input, the second amplifier's output leads to the third amplifier's input, and so on. The first amplifier's input value is 0, and the last amplifier's output leads to your ship's thrusters.
#  
    #  O-------O  O-------O  O-------O  O-------O  O-------O
#  0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
    #  O-------O  O-------O  O-------O  O-------O  O-------O
#  The Elves have sent you some Amplifier Controller Software (your puzzle input), a program that should run on your existing Intcode computer. Each amplifier will need to run a copy of the program.
#  
#  When a copy of the program starts running on an amplifier, it will first use an input instruction to ask the amplifier for its current phase setting (an integer from 0 to 4). Each phase setting is used exactly once, but the Elves can't remember which amplifier needs which phase setting.
#  
#  The program will then call another input instruction to get the amplifier's input signal, compute the correct output signal, and supply it back to the amplifier with an output instruction. (If the amplifier has not yet received an input signal, it waits until one arrives.)
#  
#  Your job is to find the largest output signal that can be sent to the thrusters by trying every possible combination of phase settings on the amplifiers. Make sure that memory is not shared or reused between copies of the program.
#  
#  For example, suppose you want to try the phase setting sequence 3,1,2,4,0, which would mean setting amplifier A to phase setting 3, amplifier B to setting 1, C to 2, D to 4, and E to 0. Then, you could determine the output signal that gets sent from amplifier E to the thrusters with the following steps:
#  
#  Start the copy of the amplifier controller software that will run on amplifier A. At its first input instruction, provide it the amplifier's phase setting, 3. At its second input instruction, provide it the input signal, 0. After some calculations, it will use an output instruction to indicate the amplifier's output signal.
#  Start the software for amplifier B. Provide it the phase setting (1) and then whatever output signal was produced from amplifier A. It will then produce a new output signal destined for amplifier C.
#  Start the software for amplifier C, provide the phase setting (2) and the value from amplifier B, then collect its output signal.
#  Run amplifier D's software, provide the phase setting (4) and input value, and collect its output signal.
#  Run amplifier E's software, provide the phase setting (0) and input value, and collect its output signal.
#  The final output signal from amplifier E would be sent to the thrusters. However, this phase setting sequence may not have been the best one; another sequence might have sent a higher signal to the thrusters.
#  
#  Here are some example programs:
#  
#  Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):
#  
#  3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
#  Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):
#  
#  3,23,3,24,1002,24,10,24,1002,23,-1,23,
#  101,5,23,23,1,24,23,23,4,23,99,0,0
#  Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):
#  
#  3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
#  1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
#  Try every combination of phase settings on the amplifiers. 
#  What is the highest signal that can be sent to the thrusters?

import os 
import sys 
import itertools
sys.path.append("c:\\development\\advent-of-code-2019")
from compute_engine.engine import ComputeEngine


def all_permutations_list(amplifier_count):
    """ Return every valid permutation for an amp count of X """
    pick_list = [x for x in range(amplifier_count)]
    result_iterator = itertools.permutations(pick_list, amplifier_count)
    return result_iterator


# just in case we end up doing the same thing many times 
cached_results = {}
def has_cached_result(amplifier_setting, initial_input):
    global cached_results
    key = (amplifier_setting, initial_input)
    if key in cached_results:
        result = True 
    else:
        result = False
    return result 

def get_cached_result(amplifier_setting, initial_input):
    global cached_results
    key = (amplifier_setting, initial_input)
    return cached_results[key]

def store_result_in_cache(amplifier_setting, initial_input, result):
    global cached_results
    key = (amplifier_setting, initial_input)
    cached_results[key] = result 



def calculate_one_signal(program_code, amplifier_settings, initial_input):
    """ 
      Run the program X times where X is the number of settings in amplifier_settings
      Each run should have the input to the intcode machine set to [setting, X]
      On the first run, the X value is passed in initial_input
      After the first execution, the output value from the previous run becomes the X value 
    """
    value_X = initial_input
    for this_amplifier_setting in amplifier_settings:
        print(f"executing for {this_amplifier_setting},{value_X}")
        if has_cached_result(this_amplifier_setting, value_X):
            value_X = get_cached_result(this_amplifier_setting, value_X)
        else:
            c = ComputeEngine()
            c.load_memory(program_code)
            c.load_data([this_amplifier_setting, value_X])
            c.run(False)
            new_value_X = c.output_buffer[0]
            store_result_in_cache(this_amplifier_setting, value_X, new_value_X)
            value_X = new_value_X
    return value_X


def determine_highest_signal(program_code, amplifier_count = 5, initial_input = 0):
    """
    Get the best score from all the possible settings 
    """
    dial_setting_combinations = all_permutations_list(amplifier_count)
    best_result = -1
    best_settings = None

    for this_dial_setting in dial_setting_combinations:
        this_result = calculate_one_signal(program_code, this_dial_setting, initial_input)
        print(f"{this_dial_setting} -> {this_result}")
        if this_result > best_result:
            best_result = this_result 
            best_settings = [*this_dial_setting]

    return best_settings, best_result


test_program_answer_43210 = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
test_program_answer_54321 = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
test_program_answer_65210 = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
puzzle_program = "3,8,1001,8,10,8,105,1,0,0,21,46,59,72,93,110,191,272,353,434,99999,3,9,101,4,9,9,1002,9,3,9,1001,9,5,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,1002,9,5,9,1001,9,5,9,4,9,99,3,9,101,4,9,9,1002,9,4,9,4,9,99,3,9,102,3,9,9,101,3,9,9,1002,9,2,9,1001,9,5,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99"
winner, score = determine_highest_signal(puzzle_program, 5)
print(f"winner is {winner} with a result of {score}")


