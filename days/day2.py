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
input_data = input_data[0].split(',')
id_ranges = [[line.split('-')[0], line.split('-')[1]] for line in input_data]

# part 1
result_part_1 = 0

for range_pair in id_ranges:
    start, end = range_pair[0], range_pair[1]
    
    # check the whole id range for invalid IDs
    for curr_id in range(int(start), int(end) + 1):
        string_id = str(curr_id)
        id_len = len(string_id)
        
        # only even length IDs can be checked for invalidity
        if id_len % 2 != 0:
            continue
        
        # check if the first half is in the second half -> repeated twice
        half_len = id_len // 2
        if string_id[: half_len] in string_id[half_len:]:
            result_part_1 += curr_id

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 12599655151
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")