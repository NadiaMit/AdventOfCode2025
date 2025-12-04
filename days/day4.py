import sys
import time

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input_data = helpers.read_input(day, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# 8 directions with (y, x) pairs
# up, down, left, right, up-left, up-right, down-left, down-right
directions = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]   

paper_rolls = 0
# code for both parts
for y, row in enumerate(input_data):
    for x, curr_pos in enumerate(row):
        # get the current positions value
        if curr_pos != '@':
            continue
        
        adjacent_rolls = 0
        # check all 8 directions and count the paper rolls
        for direction in directions:
            if 0 <= y + direction[0] < len(input_data) and 0 <= x + direction[1] < len(row):
                if input_data[y + direction[0]][x + direction[1]] == '@':
                    adjacent_rolls += 1

        if adjacent_rolls < 4:
            paper_rolls += 1

# part 1
result_part_1 = paper_rolls

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 1508
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")