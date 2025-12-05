with open("list.txt", "r") as file:
    ranges = []
    ids = []
    for line in file:
        if (line.find("-") != -1):
            ranges.append(line.strip())
        else:
            ids.append(line.strip())
    if (len(ids) > 0):
        ids.pop(0)

def in_range(num_range, num):
    upper_bound = int(num_range.split('-')[1])
    lower_bound = int(num_range.split('-')[0])
    return int(num) in range(lower_bound, upper_bound + 1)


def part_one():
    sum = 0
    for id in ids:
        within_range = False
        for range in ranges:
            if (in_range(range, id)):
                within_range = True
                break
        
        if within_range:
            sum += 1
    return sum

def part_two():
    ids = []
    for range in ranges:
        upper_bound = int(range.split('-')[1])
        lower_bound = int(range.split('-')[0]) 
        while lower_bound <= upper_bound:
            if not lower_bound in ids:
                ids.append(lower_bound)
            lower_bound += 1
        print(f"done with line {ranges.index(range)}")
    return len(ids)

print(part_two())
