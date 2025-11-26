with open("list.txt", 'r') as file:
    game_list = [line.strip() for line in file]

NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14
id_sum = 0

for line in game_list:
    game_id = line.split(':')[0].split(' ')[1]
    rounds = line.split(':')[1].split(';')
    for round in rounds:
        if (round.find("blue") != -1):
            blue_amt = round[round.find(" "):round.find(" blue")]
        