# Day nineteen of the advent of code 2023
#
# using eval() can leave you open to malicious inputs. 
# so we define < and >
# a < b
# => a.__lt__(b)
# => type(a).__lt__(a, b)
# => int.__lt__(a, b)

def accept_item(item:dict, workflows:dict, ops:dict, name:str = 'in') -> bool:
    if name == 'R':
        return False
    if name == 'A':
        return True
    
    rules, fallback = workflows[name]
    for key, cmp, n, target in rules:
        # if eval(f'{item[key]} {cmp} {n}'):
        if ops[cmp](item[key], n):
            return accept_item(item, workflows, ops, name=target)
    return accept_item(item, workflows, ops, name=fallback)


def range_count(ranges, workflows:dict, name:str = 'in'):
    if name == 'R':
        return 0
    if name == 'A':
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflows[name]
    total = 0
    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == '<':
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += range_count(copy, workflows, name=target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += range_count(ranges, workflows, name=fallback)    
    return total

def main() -> None:

    flow, parts = open('data/part_sorting.txt').read().split('\n\n')

    ops={'>':int.__gt__, '<':int.__lt__}
    workflows = {}
    for line in flow.splitlines():
        name, rules = line[:-1].split('{')
        rules = rules.split(',')
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(':')
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    total = 0
    for part in parts.splitlines():
        item = {}
        for seg in part[1:-1].split(','):
            ch, n = seg.split('=')
            item[ch] = int(n)
        
        if accept_item(item, workflows, ops):
            total += sum(item.values())

    print(f'Part 1: {total}')


    print(range_count({key: (1, 4000) for key in 'xmas'}, workflows))

    return 

if __name__ == '__main__':
    main()