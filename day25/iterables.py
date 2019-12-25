# iterate everything 

from itertools import combinations 

options = ['a', 'b', 'c']
l = list(combinations(options, 3))

print(f"options are : {l}")


def every_combination_of_a_thing(options):
    """
    all the possible combinations of the thing 
    """
    result = list()
    for combo_length in range(1, len(options) + 1):
        this_set_of_combos = list(combinations(options, combo_length))
        result.extend(this_set_of_combos)
    return result 

l = every_combination_of_a_thing(options)
print(f"all combos:{l}")
