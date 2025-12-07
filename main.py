import os
import sys
from dotenv import load_dotenv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'helpers')))
import helpers

# load .env file
load_dotenv()

# constant paths
INPUTS_FOLDER = "./inputs"
DAYS_FOLDER = "./days"
TEMPLATE_FILE = "./helpers/template.py"

def create_day(day, year):
    """
    Prepares all needed files for a new day.
        - `dayX.py` in the `days` folder with the template content from `template.py`
        - `dayX.txt` in the `inputs` folder
    """
    # set the file paths
    input_file_path = os.path.join(INPUTS_FOLDER, f"day{day}.txt")
    day_file_path = os.path.join(DAYS_FOLDER, f"day{day}.py")

    # check if the folders exist, otherwise give an error message
    if not os.path.exists(INPUTS_FOLDER) or not os.path.exists(DAYS_FOLDER):
        print(f"ERROR: Folders '{INPUTS_FOLDER}' and/or '{DAYS_FOLDER}' not found!\nPlease make sure they exist and to run the script from the root folder.")
        return

    # create the input file dayX.txt
    helpers.create_file(input_file_path)
    
    # try to download the input file from the website
    try:
        session_token = os.getenv("SESSION_TOKEN")
        if not session_token:
            raise Exception("SESSION_TOKEN not found in .env file.")
        helpers.download_input(year=year, day=day, session_token=session_token)
    except Exception as e:
        print(f"WARNING: Could not download input for day {day}. Error: {e}")

    # create the dayX.py file and fill it with the template content
    if os.path.exists(TEMPLATE_FILE):
        template = helpers.read_file(TEMPLATE_FILE)
        helpers.create_file(day_file_path, template)
    else:
        print(f"WARNING: Template file '{TEMPLATE_FILE}' not found. Creating an empty Python file for day {day}.")
        helpers.create_file(day_file_path)

    print(f"Created {input_file_path} and {day_file_path}")

def run_day(day):
    """
    Runs the code of a specific day with the day input or the test input.
    """
    # set the file paths
    day_file = os.path.join(DAYS_FOLDER, f"day{day}.py")

    # check if the day file exists
    if not os.path.exists(day_file):
        print(f"Day {day} not found.")
        return

    # run the day code
    with open(day_file, "r") as file:
        code = file.read()
        exec(code, {'helpers': helpers, 'sys': sys, '__file__': day_file})


if __name__ == "__main__":
    # Main function that either creates a new day or runs a specific day.
    # Usage:
    #     - Create a new day: `python main.py create <day_number>`
    #     - Run a specific day: `python main.py <day_number> [test]`

    # check if a command was provided
    if len(sys.argv) < 3:
        print("Please provide a command and a day number.")
        sys.exit()

    # get the command and the day number
    command = sys.argv[1]
    day_number = sys.argv[2]
    year = 2025
    
    # execute the command based on the input
    if command == "create":
        create_day(day_number, year=year)
    else:
        run_day(day_number)