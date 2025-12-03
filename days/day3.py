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
biggest_joltages = []

for bank in input_data:
    batteries = [int(bat) for bat in bank]
    max_joltage = max(batteries)
    max_index = batteries.index(max_joltage)
    
    left_batteries = batteries[:max_index]
    right_batteries = batteries[max_index+1:]
    
    max_left, max_right = None, None
    if left_batteries:
        max_left = int(f"{max(left_batteries)}{max_joltage}")
    if right_batteries:
        max_right = int(f"{max_joltage}{max(right_batteries)}")
    
    # add the biggest joltage to the result
    biggest_joltages.append(max(max_left or 0, max_right or 0))


# part 1
result_part_1 = sum(biggest_joltages)
# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 17107
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")