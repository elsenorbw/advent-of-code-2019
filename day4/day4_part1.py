#  --- Day 4: Secure Container ---
#  You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.
#  
#  However, they do remember a few key facts about the password:
#  
#  It is a six-digit number.
#  The value is within the range given in your puzzle input.
#  Two adjacent digits are the same (like 22 in 122345).
#  Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
#  Other than the range rule, the following are true:
#  
#  111111 meets these criteria (double 11, never decreases).
#  223450 does not meet these criteria (decreasing pair of digits 50).
#  123789 does not meet these criteria (no double).
#  How many different passwords within the range given in your puzzle input meet these criteria?
#  
#  Your puzzle input is 240920-789857.

#
#  Ok, so a key-space reduction problem. We can work on individual digits to limit the space 
#  if the one to the left is 5 then the space for this digit it 5-9 
#  also, in the first and last cases we can discount anything less than max(left_digit, my_max)
#  and in the last case, the ceiling isn't 9, it's whatever my max is 
#

#
#  So this turns into some very nested loops, there may be something clever we can do around moving doubles 
#  down the list, will have to think about that.
#

def count_possible_passwords(my_index,               # which digit are we processing  
                             previous_digit,         # what is the previous digit in this iteration
                             all_previous_are_min,   # are all the previous digits their minimum possible values
                             all_previous_are_max,   # are all the previous digits their maximum possible values
                             already_has_double,     # have we already seen a double in the sequence ?
                             min_digit_vals,         # the list of minimum values (avoiding a global)
                             max_digit_vals,         # the list of maximum values (avoiding another global)
                             final_index):           # the final index in the list - to know when to stop quickly
    """
    Handle the logic for one single digit 
    """
    # ok, so this value can loop from (by default) the previous digit value until 9 
    my_acceptable_min = previous_digit
    my_acceptable_max = 9 
    # unless we are in the minimum case, in which case it must be the larger of the normal min 
    # and the starting min for this position (i.e. if the minimum value is 17, we have to start at 7 for the second digit if 1 is)
    if all_previous_are_min:
        my_acceptable_min = max(my_acceptable_min, min_digit_vals[my_index])

    # we also have an exception on the top end, as if this is the max value and our max digit is 5 then that's 
    # where we need to stop 
    if all_previous_are_max:
        my_acceptable_max = max_digit_vals[my_index]  # no need for a min() here, the max digit can never be more than 9

    # right - is this the last digit in the list ?
    is_last_digit = (my_index == final_index) 
    if is_last_digit:
        #
        #  ok, we're the last digit, so two options - 
        #    either we have had a double already, in which case the full range will be acceptable passwords
        #    or we have had no double so far and only a maximum of one will be (it's possible that the 
        #               our range does not encompass the previous digit value, making a double impossible)
        #
        if already_has_double:
            # calculate how many numbers are in the acceptable range and return that as the answer
            result = my_acceptable_max - my_acceptable_min + 1
        else:
            # can we make a double in this final digit ?
            if previous_digit >= my_acceptable_min and previous_digit <= my_acceptable_max:
                result = 1
            else:
                result = 0
    else: 
        # ok, this is not the last digit, we need to loop and add up the down-stream results
        # so, we have the min and max values.. 
        # generate the downstream parameters and call them 
        result = 0
        print(f"Level {my_index} processing digits {my_acceptable_min} to {my_acceptable_max}")
        for this_digit in range(my_acceptable_min, my_acceptable_max + 1):
            new_index = my_index + 1  # child index will be one more than this one
            previous_min_flag = (all_previous_are_min and this_digit == min_digit_vals[my_index])
            previous_max_flag = (all_previous_are_max and this_digit == max_digit_vals[my_index])
            now_has_double = (already_has_double or previous_digit == this_digit)
            result += count_possible_passwords(new_index, 
                                              this_digit, 
                                              previous_min_flag,
                                              previous_max_flag,
                                              now_has_double,
                                              min_digit_vals,
                                              max_digit_vals,
                                              final_index)
    print(f"count_possible_passwords({my_index}, {previous_digit}, {all_previous_are_min}, {all_previous_are_max}, {already_has_double}) -> {result}")
    return result


def find_possible_passwords(min_val, max_val):
    """
    Return a count of all the passwords between the range provided which meet the rules:
      digits must never decrease from left to right
      must contain at least one double
    """
    # chop the passwords up into arrays of single digits 
    min_digit_vals = [int(x) for x in str(min_val)]
    max_digit_vals = [int(x) for x in str(max_val)]
    print(f"{min_digit_vals} -> {min_val}")
    print(f"{max_digit_vals} -> {max_val}")

    # right start the recursive magic, I think this has to be the way to go although the problem 
    # does specify a fixed length, so potentially that's a winner, let's see 
    result = 0;
    for starting_digit in range(min_digit_vals[0], max_digit_vals[0] + 1):
        # do the recusrive magic with the remaining digits 
        result += count_possible_passwords(1,               # which digit are we processing  
                              starting_digit,         # what is the previous digit in this iteration
                              starting_digit == min_digit_vals[0],   # are all the previous digits their minimum possible values
                              starting_digit == max_digit_vals[0],   # are all the previous digits their maximum possible values
                              False,     # have we already seen a double in the sequence ?
                              min_digit_vals,         # the list of minimum values (avoiding a global)
                              max_digit_vals,         # the list of maximum values (avoiding another global)
                              len(max_digit_vals) - 1)           # the final index in the list - to know when to stop quickly
    return result;



puzzle_min = 240920
puzzle_max = 789857
test_min = 123
test_max = 456
#total_passwords = find_possible_passwords(test_min, test_max)
total_passwords = find_possible_passwords(puzzle_min, puzzle_max)

print(f"{total_passwords} total potential passwords")





