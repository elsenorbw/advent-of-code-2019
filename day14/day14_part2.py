#  --- Day 14: Space Stoichiometry ---
#  As you approach the rings of Saturn, your ship's low fuel indicator turns on. There isn't 
#  any fuel here, but the rings have plenty of raw material. Perhaps your ship's Inter-Stellar 
#  Refinery Union brand nanofactory can turn these raw materials into fuel.
#  
#  You ask the nanofactory to produce a list of the reactions it can perform that are relevant 
#  to this process (your puzzle input). Every reaction turns some quantities of specific input 
#  chemicals into some quantity of an output chemical. Almost every chemical is produced by exactly 
#  one reaction; the only exception, ORE, is the raw material input to the entire process and is not 
#  produced by a reaction.
#  
#  You just need to know how much ORE you'll need to collect before you can produce one unit of FUEL.
#  
#  Each reaction gives specific quantities for its inputs and output; reactions cannot be partially 
#  run, so only whole integer multiples of these quantities can be used. (It's okay to have leftover 
#  chemicals when you're done, though.) For example, the reaction 1 A, 2 B, 3 C => 2 D means that 
#  exactly 2 units of chemical D can be produced by consuming exactly 1 A, 2 B and 3 C. You can run 
#  the full reaction as many times as necessary; for example, you could produce 10 D by consuming 5 A, 
#  10 B, and 15 C.
#  
#  Suppose your nanofactory produces the following list of reactions:
#  
#  10 ORE => 10 A
#  1 ORE => 1 B
#  7 A, 1 B => 1 C
#  7 A, 1 C => 1 D
#  7 A, 1 D => 1 E
#  7 A, 1 E => 1 FUEL
#  The first two reactions use only ORE as inputs; they indicate that you can produce as much of 
#  chemical A as you want (in increments of 10 units, each 10 costing 10 ORE) and as much of 
#  chemical B as you want (each costing 1 ORE). To produce 1 FUEL, a total of 31 ORE is required: 
#  1 ORE to produce 1 B, then 30 more ORE to produce the 7 + 7 + 7 + 7 = 28 A (with 2 extra A wasted) 
#  required in the reactions to convert the B into C, C into D, D into E, and finally E into FUEL. 
#  (30 A is produced because its reaction requires that it is created in increments of 10.)
#  
#  Or, suppose you have the following list of reactions:
#  
#  9 ORE => 2 A
#  8 ORE => 3 B
#  7 ORE => 5 C
#  3 A, 4 B => 1 AB
#  5 B, 7 C => 1 BC
#  4 C, 1 A => 1 CA
#  2 AB, 3 BC, 4 CA => 1 FUEL
#  The above list of reactions requires 165 ORE to produce 1 FUEL:
#  
#  Consume 45 ORE to produce 10 A.
#  Consume 64 ORE to produce 24 B.
#  Consume 56 ORE to produce 40 C.
#  Consume 6 A, 8 B to produce 2 AB.
#  Consume 15 B, 21 C to produce 3 BC.
#  Consume 16 C, 4 A to produce 4 CA.
#  Consume 2 AB, 3 BC, 4 CA to produce 1 FUEL.
#  Here are some larger examples:
#  
#  13312 ORE for 1 FUEL:
#  
#  157 ORE => 5 NZVS
#  165 ORE => 6 DCFZ
#  44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
#  12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
#  179 ORE => 7 PSHF
#  177 ORE => 5 HKGWZ
#  7 DCFZ, 7 PSHF => 2 XJWVT
#  165 ORE => 2 GPVTF
#  3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT
#  180697 ORE for 1 FUEL:
#  
#  2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
#  17 NVRVD, 3 JNWZP => 8 VPVL
#  53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
#  22 VJHF, 37 MNCFX => 5 FWMGM
#  139 ORE => 4 NVRVD
#  144 ORE => 7 JNWZP
#  5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
#  5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
#  145 ORE => 6 MNCFX
#  1 NVRVD => 8 CXFTF
#  1 VJHF, 6 MNCFX => 4 RFSQX
#  176 ORE => 6 VJHF
#  2210736 ORE for 1 FUEL:
#  
#  171 ORE => 8 CNZTR
#  7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
#  114 ORE => 4 BHXH
#  14 VRPVC => 6 BMBT
#  6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
#  6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
#  15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
#  13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
#  5 BMBT => 4 WPTQ
#  189 ORE => 9 KTJDG
#  1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
#  12 VRPVC, 27 CNZTR => 2 XDBXC
#  15 KTJDG, 12 BHXH => 5 XCVML
#  3 BHXH, 2 VRPVC => 7 MZWV
#  121 ORE => 7 VRPVC
#  7 XCVML => 6 RJRHP
#  5 BHXH, 4 VRPVC => 5 LTCX
#  Given the list of reactions in your puzzle input, what is the minimum amount of ORE required 
#  to produce exactly 1 FUEL?
#  
#  To begin, get your puzzle input.

