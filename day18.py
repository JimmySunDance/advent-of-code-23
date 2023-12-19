# Day 18 of the advent of code 2023
#
# Shoelace formula
# abs(Sum(x(y_i+1 - y_i-1))) / 2
#
# Also use Pick's theorem
# Area = interior + (boundary/2) + 1
#

def main() -> None:
    print('Day 18')

    # --- Part 1 ---
    points = [(0, 0)]
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    B = 0 # boundary_points
    for line in open('data/dig_plan.txt'):
       d, n, _ = line.split()
       dr, dc = dirs[d]
       n = int(n)
       B += n
       r, c = points[-1]
       points.append((r + dr * n, c + dc * n))

    # shoelace formula 
    A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points))))/2

    # Pick's theorem
    i = A - (B//2) + 1
    print(f'Part 1: {i + B}')

    # --- Part 2 ---
    points_2 = [(0, 0)]
    B_2 = 0 # boundary_points
    for line in open('data/dig_plan.txt'):
       _, _, x = line.split()
       x = x[2:-1]
       dr, dc = dirs["RDLU"[int(x[-1])]]
       n = int(x[:-1], 16)
       B_2 += n
       r, c = points_2[-1]
       points_2.append((r + dr * n, c + dc * n))

    # shoelace formula 
    A = abs(sum(points_2[i][0] * (points_2[i - 1][1] - points_2[(i + 1) % len(points_2)][1]) for i in range(len(points_2))))/2

    # Pick's theorem
    i_2 = A - (B_2//2) + 1
    print(f'Part 2: {int(i_2 + B_2)}')

    return 

if __name__ == "__main__":
    main()