# Day three of the Advent of Code '23
# 
# add up all the part numbers in the engine schematic any number adjacent to a 
# symbol, even diagonally, is a "part number" and should be included in your 
# sum. What is the sum of all of the part numbers in the engine schematic?
#
# https://github.com/BroFromSpace/advent-of-code-2023/tree/master/advent_of_code_2023/day_3

from collections import defaultdict
import string

SYMBOLS = set(string.punctuation.replace('.', ''))

def get_part_numbers_sum(lines: list[str]):
    schema_height = len(lines) - 1
    schema_length = len(lines[0]) - 1

    def _get_nearest_symbols(self_x: int, self_y: int, self_l: int) -> set[str]:
        x_0 = max(0, self_x - self_l)
        y_0 = max(0, self_y - 1)
        x_1 = min(schema_length, self_x + 1)
        y_1 = min(schema_height, self_y + 1)

        return set(lines[y_0][x_0:x_1 + 1] + lines[self_y][x_0:x_1 + 1] + lines[y_1][x_0:x_1 + 1])

    part_numbers_sum = 0
    for y, line in enumerate(lines):
        number_chunk = ""
        for x, char in enumerate(line):
            if char.isdigit():
                number_chunk += char

                if x == schema_length or not line[x + 1].isdigit():
                    nearest_symbols = _get_nearest_symbols(x, y, len(number_chunk))

                    if SYMBOLS.intersection(nearest_symbols):
                        part_numbers_sum += int(number_chunk)
                    number_chunk = ""
    return part_numbers_sum


def get_gear_ratio_sum(lines: list[str]) -> int:
    schema_height = len(lines) - 1
    schema_length = len(lines[0]) - 1

    def _find_gear_positions(self_x: int, self_y: int, self_l: int) -> set[tuple[int, int]]:
        x_0 = max(0, self_x - self_l)
        y_0 = max(0, self_y - 1)
        x_1 = min(schema_length, self_x + 2)
        y_1 = min(schema_height, self_y + 2)

        return {
            (y, x) for y in range(y_0, y_1)
            for x in range(x_0, x_1) if lines[y][x] == "*"
        }

    gear_pos_num_map = defaultdict(list)

    for y, line in enumerate(lines):
        number_chunk = ""
        for x, char in enumerate(line):
            if char.isdigit():
                number_chunk += char

                if x == schema_length or not line[x + 1].isdigit():
                    for position in _find_gear_positions(x, y, len(number_chunk)):
                        gear_pos_num_map[position].append(int(number_chunk))

                    number_chunk = ""

    return sum((v[0] * v[1] for v in gear_pos_num_map.values() if len(v) == 2))

def main() -> None:
    with open("data/engine_schematic.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(get_part_numbers_sum(lines))
    print(get_gear_ratio_sum(lines))

if __name__ == '__main__':
    main()


    