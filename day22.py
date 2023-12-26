# Day twenty two of the advent of code 2023
#
#
from collections import deque

def overlaps(brickA, brickB):
    """ Check to see if bricks overlap in x ad y 
    bricks in form [x1, y1, z1, x2, y2, z2]"""
    in_x = max(brickA[0], brickB[0]) <= min(brickA[3], brickB[3])
    in_y = max(brickA[1], brickB[1]) <= min(brickA[4], brickB[4])
    return in_x and in_y

def main() -> None:
    print('Day 22')

    bricks = []
    for line in open('data/sand_blocks.txt'):
        bricks.append(list(map(int, line.replace('~', ',').split(','))))
    
    bricks.sort(key=lambda brick: brick[2])
    
    ## Code to simulate the bricks falling - if they overlap then they stack
    ## else they fall to the next layer and stack
    for index, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:index]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z
    bricks.sort(key=lambda brick: brick[2])

    ## Check for bricks supporting each other 
    k_supports_v = {i: set() for i in range(len(bricks))}
    v_supports_k = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)
    ## see which blocks support which
    # print(k_supports_v)
    # print(v_supports_k)
                
    total_1 = total_2 = 0

    for i in range(len(bricks)):
        if all(len(v_supports_k[j]) >= 2 for j in k_supports_v[i]):
            total_1 += 1

        ## Here is part two 
        q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
        falling = set(q)
        falling.add(i)
        while q:
            j = q.popleft()
            for k in k_supports_v[j] - falling: ## set subtraction
                if v_supports_k[k] <= falling: ## <= here is a subset
                    q.append(k)
                    falling.add(k)
        
        total_2 += len(falling) - 1


    print(f'Part 1: {total_1}')
    print(f'Part 2: {total_2}')

    return 


if __name__ == '__main__':
    main()