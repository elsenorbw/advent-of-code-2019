#  --- Day 6: Universal Orbit Map ---
#  You've landed at the Universal Orbit Map facility on Mercury. Because navigation in space often involves transferring between orbits, the orbit maps here are useful for finding efficient routes between, for example, you and Santa. You download a map of the local orbits (your puzzle input).
#  
#  Except for the universal Center of Mass (COM), every object in space is in orbit around exactly one other object. An orbit looks roughly like this:
#  
#                    \
#                     \
#                      |
#                      |
#  AAA--> o            o <--BBB
#                      |
#                      |
#                     /
#                    /
#  In this diagram, the object BBB is in orbit around AAA. The path that BBB takes around AAA (drawn with lines) is only partly shown. In the map data, this orbital relationship is written AAA)BBB, which means "BBB is in orbit around AAA".
#  
#  Before you use your map data to plot a course, you need to make sure it wasn't corrupted during the download. To verify maps, the Universal Orbit Map facility uses orbit count checksums - the total number of direct orbits (like the one shown above) and indirect orbits.
#  
#  Whenever A orbits B and B orbits C, then A indirectly orbits C. This chain can be any number of objects long: if A orbits B, B orbits C, and C orbits D, then A indirectly orbits D.
#  
#  For example, suppose you have the following map:
#  
#  COM)B
#  B)C
#  C)D
#  D)E
#  E)F
#  B)G
#  G)H
#  D)I
#  E)J
#  J)K
#  K)L
#  Visually, the above map of orbits looks like this:
#  
#          G - H       J - K - L
#         /           /
#  COM - B - C - D - E - F
#                 \
#                  I
#  In this visual representation, when two objects are connected by a line, the one on the right directly orbits the one on the left.
#  
#  Here, we can count the total number of orbits as follows:
#  
#  D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
#  L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a total of 7 orbits.
#  COM orbits nothing.
#  The total number of direct and indirect orbits in this example is 42.
#  
#  What is the total number of direct and indirect orbits in your map data?
#  
#  Your puzzle answer was 621125.
#  
#  The first half of this puzzle is complete! It provides one gold star: *
#  
#  --- Part Two ---
#  Now, you just need to figure out how many orbital transfers you (YOU) need to take to get to Santa (SAN).
#  
#  You start at the object YOU are orbiting; your destination is the object SAN is orbiting. An orbital transfer lets you move from any object to an object orbiting or orbited by that object.
#  
#  For example, suppose you have the following map:
#  
#  COM)B
#  B)C
#  C)D
#  D)E
#  E)F
#  B)G
#  G)H
#  D)I
#  E)J
#  J)K
#  K)L
#  K)YOU
#  I)SAN
#  Visually, the above map of orbits looks like this:
#  
#                            YOU
#                           /
#          G - H       J - K - L
#         /           /
#  COM - B - C - D - E - F
#                 \
#                  I - SAN
#  In this example, YOU are in orbit around K, and SAN is in orbit around I. To move from K to I, a minimum of 4 orbital transfers are required:
#  
#  K to J
#  J to E
#  E to D
#  D to I
#  Afterward, the map of orbits looks like this:
#  
#          G - H       J - K - L
#         /           /
#  COM - B - C - D - E - F
#                 \
#                  I - SAN
#                   \
#                    YOU
#  What is the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting? (Between the objects they are orbiting - not between YOU and SAN.)

class planet:
    def __init__(self, name):
        self.name = name 
        self.moons = []
        self.sun = None
    
    def __repr__(self):
        return f"{self.name} ({self.get_orbit_count()})"

    def add_moon(self, moon):
        self.moons.append(moon)

    def set_sun(self, sun):
        if self.sun is not None:
            raise ValueError(f"{self.name} trying to set a second sun value of {sun.name}")
        self.sun = sun 

    def get_all_suns(self):
        """ Return a list of all suns """
        result = []
        current_planet = self.sun 
        while current_planet is not None:
            result.append(current_planet)
            current_planet = current_planet.sun 
        return result

    def get_orbit_count(self):
        """ Return how many direct and indirect orbits this planet has """
        direct_orbits = 0
        indirect_orbits = 0
        if self.sun is not None:
            direct_orbits = 1
            parent_a, parent_b = self.sun.get_orbit_count()
            indirect_orbits = parent_a + parent_b
        return direct_orbits, indirect_orbits


#
#  ok, read through the whole list and add each one with their relationships
#
def read_input_to_universe(filename):
    universe = {}
    with open(filename, 'r') as f:
        for this_line in f:
            this_line = this_line.strip()
            if '' != this_line:
                # line format is Sun)Moon 
                objects = this_line.split(')')
                if 2 != len(objects):
                    print(f"Weird line: {this_line} - stopping")
                    raise ValueError(f"Weird input line: {this_line}")
                else:
                    sun_name = objects[0]
                    moon_name = objects[1]
                    if sun_name not in universe:
                        universe[sun_name] = planet(sun_name)
                    if moon_name not in universe:
                        universe[moon_name] = planet(moon_name)
                    # add the relationships
                    universe[sun_name].add_moon(universe[moon_name])
                    universe[moon_name].set_sun(universe[sun_name])
    return universe


def find_shortest_orbital_transfer(planet_a, planet_b):
    """ Find the minimum number of transfers to move from a to b """
    # this would be easy with two lists of the planets' suns 
    # first sun which appears in both lists wins 
    suns_for_a = planet_a.get_all_suns()
    suns_for_b = planet_b.get_all_suns()
    print(f"Suns a: {suns_for_a}")
    print(f"Suns b: {suns_for_b}")
    # ok, find the first planet in list a that is also in list b 
    fast_lookup_b = set(suns_for_b)
    idx = 0
    while idx < len(suns_for_a) and suns_for_a[idx] not in fast_lookup_b:
        idx += 1

    # sanity check - did we find a match ?
    if idx >= len(suns_for_a):
        result = None 
    else:
        # we found that sucker - these are already parents so...
        idx_b = suns_for_b.index(suns_for_a[idx])
        trip_length_a = idx + 1 # add one because we are already starting at our first parent 
        trip_length_b = idx_b + 1   # ditto here 
        total_trip_length = trip_length_a + trip_length_b
        print(f"intersection planet is {suns_for_a[idx]} a index: {idx}, b index: {idx_b} - total_trip is {total_trip_length}")
        result = total_trip_length
    return result 

def count_universal_links(universe):
    """
    Count the number of links in the universe including both direct and indirect orbits
    """
    total_direct_orbits = 0
    total_indirect_orbits = 0
    for this_planet in universe.values():
        a, b = this_planet.get_orbit_count()
        total_direct_orbits += a
        total_indirect_orbits += b 
    total_orbits = total_direct_orbits + total_indirect_orbits
    print(f"universe has {total_direct_orbits} direct and {total_indirect_orbits} indirect orbits for a total of {total_orbits}")
    return total_orbits

puzzle_filename = 'puzzle_input.txt'
test_filename = 'example2_input.txt'

universe = read_input_to_universe(puzzle_filename)
#print(f"test_universe {test_universe.values()}")

# get the two planets in question 
my_planet = universe['YOU'].sun 
santas_planet = universe['SAN'].sun

print(f"My planet: {my_planet}")
print(f"Santa's planet: {santas_planet}")

shortest_orbit = find_shortest_orbital_transfer(my_planet, santas_planet)

#link_count = count_universal_links(universe)
#print(f"universe has {len(universe.keys())} planets with {link_count} orbits")

