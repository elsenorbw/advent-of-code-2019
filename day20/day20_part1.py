#  --- Day 20: Donut Maze ---
#  You notice a strange pattern on the surface of Pluto and land nearby to get a closer look. 
#  Upon closer inspection, you realize you've come across one of the famous space-warping mazes of 
#  the long-lost Pluto civilization!
#  
#  Because there isn't much space on Pluto, the civilization that used to live here thrived by inventing 
#  a method for folding spacetime. Although the technology is no longer understood, mazes like this one 
#  provide a small glimpse into the daily life of an ancient Pluto citizen.
#  
#  This maze is shaped like a donut. Portals along the inner and outer edge of the donut can instantly 
#  teleport you from one side to the other. For example:
#  
#           A           
#           A           
#    #######.#########  
#    #######.........#  
#    #######.#######.#  
#    #######.#######.#  
#    #######.#######.#  
#    #####  B    ###.#  
#  BC...##  C    ###.#  
#    ##.##       ###.#  
#    ##...DE  F  ###.#  
#    #####    G  ###.#  
#    #########.#####.#  
#  DE..#######...###.#  
#    #.#########.###.#  
#  FG..#########.....#  
#    ###########.#####  
#               Z       
#               Z       
#  This map of the maze shows solid walls (#) and open passages (.). Every maze on Pluto has a 
#  start (the open tile next to AA) and an end (the open tile next to ZZ). Mazes on Pluto also have 
#  portals; this maze has three pairs of portals: BC, DE, and FG. When on an open tile next to one 
#  of these labels, a single step can take you to the other tile with the same label. 
#  (You can only walk on . tiles; labels and empty space are not traversable.)
#  
#  One path through the maze doesn't require any portals. 
#  Starting at AA, you could go down 1, right 8, down 12, left 4, and down 1 to reach ZZ, a total of 26 steps.
#  
#  However, there is a shorter path: You could walk from AA to the inner BC portal (4 steps), 
#  warp to the outer BC portal (1 step), walk to the inner DE (6 steps), warp to the outer DE (1 step), 
#  walk to the outer FG (4 steps), warp to the inner FG (1 step), and finally walk to ZZ (6 steps). 
#  In total, this is only 23 steps.
#  
#  Here is a larger example:
#  
#                     A               
#                     A               
#    #################.#############  
#    #.#...#...................#.#.#  
#    #.#.#.###.###.###.#########.#.#  
#    #.#.#.......#...#.....#.#.#...#  
#    #.#########.###.#####.#.#.###.#  
#    #.............#.#.....#.......#  
#    ###.###########.###.#####.#.#.#  
#    #.....#        A   C    #.#.#.#  
#    #######        S   P    #####.#  
#    #.#...#                 #......VT
#    #.#.#.#                 #.#####  
#    #...#.#               YN....#.#  
#    #.###.#                 #####.#  
#  DI....#.#                 #.....#  
#    #####.#                 #.###.#  
#  ZZ......#               QG....#..AS
#    ###.###                 #######  
#  JO..#.#.#                 #.....#  
#    #.#.#.#                 ###.#.#  
#    #...#..DI             BU....#..LF
#    #####.#                 #.#####  
#  YN......#               VT..#....QG
#    #.###.#                 #.###.#  
#    #.#...#                 #.....#  
#    ###.###    J L     J    #.#.###  
#    #.....#    O F     P    #.#...#  
#    #.###.#####.#.#####.#####.###.#  
#    #...#.#.#...#.....#.....#.#...#  
#    #.#####.###.###.#.#.#########.#  
#    #...#.#.....#...#.#.#.#.....#.#  
#    #.###.#####.###.###.#.#.#######  
#    #.#.........#...#.............#  
#    #########.###.###.#############  
#             B   J   C               
#             U   P   P               
#  Here, AA has no direct path to ZZ, but it does connect to AS and CP. 
#  By passing through AS, QG, BU, and JO, you can reach ZZ in 58 steps.
#  
#  In your maze, how many steps does it take to get from the open tile marked AA to the open tile marked ZZ?
#  
#  To begin, get your puzzle input.
#  

# ok, so load the whole thing, markup the portals, write a maze solver, simples
# also, immediately obvious that we can use the cement trick here, although limited use for a single solve.
# 

PORTAL_START = 'AA'
PORTAL_FINISH = 'ZZ'

ARRIVAL_WALKING = 'WALK'
ARRIVAL_WARPING = 'WARP'

