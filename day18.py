# Day eighteen of the advent of code 2023
#
# Shoelace formula
# abs(Sum(x(y_i+1 - y_i-1))) / 2
#
# Also use Pick's theorem
# Area = interior + (boundary/2) + 1
#

def main() -> None:
    print('Day 18')

    points, points_2 = [(0, 0)], [(0, 0)]
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    B, B_2 = 0, 0 # boundary_points
    for line in open('data/dig_plan.txt'):
        d, n, x = line.split()
        x = x[2:-1]
        dr, dc = dirs[d]
        dr_2, dc_2 = dirs["RDLU"[int(x[-1])]]
        n, n_2 = int(n), int(x[:-1], 16)
        B += n
        B_2 += n_2
        r, c = points[-1]
        r_2, c_2 = points_2[-1]
        points.append((r + dr * n, c + dc * n))
        points_2.append((r_2 + dr_2 * n_2, c_2 + dc_2 * n_2))

    # shoelace formula 
    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points))))/2
    A_2 = abs(sum(points_2[i][0] * (points_2[i - 1][1] - points_2[(i + 1) % len(points_2)][1]) for i in range(len(points_2))))/2

    # Pick's theorem
    i = A - (B//2) + 1
    i_2 = A_2 - (B_2//2) + 1
    print(f'Part 1: {int(i + B)}')
    print(f'Part 2: {int(i_2 + B_2)}')

    return 

if __name__ == "__main__":
    main()