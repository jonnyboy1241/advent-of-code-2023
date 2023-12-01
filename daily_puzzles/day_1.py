# --- Day 1: Trebuchet?! ---

# https://adventofcode.com/2023/day/1

from shared.utils import get_input, print_answer

import re


def get_calibration_value(calibration_line: str) -> int:
    """
    Determine the calibration value from the calibration line.
    This is done by combining the first and last numeric characters in the calibration_line to get a 2-digit number
    :param calibration_line: The calibration line
    :returns: The calibration value as an int.
    """
    # Replace all non-numerical characters with nothing (we're left with only a numerical string)
    calibration_nums = re.sub("[^0-9]", "", calibration_line)

    # Append the first and last calibration num together and form a 2-digit int - this works even if there's only 1
    # calibration num. For example, if calibration_nums = "7", this will return 77 per the requirements
    return int(f"{calibration_nums[0]}{calibration_nums[-1]}")


if __name__ == "__main__":
    puzzle_input = get_input(1)

    # Part 1
    running_sum = 0

    for x in puzzle_input:
        running_sum += get_calibration_value(x)

    print_answer(1, running_sum)
