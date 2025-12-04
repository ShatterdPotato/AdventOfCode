with open("list.txt", "r") as file:
    paper_roll = [line.strip() for line in file]
    for i in range(len(paper_roll)):
        paper_roll[i] = list(paper_roll[i])
PAPER_ROLL = '@'
def num_rolls_adjacent(row, col):
    top = row - 1 < 0
    bottom = row + 1 >= len(paper_roll)
    left = col - 1 < 0
    right = col + 1 >= len(paper_roll[row])
    num_rolls = 0
    if not right and paper_roll[row][col + 1] == PAPER_ROLL: #right
        num_rolls += 1
    if not left and paper_roll[row][col - 1] == PAPER_ROLL: #left
        num_rolls += 1
    if not bottom and paper_roll[row + 1][col] == PAPER_ROLL: #down
        num_rolls += 1
    if not top and paper_roll[row - 1][col] == PAPER_ROLL: #up
        num_rolls += 1
    if not bottom and not right and paper_roll[row + 1][col + 1] == PAPER_ROLL: #bottom-right
        num_rolls += 1
    if not bottom and not left and paper_roll[row + 1][col - 1] == PAPER_ROLL: #bottom-left
        num_rolls += 1
    if not top and not right and paper_roll[row - 1][col + 1] == PAPER_ROLL: #top-right
        num_rolls += 1
    if not top and not left and paper_roll[row - 1][col - 1] == PAPER_ROLL: #top-left
        num_rolls += 1
    return num_rolls

def part_one():
    sum = 0
    for r in range(len(paper_roll)):
        for c in range(len(paper_roll[r])):
            if (paper_roll[r][c] == PAPER_ROLL and num_rolls_adjacent(r, c) < 4):
                sum += 1
    return sum

def part_two():
    sum = 0
    list_of_shame = [("filler", "lol")]
    while len(list_of_shame) != 0:
        list_of_shame = []
        for r in range(len(paper_roll)):
            for c in range(len(paper_roll[r])):
                if (paper_roll[r][c] == PAPER_ROLL and num_rolls_adjacent(r, c) < 4):
                    sum += 1
                    list_of_shame.append((r,c))
        
        for coordinate in list_of_shame:
            r = coordinate[0]
            c = coordinate[1]
            paper_roll[r][c] =  '.'
    return sum

print(part_two())
