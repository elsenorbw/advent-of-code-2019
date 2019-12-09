#
#  Use all the test programs to make sure that we don't break things while making changes 
#

from .engine import ComputeEngine




def test_large_number():
    program_code = "104,1125899906842624,99"
    c = ComputeEngine(program_code)
    c.run(True)
    the_output = c.output_buffer
    assert(len(the_output) == 1)
    assert(the_output[0] == 1125899906842624)


def test_16_digit_number():
    program_code = "1102,34915192,34915192,7,4,7,99,0"
    c = ComputeEngine(program_code)
    c.run(True)
    the_output = c.output_buffer
    assert(len(the_output) == 1)
    assert(len(f"{the_output[0]}") == 16)

# test the addressing 
def test_addressing_positional():
    program_code = "1,7,8,9,4,9,99,18,20"
    # output should be 38 
    c = ComputeEngine(program_code)
    c.run(True)
    the_output = c.output_buffer
    assert(len(the_output) == 1)
    assert(38 == the_output[0])
    assert(38 == c.peek(9))

#def test_addressing_relational():
#    program_code = "201  7 8 "
