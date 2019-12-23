#
#  run.ss - a Spring Script file 
#  
#  There are only three instructions available in springscript:
#  
#  AND X Y sets Y to true if both X and Y are true; otherwise, it sets Y to false.
#  OR X Y sets Y to true if at least one of X or Y is true; otherwise, it sets Y to false.
#  NOT X Y sets Y to true if X is false; otherwise, it sets Y to false.
#  In all three instructions, the second argument (Y) needs to be a writable register (either T or J). 
#  The first argument (X) can be any register (including A, B, C, or D).
#
#  Readable registers are A - step directly in front has floor ? TRUE - Yes, there is floor, FALSE - No floor 
#                         B - two steps in front 
#                         .. I - nine steps in front 
#
#                         T - temporary storage - starts FALSE 
#                         J - the jump register, if TRUE then we will jump, starts FALSE  
#

# We land on top of the square 4 characters in front so we basically need to decide whether this is a good time to jump
# First question, is there anything to jump over ? If not then we can keep on trucking.
# Ignoring the step directly in front as we will have to jump if that's missing and there's logic for that at the end
# So... is there anything to jump ?

# ok, so if we have something to jump then we need to not jump if there's nothing to land on..

# so far so good.. but we have a problem with this layout 
#  ####.#.#...###  
# so how can we identify this situation ?
# maybe we need to look at how far forwards we can jump ?
# tricky one. So actually we can have a look at it this way.. 
# for any given hole, what's the latest we can jump ?

# right, quick test - if there's a hole at B (2 in front), then we would jump one in front ideally
# so, if B is missing..
#NOT B T
#OR T J 
# now, if B is missing then J is set 
# but.. could we jump later ?
# T is set to TRUE at this point, so is J 
# we need to unset J if E is TRUE 
#NOT E T 
#AND T J 
# but a second problem arises if we land where we're going to land (D), will we need to jump immediately ?
# if so, is there somewhere to land ?
# weird situation but ok.. so we may have decided not to jump but is there a 

# actually - new plan 
# if we want to jump then.. don't jump if we can't double bounce or land and walk  
# jump if we can bounce 2 goes immediately or we can land and walk 

# so, do we want to jump ?
# is there anything missing in B or C ?
# ignoring A as missing A is an automatic jump 
NOT B T
OR T J 
NOT C T
OR T J

# ok, so now J is set if we want to jump, can we bounce twice ?
# we can bounce twice, we'll land at D, jump again and land at H 
# get the Temp register set to true if we're jumping 
OR J T
# can we bounce twice ?
AND H T 
# now the temp register will be false if we can't land there..
OR E T
# ok, so Temp will be set to true if either of the landing potentials are good..
AND T J 

# sanity check, is there something to land on ? if not then jumping is probably bad
AND D J 

# right, so if there is a hole directly in front of us then we need to jump regardless of what we previously thought
NOT A T
OR T J

# and let her rip!
RUN
