import requests

# INPUT / OUTPUT HELPERS ------------------------------------------------
def read_file(file_path):
    """
    Reads the content of a file.
    """
    with open(file_path, "r") as file:
        return file.read()

def create_file(file_path, file_content = None):
    """
    Creates a file with the given content or an empty file if no content is provided.
    """
    with open(file_path, "w") as file:
        file.write(file_content if file_content else "")

def download_input(year, day, session_token):
    """
    Downloads the input from the Advent of Code for the given year and day from the website using the provided session token and saves it to the correct file
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session_token}
    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        with open(f"./inputs/day{day}.txt", "w") as file:
            file.write(response.text)
    else:
        raise Exception(f"Failed to download input: {response.status_code}")

def get_current_day(file_path):
    """
    Extracts the day number from the file path.
    """
    return file_path.split('\\')[-1].split(".")[0].replace("day", "")

def read_input(day, split_lines=True, create_map=False, test=False):
    """
    Reads the input from the current days txt file.
    split_lines: if True, the input will be split by lines [default: True]
    test: if True, the test input will be read [default: False]
    """
    path = f"./inputs/day{day}.txt" if not test else "./inputs/test.txt"
    input_result = read_file(path)
    
    if create_map:
        return [list(line) for line in input_result.splitlines()]
    return input_result.splitlines() if split_lines else input_result


# CODE HELPERS ----------------------------------------------------------------------

def in_bounds(pos, input_map):
    """
    Checks if a position is inside the map.
    """
    y, x = pos
    return 0 <= x < len(input_map) and 0 <= y < len(input_map[0])

def print_map(input_map: list[list[object]]):
    """
    Prints the input map.
    """
    result = ""
    for row in input_map:
        result += "".join(str(cell) for cell in row) + "\n"
    print(result)

def eucleadian_distance_2d(pos_1, pos_2):
    """
    Calculates the Euclidean distance between two 2D points.
    """
    x_1, y_1 = pos_1
    x_2, y_2 = pos_2
    return ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5

def eucleadian_distance_3d(pos_1, pos_2):
    """
    Calculates the Euclidean distance between two 3D points.
    """
    x_1, y_1, z_1 = pos_1
    x_2, y_2, z_2 = pos_2
    return ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2 + (z_1 - z_2) ** 2) ** 0.5