# Day fourteen of the advent of code 2023

def slide_rocks(grid):
    new_grid=[]
    for line in grid:
        roll=[]
        for group in line.split('#'):
            roll.append("".join(sorted(list(group), reverse=True)))
        new_pos = '#'.join(roll)
        new_grid.append(new_pos)
    return tuple(new_grid)


def cycle(grid):
    for _ in range(4):
        grid = tuple(map(''.join, zip(*grid)))
        grid = slide_rocks(grid)
        grid = tuple(row[::-1] for row in grid)
    return grid

def weight_sum(grid):
    return sum(row.count('O')*(len(grid) - r) for r, row in enumerate(grid))

def main() -> None:
    print('Day 14!')
    s_grid = tuple(open('data/boulders.txt').read().splitlines())

    grid = slide_rocks(list(map(''.join, zip(*s_grid))))
    grid = list(map(''.join, zip(*grid)))
    weight = weight_sum(grid)

    print(f'Part 1: {weight}')

    s_grid=tuple(s_grid)
    seen={s_grid}
    array = [s_grid]
    iter=0

    while True:
        iter+=1
        s_grid = cycle(s_grid)
        if s_grid in seen:
            break
        seen.add(s_grid)
        array.append(s_grid)

    first = array.index(s_grid)

    s_grid = array[(1000000000 - first)%(iter - first) + first]
    weight = weight_sum(s_grid)
    print(f'Part 2: {weight}')
    return 

if __name__ == '__main__':
    main()