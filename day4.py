# Day four of the Advent of Code '23
#
# figure out which of the numbers you have appear in the list of winning 
# numbers. The first match makes the card worth one point and each match 
# after the first doubles the point value of that card.

def total_points(lines: list[str]) -> int:
    score = 0

    for line in lines:
        card, draw = line.split(':')[1].split('|')
        card = set([eval(i) for i in card.split()])
        draw = set([eval(i) for i in draw.split()])

        c_score = 0
        inter = card.intersection(draw)
        if inter:
            c_score = 1
            if len(inter) > 1:
                c_score = pow(2, len(inter)-1)
        score += c_score

    return score

def total_cards(lines: list[str]) -> int:
    
    copies = [1 for line in lines]
    for i, card in enumerate(lines):
        winning = list(map(int, card.split(":")[1].split("|")[0].strip().split()))
        numbers = list(map(int, card.split("|")[1].strip().split()))

        matches = sum(1 for x in numbers if x in winning)
        for j in range(i + 1, i + matches + 1):
            copies[j] += 1 * copies[i]

    return sum(copies)

def main() -> None:
    with open("data/score_cards.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print(total_points(lines))
        print(total_cards(lines))

if __name__ == '__main__':
    main()
