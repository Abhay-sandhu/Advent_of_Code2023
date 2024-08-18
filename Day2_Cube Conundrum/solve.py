
max_red = 12
max_green = 13
max_blue = 14


#parse input games
with open('Day2_Cube Conundrum\\input.txt', 'r') as file:
    
    content = file.readlines()
    games = [] # list of game tuples (game id, [ball_group_dicts{color:count}])
    
    for line in content:
        semicolon = line.index(':')
        ball_sets = []
        unparsed_ballsets = line[semicolon+1:].split(';')

        for ballset in unparsed_ballsets:
            
            ballset = ballset.strip()
            ballset_list = ballset.split(', ')
            
            ball_group_dict = {}
            
            for balls in ballset_list:
                number, color = balls.split(' ')
                ball_group_dict[color] =  int(number)
            ball_sets.append(ball_group_dict)
        games.append((line[:semicolon], ball_sets))

# part 1
# validate possible games
possible_games = []
for game in games:
    possible_games.append(game[0])
    for ball_dict in game[1]:
        if ball_dict.get('red', 0) > 12 or ball_dict.get('green', 0) > 13 or ball_dict.get('blue', 0) > 14:
                if game[0] in possible_games: possible_games.remove(game[0]) # remove impossible
                continue
possible_game_ids = [int(game.split(' ')[1]) for game in possible_games]
print(sum(possible_game_ids))


# part 2
powerofgame = []
for game in games:
    max_red = 0
    max_blue = 0
    max_green = 0
    for set in game[1]:
        if set.get('red', 0) > max_red:
            max_red = set['red']
        if set.get('blue', 0) > max_blue:
            max_blue = set['blue']
        if set.get('green', 0) > max_green:
            max_green = set['green']
    power = max_red * max_green * max_blue
    powerofgame.append(power)
print(sum(powerofgame))