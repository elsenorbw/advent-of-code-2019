import math 


# explore the atan2 results.. the results are based, I believe, on angle from 0,0
# 
# 

points = [
    (0, -10),
    (10, -10),
    (10, 0),
    (10, 10),
    (0, 10),
    (-10, 10),
    (-10, 0),
    (-10, -10)
]

for this_point in points:
    x = this_point[0]
    y = this_point[1]
    rads = math.atan2(y, x)
    degrees = rads * (180.0 / math.pi)
    adjusted = (degrees + 90 + 360) % 360
    distance = math.sqrt(((x-0) ** 2) + ((y-0) ** 2))
    print(f"{x},{y} -> {rads} {degrees} {adjusted} {distance}")

