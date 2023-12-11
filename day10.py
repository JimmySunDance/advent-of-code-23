# Day ten of the advent of code 2023
#
# Find your way around the loop.

def move(pipes, position, prev_position):
    piece = pipes[position[1]][position[0]]
    add_x, add_y = 0, 0

    if piece == '|':
        if prev_position[1] < position[1]: # from above
            add_y = 1 # move down
        else:
            add_y = -1 # move up

    elif piece == '-':
        if prev_position[0] < position[0]: # from left
            add_x = 1 # move right
        else:
            add_x = -1 # move left

    elif piece == 'L':
        if prev_position[1] < position[1]: # from above
            add_x = 1 # move right
        else:
            add_y = -1 # move up

    elif piece == 'J':
        if prev_position[1] < position[1]: # from above
            add_x = -1 # move left
        else:
            add_y = -1 # move up

    elif piece == '7':
        if prev_position[1] > position[1]: # from below
            add_x = -1 # move left
        else:
            add_y = 1 # move down

    elif piece == 'F':
        if prev_position[1] > position[1]:
            add_x = 1 # move right
        else:
            add_y = 1 # move down
    else:
        raise Exception(f'Run aground at ({position[0]}, {position[1]})!')

    prev_position[0] = position[0]
    prev_position[1] = position[1]
    position[0] += add_x
    position[1] += add_y


def part_1(pipes, connections, start_x, start_y):
    # get first and second connections and save previous positions
    counter = 1
    first, second = connections[0], connections[1]
    prev_first, prev_second = [start_x, start_y], [start_x, start_y]
    
    # while the first and second connections are not the same
    while first[0] != second[0] or first[1] != second[1]:
        # get next location
        move(pipes, first, prev_first)
        move(pipes, second, prev_second)
        # increment counter
        counter += 1
    print(f'Part 1: {counter}')
    return 
    

def part_2(pipes, connections, start_x, start_y):
    # if first connection is above start
    if connections[0][0] == start_x and connections[0][1] == start_y-1:
        if connections[1][0] == start_x-1: # left of start
            start_pipe = "J"
        elif connections[1][0] == start_x+1: # right of start
            start_pipe = "L"
        else:
            start_pipe = "|" # below start

    # if first connection is below start
    if connections[0][0] == start_x and connections[0][1] == start_y+1:
        if connections[1][0] == start_x-1: # left of start
            start_pipe = "7"
        elif connections[1][0] == start_x+1: # right of start
            start_pipe = "F"
        else:
            start_pipe = "|" # above start

    # if first connection is left of start
    if connections[0][1] == start_y and connections[0][0] == start_x-1:
        if connections[1][1] == start_y-1: # above start
            start_pipe = "J"
        elif connections[1][1] == start_y+1: # below start
            start_pipe = "7"
        else:
            start_pipe = "-" # right of start

    # if first connection is right of start
    if connections[0][1] == start_y and connections[0][0] == start_x+1:
        if connections[1][1] == start_y-1: # above start
            start_pipe = "L"
        elif connections[1][1] == start_y+1: # below start
            start_pipe = "F"
        else:
            start_pipe = "-" # left of start
    
    else:
        raise Exception('No start_pipe')
    
    # set start pipe character
    py = pipes[start_y][:start_x] + start_pipe + pipes[start_y][start_x+1:]
    pipes[start_y] = py
    
    # get first and second connections and save previous positions
    first = connections[0]
    prev_first = [start_x, start_y]
    second = connections[1]
    prev_second = [start_x, start_y]
    
    # set of positions of all pipes that are in the loop
    # starting with the start pipe and the two connections
    pipe_rout = set([(start_x, start_y),(first[0],first[1]),(second[0],second[1])])
    # while the first and second connections are not the same

    while first[0] != second[0] or first[1] != second[1]:
        # get next locations
        move(list(pipes), first, prev_first)
        move(list(pipes), second, prev_second)
        # add them to the set of pipes
        pipe_rout.add((first[0], first[1]))
        pipe_rout.add((second[0], second[1]))
    
    # switch weather we are in a region or not
    is_region = False
    # count the number of cells in a region
    region_counter = 0
    # keep track of the previous edge if it was an edge pipe (L, F)
    previous_edge = None
    # for every cell in the grid
    for y, line in enumerate(pipes):
        for x, c in enumerate(line):
            # if the cell is not a pipe of the loop and we are in a region
            if (x,y) not in pipe_rout and is_region:
                region_counter += 1
            # if the cell is a pipe of the loop
            elif (x,y) in pipe_rout:
                # a pipe down always switches the region
                if c == "|":
                    is_region = not is_region
                # a pipe right doesn't affect the region
                elif c == "-":
                    continue
                # a pipe edge pointing to the right
                # will begin a series of 0..n "-" pipes ending with either J or 7
                # we count each L----J or F----7 as non existent
                # and each L----7 or F----J as existent region boundary
                if c in "LF":
                    previous_edge = c
                # a pipe edge pointing to the left
                elif c == "J":
                    # if previous edge wasn't pointing up
                    if previous_edge == "F":
                        # switch region
                        is_region = not is_region
                    previous_edge = None
                # a pipe edge pointing to the right
                elif c == "7":
                    # if previous edge wasn't pointing down
                    if previous_edge == "L":
                        # switch region
                        is_region = not is_region
                    previous_edge = None

    print(f'Part 2: {region_counter}')
    return 


def main() -> None:
    print('Day 10!')
    with open('data/pipe_works.txt') as f:
        pipes = f.readlines()


    for i, y in enumerate(pipes):
        for j, x in enumerate(y):
            if x == 'S':
                start_x, start_y = j, i
    
    connections = []
    if pipes[start_y][start_x - 1] in '-FL':
        connections.append([start_x - 1, start_y])
    if pipes[start_y][start_x + 1] in '-J7':
        connections.append([start_x + 1, start_y])
    if pipes[start_y - 1][start_x] in '|F7':
        connections.append([start_x, start_y - 1])
    if pipes[start_y][start_x + 1] in '|JL':
        connections.append([start_x, start_y + 1])
    if len(connections) != 2:
        raise Exception(f"Start has {len(connections)} connections")
    part_1(pipes, connections, start_x, start_y)

    # I cannot work out why/how this values is being changed in part 1
    connections = []
    if pipes[start_y][start_x - 1] in '-FL':
        connections.append([start_x - 1, start_y])
    if pipes[start_y][start_x + 1] in '-J7':
        connections.append([start_x + 1, start_y])
    if pipes[start_y - 1][start_x] in '|F7':
        connections.append([start_x, start_y - 1])
    if pipes[start_y][start_x + 1] in '|JL':
        connections.append([start_x, start_y + 1])
    if len(connections) != 2:
        raise Exception(f"Start has {len(connections)} connections")
    part_2(pipes, connections, start_x, start_y)
    return 


if __name__ == '__main__':
    main()