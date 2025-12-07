import sys
import time

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input_data = helpers.read_input(day, test=isTest, create_map=True)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# code for both parts

# set starting mark down -> directly below the S
input_data[1][input_data[0].index('S')] = '|'

splits = 0 
for y in range(len(input_data)):
    for x in range(len(input_data[0])):
        # if path downwards -> check if splitting happens or simply go down
        if input_data[y][x] == '|':
            if (y+1) < len(input_data) and input_data[y+1][x] == '^':
                left = x - 1
                right = x + 1
                if left >= 0 and right < len(input_data[0]):
                    input_data[y+1][left] = '|'
                    input_data[y+1][right] = '|'
                    splits += 1
            else:
                if (y+1) < len(input_data):
                    input_data[y+1][x] = '|'

# part 1
result_part_1 = splits

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 1585
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")