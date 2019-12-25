#  --- Day 22: Slam Shuffle ---
#  There isn't much to do while you wait for the droids to repair your ship. At least you're drifting in 
#  the right direction. You decide to practice a new card shuffle you've been working on.
#  
#  Digging through the ship's storage, you find a deck of space cards! Just like any deck of space cards, 
#  there are 10007 cards in the deck numbered 0 through 10006. The deck must be new - they're still in 
#  factory order, with 0 on the top, then 1, then 2, and so on, all the way through to 10006 on the bottom.
#  
#  You've been practicing three different techniques that you use while shuffling. Suppose you have a 
#  deck of only 10 cards (numbered 0 through 9):
#  
#  To deal into new stack, create a new stack of cards by dealing the top card of the deck onto the top 
#  of the new stack repeatedly until you run out of cards:
#  
#  Top          Bottom
#  0 1 2 3 4 5 6 7 8 9   Your deck
#                        New stack
#  
#    1 2 3 4 5 6 7 8 9   Your deck
#                    0   New stack
#  
#      2 3 4 5 6 7 8 9   Your deck
#                  1 0   New stack
#  
#        3 4 5 6 7 8 9   Your deck
#                2 1 0   New stack
#  
#  Several steps later...
#  
#                    9   Your deck
#    8 7 6 5 4 3 2 1 0   New stack
#  
#                        Your deck
#  9 8 7 6 5 4 3 2 1 0   New stack
#  Finally, pick up the new stack you've just created and use it as the deck for the next technique.
#  
#  To cut N cards, take the top N cards off the top of the deck and move them as a single unit to the bottom 
#  of the deck, retaining their order. For example, to cut 3:
#  
#  Top          Bottom
#  0 1 2 3 4 5 6 7 8 9   Your deck
#  
#        3 4 5 6 7 8 9   Your deck
#  0 1 2                 Cut cards
#  
#  3 4 5 6 7 8 9         Your deck
#                0 1 2   Cut cards
#  
#  3 4 5 6 7 8 9 0 1 2   Your deck
#  You've also been getting pretty good at a version of this technique where N is negative! In that case, 
#  cut (the absolute value of) N cards from the bottom of the deck onto the top. For example, to cut -4:
#  
#  Top          Bottom
#  0 1 2 3 4 5 6 7 8 9   Your deck
#  
#  0 1 2 3 4 5           Your deck
#              6 7 8 9   Cut cards
#  
#          0 1 2 3 4 5   Your deck
#  6 7 8 9               Cut cards
#  
#  6 7 8 9 0 1 2 3 4 5   Your deck
#  To deal with increment N, start by clearing enough space on your table to lay out all of the cards 
#  individually in a long line. Deal the top card into the leftmost position. Then, move N positions to 
#  the right and deal the next card there. If you would move into a position past the end of the space 
#  on your table, wrap around and keep counting from the leftmost card again. Continue this process until 
#  you run out of cards.
#  
#  For example, to deal with increment 3:
#  
#  
#  0 1 2 3 4 5 6 7 8 9   Your deck
#  . . . . . . . . . .   Space on table
#  ^                     Current position
#  
#  Deal the top card to the current position:
#  
#    1 2 3 4 5 6 7 8 9   Your deck
#  0 . . . . . . . . .   Space on table
#  ^                     Current position
#  
#  Move the current position right 3:
#  
#    1 2 3 4 5 6 7 8 9   Your deck
#  0 . . . . . . . . .   Space on table
#        ^               Current position
#  
#  Deal the top card:
#  
#      2 3 4 5 6 7 8 9   Your deck
#  0 . . 1 . . . . . .   Space on table
#        ^               Current position
#  
#  Move right 3 and deal:
#  
#        3 4 5 6 7 8 9   Your deck
#  0 . . 1 . . 2 . . .   Space on table
#              ^         Current position
#  
#  Move right 3 and deal:
#  
#          4 5 6 7 8 9   Your deck
#  0 . . 1 . . 2 . . 3   Space on table
#                    ^   Current position
#  
#  Move right 3, wrapping around, and deal:
#  
#            5 6 7 8 9   Your deck
#  0 . 4 1 . . 2 . . 3   Space on table
#      ^                 Current position
#  
#  And so on:
#  
#  0 7 4 1 8 5 2 9 6 3   Space on table
#  Positions on the table which already contain cards are still counted; they're not skipped. Of course, 
#  this technique is carefully designed so it will never put two cards in the same position or leave a 
#  position empty.
#  
#  Finally, collect the cards on the table so that the leftmost card ends up at the top of your deck, 
#  the card to its right ends up just below the top card, and so on, until the rightmost card ends up 
#  at the bottom of the deck.
#  
#  The complete shuffle process (your puzzle input) consists of applying many of these techniques. Here 
#  are some examples that combine techniques; they all start with a factory order deck of 10 cards:
#  
#  deal with increment 7
#  deal into new stack
#  deal into new stack
#  Result: 0 3 6 9 2 5 8 1 4 7
#  cut 6
#  deal with increment 7
#  deal into new stack
#  Result: 3 0 7 4 1 8 5 2 9 6
#  deal with increment 7
#  deal with increment 9
#  cut -2
#  Result: 6 3 0 7 4 1 8 5 2 9
#  deal into new stack
#  cut -2
#  deal with increment 7
#  cut 8
#  cut -4
#  deal with increment 7
#  cut 3
#  deal with increment 9
#  deal with increment 3
#  cut -1
#  Result: 9 2 5 8 1 4 7 0 3 6
#  Positions within the deck count from 0 at the top, then 1 for the card immediately below the top card, 
#  and so on to the bottom. (That is, cards start in the position matching their number.)
#  
#  After shuffling your factory order deck of 10007 cards, what is the position of card 2019?
#  
#  To begin, get your puzzle input.
#  
#  Your puzzle answer was 1234.
#  
#  The first half of this puzzle is complete! It provides one gold star: *
#  
#  --- Part Two ---
#  After a while, you realize your shuffling skill won't improve much more with merely a single 
#  deck of cards. You ask every 3D printer on the ship to make you some more cards while you check 
#  on the ship repairs. While reviewing the work the droids have finished so far, you think you see 
#  Halley's Comet fly past!
#  
#  When you get back, you discover that the 3D printers have combined their power to create for you a 
#  single, giant, brand new, factory order deck of 119315717514047 space cards.
#  
#  Finally, a deck of cards worthy of shuffling!
#  
#  You decide to apply your complete shuffle process (your puzzle input) to the deck 101741582076661 
#  times in a row.
#  
#  You'll need to be careful, though - one wrong move with this many cards and you might overflow your 
#  entire ship!
#  
#  After shuffling your new, giant, factory order deck that many times, what number is on the card that 
#  ends up in position 2020?
#  



