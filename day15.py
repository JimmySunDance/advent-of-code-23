# Day fifteen of the advent of code

def hash_it(code):
    start = 0
    for char in code:
        start += ord(char)
        start *= 17
        start %= 256
    return start


def main() -> None:
    print('Day 15!')

    codes = open('data/ascii_codes.txt').read().split(',')

    total = sum([hash_it(c) for c in codes])
    print(f'Part 1: {total}')


    boxes = [[] for _ in range (256)]
    focal_lengths = {}
    for c in codes:
        if '-' in c:
            label = c[:-1]
            index = hash_it(label)
            if label in boxes[index]:
                boxes[index].remove(label)
        else:
            label, length = c.split('=')
            length = int(length)
            
            index = hash_it(label)
            if label not in boxes[index]:
                boxes[index].append(label)
            
            focal_lengths[label] = length
            
    total = 0
    for box_number, box in enumerate(boxes, 1):
        for lens_slot, label in enumerate(box, 1):
            total += box_number * lens_slot * focal_lengths[label]
    print(f'Part 2: {total}')
    
    return

if __name__ == '__main__':
    main()