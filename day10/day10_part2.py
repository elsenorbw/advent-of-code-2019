#  --- Day 10: Monitoring Station ---
#  You fly into the asteroid belt and reach the Ceres monitoring station. The Elves here have an emergency: they're having trouble tracking all of the asteroids and can't be sure they're safe.
#  
#  The Elves would like to build a new monitoring station in a nearby area of space; they hand you a map of all of the asteroids in that region (your puzzle input).
#  
#  The map indicates whether each position is empty (.) or contains an asteroid (#). The asteroids are much smaller than they appear on the map, and every asteroid is exactly in the center of its marked position. The asteroids can be described with X,Y coordinates where X is the distance from the left edge and Y is the distance from the top edge (so the top-left corner is 0,0 and the position immediately to its right is 1,0).
#  
#  Your job is to figure out which asteroid would be the best place to build a new monitoring station. A monitoring station can detect any asteroid to which it has direct line of sight - that is, there cannot be another asteroid exactly between them. This line of sight can be at any angle, not just lines aligned to the grid or diagonally. The best location is the asteroid that can detect the largest number of other asteroids.
#  
#  For example, consider the following map:
#  
#  .#..#
#  .....
#  #####
#  ....#
#  ...##
#  The best location for a new monitoring station on this map is the highlighted asteroid at 3,4 because it can detect 8 asteroids, more than any other location. (The only asteroid it cannot detect is the one at 1,0; its view of this asteroid is blocked by the asteroid at 2,2.) All other asteroids are worse locations; they can detect 7 or fewer other asteroids. Here is the number of other asteroids a monitoring station on each asteroid could detect:
#  
#  .7..7
#  .....
#  67775
#  ....7
#  ...87
#  Here is an asteroid (#) and some examples of the ways its line of sight might be blocked. If there were another asteroid at the location of a capital letter, the locations marked with the corresponding lowercase letter would be blocked and could not be detected:
#  
#  #.........
#  ...A......
#  ...B..a...
#  .EDCG....a
#  ..F.c.b...
#  .....c....
#  ..efd.c.gb
#  .......c..
#  ....f...c.
#  ...e..d..c
#  Here are some larger examples:
#  
#  Best is 5,8 with 33 other asteroids detected:
#  
#  ......#.#.
#  #..#.#....
#  ..#######.
#  .#.#.###..
#  .#..#.....
#  ..#....#.#
#  #..#....#.
#  .##.#..###
#  ##...#..#.
#  .#....####
#  Best is 1,2 with 35 other asteroids detected:
#  
#  #.#...#.#.
#  .###....#.
#  .#....#...
#  ##.#.#.#.#
#  ....#.#.#.
#  .##..###.#
#  ..#...##..
#  ..##....##
#  ......#...
#  .####.###.
#  Best is 6,3 with 41 other asteroids detected:
#  
#  .#..#..###
#  ####.###.#
#  ....###.#.
#  ..###.##.#
#  ##.##.#.#.
#  ....###..#
#  ..#.#..#.#
#  #..#.#.###
#  .##...##.#
#  .....#.#..
#  Best is 11,13 with 210 other asteroids detected:
#  
#  .#..##.###...#######
#  ##.############..##.
#  .#.######.########.#
#  .###.#######.####.#.
#  #####.##.#.##.###.##
#  ..#####..#.#########
#  ####################
#  #.####....###.#.#.##
#  ##.#################
#  #####.##.###..####..
#  ..######..##.#######
#  ####.##.####...##..#
#  .#####..#.######.###
#  ##...#.##########...
#  #.##########.#######
#  .####.#.###.###.#.##
#  ....##.##.###..#####
#  .#.#.###########.###
#  #.#.#.#####.####.###
#  ###.##.####.##.#..##
#  Find the best location for a new monitoring station. How many other asteroids can be detected from that location?
#  
#  Your puzzle answer was 334.
#  
#  The first half of this puzzle is complete! It provides one gold star: *
#  
#  --- Part Two ---
#  Once you give them the coordinates, the Elves quickly deploy an Instant Monitoring Station to the location and discover the worst: there are simply too many asteroids.
#  
#  The only solution is complete vaporization by giant laser.
#  
#  Fortunately, in addition to an asteroid scanner, the new monitoring station also comes equipped with a giant rotating laser perfect for vaporizing asteroids. The laser starts by pointing up and always rotates clockwise, vaporizing any asteroid it hits.
#  
#  If multiple asteroids are exactly in line with the station, the laser only has enough power to vaporize one of them before continuing its rotation. In other words, the same asteroids that can be detected can be vaporized, but if vaporizing one asteroid makes another one detectable, the newly-detected asteroid won't be vaporized until the laser has returned to the same position by rotating a full 360 degrees.
#  
#  For example, consider the following map, where the asteroid with the new monitoring station (and laser) is marked X:
#  
#  .#....#####...#..
#  ##...##.#####..##
#  ##...#...#.#####.
#  ..#.....X...###..
#  ..#.#.....#....##
#  The first nine asteroids to get vaporized, in order, would be:
#  
#  .#....###24...#..
#  ##...##.13#67..9#
#  ##...#...5.8####.
#  ..#.....X...###..
#  ..#.#.....#....##
#  Note that some asteroids (the ones behind the asteroids marked 1, 5, and 7) won't have a chance to be vaporized until the next full rotation. The laser continues rotating; the next nine to be vaporized are:
#  
#  .#....###.....#..
#  ##...##...#.....#
#  ##...#......1234.
#  ..#.....X...5##..
#  ..#.9.....8....76
#  The next nine to be vaporized are then:
#  
#  .8....###.....#..
#  56...9#...#.....#
#  34...7...........
#  ..2.....X....##..
#  ..1..............
#  Finally, the laser completes its first full rotation (1 through 3), a second rotation (4 through 8), and vaporizes the last asteroid (9) partway through its third rotation:
#  
#  ......234.....6..
#  ......1...5.....7
#  .................
#  ........X....89..
#  .................
#  In the large example above (the one with the best monitoring station location at 11,13):
#  
#  The 1st asteroid to be vaporized is at 11,12.
#  The 2nd asteroid to be vaporized is at 12,1.
#  The 3rd asteroid to be vaporized is at 12,2.
#  The 10th asteroid to be vaporized is at 12,8.
#  The 20th asteroid to be vaporized is at 16,0.
#  The 50th asteroid to be vaporized is at 16,9.
#  The 100th asteroid to be vaporized is at 10,16.
#  The 199th asteroid to be vaporized is at 9,6.
#  The 200th asteroid to be vaporized is at 8,2.
#  The 201st asteroid to be vaporized is at 10,9.
#  The 299th and final asteroid to be vaporized is at 11,1.
#  The Elves are placing bets on which will be the 200th asteroid to be vaporized. Win the bet by determining which asteroid that will be; what do you get if you multiply its X coordinate by 100 and then add its Y coordinate? (For example, 8,2 becomes 802.)
#  
#  Although it hasn't changed, you can still get your puzzle input.

