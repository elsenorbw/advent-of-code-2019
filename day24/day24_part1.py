#  --- Day 24: Planet of Discord ---
#  You land on Eris, your last stop before reaching Santa. As soon as you do, your sensors start picking up strange life forms moving around: Eris is infested with bugs! With an over 24-hour roundtrip for messages between you and Earth, you'll have to deal with this problem on your own.
#  
#  Eris isn't a very large place; a scan of the entire area fits into a 5x5 grid (your puzzle input). The scan shows bugs (#) and empty spaces (.).
#  
#  Each minute, The bugs live and die based on the number of bugs in the four adjacent tiles:
#  
#  A bug dies (becoming an empty space) unless there is exactly one bug adjacent to it.
#  An empty space becomes infested with a bug if exactly one or two bugs are adjacent to it.
#  Otherwise, a bug or empty space remains the same. (Tiles on the edges of the grid have fewer than four adjacent tiles; the missing tiles count as empty space.) This process happens in every location simultaneously; that is, within the same minute, the number of adjacent bugs is counted for every tile first, and then the tiles are updated.
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
#  To understand the nature of the bugs, watch for the first time a layout of bugs and empty spaces matches any previous layout. In the example above, the first layout to appear twice is:
#  
#  .....
#  .....
#  .....
#  #....
#  .#...
#  To calculate the biodiversity rating for this layout, consider each tile left-to-right in the top row, then left-to-right in the second row, and so on. Each of these tiles is worth biodiversity points equal to increasing powers of two: 1, 2, 4, 8, 16, 32, and so on. Add up the biodiversity points for tiles with bugs; in this example, the 16th tile (32768 points) and 22nd tile (2097152 points) have bugs, a total biodiversity rating of 2129920.
#  
#  What is the biodiversity rating for the first layout that appears twice?
#  
#  To begin, get your puzzle input.
#  
#  

EMPTY = '.'
BUG = '#'

# seems simple..
class ErisLife:
    def __init__(self, width=5, height=5):
        self.grid = dict()
        self.width = width
        self.height = height

    def value_for_location(self, x, y):
        """
        Calculate the value for a given location
        powers of 2, starting top left (0,0) and increasing..
        so the power of 2 is 2 ^ ((y * width) + x)
        """
        a = y * self.width + x
        result = 2 ** a
        return result
    
    def is_bug(self, x, y):
        """
        Return True if this is a bug 
        """
        result = False
        if BUG == self.get_location(x, y):
            result = True
        return result 

    def store(self, x, y, value):
        """
        Store value in location x,y 
        """
        if x >= self.width or y >= self.height:
            raise ValueError(f"Bad location for store {x},{y}")
        self.grid[(x, y)] = value

    def load(self, filename):
        """
        load a file with a planet scan
        """
        with open(filename, 'r') as f:
            y = 0
            for this_line in f:
                this_line = this_line.strip()
                if '' != this_line:
                    # process one line 
                    for x, this_char in enumerate(this_line):
                        if '.' == this_char:
                            self.store(x, y, EMPTY)
                        elif '#' == this_char:
                            self.store(x, y, BUG)
                    # next line 
                    y += 1

    def get_location(self, x, y, default_value='?'):
        result = default_value
        if (x, y) in self.grid:
            result = self.grid[(x, y)]
        return result

    def count_bug_neighbours(self, x, y):
        """
        Return the count of how many orthagonal neighbours have a bug in them
        """
        result = 0
        if self.is_bug(x - 1, y):
            result += 1
        if self.is_bug(x + 1, y):
            result += 1
        if self.is_bug(x, y - 1):
            result += 1
        if self.is_bug(x, y + 1):
            result += 1
        return result 

    def calculate_biodiversity(self):
        """
        calculate the bio-diversity for this grid 
        """
        result = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.is_bug(x, y):
                    result += self.value_for_location(x, y)
        return result

    def print(self):
        """
        Show the grid 
        """
        for y in range(self.height):
            s = ''
            for x in range(self.width):
                s += self.get_location(x, y)
            print(s)
        print(f"Biodiversity score: {self.calculate_biodiversity()}\n\n")

    def evolve(self):
        """
        Run one day of life..
        """
        next_grid = dict()
        for x in range(self.width):
            for y in range(self.height):
                # how many neighbours do we have in the current grid ?
                n = self.count_bug_neighbours(x, y)
                isbug = self.is_bug(x, y)
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
                next_grid[(x,y)] = next_time
        # and over-write the grid all at once  
        self.grid = next_grid



previous_bio_scores = set()
e = ErisLife()
e.load('puzzle_input.txt')
e.print()
while e.calculate_biodiversity() not in previous_bio_scores:
    previous_bio_scores.add(e.calculate_biodiversity())
    e.evolve()
    e.print()

