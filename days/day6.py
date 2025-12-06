import sys
import time
import math

sys.path.insert(1, sys.path[0].replace("days", "helpers"))
import helpers as helpers

# get daily input
day = helpers.get_current_day(__file__)
isTest = sys.argv[-1] == "test"
input_data = helpers.read_input(day, test=isTest)

# start timer for whole day puzzle after reading the input
start_time = time.time()

# part 1
parsed_data = [line.split() for line in input_data]
result_part_1 = 0
for i in range(0, len(parsed_data[0])):
    calculation = [line[i] for line in parsed_data]
    
    op = calculation[-1].strip()
    numbers = [int(x) for x in calculation[:-1] if x.strip().isdigit()]
    if op == '+':
        result_part_1 += sum(numbers)
    elif op == '*':
        result_part_1 += math.prod(numbers)

# part 2
result_part_2 =  0

# print the results
print(f"--- Day {day}: ---")
print(f"Part 1: {result_part_1}") # 6378679666679
print(f"Part 2: {result_part_2}")
print(f"Duration: {time.time() - start_time} seconds")