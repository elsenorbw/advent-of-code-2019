#  --- Day 18: Many-Worlds Interpretation ---
#  As you approach Neptune, a planetary security system detects you and activates a giant tractor 
#  beam on Triton! You have no choice but to land.
#  
#  A scan of the local area reveals only one interesting feature: a massive underground vault. 
#  You generate a map of the tunnels (your puzzle input). The tunnels are too narrow to move diagonally.
#  
#  Only one entrance (marked @) is present among the open passages (marked .) and stone walls (#), but 
#  you also detect an assortment of keys (shown as lowercase letters) and doors (shown as uppercase letters). 
#  Keys of a given letter open the door of the same letter: a opens A, b opens B, and so on. You aren't 
#  sure which key you need to disable the tractor beam, so you'll need to collect all of them.
#  
#  For example, suppose you have the following map:
#  
#  #########
#  #b.A.@.a#
#  #########
#  Starting from the entrance (@), you can only access a large door (A) and a key (a). Moving toward 
#  the door doesn't help you, but you can move 2 steps to collect the key, unlocking A in the process:
#  
#  #########
#  #b.....@#
#  #########
#  Then, you can move 6 steps to collect the only other key, b:
#  
#  #########
#  #@......#
#  #########
#  So, collecting every key took a total of 8 steps.
#  
#  Here is a larger example:
#  
#  ########################
#  #f.D.E.e.C.b.A.@.a.B.c.#
#  ######################.#
#  #d.....................#
#  ########################
#  The only reasonable move is to take key a and unlock door A:
#  
#  ########################
#  #f.D.E.e.C.b.....@.B.c.#
#  ######################.#
#  #d.....................#
#  ########################
#  Then, do the same with key b:
#  
#  ########################
#  #f.D.E.e.C.@.........c.#
#  ######################.#
#  #d.....................#
#  ########################
#  ...and the same with key c:
#  
#  ########################
#  #f.D.E.e.............@.#
#  ######################.#
#  #d.....................#
#  ########################
#  Now, you have a choice between keys d and e. While key e is closer, collecting it now would be 
#  slower in the long run than collecting key d first, so that's the best choice:
#  
#  ########################
#  #f...E.e...............#
#  ######################.#
#  #@.....................#
#  ########################
#  Finally, collect key e to unlock door E, then collect key f, taking a grand total of 86 steps.
#  
#  Here are a few more examples:
#  
#  ########################
#  #...............b.C.D.f#
#  #.######################
#  #.....@.a.B.c.d.A.e.F.g#
#  ########################
#  Shortest path is 132 steps: b, a, c, d, f, e, g
#  
#  #################
#  #i.G..c...e..H.p#
#  ########.########
#  #j.A..b...f..D.o#
#  ########@########
#  #k.E..a...g..B.n#
#  ########.########
#  #l.F..d...h..C.m#
#  #################
#  Shortest paths are 136 steps;
#  one is: a, f, b, j, g, n, h, d, l, o, e, p, c, i, k, m
#  
#  ########################
#  #@..............ac.GI.b#
#  ###d#e#f################
#  ###A#B#C################
#  ###g#h#i################
#  ########################
#  Shortest paths are 81 steps; one is: a, c, f, i, d, g, b, e, h
#  
#  How many steps is the shortest path that collects all of the keys?
#  
#  To begin, get your puzzle input.

