# Day eleven of the advent of code 2023

def empties(star_map):
    empty_row = []
    for r, row in enumerate(star_map):
        if all(p =='.' for p in row):
            empty_row.append(r)
    return empty_row

def main() -> None:
    print('Day 11')
    with open('data/galaxy.txt') as f:
        star_map = f.read().splitlines()

    empty_row = empties(star_map)
    empty_col = empties(zip(*star_map))

    galaxies = []
    for i, row in enumerate(star_map):
        for j, col in enumerate(row):
            if col == '#':
                galaxies.append((i, j))
    
    
    dis1, dis2 = 0, 0
    boom_1, boom_2 = 2, 1000000
    for i, (r1, c1) in enumerate(galaxies):
        for (r2, c2) in galaxies[:i]:
            for r in range(min(r1, r2), max(r1, r2)):
                dis1 += boom_1 if r in empty_row else 1
                dis2 += boom_2 if r in empty_row else 1
            for c in range(min(c1, c2), max(c1, c2)):
                dis1 += boom_1 if c in empty_col else 1
                dis2 += boom_2 if c in empty_col else 1
            
    print(f'Part 1: {dis1}')
    print(f'Part 2: {dis2}')

    return 

if __name__ == '__main__':
    main()