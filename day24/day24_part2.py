#  
#  
#  --- Day 24: Planet of Discord ---
#  You land on Eris, your last stop before reaching Santa. As soon as you do, your sensors start picking 
#  up strange life forms moving around: Eris is infested with bugs! With an over 24-hour roundtrip for 
#  messages between you and Earth, you'll have to deal with this problem on your own.
#  
#  Eris isn't a very large place; a scan of the entire area fits into a 5x5 grid (your puzzle input). 
#  The scan shows bugs (#) and empty spaces (.).
#  
#  Each minute, The bugs live and die based on the number of bugs in the four adjacent tiles:
#  
#  A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
#  An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
#  Otherwise, a bug or empty space remains the same. (Tiles on the edges of the grid have fewer than 
#  four adjacent tiles; the missing tiles count as empty space.) This process happens in every location 
#  simultaneously; that is, within the same minute, the number of adjacent bugs is counted for every tile 
#  first, and then the tiles are updated.
#  
#  Here are the first few minutes of an example scenario:
#  
#  Initial state:
#  ....#
#  #..#.
#  #..##
#  ..#..
#  #....
#  
#  After 1 minute:
#  #..#.
#  ####.
#  ###.#
#  ##.##
#  .##..
#  
#  After 2 minutes:
#  #####
#  ....#
#  ....#
#  ...#.
#  #.###
#  
#  After 3 minutes:
#  #....
#  ####.
#  ...##
#  #.##.
#  .##.#
#  
#  After 4 minutes:
#  ####.
#  ....#
#  ##..#
#  .....
#  ##...
#  To understand the nature of the bugs, watch for the first time a layout of bugs and empty spaces 
#  matches any previous layout. In the example above, the first layout to appear twice is:
#  
#  .....
#  .....
#  .....
#  #....
#  .#...
#  To calculate the biodiversity rating for this layout, consider each tile left-to-right in the top row, 
#  then left-to-right in the second row, and so on. Each of these tiles is worth biodiversity points equal 
#  to increasing powers of two: 1, 2, 4, 8, 16, 32, and so on. Add up the biodiversity points for tiles with 
#  bugs; in this example, the 16th tile (32768 points) and 22nd tile (2097152 points) have bugs, a total 
#  biodiversity rating of 2129920.
#  
#  What is the biodiversity rating for the first layout that appears twice?
#  
#  Your puzzle answer was 28615131.
#  
#  The first half of this puzzle is complete! It provides one gold star: *
#  
#  --- Part Two ---
#  After careful analysis, one thing is certain: you have no idea where all these bugs are coming from.
#  
#  Then, you remember: Eris is an old Plutonian settlement! Clearly, the bugs are coming from 
#  recursively-folded space.
#  
#  This 5x5 grid is only one level in an infinite number of recursion levels. The tile in the middle of 
#  the grid is actually another 5x5 grid, the grid in your scan is contained as the middle tile of a 
#  larger 5x5 grid, and so on. Two levels of grids look like this:
#  
#       |     |         |     |     
#       |     |         |     |     
#       |     |         |     |     
#  -----+-----+---------+-----+-----
#       |     |         |     |     
#       |     |         |     |     
#       |     |         |     |     
#  -----+-----+---------+-----+-----
#       |     | | | | | |     |     
#       |     |-+-+-+-+-|     |     
#       |     | | | | | |     |     
#       |     |-+-+-+-+-|     |     
#       |     | | |?| | |     |     
#       |     |-+-+-+-+-|     |     
#       |     | | | | | |     |     
#       |     |-+-+-+-+-|     |     
#       |     | | | | | |     |     
#  -----+-----+---------+-----+-----
#       |     |         |     |     
#       |     |         |     |     
#       |     |         |     |     
#  -----+-----+---------+-----+-----
#       |     |         |     |     
#       |     |         |     |     
#       |     |         |     |     
#  (To save space, some of the tiles are not drawn to scale.) Remember, this is only a small part of the 
# infinitely recursive grid; there is a 5x5 grid that contains this diagram, and a 5x5 grid that contains 
#  that one, and so on. Also, the ? in the diagram contains another 5x5 grid, which itself contains another 
#  5x5 grid, and so on.
#  
#  The scan you took (your puzzle input) shows where the bugs are on a single level of this structure. 
#  The middle tile of your scan is empty to accommodate the recursive grids within it. Initially, no other 
#  levels contain bugs.
#  
#  Tiles still count as adjacent if they are directly up, down, left, or right of a given tile. Some tiles 
#  have adjacent tiles at a recursion level above or below its own level. For example:
#  
#       |     |         |     |     
#    1  |  2  |    3    |  4  |  5  
#       |     |         |     |     
#  -----+-----+---------+-----+-----
#       |     |         |     |     
#    6  |  7  |    8    |  9  |  10 
#       |     |         |     |     
#  -----+-----+---------+-----+-----
#       |     |A|B|C|D|E|     |     
#       |     |-+-+-+-+-|     |     
#       |     |F|G|H|I|J|     |     
#       |     |-+-+-+-+-|     |     
#   11  | 12  |K|L|?|N|O|  14 |  15 
#       |     |-+-+-+-+-|     |     
#       |     |P|Q|R|S|T|     |     
#       |     |-+-+-+-+-|     |     
#       |     |U|V|W|X|Y|     |     
#  -----+-----+---------+-----+-----
#       |     |         |     |     
#   16  | 17  |    18   |  19 |  20 
#       |     |         |     |     
#  -----+-----+---------+-----+-----
#       |     |         |     |     
#   21  | 22  |    23   |  24 |  25 
#       |     |         |     |     
#  Tile 19 has four adjacent tiles: 14, 18, 20, and 24.
#  Tile G has four adjacent tiles: B, F, H, and L.
#  Tile D has four adjacent tiles: 8, C, E, and I.
#  Tile E has four adjacent tiles: 8, D, 14, and J.
#  Tile 14 has eight adjacent tiles: 9, E, J, O, T, Y, 15, and 19.
#  Tile N has eight adjacent tiles: I, O, S, and five tiles within the sub-grid marked ?.
#  The rules about bugs living and dying are the same as before.
#  
#  For example, consider the same initial state as above:
#  
#  ....#
#  #..#.
#  #.?##
#  ..#..
#  #....
#  The center tile is drawn as ? to indicate the next recursive grid. Call this level 0; the grid within this one is level 1, and the grid that contains this one is level -1. Then, after ten minutes, the grid at each level would look like this:
#  
#  Depth -5:
#  ..#..
#  .#.#.
#  ..?.#
#  .#.#.
#  ..#..
#  
#  Depth -4:
#  ...#.
#  ...##
#  ..?..
#  ...##
#  ...#.
#  
#  Depth -3:
#  #.#..
#  .#...
#  ..?..
#  .#...
#  #.#..
#  
#  Depth -2:
#  .#.##
#  ....#
#  ..?.#
#  ...##
#  .###.
#  
#  Depth -1:
#  #..##
#  ...##
#  ..?..
#  ...#.
#  .####
#  
#  Depth 0:
#  .#...
#  .#.##
#  .#?..
#  .....
#  .....
#  
#  Depth 1:
#  .##..
#  #..##
#  ..?.#
#  ##.##
#  #####
#  
#  Depth 2:
#  ###..
#  ##.#.
#  #.?..
#  .#.##
#  #.#..
#  
#  Depth 3:
#  ..###
#  .....
#  #.?..
#  #....
#  #...#
#  
#  Depth 4:
#  .###.
#  #..#.
#  #.?..
#  ##.#.
#  .....
#  
#  Depth 5:
#  ####.
#  #..#.
#  #.?#.
#  ####.
#  .....
#  In this example, after 10 minutes, a total of 99 bugs are present.
#  
#  Starting with your scan, how many bugs are present after 200 minutes?
#  
#  Although it hasn't changed, you can still get your puzzle input.


