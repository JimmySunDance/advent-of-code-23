# Day twenty one of the advent of code 2023
#
#
from collections import deque

def step_fill(sr, sc, ss, grid):
    ans = set()
    seen = {(sr, sc)}
    q = deque([(sr, sc, ss)])

    while q:
        r, c, s = q.popleft()

        if s % 2 == 0:
            ans.add((r, c))
        if s == 0:
            continue

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "#" or (nr, nc) in seen:
                continue
            seen.add((nr, nc))
            q.append((nr, nc, s - 1))
    
    return len(ans)


def main() -> None:
    print('Day 21!')

    garden = open('data/garden_plan.txt').read().splitlines()
    sr, sc = next((r, c) for r, row in enumerate(garden) for c, ch in enumerate(row) if ch == 'S')

    size = len(garden)
    steps = 26501365

    print(f'Part 1: {step_fill(sr, sc, 64, garden)}')

    grid_width = steps // size - 1
    
    odd_grids = (grid_width // 2 * 2 + 1) ** 2
    even_grids = ((grid_width + 1) // 2 * 2) ** 2

    # Calc points in full grids
    odd_points = step_fill(sr, sc, size * 2 + 1, garden)
    even_points = step_fill(sr, sc, size * 2, garden)
    
    # Calc corners of the diamond
    corner_t = step_fill(size - 1, sc, size-1, garden)
    corner_b = step_fill(0, sc, size-1, garden)
    corner_l = step_fill(sr, size-1, size-1, garden)
    corner_r = step_fill(sr, 0, size-1, garden)

    # Calc small segment remainders
    small_tr = step_fill(size - 1, 0, size // 2 - 1, garden)
    small_tl = step_fill(size - 1, size - 1, size // 2 - 1, garden)
    small_br = step_fill(0, 0, size // 2 - 1, garden)
    small_bl = step_fill(0, size - 1, size // 2 - 1, garden)

    # Calc large segment remainders
    large_tr = step_fill(size - 1, 0, size * 3 // 2 - 1, garden)
    large_tl = step_fill(size - 1, size - 1, size * 3 // 2 - 1, garden)
    large_br = step_fill(0, 0, size * 3 // 2 - 1, garden)
    large_bl = step_fill(0, size - 1, size * 3 // 2 - 1, garden)


    final_answer = (
        odd_grids * odd_points + even_grids * even_points + 
        corner_t + corner_b + corner_l + corner_r + 
        (grid_width + 1) * (small_bl + small_br + small_tl + small_tr) +
        grid_width * (large_tr + large_tl + large_br + large_bl)
    )
    
    print(f'Part 2: {final_answer}')
    # My part 1 
    # for r, row in enumerate(garden):
    #     for c, col in enumerate(row):
    #         if col == 'S':
    #             sr, sc = r, c
    # for _ in range(64):
    #     possible = []
    #     for (s_x, s_y) in start:
    #         for (y, x) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
    #             if garden[s_x+x][s_y + y] != '#':
    #                 if (s_x+x, s_y+y) not in possible:
    #                     possible.append((s_x+x, s_y+y))
    #     start = possible
    # print(len(possible))
    
    return 

if __name__ == '__main__':
    main()