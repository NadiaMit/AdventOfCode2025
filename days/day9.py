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

# code for both parts
input_data = [[int(x), int(y)] for x, y in (line.split(",") for line in input_data)]

largest_area = 0
for i in range(len(input_data)):
    curr_x, curr_y = input_data[i]
    for j in range(i, len(input_data)):
        other_x, other_y = input_data[j]
        
        width = abs(curr_x - other_x) +1
        height = abs(curr_y - other_y) +1
        
        area = helpers.rectangle_area(width, height)
        if area > largest_area:
            largest_area = area

# part 1
result_part_1 = largest_area

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 4777824480
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")