EMPTY = '.'
BUG = '#'

CAMEFROM_RIGHT = 'right'
CAMEFROM_LEFT = 'left'
CAMEFROM_UP = 'up'
CAMEFROM_DOWN = 'down'

# seems simple..
class ErisLife:
    def __init__(self, width=5, height=5):
        self.grid = dict()
        self.width = width
        self.height = height
        self.min_z = 0
        self.max_z = 0
    
    def is_bug(self, x, y, z):
        """
        Return True if this is a bug 
        """
        result = False
        if BUG == self.get_location(x, y, z):
            result = True
        return result 

    def store(self, x, y, z, value):
        """
        Store value in location x,y,z 
        """
        if x >= self.width or y >= self.height:
            raise ValueError(f"Bad location for store {x},{y},{z}")
        if x == 2 and y ==2:
            raise ValueError(f"Attempting to store in the sacred spot {x}, {y}, {z}")
        self.grid[(x, y, z)] = value

    def load(self, filename):
        """
        load a file with a planet scan
        """
        with open(filename, 'r') as f:
            z = 0 
            y = 0
            for this_line in f:
                this_line = this_line.strip()
                if '' != this_line:
                    # process one line 
                    for x, this_char in enumerate(this_line):
                        if y == 2 and x == 2:
                            pass
                        else:
                            if '.' == this_char:
                                self.store(x, y, z, EMPTY)
                            elif '#' == this_char:
                                self.store(x, y, z, BUG)
                    # next line 
                    y += 1

    def get_location(self, x, y, z, default_value='?'):
        result = default_value
        if (x, y, z) in self.grid:
            result = self.grid[(x, y, z)]
        return result

    def count_one_edge(self, z, came_from):
        """
        Add up all the values on the appropriate edge and return them 
        """
        xmin = 0
        xmax = 4
        ymin = 0 
        ymax = 4 
        # decide which one to limit 
        if CAMEFROM_LEFT == came_from:
            # we need to do the LHS.. so x is limited to 0 
            xmax = 0
        elif CAMEFROM_RIGHT == came_from:
            # we need to do the RHS .. so 4
            xmin = 4 
        elif CAMEFROM_UP == came_from:
            # so we need to do the top row
            ymax = 0
        elif CAMEFROM_DOWN == came_from:
            # or we came from underneath so we need to do the bottom row 
            ymin = 4
        else:
            raise ValueError(f"Came from where ? {came_from}")

        # and add up the result 
        result = 0
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                if self.is_bug(x, y, z):
                    result += 1
        #print(f"count_one_edge: z={z} camefrom={came_from} iterated x={xmin},{xmax} y={ymin},{ymax} result={result}")
        return result 

    def sum_one_bug_square(self, x, y, z, came_from):
        """
        The logic for one square, to avoid duplicating everything a lot.
        """
        result = 0
        # is this square outside the grid boundaries ?
        if x < 0:
            # x is too small, we need to read one level up
            if self.is_bug(1, 2, z - 1):
                result = 1
            #print(f"sum_one_bug_square({x}, {y}, {z} --> reading (1,2,{z-1}) -> {result}") 
        elif x > 4:
            # x is too big, we need to read one up again 
            if self.is_bug(3, 2, z - 1):
                result = 1
            #print(f"sum_one_bug_square({x}, {y}, {z} --> reading (3,2,{z-1}) -> {result}") 
        elif y < 0:
            if self.is_bug(2, 1, z - 1):
                result = 1
        elif y > 4:
            if self.is_bug(2, 3, z - 1):
                result = 1
        elif x == 2 and y == 2:
            # the deep, delving magic here..
            result = self.count_one_edge(z + 1, came_from)
        else:
            if self.is_bug(x, y, z):
                result = 1

        return result 

    def count_bug_neighbours(self, x, y, z):
        """
        Return the count of how many orthagonal neighbours have a bug in them
        Need to add some special, space-foldey rules here..
        Basically, if we read off the edge of the grid then we want to read one level up (z-1) 
        and the appropriate square from 2,2 based on the edge - so if we read off the RHS of level 0 it would be
        looking for 3,2,-1  while reading from the upper edge would read 2,1,-1 - so far so simple..
        Attempts to read 2,2 however are a little more complicated, they read one level down, but they also 
        read the whole side which gives us: 
          Reading 2,2,0 from 1,2 i.e. the RHS is 2,2,0 - we need to read and sum (0,0,1) -> (4,0,1)
        Simple, let's get cracking :)
        """
        result = 0
        # ok, reading to the left 
        result += self.sum_one_bug_square(x - 1, y, z, CAMEFROM_RIGHT)
        result += self.sum_one_bug_square(x + 1, y, z, CAMEFROM_LEFT)
        result += self.sum_one_bug_square(x, y - 1, z, CAMEFROM_DOWN)
        result += self.sum_one_bug_square(x, y + 1, z, CAMEFROM_UP)
        return result 

    def count_total_bugs(self):
        """
        calculate how many bugs now exist 
        """
        result = 0
        for contents in self.grid.values():
            if BUG == contents:
                result += 1
        return result 

    def print(self):
        """
        Show the grid 
        """
        for z in range(self.min_z, self.max_z + 1):
            print(f"Grid {z}")    
            for y in range(self.height):
                s = ''
                for x in range(self.width):
                    if x == 2 and y == 2:
                        s += '?'
                    else:
                        s += self.get_location(x, y, z)
                print(s)
            print("\n")
        # and finally, the total bug count 
        print(f"Total Bugs: {self.count_total_bugs()}\n\n")


    def evolve(self):
        """
        Run one day of life..
        """
        # new day, new potential grid
        min_z = self.min_z
        max_z = self.max_z 

        # now iterate all of the potential grids doing all of the logic
        next_grid = dict()
        for z in range(self.min_z - 1, self.max_z + 2):
            for x in range(self.width):
                for y in range(self.height):
                    if x == 2 and y == 2:
                        # we just never do this square 
                        pass
                    else:
                        # how many neighbours do we have in the current grid ?
                        n = self.count_bug_neighbours(x, y, z)
                        isbug = self.is_bug(x, y, z)
                        # A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
                        if isbug:
                            if 1 != n:
                                isbug = False
                        else:
                            # An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
                            if n in [1, 2]:
                                isbug = True 
                        # store it in the next place
                        next_time = EMPTY
                        if isbug:
                            next_time = BUG  
                            # and remember how deep we are going..
                            min_z = min(min_z, z)
                            max_z = max(max_z, z)
                            
                        next_grid[(x,y,z)] = next_time
                    

        # and over-write the grid all at once  
        self.grid = next_grid
        self.min_z = min_z
        self.max_z = max_z



previous_bio_scores = set()
e = ErisLife()
e.load('puzzle_input.txt')
e.print()

#print(f"is_bug(3, 2, 0) -> {e.is_bug(3, 2, 0)}")

for iteration in range(200):
    e.evolve()


e.print()

