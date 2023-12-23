# Day 23 of the advent of code 2023
#
# Using Edge contraction
# https://en.wikipedia.org/wiki/Edge_contraction
# We remove nodes with edge = 2



def main() -> None:
    print('Day 23')

    forest = open('data/forest_map.txt').read().splitlines()

    start = (0, forest[0].index('.'))
    end = (len(forest) - 1, forest[-1].index('.'))

    # starting node and ending node
    points = [start, end]

    for r, row in enumerate(forest):
        for c, ch in enumerate(row):
            if ch == '#':
                continue
            neighbour = 0
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < len(forest) and 0 <= nc < len(forest[0]) and forest[nr][nc] != "#":
                    neighbour += 1
                if neighbour >= 3:
                    points.append((r, c)) # add nodes to list

    graph = {pt: {} for pt in points}
    dirs = {
        '^':[(-1, 0)], 'v':[(1, 0)], '<':[(0, -1)], '>':[(0, 1)],
        '.':[(-1, 0), (1, 0), (0, -1), (0, 1)]
    }

    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()

            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in dirs[forest[r][c]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(forest) and 0 <= nc < len(forest[0]) and forest[nr][nc] != "#" and (nr, nc) not in seen:
                    stack.append((n+1, nr, nc))
                    seen.add((nr, nc))

    seen = set()
    def dfs(pt):
        if pt == end:
            return 0
        
        m = -float('inf')
       
        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[pt][nx])
        seen.remove(pt)
        
        return m

    print(f'Part 1: {dfs(start)}')


    graph = {pt: {} for pt in points}
    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()

            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(forest) and 0 <= nc < len(forest[0]) and forest[nr][nc] != "#" and (nr, nc) not in seen:
                    stack.append((n+1, nr, nc))
                    seen.add((nr, nc))

    seen = set()
    print(f'Part 2: {dfs(start)}')



    return 

if __name__ == '__main__':
    main()