#  Your puzzle answer was 1185296.
#  
#  The first half of this puzzle is complete! It provides one gold star: *
#  
#  --- Part Two ---
#  After collecting ORE for a while, you check your cargo hold: 1 trillion (1000000000000) units of ORE.
#  
#  With that much ore, given the examples above:
#  
#  The 13312 ORE-per-FUEL example could produce 82892753 FUEL.
#  The 180697 ORE-per-FUEL example could produce 5586022 FUEL.
#  The 2210736 ORE-per-FUEL example could produce 460664 FUEL.
#  Given 1 trillion ORE, what is the maximum amount of FUEL you can produce?



#
#   right each widget needs to understand how much of itself we have left and how to make more
#
# for an input of 3 A, 4 B => 1 AB
# Chemical('AB', ((3, 'A'), (4, 'B')), 1)
#
class Chemical:
    def __init__(self, name, components, produces, quantity=0, provided=0):
        self.quantity_at_hand = quantity
        self.name = name 
        self.components = components
        self.produce_quantity = produces
        self.provided = provided

    def __repr__(self):
        s = f"<Chemical {self.name} provided={self.provided} holding={self.quantity_at_hand} composition={self.components} produces={self.produce_quantity}>"
        return s

    def add_stock(self, additional_amount):
        self.quantity_at_hand += additional_amount

    def obtain(self, required_amount, chemical_store):
        result = False
        # either we have enough of this or we don't (very deep)
        if self.quantity_at_hand >= required_amount:
            # easy win, we have the material at hand
            self.quantity_at_hand -= required_amount
            result = True 
        else:
            # we will need to produce at least one batch 
            # this may be a raw material though.. so be careful 
            if 0 == self.produce_quantity:
                result = False
            else:
                #print(f"a) required={required_amount}, at_hand={self.quantity_at_hand}")
                required_amount -= self.quantity_at_hand
                self.quantity_at_hand = 0
                #print(f"b) required={required_amount}, at_hand={self.quantity_at_hand}")
                # we need to produce an additional required_amount's worth 
                batches_to_produce = (required_amount + self.produce_quantity - 1) // self.produce_quantity
                #print(f"c) batches_to_produce={batches_to_produce}, produce_quantity={self.produce_quantity}, required={required_amount}")
                result = self.produce(chemical_store, batches_to_produce)
                if result:
                    self.quantity_at_hand -= required_amount

        if result:
            self.provided += required_amount
        return result



    def produce(self, chemical_store, batches):
        """
        Produce X batches of this chemical
        """
        result = True 
        # obtain enough of each chemical 
        for required_quantity, required_chemical in self.components:
            if not chemical_store.obtain(required_chemical, required_quantity * batches):
                #print(f"Couldn't obtain {required_quantity} of {required_chemical}")
                result = False

        # and we have produced
        if result:
            self.quantity_at_hand += self.produce_quantity * batches
        return result 


def component_parse(s):
    s = s.strip()
    parts = s.split(' ')
    return(int(parts[0]), parts[1])

