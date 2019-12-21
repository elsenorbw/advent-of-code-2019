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

# ok, so the logic I'm thinking is that we have to try all possible paths everywhere we get an option.
# so for any given starting location and map we sould be able to sort out the possible keys we can hit next.

# so we need to get a maze loaded into an object..

potential_keys = "abcdefghijklmnopqrstuvwxyz"
potential_doors = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

TILE_WALL = '#'
TILE_EMPTY = '.'


class StartFromHere:
    def __init__(self, keys, distance_so_far, x, y):
        self.keys = keys.copy()
        self.distance_so_far = distance_so_far
        self.x = x
        self.y = y
    def __repr__(self):
        return f"<StartFrom {self.x},{self.y} distance={self.distance_so_far} keys={self.keys}>"
    def add_key(self, the_key):
        self.keys.append(the_key)
    def add_distance(self, the_distance):
        self.distance_so_far += the_distance



class NeedToEvaluate:
    def __init__(self):
        self.the_list = dict()
    

    def might_be_best(self, all_keys, full_distance):
        """
        See whether the path we are passed could potentially be the best path and hence should be evaluated
        """
        result = True 
        # build a key 
        if 0 < len(all_keys):
            skeys = [str(x) for x in sorted(all_keys[:-1])]
            the_key = all_keys[-1] + ' ' + "".join(skeys)
            if the_key in self.the_list and self.the_list[the_key] < full_distance:
                result = False
            
        return result

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
        self.current_x = 0
        self.current_y = 0 
        self.steps_so_far = 0
        self.key_order = []
        self.eval_helper = NeedToEvaluate()
        # best result so far, for short-circuit
        self.shortest_distance = None
        self.shortest_route = None
        # any other strands we need to try before we get to the end ?
        self.routes_to_evaluate = []

    def duplicate(self):
        new_solver = MazeSolver()
        new_solver.maze = self.maze.copy()
        new_solver.max_x = self.max_x
        new_solver.max_y = self.max_y 
        new_solver.keys = self.keys.copy()
        new_solver.doors = self.doors.copy()
        new_solver.current_x = self.current_x
        new_solver.current_y = self.current_y
        new_solver.steps_so_far = self.steps_so_far
        new_solver.key_order = self.key_order.copy()
        return new_solver

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
            self.current_x = x
            self.current_y = y 


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
                    
    def print_maze(self):
        """
        output the current maze 
        """
        for y in range(self.max_y + 1):
            s = ''
            for x in range(self.max_x + 1):
                if x == self.current_x and y == self.current_y:
                    s += 'X'
                else:
                    s += self.maze[(x, y)]
            print(s)

        print(f"\nKeys: {self.keys}")
        print(f"Doors: {self.doors}")


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
        


    def get_walk_options(self, this_x, this_y, current_walk_distance = 0):
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
                        self.routes_to_keys[key] = current_walk_distance
                else:
                    self.routes_to_keys[key] = current_walk_distance 
            else:
                # empty space, so we can try the surrounding squares 
                if (this_x - 1, this_y) not in self.walls:
                    self.get_walk_options(this_x - 1, this_y, current_walk_distance + 1)
                if (this_x + 1, this_y) not in self.walls:
                    self.get_walk_options(this_x + 1, this_y, current_walk_distance + 1)
                if (this_x, this_y - 1) not in self.walls:
                    self.get_walk_options(this_x, this_y - 1, current_walk_distance + 1)
                if (this_x, this_y + 1) not in self.walls:
                    self.get_walk_options(this_x, this_y + 1, current_walk_distance + 1)


    def reset_walk(self, total_clear = False):
        """
        restart all the walk values 
        """
        self.routes_to_keys = dict()
        self.visited = dict()
        if total_clear:
            self.steps_so_far = 0
            self.key_order = []
            self.shortest_distance = None
            self.shortest_route = None

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
        start = StartFromHere(keys=[], distance_so_far=0, x=self.current_x, y=self.current_y)
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
                if self.eval_helper.might_be_best(this_route_config.keys, this_route_config.distance_so_far):
                    # Setup the necessary variables..
                    self.key_order = this_route_config.keys.copy()
                    self.current_x = this_route_config.x
                    self.current_y = this_route_config.y
                    self.steps_so_far = this_route_config.distance_so_far
                    # And solve this route
                    self.solve_this_route()
                    evaluated += 1
                else:
                    eval_skip += 1
        return self.shortest_distance, self.shortest_route

    def solve_this_route(self):
        """
        Solve this maze from the current step, if we run into divergent options then we can 
        add them to the list and return None, otherwise we'll finish and return the number of steps and the order
        if we give up on one of these as a bad a job then we will also return None 
        
        """
        # so we need to see which options we now have, and the shortest path to 
        # each of the keys we can actually hit
        # so walk everywhere and record the shortest route to each one 
        # we are stopping at anything that is a wall, key or door 
        # so generate a list of the doors we can hit with a distance to each one
        self.reset_walk()
        self.get_walk_options(self.current_x, self.current_y)
        # right, we should have some options 
        #self.print_maze()
        #print(f"After initial walk options: {self.routes_to_keys}")
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
                self.move_to_key(target_key, self.routes_to_keys[target_key])
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
                target_distance = self.routes_to_keys[target_key]
                if self.eval_helper.should_evaluate(self.key_order, target_key, self.steps_so_far, target_distance):
                    next_x, next_y = self.keys[target_key]
                    sp = StartFromHere(keys=self.key_order, distance_so_far=self.steps_so_far, x=next_x, y=next_y)
                    sp.add_key(target_key)
                    sp.add_distance(target_distance)
                    #print(f"Adding a route[{idx}]:{sp}")
                    self.routes_to_evaluate.append(sp)
            
            # and now, execute the first option 
            target_key = all_option_keys[0]
            target_distance = self.routes_to_keys[target_key]
            self.move_to_key(target_key, target_distance)
            return self.solve_this_route()


    def move_to_key(self, the_key, the_distance):
        """
        Update the distance so far, remove the key and the door
        """
        self.steps_so_far += the_distance
        # update the current_x and current_y
        self.current_x, self.current_y = self.keys[the_key]

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
    test_filename = 'test_136.txt'
    #test_filename = 'test_longway.txt'
    #test_filename = 'test_cement.txt'

    m = MazeSolver()
    m.load_maze(test_filename)
    m.print_maze()
    m.cement()
    m.print_maze()
    #shortest = m.solve()
    print(f"Shortest route is {shortest}")





puzzle_filename = 'puzzle_input.txt'

m = MazeSolver()
m.load_maze(puzzle_filename)
m.print_maze()
m.cement()
m.print_maze()
shortest = m.solve()
print(f"Shortest route for real input is {shortest}")



