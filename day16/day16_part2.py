#  --- Day 16: Flawed Frequency Transmission ---
#  You're 3/4ths of the way through the gas giants. Not only do roundtrip signals to Earth take five 
#  hours, but the signal quality is quite bad as well. You can clean up the signal with the Flawed 
#  Frequency Transmission algorithm, or FFT.
#  
#  As input, FFT takes a list of numbers. In the signal you received (your puzzle input), each number 
#  is a single digit: data like 15243 represents the sequence 1, 5, 2, 4, 3.
#  
#  FFT operates in repeated phases. In each phase, a new list is constructed with the same length as 
#  the input list. This new list is also used as the input for the next phase.
#  
#  Each element in the new list is built by multiplying every value in the input list by a value in a 
#  repeating pattern and then adding up the results. So, if the input list were 9, 8, 7, 6, 5 and the 
#  pattern for a given element were 1, 2, 3, the result would be 9*1 + 8*2 + 7*3 + 6*1 + 5*2 
#  (with each input element on the left and each value in the repeating pattern on the right of each 
#  multiplication). Then, only the ones digit is kept: 38 becomes 8, -17 becomes 7, and so on.
#  
#  While each element in the output array uses all of the same input array elements, the actual 
#  repeating pattern to use depends on which output element is being calculated. 
#  The base pattern is 0, 1, 0, -1. Then, repeat each value in the pattern a number of times equal 
#  to the position in the output list being considered. Repeat once for the first element, twice for 
#  the second element, three times for the third element, and so on. 
#  So, if the third element of the output list is being calculated, repeating the values would 
#  produce: 0, 0, 0, 1, 1, 1, 0, 0, 0, -1, -1, -1.
#  
#  When applying the pattern, skip the very first value exactly once. 
#  (In other words, offset the whole pattern left by one.) So, for the second element of the 
#  output list, the actual pattern used would be: 0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0, -1, -1, ....
#  
#  After using this process to calculate each element of the output list, 
#  the phase is complete, and the output list of this phase is used as the new input list for the 
#  next phase, if any.
#  
#  Given the input signal 12345678, below are four phases of FFT. 
#  Within each phase, each output digit is calculated on a single line with the result at the far right; 
#  each multiplication operation shows the input digit on the left and the pattern value on the right:
#  
#  Input signal: 12345678
#  
#  1*1  + 2*0  + 3*-1 + 4*0  + 5*1  + 6*0  + 7*-1 + 8*0  = 4
#  1*0  + 2*1  + 3*1  + 4*0  + 5*0  + 6*-1 + 7*-1 + 8*0  = 8
#  1*0  + 2*0  + 3*1  + 4*1  + 5*1  + 6*0  + 7*0  + 8*0  = 2
#  1*0  + 2*0  + 3*0  + 4*1  + 5*1  + 6*1  + 7*1  + 8*0  = 2
#  1*0  + 2*0  + 3*0  + 4*0  + 5*1  + 6*1  + 7*1  + 8*1  = 6
#  1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*1  + 7*1  + 8*1  = 1
#  1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*0  + 7*1  + 8*1  = 5
#  1*0  + 2*0  + 3*0  + 4*0  + 5*0  + 6*0  + 7*0  + 8*1  = 8
#  
#  After 1 phase: 48226158
#  
#  4*1  + 8*0  + 2*-1 + 2*0  + 6*1  + 1*0  + 5*-1 + 8*0  = 3
#  4*0  + 8*1  + 2*1  + 2*0  + 6*0  + 1*-1 + 5*-1 + 8*0  = 4
#  4*0  + 8*0  + 2*1  + 2*1  + 6*1  + 1*0  + 5*0  + 8*0  = 0
#  4*0  + 8*0  + 2*0  + 2*1  + 6*1  + 1*1  + 5*1  + 8*0  = 4
#  4*0  + 8*0  + 2*0  + 2*0  + 6*1  + 1*1  + 5*1  + 8*1  = 0
#  4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*1  + 5*1  + 8*1  = 4
#  4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*0  + 5*1  + 8*1  = 3
#  4*0  + 8*0  + 2*0  + 2*0  + 6*0  + 1*0  + 5*0  + 8*1  = 8
#  
#  After 2 phases: 34040438
#  
#  3*1  + 4*0  + 0*-1 + 4*0  + 0*1  + 4*0  + 3*-1 + 8*0  = 0
#  3*0  + 4*1  + 0*1  + 4*0  + 0*0  + 4*-1 + 3*-1 + 8*0  = 3
#  3*0  + 4*0  + 0*1  + 4*1  + 0*1  + 4*0  + 3*0  + 8*0  = 4
#  3*0  + 4*0  + 0*0  + 4*1  + 0*1  + 4*1  + 3*1  + 8*0  = 1
#  3*0  + 4*0  + 0*0  + 4*0  + 0*1  + 4*1  + 3*1  + 8*1  = 5
#  3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*1  + 3*1  + 8*1  = 5
#  3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*0  + 3*1  + 8*1  = 1
#  3*0  + 4*0  + 0*0  + 4*0  + 0*0  + 4*0  + 3*0  + 8*1  = 8
#  
#  After 3 phases: 03415518
#  
#  0*1  + 3*0  + 4*-1 + 1*0  + 5*1  + 5*0  + 1*-1 + 8*0  = 0
#  0*0  + 3*1  + 4*1  + 1*0  + 5*0  + 5*-1 + 1*-1 + 8*0  = 1
#  0*0  + 3*0  + 4*1  + 1*1  + 5*1  + 5*0  + 1*0  + 8*0  = 0
#  0*0  + 3*0  + 4*0  + 1*1  + 5*1  + 5*1  + 1*1  + 8*0  = 2
#  0*0  + 3*0  + 4*0  + 1*0  + 5*1  + 5*1  + 1*1  + 8*1  = 9
#  0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*1  + 1*1  + 8*1  = 4
#  0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*0  + 1*1  + 8*1  = 9
#  0*0  + 3*0  + 4*0  + 1*0  + 5*0  + 5*0  + 1*0  + 8*1  = 8
#  
#  After 4 phases: 01029498
#  Here are the first eight digits of the final output list after 100 phases for some larger inputs:
#  
#  80871224585914546619083218645595 becomes 24176176.
#  19617804207202209144916044189917 becomes 73745418.
#  69317163492948606335995924319873 becomes 52432133.
#  After 100 phases of FFT, what are the first eight digits in the final output list?
#  
#  To begin, get your puzzle input.
#
#  
#  Your puzzle answer was 58672132.
#  
#  The first half of this puzzle is complete! It provides one gold star: *
#  
#  --- Part Two ---
#  Now that your FFT is working, you can decode the real signal.
#  
#  The real signal is your puzzle input repeated 10000 times. Treat this new signal as a 
#  single input list. Patterns are still calculated as before, and 100 phases of FFT are 
#  still applied.
#  
#  The first seven digits of your initial input signal also represent the message offset. 
#  The message offset is the location of the eight-digit message in the final output list. 
#  Specifically, the message offset indicates the number of digits to skip before reading the 
#  eight-digit message. For example, if the first seven digits of your initial input signal 
#  were 1234567, the eight-digit message would be the eight digits after skipping 1,234,567 
#  digits of the final output list. Or, if the message offset were 7 and your final output 
#  list were 98765432109876543210, the eight-digit message would be 21098765. 
#  (Of course, your real message offset will be a seven-digit number, not a one-digit number like 7.)
#  
#  Here is the eight-digit message in the final output list after 100 phases. 
#  The message offset given in each input has been highlighted. 
#  (Note that the inputs given below are repeated 10000 times to find the actual starting input lists.)
#  
#  03036732577212944063491565474664 becomes 84462026.
#  02935109699940807407585447034323 becomes 78725270.
#  03081770884921959731165446850517 becomes 53553731.
#  After repeating your input signal 10000 times and running 100 phases of FFT, 
#  what is the eight-digit message embedded in the final output list?
#  
#  Although it hasn't changed, you can still get your puzzle input.

