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
split_idx = input_data.index("")
ranges = input_data[:split_idx]
inventory = input_data[split_idx + 1:]

fresh_inventory = set()
for r in ranges:
    start, end = map(int, r.split("-"))
    for inv in inventory:
        inv_num = int(inv)
        if start <= inv_num <= end:
            fresh_inventory.add(inv_num)

# part 1
result_part_1 = len(fresh_inventory)

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 681
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")