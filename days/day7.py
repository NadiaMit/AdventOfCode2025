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
non_path_symbols = ['^', 'S', '.']
beam_symbol = '^'
# set starting mark down -> directly below the S (with a path weight)
input_data[1][input_data[0].index('S')] = '1'

splits = 0 
for y in range(len(input_data)):
    for x in range(len(input_data[0])):
        # if path downwards -> check if splitting happens or simply go down
        if input_data[y][x] not in non_path_symbols:
            current_weight = int(input_data[y][x])
            # if split -> calculate the new path weights based on the pascals triangle
            if (y+1) < len(input_data) and input_data[y+1][x] == beam_symbol:
                if (x - 1) >= 0 and (x + 1) < len(input_data[0]):
                    # left split
                    new_weight = current_weight
                    if (x - 2) >= 0 and input_data[y][x - 2] not in non_path_symbols and input_data[y+1][x-2] == beam_symbol:
                        new_weight += int(input_data[y][x - 2])
                    if input_data[y][x - 1] not in non_path_symbols:
                        new_weight += int(input_data[y][x - 1])
                    input_data[y+1][x - 1] = str(new_weight)
                    
                    # right split
                    new_weight = current_weight
                    if (x + 2) < len(input_data[0]) and input_data[y][x + 2] not in non_path_symbols and input_data[y+1][x+2] == beam_symbol:
                        new_weight += int(input_data[y][x + 2])
                    if input_data[y][x + 1] not in non_path_symbols:
                        new_weight += int(input_data[y][x + 1])
                    input_data[y+1][x + 1] = str(new_weight)
                    
                    # count split
                    splits += 1
            
            # if go straight down -> set it to the same path weight
            elif (y+1) < len(input_data):
                next_weight = int(input_data[y+1][x]) if input_data[y+1][x] not in non_path_symbols else 0
                if current_weight > next_weight:
                    input_data[y+1][x] = str(current_weight)

# part 1
result_part_1 = splits

# part 2
result_part_2 =  sum([int(element) for element in input_data[-1] if element not in non_path_symbols])

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 1585
print(f"Part 2: {result_part_2}") # 16716444407407
print(f"Duration: {time.time() - start_time} seconds")