# right - so lots of things are hopefully reusable here, but we're going to have to add lists 
# thinking about it, we need to order these things by angle starting at the top and heading clock-wise
# each spot in the ordered list needs to be able to contain a list of items and a distance, ordered by distance 
# so we could get, for example : 
#
#  0 degrees: (x1, y1, d1), (x2, y2, d2), (x3, y3, d3)
#  12 degrees: (x4, y4, d4), (x5, y5, d5)
#  241 degrees: (x6, y6, d6)
#
#  At that point we can simply walk through the list popping off the first one in the list each time:
#  Destruction order: (x1, y1, d1), (x4, y4, d4), (x6, y6, d6), (x2, y2, d2), (x5, y5, d5), (x3, y3, d3) 
#
#  So.. first thing first, we need to know how to calculate the angle from origin of a given object:
#  google says it's : 
#
#  <no internet at the moment>
#  
#  ok - doing the rest of the work based on some shoddy imaginary math function which can be pumped up later
#
#
import math

def rotational_angle_to(source_x, source_y, target_x, target_y):
    """
    This generates the angle between a vertical line straight up from origin - 
    which is to say is source_x, source_y -> source_x, source_y - 20000 in a universe where 0,0 is top left
    The return should be the angle and then the distance to travel (needed for sorting later)
    """
    calculated_angle = 0
    calculated_distance = 0

    x_diff = target_x - source_x
    y_diff = target_y - source_y

    # this needs fixing..
    rads = math.atan2(y_diff, x_diff)
    degrees = rads * (180.0 / math.pi)
    calculated_angle = (degrees + 90 + 360) % 360
    calculated_distance = math.sqrt((x_diff ** 2) + (y_diff ** 2))

    return calculated_angle, calculated_distance


