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
result_part_1 = 0
result_part_2 =  0

for bank in input_data:
    # part 1 logic
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
    result_part_1 += max(max_left or 0, max_right or 0)
    
    # part 2 logic
    max_combination = bank[:12]
    for i in range(12, len(bank)):
        # remove first smaller digit from the left to get bigger combination
        remove_index = None
        for j in range(len(max_combination)-1):
            if max_combination[j] < max_combination[j+1]:
                remove_index = j
                break
        
        if remove_index is None:
            remove_index = len(max_combination) - 1
        
        new_combination = max_combination[:remove_index] + max_combination[remove_index+1:] + bank[i]
        
        if int(new_combination) > int(max_combination):
            max_combination = new_combination
    
    result_part_2 += int(max_combination)

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 17107
print(f"Part 2: {result_part_2}") # 169349762274117
print(f"Duration: {time.time() - start_time} seconds")