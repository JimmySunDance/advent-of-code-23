# Day nine of the advent of code 2023
# 
# Calculate the next number in a sequence
# Calculate the previous number in a sequence


def next_term(line):
    ends=[]
    iter = line
    while not all(x == 0 for x in iter):
        v = [iter[i+1] - iter[i] for i in range(len(iter) - 1)]
        if sum(v) != 0:
            ends.append(v[-1])
        iter = v
    return line[-1] + sum(ends)


def main() -> None:
    print('Day 9')

    readings = []
    with open('data/instability_sensor.txt') as f:
        for line in f.readlines():
            readings.append(list(map(int,line.strip().split())))
    

    total_1 = 0
    total_2 = 0
    for line in readings:
        total_1 += next_term(line)
        total_2 += next_term(line[::-1])

    print(f'Part 1: {total_1}')
    print(f'Part 2: {total_2}')

    return 

if __name__ == '__main__':
    main()