def generate_hit_list(asteroid_field, base_asteroid):
    """
    Return a list of objects where (degrees, distance, x, y) are the values
    """
    result = list()
    base_x = base_asteroid[0]
    base_y = base_asteroid[1]
    for target_asteroid in asteroid_field:
        if target_asteroid != base_asteroid:
            # do the calculation and add to the set 
            this_x, this_y = target_asteroid
            this_angle, this_distance = rotational_angle_to(base_x, base_y, this_x, this_y)
            result.append((this_angle, this_distance, this_x, this_y))
    return result

def compare_asteroid_info(item1, item2):
    if item1[1] < item2[1]:
        result = -1
    elif item1[1] > item2[1]:
        result = 1
    else:
        result = 0
    return result

def hit_list_to_tree(all_asteroids):
    """
    Return a dictionary of sorted lists where the nearest objects are first 
    """
    result = {}
    for this_asteroid in all_asteroids:
        the_angle = this_asteroid[0]
        the_distance = this_asteroid[1]
        if the_angle not in result:
            result[the_angle] = []
        result[the_angle].append(this_asteroid)

    # and now sort the lists..
    from functools import cmp_to_key
    for this_angle in result.keys():
        result[this_angle] = sorted(result[this_angle], key=cmp_to_key(compare_asteroid_info))
    return result


def blow_up_everything(hit_tree):
    result = []

    while(0 < len(hit_tree.keys())):
        # loop through the remaining keys in order 
        for this_angle in sorted(hit_tree.keys()):
            # grab the first asteroid in the list
            result.append(hit_tree[this_angle][0])
            # now either trim the list or delete the key 
            if 1 == len(hit_tree[this_angle]):
                del hit_tree[this_angle]
            else:
                hit_tree[this_angle] = hit_tree[this_angle][1:]

    return result

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
        # print(f"asteroid at {this_asteroid} can see {len(detected_asteroids)}")
        this_view_count = len(detected_asteroids)
        if best_view_count is None or best_view_count < this_view_count:
            best_view_count = this_view_count 
            best_location = this_asteroid

    return best_location, best_view_count 

filename = 'puzzle_input.txt'
#filename = 'test_11_13.txt'

field = read_asteroid_field(filename)
print(field)
# and find the best vantage_point 
best_location, view_count = find_best_vantage_point(field)
print(f"best location is {best_location} with a view of {view_count} other asteroids")

# ok, now we need to run the destruction laser routine - at this point we need to process the 
# asteroid field from the point of view of the best vantage point and generate a list of 
# degrees, distance, x, y  which we can then sort into shape. Small data, no memory limitations
# so clarity over memory efficiency I think 

hit_list = generate_hit_list(field, best_location)
print(f"Hit list is {hit_list}")
hit_tree = hit_list_to_tree(hit_list)
for a in sorted(hit_tree):
    print(f"Hit tree {a} is {hit_tree[a]}")

# and now blow them up in order..
blown_up_asteroids = blow_up_everything(hit_tree)
print(f"blown up list:")
for index, this_asteroid in enumerate(blown_up_asteroids, start=1):
    print(f"{index:03}) {this_asteroid}") 
