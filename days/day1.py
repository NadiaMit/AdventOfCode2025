import sys
import time

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__) # pyright: ignore[reportAttributeAccessIssue]
isTest = sys.argv[-1] == "test"
input = helpers.read_input(day, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts
dial = 50
min = 0
max = 99
total_clicks = max - min + 1

# part 1
zero = 0

# part 2
zero_rotation = 0

for rotation in input:
  direction = rotation[0]
  amount = int(rotation[1:])
  
  before_dial = dial
  
  # if the amount is bigger than the dial range (99-0+1 = 100), reduce it to not count the full rotations
  if(abs(amount) > total_clicks): 
    zero_rotation += abs(amount) // total_clicks
    amount = abs(amount) % total_clicks
  
  if direction == 'R':
    dial += amount
    
    # if dial is over max, add the overflowing value to min
    if(dial > max):
      dial = min + (dial - max - 1)
      
      # only count zero in rotation if before and after aren't already zero
      if (before_dial != 0 and dial != 0):
        zero_rotation += 1
  
  if direction == 'L':
    dial -= amount
    
    # if dial is below min, add the overflowing value to max
    if(dial < min):
      dial = max - (min - dial - 1)
      
      # only count zero in rotation if before and after aren't already zero
      if (before_dial != 0 and dial != 0):
        zero_rotation += 1
  
  if dial == 0:
    zero += 1


result_part_1 = zero
result_part_2 = zero_rotation + zero

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 1129
print(f"Part 2: {result_part_2}") # 6638
print(f"Duration: {time.time() - start_time} seconds")
