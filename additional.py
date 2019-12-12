# what does t>>6&1?t>>5:-t>>41t%13 do ?

for t in range(256):
    shifted = t >> 6
    conditional = shifted & 1
    five_shifted = t >> 5
    negative_t = -t
    neg_shifted = negative_t >> 41
    multiplied = neg_shifted * t 
    modulo = multiplied % 13 

    if conditional:
        print(f"{t:03} -> {shifted} -> {conditional} -> {five_shifted}")
    # so true only for 64-127, 192-255 which yield 2-3, 6-7 for those ranges 
    # the other side of things looks weird though
    else:
        print(f"{t:03} -> {shifted} -> {conditional} -> {negative_t} -> {neg_shifted} -> {multiplied} -> {modulo}")
