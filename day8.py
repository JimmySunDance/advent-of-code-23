# Day 8 of the advent of code 2023

import math as m

def main() -> None:
    print('Day 8')
    with open('data/rl_map.txt') as f:
        dir, _, *rest = f.read().splitlines()

    rout_map = {}
    for line in rest:
        pos, targets = line.split(' = ')
        rout_map[pos] = targets[1:-1].split (", ")

    directions = [0 if d =='L' else 1 for d in list(dir)]

    # ----- Part 1 -----
    steps, d = 0, 0
    position = 'AAA'
    while position != 'ZZZ':
        if d >= len(directions):
            d=0
        position = rout_map[position][directions[d]]
        d +=1
        steps += 1

    # ----- Part 2 -----
    g_position = [ k for k in rout_map if k.endswith('A') ]
    cycles=[]
    
    for current in g_position:
        cycle=[]

        current_steps = dir
        step_count = 0
        first_z = None

        while True:
            while step_count == 0 or not current.endswith("Z"):
                step_count += 1
                current = rout_map[current][0 if current_steps[0] == "L" else 1]
                current_steps = current_steps[1:] + current_steps[0]
            
            cycle.append(step_count)

            if first_z is None:
                first_z = current
                step_count = 0
            elif current == first_z:
                break

        cycles.append(cycle)

    nums = [cycle[0] for cycle in cycles]
    lcm = nums.pop()
    for num in nums:
        lcm = lcm * num // m.gcd(lcm, num)

    print(f'Part 1: {steps}')
    print(f'Part 2: {lcm}')
    return 

if __name__ == "__main__":
    main()