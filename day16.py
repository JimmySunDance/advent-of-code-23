# Day sixteen of the advent of code
#
# Breadth first fill

from collections import deque # Doubly Ended Queue

def calc(r, c, dr, dc, grid):
     # row, col, delta_row, delta_col
    a = [(r, c, dr, dc)]
    seen = set()
    q = deque(a)

    while q:
        r, c, dr, dc = q.popleft() 
        r += dr
        c += dc

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue
        ch = grid[r][c]

        if ch == '.' or (ch == '-' and dc != 0) or (ch == '|' and dr != 0):
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == '/':
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        elif ch == '\\':
            dr, dc = dc, dr
            if (r, c, dr, dc) not in seen:
                seen.add((r, c, dr, dc))
                q.append((r, c, dr, dc))
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == '|' else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in seen:
                    seen.add((r, c, dr, dc))
                    q.append((r, c, dr, dc))

    return len({(r, c) for (r, c, _, _) in seen})


def main() -> None:
    print('Day 16')

    grid = open('data/mirror_array.txt').read().splitlines()

    energized = calc(0, -1, 0, 1, grid)
    print(f'Part 1: {energized}')
   

    max_energize = 0
    for r in range(len(grid)):
        max_energize = max(max_energize, calc(r, -1, 0, 1, grid))
        max_energize = max(max_energize, calc(r, len(grid[0]), 0, -1, grid))
    for c in range(len(grid)):
        max_energize = max(max_energize, calc(-1, c, 1, 0, grid))
        max_energize = max(max_energize, calc(len(grid), c, -1, 0, grid))
    
    print(f'Part 2: {max_energize}')
    return

if __name__ =='__main__':
    main()