class SolvePosition:
    def __init__(self, x, y, arrival_method, distance_so_far):
        """
        Store the important parts of a traversal to allow the 
        """
        self.x = x
        self.y = y 
        self.arrival_method = arrival_method
        self.distance_so_far = distance_so_far

    

class MazeLocation:
    def __init__(self, x, y, tile, portal_id = None):
        self.x = x
        self.y = y 
        self.tile = tile 
        self.portal_id = None
        self.warp_destination = None
        self.is_warp_portal = False

    def __repr__(self):
        portal = ''
        destination = ''
        if self.is_portal():
            portal = f' ({self.portal_id})'
        if self.warp_destination is not None:
            destination = f' -> ({self.warp_destination.x}, {self.warp_destination.y})'
        return f"<{self.x},{self.y}={self.tile}{portal}{destination}>"

    def set_portal_id(self, portal_id):
        """
        Store the label for this location
        """
        self.portal_id = portal_id

    def set_warp_portal(self, is_warp_portal):
        self.is_warp_portal = is_warp_portal

    def set_warp_destination(self, destination_location):
        """
        Store the warp destinations
        """
        self.warp_destination = destination_location

    def get_warp_destination(self):
        """
        Return the warp destination
        """
        return self.warp_destination

    def is_label(self):
        """
        Return True if the square holds a label value (A-Z)
        """
        LABEL_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return self.tile in LABEL_CHARACTERS

    def is_portal(self):
        return self.is_warp_portal 

    def is_wall(self):
        return self.tile == '#'

    def is_moveable(self):
        return self.tile == '.'

    def get_character(self):
        return self.tile

    def get_map_character(self):
        """
        Return how we want the map to be drawn 
        """
        result = self.tile
        if self.portal_id is not None:
            result = '*'
            if self.portal_id == PORTAL_START:
                result = '@'
            elif self.portal_id == PORTAL_FINISH:
                result = 'X'
        return result