#
# right - this is way too big to do the naive way now..
# we will have 6.5 million input values
# the way that we absolute the results means that the work becomes effectively adding, not multiplication
# the first digit is the sum of the every other digit % 10 
# the second digit is the sum of every other set of 2 digits 
# the third - sets of three etc.. 
# so for an input of 12345678 -> 48226158 after 1 phase 
#




# chop the input into integer arrays 

class PatternIterator:
    def __init__(self, output_digit, pattern=[0, 1, 0, -1]):
        self.repeats = output_digit
        self.current_idx = 0
        self.current_count = 0
        self.pattern = pattern

    def __iter__(self):
        # initialise the various pointers to skip the first item 
        if 0 == self.repeats:
            self.current_idx = 1
        else:
            self.current_count = 1 
        return self

    def __next__(self):
        # return this value, then setup the next one 
        result = self.pattern[self.current_idx]
        self.current_count += 1
        if self.current_count > self.repeats:
            self.current_count = 0
            self.current_idx += 1
            if self.current_idx >= len(self.pattern):
                self.current_idx = 0
        return result




# algorithm for executing one phase 
def apply_one_fft(phase_input, phase_number):
    """
    Apply the maths for a single phase
    """
    result = []
    input_length = len(phase_input)
    for this_output_digit in range(input_length):
        # generate an appropriate pattern array 
        pattern_object = PatternIterator(this_output_digit)
        pattern_iterator = iter(pattern_object)
        raw_results = [next(pattern_iterator) * phase_input[i] for i in range(input_length)]
        summed_result = sum(raw_results)
        abs_summed_result = abs(summed_result)
        last_digit = abs_summed_result % 10
        #print(f"raw result: {raw_results} -> {summed_result} -> {abs_summed_result} -> {last_digit}")
        result.append(last_digit)
    return result

