real = 'data/seed_almanac.txt'
test = 'data/seed_test.txt'


def main() -> None:
    print("Day 05:")
    with open(real) as f:
        inputs, *blocks = f.read().split('\n\n')
    inputs = list(map(int, inputs.split(':')[1].split()))
    
    seeds = []
    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i +1]))

    for block in blocks:
        # Part 1
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))    
        
        new_1 = []
        for x in inputs:
            for a, b, c in ranges:
                if x in range(b, b+c):
                    new_1.append(x - b + a)
                    break
            else:
                new_1.append(x)
        
        inputs = new_1

        # Part 2
        new =[]
        while len(seeds) > 0:
            start, end = seeds.pop()
            for a, b, c in ranges:
                olap_s = max(start, b)
                olap_e = min(end, b+c)
                if olap_s < olap_e:
                    new.append((olap_s - b + a, olap_e - b + a))
                    if olap_s > start:
                        seeds.append((start, olap_s))
                    if end > olap_e:
                        seeds.append((olap_e, end))
                    break
            else:
                new.append((start, end))
        seeds = new

    print(f'Part 1: {min(new_1)}')
    print(f'Part 2: {min(seeds)[0]}')

if __name__ == "__main__":
    main()