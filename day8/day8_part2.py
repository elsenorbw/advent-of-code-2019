#  --- Day 8: Space Image Format ---
#  The Elves' spirits are lifted when they realize you have an opportunity to reboot one of their Mars rovers, and so they are curious if you would spend a brief sojourn on Mars. You land your ship near the rover.
#  
#  When you reach the rover, you discover that it's already in the process of rebooting! It's just waiting for someone to enter a BIOS password. The Elf responsible for the rover takes a picture of the password (your puzzle input) and sends it to you via the Digital Sending Network.
#  
#  Unfortunately, images sent via the Digital Sending Network aren't encoded with any normal encoding; instead, they're encoded in a special Space Image Format. None of the Elves seem to remember why this is the case. They send you the instructions to decode it.
#  
#  Images are sent as a series of digits that each represent the color of a single pixel. The digits fill each row of the image left-to-right, then move downward to the next row, filling rows top-to-bottom until every pixel of the image is filled.
#  
#  Each image actually consists of a series of identically-sized layers that are filled in this way. So, the first digit corresponds to the top-left pixel of the first layer, the second digit corresponds to the pixel to the right of that on the same layer, and so on until the last digit, which corresponds to the bottom-right pixel of the last layer.
#  
#  For example, given an image 3 pixels wide and 2 pixels tall, the image data 123456789012 corresponds to the following image layers:
#  
#  Layer 1: 123
#           456
#  
#  Layer 2: 789
#           012
#  The image you received is 25 pixels wide and 6 pixels tall.
#  
#  To make sure the image wasn't corrupted during transmission, the Elves would like you to find the layer that contains the fewest 0 digits. On that layer, what is the number of 1 digits multiplied by the number of 2 digits?
#  
#  Your puzzle answer was 1742.
#  
#  The first half of this puzzle is complete! It provides one gold star: *
#  
#  --- Part Two ---
#  Now you're ready to decode the image. The image is rendered by stacking the layers and aligning the pixels with the same positions in each layer. The digits indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is transparent.
#  
#  The layers are rendered with the first layer in front and the last layer in back. So, if a given position has a transparent pixel in the first and second layers, a black pixel in the third layer, and a white pixel in the fourth layer, the final image would have a black pixel at that position.
#  
#  For example, given an image 2 pixels wide and 2 pixels tall, the image data 0222112222120000 corresponds to the following image layers:
#  
#  Layer 1: 02
#           22
#  
#  Layer 2: 11
#           22
#  
#  Layer 3: 22
#           12
#  
#  Layer 4: 00
#           00
#  Then, the full image can be found by determining the top visible pixel in each position:
#  
#  The top-left pixel is black because the top layer is 0.
#  The top-right pixel is white because the top layer is 2 (transparent), but the second layer is 1.
#  The bottom-left pixel is white because the top two layers are 2, but the third layer is 1.
#  The bottom-right pixel is black because the only visible pixel in that position is 0 (from layer 4).
#  So, the final image looks like this:
#  
#  01
#  10
#  What message is produced after decoding your image?

class SpaceImage:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size 
        self.layers = {}
    
    def layer_count(self):
        return len(self.layers.keys())

    def count_instances_of(self, layer, the_value):
        """ Return a count of how many instances of the_value exist in the specified layer """
        result = 0
        if layer in self.layers:
            for x in range(self.x_size):
                for y in range(self.y_size):
                    this_value = self.get_one_value(layer, x, y)
                    if this_value == the_value:
                        result += 1

        return result

    def get_one_value(self, layer, x, y):
        return self.layers[layer][y][x]


    def store_one_value(self, layer, x, y, the_value):
        # check that the target indices exist, they should and we will allocate layer by layer
        if layer not in self.layers:
            self.layers[layer] = [[-42 for column in range(self.x_size)] for row in range(self.y_size)]
        # and store 
        self.layers[layer][y][x] = the_value

    def print(self):
        print(f"Space Image ({len(self.layers.keys())} layers of {self.x_size}x{self.y_size})")
        for this_layer_key in sorted(self.layers.keys()):
            this_layer = self.layers[this_layer_key]
            # print out one layer
            print(f"Layer {this_layer_key}")
            # for every row, print out all the columns 
            for y in range(self.y_size):
                s = ''
                for x in range(self.x_size):
                    the_val = this_layer[y][x]
                    s += f"{the_val:02} "
                print(f"  {s}")
    
    def print_flattened(self):
        """ The 2 digits are transparent, starting at layer 1 """
        total_layers = self.layer_count()
        for y in range(self.y_size):
            s = ''
            for x in range(self.x_size):
                layer = 0
                this_final_value = self.get_one_value(layer, x, y)
                while 2 == this_final_value and layer < total_layers:
                    layer += 1
                    this_final_value = self.get_one_value(layer, x, y)
                # and output the value 
                if 1 == this_final_value:
                    s += "X"
                else:
                    s += " "
            print(f"{s}")

    def from_data(self, data):
        """ Read the input data and store it in layers[] -> rows[] -> column[]"""
        #
        #  Loop through the values remembering where we are up to 
        #
        individual_values = [int(x) for x in data]
        current_x = 0
        current_y = 0
        current_layer = 0 
        for this_value in individual_values:
            # ensure that this space exists 
            self.store_one_value(current_layer, current_x, current_y, this_value)
            # and increment the counters
            current_x += 1
            if current_x >= self.x_size:
                current_x = 0
                current_y += 1
                if current_y >= self.y_size:
                    current_y = 0
                    current_layer += 1
            
def read_puzzle_input(filename):
    result = ''
    with open(filename, 'r') as f:
        for this_line in f:
            clean_line = this_line.strip()
            if '' != clean_line:
                result += clean_line
    return result

# test image 
test_data = "123456789012"
image = SpaceImage(3, 2)
image.from_data(test_data)
image.print()

# real image 
puzzle_input = read_puzzle_input('puzzle_input.txt')
print(f"*{puzzle_input}*")
image = SpaceImage(25, 6)
image.from_data(puzzle_input)
image.print()

# answer the questions, remembering that this is 1-based (the elves are savages)
# find the layer with the fewest 1 digits, on that layer what is the count of 
# the 1 digits multiplied by the count of the 2 digits 

# seems like if we have a count_instances_of(layer, the_value) then we'd be done very quickly
best_count = None
best_layer_index = None
for this_layer in range(image.layer_count()):
    this_layer_count = image.count_instances_of(this_layer, 0)
    if best_count is None or this_layer_count < best_count:
        best_count = this_layer_count 
        best_layer_index = this_layer
# and now multiply the winning layer 
best_one_count = image.count_instances_of(best_layer_index, 1)
best_two_count = image.count_instances_of(best_layer_index, 2)
result = best_one_count * best_two_count
print(result)

image.print_flattened()