def apply_one_fft_fast(phase_input, phase_number):
    """
    Do one full execution of the looping 
    """
    result = []
    input_length = len(phase_input)
    for this_output_digit in range(input_length):
        if 0 == this_output_digit % 100:
            print(f"doing digit {this_output_digit} in phase  {phase_number}")
        # this output digit 0..size of the input 
        # phase_number is 1..100 
        # ok, so use some faster maths to add up these values 
        # not convinced that this is enough, but worth a shot initially
        # so.. we have a repeating pattern where we start by ignoring x characters 
        # pattern is 0, 1, 0, -1.. and given abs we're doing..
        # 0, 1, 0, 1...
        # so far so hoopy..
        # and now we always skip the first option, which is harmless because it's always 0
        # so we can ignore that
        # realistically we're talking about.. skip x, sum x, skip x, sum x.. repeat until we're out of values
        # so... 
        # x is this_output_digit
        # actually.. this isn't the case where this_output_digit is 0 - in that case we  
        # and then we pop into a rhythm of summing the values in batches of this_output_digit
        # and skipping this_output_digits' worth of values.. until then end 
        # 
        # however.. the -1 / +1 thing is a problem..
        # so we do need to flip that sign each time..
        first_useful_value = this_output_digit
        chunk_size = this_output_digit + 1
        current_position = first_useful_value
        sign = 1
        # loop through this chunk using sum
        total = 0
        while current_position < input_length:
            # add this chunk 
            this_bit = sign * sum(phase_input[current_position:current_position + chunk_size])
            #print(f"Adding from {current_position}:{current_position + chunk_size} with sign {sign} -> {this_bit}")
            total += this_bit 
            sign *= -1
            # increment and skip the 0 values
            current_position += chunk_size * 2
        # and go looping
        #print(f"final for digit {this_output_digit} is {total}")
        the_value = abs(total) % 10  
        result.append(the_value)
    return result




from datetime import datetime 
# loop the phases as required 
def apply_fft(input_signal, phases_to_execute):
    phase_input = input_signal
    for this_phase in range(1, phases_to_execute + 1):
        phase_output = apply_one_fft_fast(phase_input, this_phase) 
        #print(f"After {this_phase:03}) {phase_output}")
        print(f"{datetime.now()} completed {this_phase} -> {phase_output}")
        phase_input = phase_output
    return phase_output



def run_fft_cycle(input, copies, phases_to_execute):
    signal = [int(x) for x in input]
    combo_signal = signal * copies
    print(f"Input is : {combo_signal}")
    result = apply_fft(combo_signal, phases_to_execute)
    formatted = "".join([str(x) for x in result])
    print(f"After {phases_to_execute} phases: {formatted}")
    print(f"First 7 are : {formatted[:7]}")
    offset_for_answer = int(formatted[:7])
    print(f"Getting results from offset {offset_for_answer}")
    answer = formatted[offset_for_answer:offset_for_answer+8]
    print(f"Answer is: {answer}")
    return answer


test_input_4_01029498 = '12345678'
test_input_100_24176176 = '80871224585914546619083218645595'
test_input_100_73745418 = '19617804207202209144916044189917'
test_input_100_52432133 = '69317163492948606335995924319873'
puzzle_input = '59717238168580010599012527510943149347930742822899638247083005855483867484356055489419913512721095561655265107745972739464268846374728393507509840854109803718802780543298141398644955506149914796775885246602123746866223528356493012136152974218720542297275145465188153752865061822191530129420866198952553101979463026278788735726652297857883278524565751999458902550203666358043355816162788135488915722989560163456057551268306318085020948544474108340969874943659788076333934419729831896081431886621996610143785624166789772013707177940150230042563041915624525900826097730790562543352690091653041839771125119162154625459654861922989186784414455453132011498'

def do_it_faster(base_pattern, repeat_count, iterations):
    # so it looks like, according to the internet, in this particular pattern we are only interested in values
    # after our target value for some reason. It is unclear to me why this would be so we might need to have a 
    # think about that later or ask an adult 
    pattern = [int(x) for x in base_pattern] * repeat_count
    offset = int(base_pattern[:7])
    full_length = len(pattern)
    print(f"Offset is {offset}, full_length={full_length}")
    # so that already makes it much smaller..
    for this_iteration in range(iterations):
        partial_sum = sum(pattern[offset:full_length])
        for target_idx in range(offset, full_length):
            t = partial_sum
            partial_sum -= pattern[target_idx]
            pattern[target_idx] = abs(t) % 10
    print(pattern[offset:offset + 8])


#test_10k_100_84462026 = '03036732577212944063491565474664'
#  02935109699940807407585447034323 becomes 78725270.
#  03081770884921959731165446850517 becomes 53553731.
#  After repeating your input signal 10000 times and running 100 phases of FFT, 


#run_fft_cycle(test_input_100_52432133, 10000, 100)
#run_fft_cycle("11111111", 10, 10)

do_it_faster(puzzle_input, 10000, 100)