class PlutoMaze:
    def __init__(self):
        """
        Initialise all the class variables we will use 
        """
        self.maze = dict()
        self.max_x = 0
        self.max_y = 0 
        self.start_x = None
        self.start_y = None
        self.finish_x = None
        self.finish_y = None
        self.portals = {}
        self.shortest_distance = None

    def get_location(self, x, y):
        """
        Return the requested tile or a space tile if missing
        """
        result =  MazeLocation(x, y, ' ')
        if (x, y) in self.maze:
            result = self.maze[(x, y)]
        return result 

    def get_locations(self, x, y, x_increment, y_increment, locations_required):
        """
        return a list of n locations from x,y with the increments given.
        The first location will already have the increments applied once i.e.
        10,10,1,1 will start with 11,11
        """
        result = []
        for _ in range(locations_required):
            x += x_increment
            y += y_increment
            result.append(self.get_location(x, y))
        return result

    def get_orthagonal_locations(self, x, y):
        """
        return a list of the 4 locations around x,y
        """
        result = [
            self.get_location(x - 1, y),
            self.get_location(x + 1, y),
            self.get_location(x, y - 1),
            self.get_location(x, y + 1)
            ]
        return result

    def establish_portals(self):
        """
        Go and collect all the portals, making sure that we connect up both ends 
        Also make a note of the start (AA) and finish (ZZ) portals as special exceptions
        """
        # loop through every square and see if we have a portal marker next to it 
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                # is this an empty square ?
                this_location = self.get_location(x, y)
                if this_location.is_moveable():
                    label = None
                    # ok, this could be a portal, let's look around 
                    # is there a label pair nearby ?
                    # labels always read Left to Right or Top to Bottom
                    pair_up = self.get_locations(x, y, 0, -1, 2)
                    pair_down = self.get_locations(x, y, 0, 1, 2)
                    pair_left = self.get_locations(x, y, -1, 0, 2)
                    pair_right = self.get_locations(x, y, 1, 0, 2)

                    if pair_up[0].is_label() and pair_up[1].is_label():
                        label = pair_up[1].get_character() + pair_up[0].get_character()
                    elif pair_down[0].is_label() and pair_down[1].is_label():
                        label = pair_down[0].get_character() + pair_down[1].get_character()
                    elif pair_left[0].is_label() and pair_left[1].is_label():
                        label = pair_left[1].get_character() + pair_left[0].get_character()
                    elif pair_right[0].is_label() and pair_right[1].is_label():
                        label = pair_right[0].get_character() + pair_right[1].get_character()

                    if label is not None:
                        this_location.set_portal_id(label)
                        # ok, is this a special label ?
                        if PORTAL_START == label:
                            self.start_x = x
                            self.start_y = y 
                        elif PORTAL_FINISH == label:
                            self.finish_x = x
                            self.finish_y = y 
                        else:
                            # this is a random label, so add to the portals list 
                            this_location.set_warp_portal(True)
                            if label not in self.portals:
                                self.portals[label] = []
                            self.portals[label].append((x,y))

        # add the portals to a jump list..
        for this_portal in self.portals.keys():
            portal_locations = self.portals[this_portal]
            place_a = self.get_location(*portal_locations[0])
            place_b = self.get_location(*portal_locations[1])
            place_a.set_warp_destination(place_b)
            place_b.set_warp_destination(place_a)
            print(f"Portal Pair: {place_a} {place_b}")


    def store_location(self, x, y, tile):
        """
        Store a tile in a location
        """
        self.maze[(x, y)] = MazeLocation(x, y, tile)
        self.max_x = max(self.max_x, x)
        self.max_y = max(self.max_y, y)


    def load(self, filename):
        """
        Load a raw maze file into memory
        """
        with open(filename, 'r') as f:
            y = 0
            for this_line in f:
                if '' != this_line.strip():
                    for x, this_char in enumerate(this_line.rstrip()):
                        self.store_location(x, y, this_char)
                    y += 1

    def print(self):
        """
        Draw the map 
        """
        for y in range(self.max_y + 1):
            s = ''
            for x in range(self.max_x + 1):
                s += self.get_location(x, y).get_map_character()
            print(s)
        print(f"Portals: {self.portals}")


    def solve_one_position(self, solve_position):
        """
        The solve position is the first location to consider, 
        pop anything else that needs solving into the solvelist 
        make sure that the visited list is updated.
        """
        x = solve_position.x
        y = solve_position.y
        distance_so_far = solve_position.distance_so_far
        arrival_method = solve_position.arrival_method
        location = self.get_location(x, y)
        print(f"Solving: {x},{y} dist={distance_so_far} arrival={arrival_method} location={location}")

        # is this already visited ? or are we getting there faster ?
        if (x,y) not in self.visited or distance_so_far < self.visited[(x,y)]:
            # ok, going to process this location:
            self.visited[(x,y)] = distance_so_far
            # are we on the final square ? If so then we can record the result..
            if x == self.finish_x and y == self.finish_y:
                # woo hoo - we win..
                print(f"We have a completed path: {distance_so_far}")
                if self.shortest_distance is None or self.shortest_distance > distance_so_far:
                    print(f"New best: {distance_so_far}")
                    self.shortest_distance = distance_so_far
            else:
                # ok, so we're not at the end.. we need to explore all the possible exits from this location
                # so normal squares are fine, we just pick anything that looks traversible and add it to the list
                # if this is a portal square then it depends how we got here..
                # if we walked here then the only option is to warp to the destination location
                # if we warped thenonly walking out is valid..
                walking = True 
                if location.is_portal() and arrival_method == ARRIVAL_WALKING:
                    walking = False 
                # right, are we walking out of here ?
                if walking:
                    # find out which of the locations around here are walkable
                    potential_next_steps = self.get_orthagonal_locations(x, y)
                    for target in potential_next_steps:
                        if target.is_moveable():
                            # cool, let's try it 
                            s = SolvePosition(target.x, target.y, ARRIVAL_WALKING, distance_so_far + 1)
                            self.solvelist.append(s)
                else:
                    # warping out - only one target
                    target = location.get_warp_destination()
                    s = SolvePosition(target.x, target.y, ARRIVAL_WARPING, distance_so_far + 1)
                    self.solvelist.append(s)
                    


    def solve(self):
        """
        Find the shortest route through the maze 
        """
        # ok, so pop out an initial starting position and then we'll loop until we get an answer
        self.solvelist = [SolvePosition(self.start_x, self.start_y, ARRIVAL_WALKING, 0)]
        self.visited = dict()

        # while there is a thing to solve, solve it..
        while 0 < len(self.solvelist):
            # get the rist one to solve now..
            solve_this = self.solvelist[0]
            # remove it from the list 
            self.solvelist = self.solvelist[1:]
            # solve this one..
            self.solve_one_position(solve_this)
        
        # and we're done.. so..
        return self.shortest_distance


filename = 'puzzle_input.txt'
the_maze = PlutoMaze()
the_maze.load(filename)
the_maze.print()
the_maze.establish_portals()
the_maze.print()
shortest = the_maze.solve()
print(f"Final result: shortest solve is {shortest}")