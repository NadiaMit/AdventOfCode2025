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
fresh_ranges = []

for r in ranges:
    start, end = map(int, r.split("-"))
    
    # part 1 -> get only fresh ids
    for inv in inventory:
        inv_num = int(inv)
        if start <= inv_num <= end:
            fresh_inventory.add(inv_num)
    
    # part 2 -> store the ranges that overlap
    if not fresh_ranges:
        fresh_ranges.append((start, end))
    else:
        overlaps = []
        for fr_start, fr_end in fresh_ranges:
            # check for overlap in any direction and then create new range with lowest start and highest end
            if fr_start <= start <= fr_end or fr_start <= end <= fr_end or start <= fr_start <= end or start <= fr_end <= end:
                overlaps.append((fr_start, fr_end))
        
        if overlaps:
            new_min = float("inf")
            new_max = -1
            
            for o_start, o_end in overlaps:
                fresh_ranges.remove((o_start, o_end))
                new_min = min(new_min, o_start, start)
                new_max = max(new_max, o_end, end)
                
            fresh_ranges.append((new_min, new_max))
        else:
            fresh_ranges.append((start, end))

# part 1
result_part_1 = len(fresh_inventory)

# part 2
result_part_2 =  0
for start, end in fresh_ranges:
    result_part_2 += end - start + 1

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 681
print(f"Part 2: {result_part_2}") # 348820208020395
print(f"Duration: {time.time() - start_time} seconds")