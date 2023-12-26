# # Day twenty four of the advent of code 2023
# #
# #
import sympy

class Hailstone:
    def __init__(self, sx, sy, sz, vx, vy, vz) -> None:
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.vx = vx
        self.vy = vy
        self.vz = vz

        self.a = vy
        self.b = -vx
        self.c = vy * sx - vx * sy
    
    def __repr__(self) -> str:
        return "Hailstones{" + f"a={self.a}, b={self.b}, c={self.c}" + "}"


def main() -> None:
    print('Day 24')

    stones = [Hailstone(*map(int, l.replace('@', ',').split(','))) for l in open('data/hail_smash.txt')]

    total = 0
    for i, hs1 in enumerate(stones):
        for hs2 in stones[:i]:
            a1, b1, c1 = hs1.a, hs1.b, hs1.c
            a2, b2, c2 = hs2.a, hs2.b, hs2.c
            if a1 * b2 == b1 * a2: ## Case where lines are parallel
                continue
            x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
            y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
            if 2e14 <= x <= 4e14 and 2e14 <= y <= 4e14:
                if all((x - hs.sx) * hs.vx >= 0 and (y - hs.sy) * hs.vy >= 0 for hs in (hs1, hs2)):
                    total += 1
    print(f'Part 1: {total}')
    return 


def sym_main() -> None:
    stones = [tuple(map(int, l.replace('@', ',').split(','))) for l in open('data/hail_smash.txt')]

    xr, yr, zr, vxr, vyr, vzr = sympy.symbols('xr, yr, zr, vxr, vyr, vzr')

    equations = []

    for i, (sx, sy, sz, vx, vy, vz) in enumerate(stones):
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        if i < 2:
            continue
        
        answers = [soln for soln in sympy.solve(equations)]
        if len(answers) == 1:
            break
    
    answers = answers[0]

    print(f'Part 2: {answers[xr] + answers[yr] + answers[zr]}')


if __name__ == '__main__':
    main()
    sym_main()