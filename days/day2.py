import re
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



result_part_1 = 0
result_part_2 =  0

# found regex patterns here: https://www.reddit.com/r/regex/comments/3devu1/how_to_match_on_repeated_substrings/
regex_pattern1 =  r'^(\d*)\1$'
regex_pattern2 = r'^(\d*)\1+$'

for range_pair in id_ranges:
    start, end = range_pair[0], range_pair[1]
    
    # check the whole id range for invalid IDs
    for curr_id in range(int(start), int(end) + 1):
        # regex check if substring repeats exactly twice
        if re.match(regex_pattern1, str(curr_id)):
            result_part_1 += curr_id
        
        # regex check if substring repeats more than twice
        if re.match(regex_pattern2, str(curr_id)):
            result_part_2 += curr_id

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 12599655151
print(f"Part 2: {result_part_2}") # 20942028255
print(f"Duration: {time.time() - start_time} seconds")