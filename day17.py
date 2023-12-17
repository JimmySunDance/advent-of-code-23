# Day seventeen of the advent of code 2023
#
# Dijkstra's algorithm

from heapq import heappush, heappop

def main() -> None:
    print('Day 17')

    city = [list(map(int, l.strip())) for l in open('data/crucible_path.txt')]

    seen = set()
    # heat value 0 - start (0, 0) - moving (0, 0) - steps taken 0
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)

        # remove last check for part 1
        if r == len(city) - 1 and c == len(city[0]) - 1 and n >= 4:
            print(hl)
            break

        if r < 0 or r >= len(city) or c < 0 or c >= len(city[0]):
            continue
        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        # change 10 to 3 for part 1
        if n < 10 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(city) and 0 <= nc < len(city[0]):
                heappush(pq, (hl + city[nr][nc], nr, nc, dr, dc, n+1))

        # Comment out for part 1
        if n >= 4 or (dr, dc) == (0, 0):
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(city) and 0 <= nc < len(city[0]):
                        heappush(pq, (hl + city[nr][nc], nr, nc, ndr, ndc, 1))


    return 

if __name__ == '__main__':
    main()