class SpaceDeck:
    def __init__(self, cards):
        self.deck = [x for x in range(cards)]
        self.count = cards 
    
    def print(self, card_count = 20):
        # print out the top 20 and last 20 assuming the deck is bigger than 20 
        if self.count <= card_count * 2:
            # print the whole thing 
            output = [str(x) for x in self.deck]
            s = " ".join(output)
            print(f"Full Deck: [{s}]")
        else:
            start = [str(x) for x in self.deck[:card_count]]
            end = [str(x) for x in self.deck[-card_count:]]
            s1 = " ".join(start)
            s2 = " ".join(end)
            print(f"Start: {s1}\nEnd: {s2}")

    def deal_to_new_stack(self):
        """
        Effectively reverses the deck
        """
        self.deck.reverse()

    def cut(self, card_count):
        """
        Cut X cards from the top of the deck and put them on the bottom
        if X is negative, cut X cards from the bottom of the deck and put them on the top 
        """
        if 0 < card_count:
            top_chunk = self.deck[:card_count]
            remainder = self.deck[card_count:]
            self.deck = remainder + top_chunk
        elif 0 > card_count:
            bottom_chunk = self.deck[card_count:]
            remainder = self.deck[:card_count]
            self.deck = bottom_chunk + remainder
        
    def deal(self, increment):
        """
        deal with increment..
        """
        # starting at position 0, the next position is x from here, wrapping around 
        # so, very naive.. stand up a new array and use a for loop, slow but there we are.
        target_pos = 0
        new_deck = [-1] * self.count
        for deal in range(self.count):
            # deal this card 
            new_deck[target_pos] = self.deck[deal]
            # next position
            target_pos += increment 
            target_pos %= self.count 
        self.deck = new_deck 
             
    def find_card(self, card):
        """
        find which index the card is in the list 
        """
        return self.deck.index(card)



#d = SpaceDeck(10)
#d.print()
#d.deal_to_new_stack()
#d.print()
#d.cut(-4)
#d.deal(3)
#d.print()
         
def match_command(command, match_string):
    """
    return True, remainder if the string matches, False otherwise
    """
    match = False
    remainder = None
    if command.startswith(match_string):
        remainder = command[len(match_string):].strip()
        match = True
    return match, remainder

class ShuffleMaster:
    def __init__(self, deck_size):
        """
        create a shiny, new shuffle master 
        """
        self.deck = SpaceDeck(deck_size)

    def handle_command(self, the_command):
        """
        handle one command, throw if we don't understand it..
        """
        matched, value = match_command(the_command, "deal with increment")
        if matched:
            self.deck.deal(int(value))
            return True 

        matched, value = match_command(the_command, "deal into new stack")
        if matched:
            self.deck.deal_to_new_stack()
            return True 

        matched, value = match_command(the_command, "cut")
        if matched:
            self.deck.cut(int(value))
            return True

        matched, value = match_command(the_command, "info")
        if matched:
            print(f"info: {value}")
            return True

        raise ValueError(f"What the hell is [{the_command}]")
        

    def process_file(self, filename):
        """
        Read an instructions file and process the deck accordingly 
        """
        with open(filename, 'r') as f:
            for this_line in f:
                # is this a blank or comment line ?
                this_line = this_line.strip()
                if '' != this_line and '#' != this_line[0]:
                    # this is a line to process..
                    print(this_line)
                    self.handle_command(this_line)

        
    def print(self, card_count=20):
        """
        print the deck 
        """
        self.deck.print(card_count)

    def find_card(self, card):
        return self.deck.find_card(card)

def testit():
    sm = ShuffleMaster(10)
    sm.print()
    #sm.process_file('test_0369258147.txt')
    sm.process_file('test4.txt')
    sm.print()
    idx4 = sm.find_card(4)
    print(f"Card 4 is at {idx4}")

#testit()

print("creating deck")
sm = ShuffleMaster(119315717514047)
print("reading file")
sm.process_file('puzzle_input.txt')
sm.print()
idx2019 = sm.find_card(2019)
print(f"index of 2019 is {idx2019}")


