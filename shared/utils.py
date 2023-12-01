from typing import List


def get_input(day: int) -> List[str]:
    """
    Read the day's puzzle input from the text file and return it as a list of strings
    :param day: An integer representing the day of the challenge we're working on
    :returns: A list of strings
    """
    with open(rf"inputs\day_{day}.txt", "r") as f:
        raw_lines = f.readlines()

    return [line.strip("\n") for line in raw_lines]


def print_answer(part: int, answer: str or int):
    """
    Print the answer of the puzzle
    :param part: The solution part (1 or 2)
    :param answer: The answer - either a string or an int
    """
    print(f"ANSWER TO PART {part}: {answer}")
