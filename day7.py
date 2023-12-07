# Day seven of the Advent of Code '23

letters_map_1 = { 'T':'A', 'J':'B', 'Q':'C', 'K':'D', 'A':'E' }
letters_map_2 = { 'T':'A', 'J':'.', 'Q':'C', 'K':'D', 'A':'E' }


def score(hand):
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0

def replacement(hand):
    if hand == '':
        return ['']
    return [
        x + y 
        for x in ('23456789TQKA' if hand[0]=='J' else hand[0]) 
        for y in replacement(hand[1:])
    ]

def classify(hand):
    return max(map(score, replacement(hand)))

def strength(hand):
    return (classify(hand), [letters_map_2.get(char, char) for char in hand])

def s_1(hand):
    return (score(hand), [letters_map_1.get(char, char) for char in hand])

def main() -> None:
    print('Dat 7:')
    
    plays = []
    for line in open('data/poker_hands.txt'):
        hand, bet = line.split()
        plays.append((hand, int(bet)))


    plays.sort(key=lambda play: s_1(play[0]))
    total = 0
    for rank, (hand, bid) in enumerate(plays, 1):
        total += rank * bid
    print(f'Part 1: {total}')


    plays.sort(key = lambda play: strength(play[0]))
    total = 0
    for rank, (hand, bid) in enumerate(plays, 1):
        total += rank * bid
    
    print(f'Part 2: {total}')
    return 


if __name__ == '__main__':
    main()
