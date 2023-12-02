# --- Day 2: Cube Conundrum ---

# https://adventofcode.com/2023/day/2

from shared.utils import get_input, print_answer

from collections import defaultdict, namedtuple
from typing import Dict, List, Tuple

import re

# Named tuple that describes a draw from the bag
RBG = namedtuple("RBG", ["red", "green", "blue"])

GREEN = "green"
BLUE = "blue"
RED = "red"


def parse_data(puzzle_input: List[str]) -> Dict[int, List[Tuple[int, int, int]]]:
    """
    Read in the puzzle input and return a data structure that describes the game.
    :param puzzle_input: The puzzle's input
    :returns: A Dictionary, keyed by an integer (the game index) with values being a list of Tuples, representing each
    round of the game
    """
    parsed_puzzle = defaultdict(list)

    for line in puzzle_input:
        # The first value in this list will be "Game XX", the rest will be the rounds
        line_pieces = re.split("[:;]", line)

        game_index = int(line_pieces[0][5:])

        for round in line_pieces[1:]:
            colors_and_numbers = [x.strip() for x in round.split(",")]

            colors_and_numbers_dict = defaultdict(int)

            for entry in colors_and_numbers:
                num, color = entry.split(" ")
                colors_and_numbers_dict[color] = int(num)

            parsed_puzzle[game_index].append(RBG(red=colors_and_numbers_dict[RED],
                                                 green=colors_and_numbers_dict[GREEN],
                                                 blue=colors_and_numbers_dict[BLUE]))

    return parsed_puzzle


def check_game(parsed_data: Dict[int, List[Tuple[int, int, int]]]) -> int:
    """
    For every game, test and see if it was possible for the game to played with a bag containing
    12 reds, 13 greens, and 14 blues. Determine the sum of the game indexes that are possible
    :param parsed_data: The parsed puzzle
    :returns: The sum of the possible game indexes
    """
    sum = 0

    for index, rounds in parsed_data.items():
        if all(is_possible_game_with_replacement(round) for round in rounds):
            sum += index

    return sum


def is_possible_game_with_replacement(round: RBG) -> bool:
    """
    Determine whether the game is possible with a bag of 12 red, 13 green, and 14 blue
    """
    return round.red <= 12 and round.green <= 13 and round.blue <= 14


if __name__ == "__main__":
    puzzle_input = get_input(2)

    parsed_data = parse_data(puzzle_input)

    answer_part_1 = check_game(parsed_data)

    print_answer(1, answer_part_1)