#  
#  Your puzzle answer was 4668.
#  
#  The first half of this puzzle is complete! It provides one gold star: *
#  
#  --- Part Two ---
#  You arrive at the vault only to discover that there is not one vault, but four - each 
#  with its own entrance.
#  
#  On your map, find the area in the middle that looks like this:
#  
#  ...
#  .@.
#  ...
#  Update your map to instead use the correct data:
#  
#  @#@
#  ###
#  @#@
#  This change will split your map into four separate sections, each with its own entrance:
#  
#  #######       #######
#  #a.#Cd#       #a.#Cd#
#  ##...##       ##@#@##
#  ##.@.##  -->  #######
#  ##...##       ##@#@##
#  #cB#Ab#       #cB#Ab#
#  #######       #######
#  Because some of the keys are for doors in other vaults, it would take much too long to collect 
#  all of the keys by yourself. Instead, you deploy four remote-controlled robots. Each starts at one 
#  of the entrances (@).
#  
#  Your goal is still to collect all of the keys in the fewest steps, but now, each robot has its own 
#  position and can move independently. You can only remotely control a single robot at a time. 
#  Collecting a key instantly unlocks any corresponding doors, regardless of the vault in which the 
#  key or door is found.
#  
#  For example, in the map above, the top-left robot first collects key a, unlocking door A in the 
#  bottom-right vault:
#  
#  #######
#  #@.#Cd#
#  ##.#@##
#  #######
#  ##@#@##
#  #cB#.b#
#  #######
#  Then, the bottom-right robot collects key b, unlocking door B in the bottom-left vault:
#  
#  #######
#  #@.#Cd#
#  ##.#@##
#  #######
#  ##@#.##
#  #c.#.@#
#  #######
#  Then, the bottom-left robot collects key c:
#  
#  #######
#  #@.#.d#
#  ##.#@##
#  #######
#  ##.#.##
#  #@.#.@#
#  #######
#  Finally, the top-right robot collects key d:
#  
#  #######
#  #@.#.@#
#  ##.#.##
#  #######
#  ##.#.##
#  #@.#.@#
#  #######
#  In this example, it only took 8 steps to collect all of the keys.
#  
#  Sometimes, multiple robots might have keys available, or a robot might have to wait for multiple 
#  keys to be collected:
#  
#  ###############
#  #d.ABC.#.....a#
#  ######@#@######
#  ###############
#  ######@#@######
#  #b.....#.....c#
#  ###############
#  First, the top-right, bottom-left, and bottom-right robots take turns collecting 
#  keys a, b, and c, a total of 6 + 6 + 6 = 18 steps. 
#  Then, the top-left robot can access key d, spending another 6 steps; 
#  collecting all of the keys here takes a minimum of 24 steps.
#  
#  Here's a more complex example:
#  
#  #############
#  #DcBa.#.GhKl#
#  #.###@#@#I###
#  #e#d#####j#k#
#  ###C#@#@###J#
#  #fEbA.#.FgHi#
#  #############
#  Top-left robot collects key a.
#  Bottom-left robot collects key b.
#  Top-left robot collects key c.
#  Bottom-left robot collects key d.
#  Top-left robot collects key e.
#  Bottom-left robot collects key f.
#  Bottom-right robot collects key g.
#  Top-right robot collects key h.
#  Bottom-right robot collects key i.
#  Top-right robot collects key j.
#  Bottom-right robot collects key k.
#  Top-right robot collects key l.
#  In the above example, the fewest steps to collect all of the keys is 32.
#  
#  Here's an example with more choices:
#  
#  #############
#  #g#f.D#..h#l#
#  #F###e#E###.#
#  #dCba@#@BcIJ#
#  #############
#  #nK.L@#@G...#
#  #M###N#H###.#
#  #o#m..#i#jk.#
#  #############
#  One solution with the fewest steps is:
#  
#  Top-left robot collects key e.
#  Top-right robot collects key h.
#  Bottom-right robot collects key i.
#  Top-left robot collects key a.
#  Top-left robot collects key b.
#  Top-right robot collects key c.
#  Top-left robot collects key d.
#  Top-left robot collects key f.
#  Top-left robot collects key g.
#  Bottom-right robot collects key k.
#  Bottom-right robot collects key j.
#  Top-right robot collects key l.
#  Bottom-left robot collects key n.
#  Bottom-left robot collects key m.
#  Bottom-left robot collects key o.
#  This example requires at least 72 steps to collect all keys.
#  
#  After updating your map and using the remote-controlled robots, what is the fewest steps necessary to collect all of the keys?



# ok, so the logic I'm thinking is that we have to try all possible paths everywhere we get an option.
# so for any given starting location and map we sould be able to sort out the possible keys we can hit next.

# so we need to get a maze loaded into an object..

potential_keys = "abcdefghijklmnopqrstuvwxyz"
potential_doors = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

TILE_WALL = '#'
TILE_EMPTY = '.'




class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y 

    def copy(self):
        r = Robot(self.x, self.y)
        return r 

    def __repr__(self):
        return f"<r {self.x},{self.y}>"



class StartFromHere:
    def __init__(self, keys, distance_so_far, robots):
        self.keys = keys.copy()
        self.distance_so_far = distance_so_far
        self.robots = [r.copy() for r in robots]

    def move_robot(self, robot_idx, new_x, new_y):
        self.robots[robot_idx].move_to(new_x, new_y)

    def __repr__(self):
        return f"<StartFrom robots={self.robots} distance={self.distance_so_far} keys={self.keys}>"

    def add_key(self, the_key):
        self.keys.append(the_key)

    def add_distance(self, the_distance):
        self.distance_so_far += the_distance

    def move_robot(self, target_robot_id, x, y):
        self.robots[target_robot_id].move_to(x, y)