class ChemicalStore:
    def __init__(self):
        self.reset()

    def reset(self):
        self.chemicals = dict()

    def copy(self):
        result = ChemicalStore()
        for c in self.chemicals.values():
            result.chemicals[c.name] = Chemical(c.name, c.components, c.produce_quantity, c.quantity_at_hand, c.provided)
        return result

    def obtain(self, chemical, amount):
        """
        Obtain the specified amount of the required chemical 
        """
        return self.chemicals[chemical].obtain(amount, self)

    def load_one_chemical(self, s):
        """
        take a line like : 
        6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
        and load it into one chemical in the list 
        """
        # split it by the => 
        parts = s.split('=>')
        components = parts[0].split(',')
        result = parts[1]
        #print(f"{result} is made of {components}")
        this_chemical = component_parse(result)
        components = tuple([component_parse(x) for x in components])
        #print(f"{this_chemical} is made of {components}")
        # got it parsed, so let's store it 
        self.chemicals[this_chemical[1]] = Chemical(this_chemical[1], components, this_chemical[0])

    def add_raw_material(self, name, amount):
        """
        Provide some raw materials to the chemical store 
        """
        self.chemicals[name] = Chemical(name, None, 0)
        self.chemicals[name].add_stock(amount)

    def provided(self, name):
        return self.chemicals[name].provided

    def quantity_at_hand(self, name):
        return self.chemicals[name].quantity_at_hand

    def load(self, filename):
        """
        Read a chemical store input file 
        """
        with open(filename, 'r') as f:
            for this_line in f:
                this_line = this_line.strip()
                if this_line != '':
                    self.load_one_chemical(this_line)

    def show(self):
        """
        Output all thr chemicals in the store 
        """
        print(f"Chemical Store\n---------------------")
        for this_chemical in sorted(self.chemicals.keys()):
            print(f"{self.chemicals[this_chemical]}")
        print("\n")




# binary chop to find out how much we can produce, although we can make a smart starting
#  guess based on ore consumption for one FUEL 
def calculate_fuel_production_capacity(chemical_store):
    # make a copy and produce one unit of fuel 
    c = chemical_store.copy()
    c.obtain('FUEL', 1)
    ore_per_fuel = c.provided('ORE')
    ore_at_hand = chemical_store.quantity_at_hand('ORE')
    starting_guess = ore_at_hand // ore_per_fuel
    c = None 
    print(f"estimating {starting_guess} from {ore_at_hand} / {ore_per_fuel}")
    lower_bound = starting_guess
    upper_bound = ore_at_hand
    # lower bound is the lowest value that is defnitely possible
    # upper bound is the highest value that is still potentially possible 
    # so if we guess in the middle and it is impossible then upper = guess - 1 but..
    # if we guess in the middle and it is possible then lower = guess 
    # we're done when they're equal 
    while(lower_bound != upper_bound):
        # make a guess in the middle
        guess = (upper_bound - lower_bound) // 2 + lower_bound
        if guess == lower_bound:
            guess += 1
        # check out this guess..
        c = chemical_store.copy()
        result = c.obtain('FUEL', guess)
        print(f"guessing: {guess} range: {lower_bound}-{upper_bound} -> {result}")
        if result:
            # we can make this much fuel...
            lower_bound = guess
        else:
            # too much.. try lower 
            upper_bound = guess - 1 
    print(f"winner is {lower_bound}")
    return lower_bound

x = 460664
#result = chemical_store.obtain('FUEL', x)
#print(f"{result} for obtaining {x} FUEL")
#chemical_store.show()

chemical_store = ChemicalStore()
#chemical_store.load('test_2210736.txt') 
#chemical_store.load('test_180697.txt') 
#chemical_store.load('test_13312.txt')
chemical_store.load('puzzle_input.txt') 

chemical_store.add_raw_material('ORE', 1000000000000)
#chemical_store.show()


calculate_fuel_production_capacity(chemical_store)
