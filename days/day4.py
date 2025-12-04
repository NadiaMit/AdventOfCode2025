import sys
import time

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input_data = helpers.read_input(day, test=isTest,  create_map=True)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# 8 directions with (y, x) pairs
# up, down, left, right, up-left, up-right, down-left, down-right
directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

# part 1
first_iteration_done = False
result_part_1 = 0

# part 2
result_part_2 =  0

# code for both parts
found_rolls = []

# check as long as there are more paper rolls to take
while True:
    found_rolls = []
    
    for y in range(0, len(input_data)):
        for x in range(0, len(input_data[0])):
            # get the current positions value
            if input_data[y][x] != '@':
                continue
            
            # check all 8 directions and count the paper rolls
            adjacent_rolls = 0
            for direction in directions:
                if 0 <= y + direction[0] < len(input_data) and 0 <= x + direction[1] < len(input_data[0]):
                    if input_data[y + direction[0]][x + direction[1]] == '@':
                        adjacent_rolls += 1

            # if fewer than 4 adjacent paper rolls -> curr_pos can be taken
            if adjacent_rolls < 4:
                found_rolls.append([y, x])
                
    # part 1
    if not first_iteration_done:
        result_part_1 += len(found_rolls)
        first_iteration_done = True
    
    # part 2
    result_part_2 += len(found_rolls)
    
    # remove the found rolls from the map
    for roll in found_rolls:
        input_data[roll[0]][roll[1]] = 'X'
    
    # if no more paper rolls can be taken -> end the process
    if len(found_rolls) == 0:
        break


# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 1508
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")