class NeedToEvaluate:
    def __init__(self):
        self.the_list = dict()
    

    def should_evaluate(self, keys_so_far, this_key, distance_so_far, distance_to_this_key):
        """
        Decide whether we have already seen this collection of keys, ending at this_key but with a shorter or the same distance
        if we have then there's no point in evaluating this later as we will always get a bigger value 
        """
        result = True
        skeys = [str(x) for x in sorted(keys_so_far)]
        the_key = this_key + '_' + "".join(skeys) 
        the_distance = distance_so_far + distance_to_this_key
        if the_key in self.the_list:
            if the_distance >= self.the_list[the_key]:
                #print(f"We have had a better offer already for {the_key}")
                result = False
        if result:
            #print(f"Storing:{the_key} -> {the_distance}")
            self.the_list[the_key] = the_distance
        return result

class MazeSolver:
    def __init__(self):
        self.maze = dict()
        self.walls = set()
        self.max_x = 0
        self.max_y = 0
        self.keys = dict()
        self.doors = dict()
        self.robots = []
        self.steps_so_far = 0
        self.key_order = []
        self.eval_helper = NeedToEvaluate()
        # best result so far, for short-circuit
        self.shortest_distance = None
        self.shortest_route = None
        # any other strands we need to try before we get to the end ?
        self.routes_to_evaluate = []

    def store_tile(self, x, y, tile):
        """
        store a tile 
        """
        self.maze[(x, y)] = tile
        self.max_x = max(x, self.max_x)
        self.max_y = max(y, self.max_y)
        # if the tile is a lower case letter, then it's a key 
        if tile in potential_keys:
            self.keys[tile] = (x, y)
        # if the tile is an upper case letter then it is a door 
        if tile in potential_doors:
            self.doors[tile.lower()] = (x, y)
        # set the starting position
        if tile == '@':
            # add a new robot 
            self.robots.append(Robot(x, y))


    def load_maze(self, filename):
        """
        Load an ASCII maze file
        """
        with open(filename, 'r') as f:
            x = 0
            y = 0
            for this_line in f:
                this_line = this_line.strip()
                if '' != this_line:
                    for x, this_char in enumerate(this_line):
                        # store a tile 
                        self.store_tile(x, y, this_char)
                    # and next line 
                    y += 1
                    
    def already_collected(self, tile):
        result = False 
        if tile.lower() in self.key_order:
            result = True
        #print(f"ac: {tile} in {self.key_order} -> {result}")
        return result

    def print_maze(self, detail=False):
        """
        output the current maze 
        """
        for y in range(self.max_y + 1):
            s = ''
            for x in range(self.max_x + 1):
                # is there a robot on this square ?
                if self.containsRobot(x, y):
                    s += 'X'
                else:
                    tile = self.maze[(x, y)]
                    if self.already_collected(tile):
                        tile = TILE_EMPTY
                    s += tile
            print(s)

        if detail:
            print(f"\nKeys: {self.keys}")
            print(f"Doors: {self.doors}")
        print(f"\nRobots: {self.robots}")


    def pour_cement(self):
        """
        Cement any holes that can be cemented, return False if nothing changed.
        Happy to cement multiple blocks at a time 
        """
        result = False
        for x in range(self.max_x + 1):
            for y in range(self.max_y + 1):
                # is this a space ?
                if TILE_EMPTY == self.get_tile(x, y):
                    # how many of the side walls are solid walls ?
                    wall_count = 0
                    if TILE_WALL == self.get_tile(x - 1, y):
                        wall_count += 1
                    if TILE_WALL == self.get_tile(x + 1, y):
                        wall_count += 1
                    if TILE_WALL == self.get_tile(x, y - 1):
                        wall_count += 1 
                    if TILE_WALL == self.get_tile(x, y + 1):
                        wall_count += 1
                    # are there 3 solid walls ? if so then this is a pointless square 
                    if 3 <= wall_count:
                        result = True 
                        self.store_tile(x, y, TILE_WALL)
        return result

    def cement(self):
        """
        Fill in any space square which is only reachable in one way, 
        it is, by definition, the end of a passage way and can be walled off 
        """
        while self.pour_cement():
            pass
        # and now, fill in all the hard forget it zones 
        self.walls = set()
        for x in range(0, self.max_x + 2):
            for y in range(0, self.max_y + 2):
                if TILE_WALL == self.get_tile(x, y):
                    self.walls.add((x,y))
        print(f"Walls: {self.walls}")

    def get_tile(self, x, y, default = TILE_WALL):
        """ 
        Return the relevant tile value 
        """
        result = default
        if (x,y) in self.maze:
            result = self.maze[(x,y)]
        return result

    def is_solid(self, x, y):
        """
        Can we walk through this square ?
        """
        result = False
        tile = self.get_tile(x, y)
        if TILE_WALL == tile:
            result = True
        if tile in potential_doors:
            if tile.lower() not in self.key_order:
                result = True
            else:
                pass
                #print(f"Ignoring opened door {tile}")
        return result 
        
    def containsRobot(self, x, y):
        """
        Returns true if the indicated location has one or more robots on it 
        """
        result = False
        for this_robot in self.robots:
            if this_robot.x == x and this_robot.y == y:
                result = True 
        return result

    def is_key(self, x, y):
        """
        Is this a key ?
        """
        result = False
        tile = self.get_tile(x, y)
        if tile in potential_keys:
            # have we already seen (and therefore collected) this key ?
            if tile not in self.key_order:
                #print(f"Found a key {tile}")
                result = True
            else:
                pass
                #print(f"Ignoring already collected key {tile}")
        return result
        


    def get_walk_options(self, this_x, this_y, this_robot_index, current_walk_distance = 0):
        """
        Decide what we will do with this spot, either we've arrived at a location with a key
        in which case we store this if it's the shortest route to that spot.
        """
        # right - is this square one we have already visited ?
        if (this_x, this_y) not in self.visited or current_walk_distance < self.visited[(this_x, this_y)]:
            # new square, ok so what are we looking at ?
            self.visited[(this_x, this_y)] = current_walk_distance
            # is this a solid wall ? of so then we're done..
            if self.is_solid(this_x, this_y):
                # forget this one
                pass
            elif self.is_key(this_x, this_y):
                # ok, we have found a useful route - add it to the results if it is the shortest one..
                key = self.get_tile(this_x, this_y)
                if key in self.routes_to_keys:
                    if current_walk_distance < self.routes_to_keys[key]:
                        self.routes_to_keys[key] = (current_walk_distance, this_robot_index)
                else:
                    self.routes_to_keys[key] = (current_walk_distance, this_robot_index) 
            else:
                # empty space, so we can try the surrounding squares 
                if (this_x - 1, this_y) not in self.walls:
                    self.get_walk_options(this_x - 1, this_y, this_robot_index, current_walk_distance + 1)
                if (this_x + 1, this_y) not in self.walls:
                    self.get_walk_options(this_x + 1, this_y, this_robot_index, current_walk_distance + 1)
                if (this_x, this_y - 1) not in self.walls:
                    self.get_walk_options(this_x, this_y - 1, this_robot_index, current_walk_distance + 1)
                if (this_x, this_y + 1) not in self.walls:
                    self.get_walk_options(this_x, this_y + 1, this_robot_index, current_walk_distance + 1)


    def reset_walk(self):
        """
        restart all the walk values 
        """
        self.routes_to_keys = dict()
        self.visited = dict()

    def solve(self):
        """
        Completely find the best option fore this maze.
        We will need to loop until we have nothing left in the routes_to_evaluate value 
        """
        # setup an initial value 
        counter = 0
        skipped = 0
        evaluated = 0
        eval_skip = 0 
        start = StartFromHere(keys=[], distance_so_far=0, robots=self.robots)
        self.routes_to_evaluate.append(start)
        while(0 < len(self.routes_to_evaluate)):
            counter += 1
            if counter % 10 == 0:
                print(f"solve({counter}): remain={len(self.routes_to_evaluate)} skipped={skipped},{eval_skip}, evaluated={evaluated}, best={self.shortest_distance}, {self.shortest_route}")
            # pop a route off the top and evaluate it 
            this_route_config = self.routes_to_evaluate[0]
            self.routes_to_evaluate = self.routes_to_evaluate[1:]
            if self.shortest_distance is not None and self.shortest_distance < this_route_config.distance_so_far:
                #print(f"No point in evaluating {this_route_config} because best is {self.shortest_distance}")
                pass
                skipped += 1
            else:
                #print(f"Evaluating {this_route_config}")
                # Setup the necessary variables..
                self.key_order = this_route_config.keys.copy()
                self.robots = [r.copy() for r in this_route_config.robots]
                self.steps_so_far = this_route_config.distance_so_far
                # And solve this route
                self.solve_this_route()
                evaluated += 1
            
        return self.shortest_distance, self.shortest_route

    def solve_this_route(self):
        """
        Solve this maze from the current step, if we run into divergent options then we can 
        add them to the list and return None, otherwise we'll finish and return the number of steps and the order
        if we give up on one of these as a bad a job then we will also return None 
        """

        #self.print_maze()
        #print(f"Current distance={self.steps_so_far} -> {self.key_order}\n\n\n")

        # so we need to see which options we now have, and the shortest path to 
        # each of the keys we can actually hit
        # so walk everywhere and record the shortest route to each one 
        # we are stopping at anything that is a wall, key or door 
        # so generate a list of the doors we can hit with a distance to each one
        self.reset_walk()
        for this_robot_idx, this_robot in enumerate(self.robots):
            self.get_walk_options(this_robot.x, this_robot.y, this_robot_idx)
        # right, we should have some options 
        #print(f"\nNEW MOVE!")
        #self.print_maze()
        #print(f"Current distance={self.steps_so_far} -> {self.key_order}")
        #print(f"Options from here: {self.routes_to_keys}")
        #print("\n\n")

        # do I have multiple options ? If so we need to do something clever and recursive 
        # so we have either no options - in which case we're done..
        if 0 == len(self.routes_to_keys.keys()):
            #self.print_maze()
            #print(f"Found a route: {self.key_order} -> {self.steps_so_far}")
            if self.shortest_distance is None or self.shortest_distance > self.steps_so_far:
                self.shortest_distance = self.steps_so_far
                self.shortest_route = self.key_order
                print(f"New best: {self.shortest_distance} ({self.shortest_route})")
            return self.steps_so_far
        elif 1 == len(self.routes_to_keys.keys()):
            # ok so no choices... update a value here..
            # TODO: fix this crappy way to find the only item in a dictionary
            for target_key in self.routes_to_keys.keys():
                # move the right robot 
                target_distance, target_robot_id = self.routes_to_keys[target_key]
                self.move_robot_to_key(target_key, target_distance, target_robot_id)
            # we can give up half way down here.. may help with speed
            if self.shortest_distance is not None and self.steps_so_far > self.shortest_distance:
                #print(f"Giving up early {self.steps_so_far}")
                return None
            else:
                return self.solve_this_route()
        else:

            # multiple options - evaluate the first and add any other options to the list to be explored
            #print(f"oh crap - many options.. {self.routes_to_keys}")

            # get a list of the options to be processed 
            #print(f"routes: {self.routes_to_keys}")
            all_option_keys = [x for x in self.routes_to_keys.keys()]
            #print(f"all_option_keys: {all_option_keys}")

            for idx in range(1, len(all_option_keys)):
                target_key = all_option_keys[idx]
                target_distance, target_robot_id = self.routes_to_keys[target_key]
                if self.eval_helper.should_evaluate(self.key_order, target_key, self.steps_so_far, target_distance):
                    next_x, next_y = self.keys[target_key]
                    sp = StartFromHere(keys=self.key_order, distance_so_far=self.steps_so_far, robots=self.robots)
                    sp.add_key(target_key)
                    sp.add_distance(target_distance)
                    sp.move_robot(target_robot_id, next_x, next_y)
                    #print(f"Adding a route[{idx}]:{sp}")
                    self.routes_to_evaluate.append(sp)
            
            # and now, execute the first option 
            target_key = all_option_keys[0]
            target_distance, target_robot_id = self.routes_to_keys[target_key]
            self.move_robot_to_key(target_key, target_distance, target_robot_id)
            return self.solve_this_route()


    def move_robot_to_key(self, the_key, the_distance, the_robot_id):
        """
        Update the distance so far, remove the key and the door
        """
        self.steps_so_far += the_distance
        # update the current_x and current_y for the relevant robot
        x, y = self.keys[the_key]
        self.robots[the_robot_id].move_to(x, y)

        # and add this key to the list
        self.key_order.append(the_key)

        # remove the key 
        #self.store_tile(self.current_x, self.current_y, TILE_EMPTY)
        # remove the door if there is one
        if the_key in self.doors:
            door_x, door_y = self.doors[the_key]
            #self.store_tile(door_x, door_y, TILE_EMPTY)
            #del self.doors[the_key]

        # and remove the door and key from the lists
        #del self.keys[the_key]



def test_it():
    test_filename = 'test_multi_72.txt'
    #test_filename = 'test_longway.txt'
    #test_filename = 'test_cement.txt'

    m = MazeSolver()
    m.load_maze(test_filename)
    m.print_maze()
    m.cement()
    m.print_maze()
    shortest = m.solve()
    print(f"Shortest route is {shortest}")


#test_it()
#exit(1)


puzzle_filename = 'puzzle_input_part2.txt'

m = MazeSolver()
m.load_maze(puzzle_filename)
m.print_maze()
m.cement()
m.print_maze()
shortest = m.solve()
print(f"Shortest route for real input is {shortest}")



