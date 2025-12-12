![](https://img.shields.io/badge/stars_⭐-17-yellow)
![](https://img.shields.io/badge/days_completed_📅-8-blue)
![](https://img.shields.io/badge/days_half_completed_🌗-1-white)

# Advent of Code 2025 in Python [![Python](https://skillicons.dev/icons?i=python)](https://skillicons.dev)

This is my try on the Advent of code of 2025 challanges in Python.

## My Progress 17/24⭐

- Day 1 - [Secret Entrance](https://adventofcode.com/2025/day/1): ⭐⭐
- Day 2 - [Gift Shop](https://adventofcode.com/2025/day/2): ⭐⭐
- Day 3 - [Lobby](https://adventofcode.com/2025/day/3): ⭐⭐
- Day 4 - [Printing Department](https://adventofcode.com/2025/day/4): ⭐⭐
- Day 5 - [Cafeteria](https://adventofcode.com/2025/day/5): ⭐⭐
- Day 6 - [Trash Compactor](https://adventofcode.com/2025/day/6): ⭐⭐
- Day 7 - [Laboratories](https://adventofcode.com/2025/day/7): ⭐⭐
- ...
- Day 9 - [Movie Theater](https://adventofcode.com/2025/day/9): ⭐
- ...
- Day 11 - [Reactor](https://adventofcode.com/2025/day/11): ⭐⭐

## Structure

- `main.py` - file: this file provides code to automatically create the needed files for each day and run the code.
- `days` - folder: the code for each day will be in the days folder as a `dayX.py` file.
- `inputs` - folder: all my input data for each day is saved the inputs folder as a `dayX.txt` file. I also have a `test.txt` file, that I use for the example input of each days puzzle.
- `helpers` - folder: contains my `helpers.py` and `template.py` files. The helper files has some functions to read the input data an I am pretty sure, I will add some other helping functions if I see that puzzles will need some generic functionality more than once. And the template file is my base for every days puzzle.

## Automatic input download notice

If you want to use the automatic input download feature, you need to create a `.env` file in the root folder of the project with your valid session token from the Advent of Code website like this:

```bash
SESSION_TOKEN=your_session_token_here
```

Additionally you will have to set the `year` variable in the `main.py` file to the wanted year (default is 2025), otherwise the input download will not work or download the input for the wrong year.

## Create a Day

To create a new day you can run the following command:

`python main.py create <day>`

where `<day>` is the number of the day you want to create.

This will create a new file in the `days` folder called `day<day>.py` (with the content of the `template.py` file is existend) and a new file in the `inputs` folder called `day<day>.txt`. If you have the automatic input download feature set up correctly (see "Automatic input download notice" above), it will also try to download your input data for that day from the Advent of Code website and fill the `day<day>.txt` file with it.

(You can also create the files by hand if you want of course)

## Run Days

There are two ways to run a day:

### 1. Run from main.py

Simply run the following command:

`python main.py run <day> [test]`

where `<day>` is the number of the day you want to run and `[test]` is an optional parameter to run the day with the test input file otherwise it will automatically use the day's input file.
<br><br><br>
Example for day1 with day1 input file:

`python main.py run 1`

Example for day1 with the test input:

`python main.py run 1 test`

### 2. Run from the day file

Simply run the wanted days file with python:

`python .\days\day<day>.py [test]`

where `<day>` is the number of the day you want to run and `[test]` is an optional parameter to run the day with the test input file otherwise it will automatically use the day's input file.
<br><br><br>
Example for day1 with day1 input file:

`python .\days\day1.py`

Example for day1 with the test input:

`python .\days\day1.py test`
