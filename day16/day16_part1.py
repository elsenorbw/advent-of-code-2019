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


# loop the phases as required 
def apply_fft(input_signal, phases_to_execute):
    phase_input = input_signal
    for this_phase in range(1, phases_to_execute + 1):
        phase_output = apply_one_fft(phase_input, this_phase) 
        print(f"After {this_phase:03}) {phase_output}")
        phase_input = phase_output
    return phase_output



def run_fft_cycle(input, phases_to_execute):
    signal = [int(x) for x in input]
    print(f"Input is : {signal}")
    result = apply_fft(signal, phases_to_execute)
    formatted = "".join([str(x) for x in result])
    print(f"After {phases_to_execute} phases: {formatted}")
    print(f"First 8 are : {formatted[:8]}")
    return result



test_input_4_01029498 = '12345678'
test_input_100_24176176 = '80871224585914546619083218645595'
test_input_100_73745418 = '19617804207202209144916044189917'
test_input_100_52432133 = '69317163492948606335995924319873'
puzzle_input = '59717238168580010599012527510943149347930742822899638247083005855483867484356055489419913512721095561655265107745972739464268846374728393507509840854109803718802780543298141398644955506149914796775885246602123746866223528356493012136152974218720542297275145465188153752865061822191530129420866198952553101979463026278788735726652297857883278524565751999458902550203666358043355816162788135488915722989560163456057551268306318085020948544474108340969874943659788076333934419729831896081431886621996610143785624166789772013707177940150230042563041915624525900826097730790562543352690091653041839771125119162154625459654861922989186784414455453132011498'

#run_fft_cycle(test_input_4_01029498, 4)
run_fft_cycle(puzzle_input, 100)