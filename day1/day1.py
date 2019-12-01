# The Elves quickly load you into a spacecraft and prepare to launch.
# 
# At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. 
# They haven't determined the amount of fuel required yet.
# 
# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, 
#   take its mass, 
#   divide by three, 
#   round down, 
#   and subtract 2.
# 
# For example:
# 
# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
# The Fuel Counter-Upper needs to know the total fuel requirement. 
# 
# To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), 
# then add together all the fuel values.
# 
# What is the sum of the fuel requirements for all of the modules on your spacecraft?
# 
import math
import pandas as pd

def calculate_fuel_for_mass(mass):
    a = mass / 3.0 
    b = math.floor(a)
    c = b - 2
    return c

#
#  This could have been a loop, but there are very few test cases
#
print("sanity checking fuel calculation function")
assert 2 == calculate_fuel_for_mass(12), "incorrect result for mass of 2"
assert 2 == calculate_fuel_for_mass(14), "incorrect result for mass of 14"
assert 654 == calculate_fuel_for_mass(1969), "incorrect result for mass of 1969"
assert 33583 == calculate_fuel_for_mass(100756), "incorrect result for mass of 100756"
print("fuel calculation function ok")

#
#  The puzzle states that we need to calculate the individual mass values for 
#  the modules and then sum them.
#

# My puzzle file has 100 values in it, called puzzle_input.txt 
input_filename = 'day1/puzzle_input.txt'
df = pd.read_csv(input_filename, header = None, names=['mass'])
print(df.head())

# So now we have a data frame with Mass as the only column..
df['fuel'] = df.apply(lambda row: calculate_fuel_for_mass(row.mass), axis=1)
print(df.head())

# We now have a data frame with mass and fuel columns, so we need to sum the fuel column
total_fuel = df.fuel.sum()
print(f"Total Fuels is {total_fuel}")


