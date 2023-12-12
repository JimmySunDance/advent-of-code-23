# Day twelve of the advent of code 2013
#
# How many different arrangement will fit into the string, given the 
# arrangement of the input values
# .??.??...### - 1, 1, 3
# The above has 4 possibilities.
#
# This is a weird one - not a clue, do not fully understand solution

from functools import cache

@cache
def count(config, nums):
    if config == '':
        return 1 if nums == () else 0 
    
    if nums == ():
        return 0 if '#' in config else 1
    
    result = 0
    if config[0] in '.?':
        result += count(config[1:], nums)

    if config[0] in '#?':
        if nums[0] <= len(config) and (
        '.' not in config[:nums[0]]) and (
        nums[0] == len(config) or config[nums[0]] != '#'):
            result += count(config[nums[0] + 1:], nums[1:])

    return result


## The below function does the same as using the functool cache decorator
##
##
# cache={}
# def count(config, nums):
#     if config == '':
#         return 1 if nums == () else 0 
    
#     if nums == ():
#         return 0 if '#' in config else 1
    
#     key = (config, nums)
#     if key in cache:
#         return cache[key]
#     result = 0
#     if config[0] in '.?':
#         result += count(config[1:], nums)

#     if config[0] in '#?':
#         if nums[0] <= len(config) and (
#         '.' not in config[:nums[0]]) and (
#         nums[0] == len(config) or config[nums[0]] != '#'):
#             result += count(config[nums[0] + 1:], nums[1:])

#     cache[key] = result
#     return result


def main() -> None:
    print('Day 12')
    t_1 = 0
    t_2 = 0
    for line in open('data/damaged_springs.txt'):
        config, pattern = line.split()
        pattern = tuple(map(int, pattern.split(',')))
        
        # Part 1
        t_1 += count(config, pattern)
        # Part 2 is the same problem bu on a much larger data set
        config = '?'.join([config] * 5)
        pattern *= 5
        t_2 += count(config, pattern)
    

    print(f'Part 1: {t_1}')
    print(f'Part 2: {t_2}')
    return 

if __name__ == '__main__':
    main()