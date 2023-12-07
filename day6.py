# Day six of the Advent of Code '23

# 1. part - Determine the number of ways you could beat the record in each 
# race and multiply them together.
import math as m

def quad(a, b, c): 
    return [(-b + (b**2 - 4*a*c)**0.5) / (2*a), (-b - (b**2 - 4*a*c)**0.5) / (2*a)]

def list_to_int(numbers: list[int]) -> int:
    return int(''.join([str(x) for x in numbers]))

def main() -> tuple:
    with open('data/boat_speeds.txt', 'r', encoding='utf-8') as input:
        times = list(map(int, input.readline().split()[1:]))
        records = list(map(int, input.readline().split()[1:]))

    total = 1
    for i, t in enumerate(times):
        r = quad(1, t, records[i])
        total *= m.ceil(r[0]) - m.floor(r[1]) - 1

    real_t = list_to_int(times)
    real_r = list_to_int(records)
    r = quad(1, -real_t, real_r)
    final = m.ceil(r[0]) - m.floor(r[1]) - 1

    return (total, final)

if __name__ == "__main__":
    print(main())