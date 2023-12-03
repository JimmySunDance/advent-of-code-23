# Day two of the Advent of Code '23
#
# The Elf would first like to know which games would have been possible if the 
# bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
#
# Determine which games would have been possible if the bag had been loaded 
# with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of
# the IDs of those games?

def play_the_game(lines:list[str]) -> tuple:
    red_max, green_max, blue_max = 12, 13, 14
    game1_ans, game2_ans = 0, 0

    for i, line in enumerate(lines):
        line = line.split(':')[1]
        draws = line.split(';')

        dd = {'red':0, 'green':0, 'blue':0}
        for draw in draws:
            for bloc in draw.split(','):
                num, col = int(bloc.split()[0]), bloc.split()[1]
                if num > dd[col]:
                    dd[col] = num
            
        if dd['red']<=red_max and dd['blue']<=blue_max and dd['green']<=green_max:
            game1_ans += i+1
        
        r = dd['red'] if dd['red'] > 0 else 1
        g = dd['green'] if dd['green'] > 0 else 1
        b = dd['blue'] if dd['blue'] > 0 else 1
        
        game2_ans += r*g*b

    return game1_ans, game2_ans

def main() -> None:
    with open('data/game_runs.txt', 'r', encoding='utf-8') as f:
        text = f.readlines()
    print(play_the_game(text))


if __name__ == '__main__':
    main()