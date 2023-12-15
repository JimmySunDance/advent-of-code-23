# Day thirteen of advent of code

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        ## Cut of excess rows to create matching pieces
        above = above[:len(below)]
        below = below[:len(above)]

        if above == below:
            return r
    return 0

def smudge_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
    
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r
    return 0



def main() -> None:
    print('Day 13')

    total = 0
    smudge_total = 0
    for blocks in  open('data/mirror.txt').read().split('\n\n'):
        grid = blocks.splitlines()

        row = find_mirror(grid)
        col = find_mirror(list(zip(*grid)))
        total += row * 100
        total += col

        row_s = smudge_mirror(grid)
        col_s = smudge_mirror(list(zip(*grid)))
        smudge_total += row_s * 100
        smudge_total += col_s

    print(f'Part 1: {total}')
    print(f'Part 2: {smudge_total}')
    return 


if __name__ == '__main__':
    main()