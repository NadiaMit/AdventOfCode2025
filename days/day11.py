import sys
import time
import functools
sys.setrecursionlimit(20000)

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

@functools.cache
def find_out_path(device, target):
    if device == target:
        return 1
    
    paths = 0
    for neighbor in devices.get(device, []):
        paths += find_out_path(neighbor, target)
    return paths

# part 1
result_part_1 = find_out_path('you', 'out')

# part 2
# possible paths 'srv' -> 'fft' -> 'dac' -> 'out'
paths_1 = find_out_path('svr', 'fft') * find_out_path('fft', 'dac') * find_out_path('dac', 'out')
# possible paths 'srv' -> 'dac' -> 'fft' -> 'out'
paths_2 = find_out_path('svr', 'dac') * find_out_path('dac', 'fft') * find_out_path('fft', 'out')

result_part_2 = paths_1 + paths_2

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 662
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")