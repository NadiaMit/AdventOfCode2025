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
devices = {}
for line in input_data:
    device, outputs = line.split(":")
    devices.setdefault(device.strip(), []).extend([out.strip() for out in outputs.strip().split(" ")])

def find_out_path(device, visited=None):
    if visited is None:
        visited = []
    current_visited = visited + [device]

    if device == "out":
        return 1
    
    outputs = devices.get(device, [])
    paths = 0
    for out in outputs:
        if out not in current_visited:
            paths += find_out_path(out, current_visited)
    return paths

# part 1
result_part_1 = find_out_path('you', [])

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 662
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")