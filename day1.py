# Day one of the Advent of Code '23
#
# On each line, the calibration value can be found by combining the first 
# digit and the last digit (in that order) to form a single two-digit number.
#
# Consider your entire calibration document. What is the sum of all 
# of the calibration values?

def numbers_numbers(lines: list[str]) -> int:
    num_str = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 
               'eight', 'nine']
    ans = 0
    for line in lines:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(num_str):
                if line[i:].startswith(val):
                    digits.append(str(d+1))
        score = int(digits[0] + digits[-1])
        ans += score

    return ans


def main() -> None:
    with open('data/calibration_values.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(numbers_numbers(lines))

if __name__ == "__main__":
    main()