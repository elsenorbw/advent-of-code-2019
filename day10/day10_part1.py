#   --- Day 10: Monitoring Station ---
#   You fly into the asteroid belt and reach the Ceres monitoring station. The Elves here have an emergency: they're having trouble tracking all of the asteroids and can't be sure they're safe.
#   
#   The Elves would like to build a new monitoring station in a nearby area of space; they hand you a map of all of the asteroids in that region (your puzzle input).
#   
#   The map indicates whether each position is empty (.) or contains an asteroid (#). The asteroids are much smaller than they appear on the map, and every asteroid is exactly in the center of its marked position. The asteroids can be described with X,Y coordinates where X is the distance from the left edge and Y is the distance from the top edge (so the top-left corner is 0,0 and the position immediately to its right is 1,0).
#   
#   Your job is to figure out which asteroid would be the best place to build a new monitoring station. A monitoring station can detect any asteroid to which it has direct line of sight - that is, there cannot be another asteroid exactly between them. This line of sight can be at any angle, not just lines aligned to the grid or diagonally. The best location is the asteroid that can detect the largest number of other asteroids.
#   
#   For example, consider the following map:
#   
#   .#..#
#   .....
#   #####
#   ....#
#   ...##
#   The best location for a new monitoring station on this map is the highlighted asteroid at 3,4 because it can detect 8 asteroids, more than any other location. (The only asteroid it cannot detect is the one at 1,0; its view of this asteroid is blocked by the asteroid at 2,2.) All other asteroids are worse locations; they can detect 7 or fewer other asteroids. Here is the number of other asteroids a monitoring station on each asteroid could detect:
#   
#   .7..7
#   .....
#   67775
#   ....7
#   ...87
#   Here is an asteroid (#) and some examples of the ways its line of sight might be blocked. If there were another asteroid at the location of a capital letter, the locations marked with the corresponding lowercase letter would be blocked and could not be detected:
#   
#   #.........
#   ...A......
#   ...B..a...
#   .EDCG....a
#   ..F.c.b...
#   .....c....
#   ..efd.c.gb
#   .......c..
#   ....f...c.
#   ...e..d..c
#   Here are some larger examples:
#   
#   Best is 5,8 with 33 other asteroids detected:
#   
#   ......#.#.
#   #..#.#....
#   ..#######.
#   .#.#.###..
#   .#..#.....
#   ..#....#.#
#   #..#....#.
#   .##.#..###
#   ##...#..#.
#   .#....####
#   Best is 1,2 with 35 other asteroids detected:
#   
#   #.#...#.#.
#   .###....#.
#   .#....#...
#   ##.#.#.#.#
#   ....#.#.#.
#   .##..###.#
#   ..#...##..
#   ..##....##
#   ......#...
#   .####.###.
#   Best is 6,3 with 41 other asteroids detected:
#   
#   .#..#..###
#   ####.###.#
#   ....###.#.
#   ..###.##.#
#   ##.##.#.#.
#   ....###..#
#   ..#.#..#.#
#   #..#.#.###
#   .##...##.#
#   .....#.#..
#   Best is 11,13 with 210 other asteroids detected:
#   
#   .#..##.###...#######
#   ##.############..##.
#   .#.######.########.#
#   .###.#######.####.#.
#   #####.##.#.##.###.##
#   ..#####..#.#########
#   ####################
#   #.####....###.#.#.##
#   ##.#################
#   #####.##.###..####..
#   ..######..##.#######
#   ####.##.####...##..#
#   .#####..#.######.###
#   ##...#.##########...
#   #.##########.#######
#   .####.#.###.###.#.##
#   ....##.##.###..#####
#   .#.#.###########.###
#   #.#.#.#####.####.###
#   ###.##.####.##.#..##
#   Find the best location for a new monitoring station. How many other asteroids can be detected from that location?
#   
#   To begin, get your puzzle input.

#
#  Right, so the plan is to get everything into an array of x,y while reading it 
#  then, we can calculate the x and y difference between the spot we're interested in and 
#  each target spot to determine the angle in each direction.
#  There is probably a clever, mathsy way of doing this.
#

def read_asteroid_field(filename):
    """ 
    Read a file of rows of dots or hash characters where . is space and # is an asteroid 
    Returns a list of asteroids where each one knows its own x,y coordinates - top-left is 0,0  
    """
    result = []
    with open(filename, 'r') as f:
        current_y = 0
        for this_line in f:
            this_line = this_line.strip()
            if '' != this_line:
                # we are adding one 
                for x_value, this_char in enumerate(this_line):
                    if '#' == this_char:
                        #print(f"Got one at {x_value},{current_y}")
                        result.append((x_value, current_y))

                # next line 
                current_y += 1
    return result


def calculate_trajectory(this_asteroid, target_asteroid):
    """
      return a quadrant (0-3) representing which quarter of the sky the target_asteroid is in 
      and a slope ratio to hit it from here. 
    """
    # calculate the deltas 
    delta_x = target_asteroid[0] - this_asteroid[0]
    delta_y = target_asteroid[1] - this_asteroid[1]
    # first thing, let's make all the values positive 
    quadrant = 0
    if delta_x < 0:
        delta_x = -delta_x
        quadrant += 1
    if delta_y < 0:
        delta_y = -delta_y
        quadrant += 2
    # ok, quadrant sorted, all values are non-negative, calculate the slope 
    # the slope value is defined as how far up the line goes for each out value
    # special case for vertical lines - the value should be infinity 
    slope = -1 # infinity probably has a nice symbol somewhere - find out 
    if 0 != delta_x:
        slope = delta_y / delta_x 
    # done 
    #print(f"{this_asteroid} to {target_asteroid} -> quad={quadrant}, slope={slope}") 
    return quadrant, slope

def find_best_vantage_point(asteroid_field):
    best_location = None
    best_view_count = None 

    # Loop through each of the points, seeing how many other points it can see 
    # going to do this by calculating the slope and which quadrant it is in and 
    # storing those as a unique count. We may need to think about rounding errors, we'll see 
    for this_asteroid in asteroid_field:
        # calculate the unique list of asteroid directions from here 
        detected_asteroids = set()
        for target_asteroid in asteroid_field:
            if target_asteroid != this_asteroid:
                # do the calculation and add to the set 
                quadrant, slope = calculate_trajectory(this_asteroid, target_asteroid)
                detected_asteroids.add((quadrant, slope))
        # right - is this the best so far ?
        print(f"asteroid at {this_asteroid} can see {len(detected_asteroids)}")
        this_view_count = len(detected_asteroids)
        if best_view_count is None or best_view_count < this_view_count:
            best_view_count = this_view_count 
            best_location = this_asteroid

    return best_location, best_view_count 

filename = 'puzzle_input.txt'

field = read_asteroid_field(filename)
print(field)
# and find the best vantage_point 
best_location, view_count = find_best_vantage_point(field)
print(f"best location is {best_location} with a view of {view_count} other asteroids")
