with open("list.txt", 'r') as file:
    game_list = [line.strip() for line in file]

NUM_RED = 12
NUM_GREEN = 13
NUM_BLUE = 14
id_sum = 0

for line in game_list:
    valid = True
    game_id = line.split(':')[0].split(' ')[1]
    rounds = line.split(':')[1].split(';')
    for round in rounds:
        green_amt = 0
        blue_amt = 0
        red_amt = 0
        colors = round.split(",")
        for color in colors:
            if color.find("blue") != -1:
                blue_amt = int(color[0:color.rindex(" ")])
            elif color.find("red") != -1:
                red_amt = int(color[0:color.rindex(" ")])
            elif color.find("green") != -1:
                green_amt = int(color[0:color.rindex(" ")])
        if (blue_amt <= NUM_BLUE and green_amt <= NUM_GREEN and red_amt <= NUM_RED):
            valid = False

print(id_sum)
        