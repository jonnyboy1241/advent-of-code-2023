# --- Day 1: Trebuchet?! ---

# https://adventofcode.com/2023/day/1

from shared.utils import get_input, print_answer

import re


def get_calibration_value(calibration_line: str, include_spelled_out_values: bool=False) -> int:
    """
    Determine the calibration value from the calibration line.
    This is done by combining the first and last numeric characters in the calibration_line to get a 2-digit number
    :param calibration_line: The calibration line
    :param include_spelled_out_values: Boolean flag, if true, include spelled out values (if one is in the calibration
    value, treat it as the number 1)
    :returns: The calibration value as an int.
    """
    if include_spelled_out_values:
        # If the include_spelled_out_values flag is set, replace the spelled out value with the corresponding number
        # before determining the calibration value
        translations = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }

        for string, value in translations.items():
            # This replacement must occur because digits can overlap here.
            # The last digit in the calibration line can be something like this:
            # "threeight" - which should be parsed as 38
            # Performing a regular replace will result in "3ight" which will later translate to 33.
            # Instead, the result of this replace will be "three3threeight8eight" which will result in the correct
            # answer of 38.
            # This is a dirty hack to handle the overlaps (I didn't want to write out a regex - that would also need
            # to deal with overlapping)
            calibration_line = calibration_line.replace(string, f"{string}{value}{string}")

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

    # Part 2
    running_sum = 0

    for x in puzzle_input:
        running_sum += get_calibration_value(x, include_spelled_out_values=True)

    print_answer(2, running_sum)
