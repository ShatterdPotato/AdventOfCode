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
    sum = 0
    sorted_ranges = []
    for r in ranges:
        upper_bound = int(r.split('-')[1])
        lower_bound = int(r.split('-')[0]) 
        sorted_ranges.append([lower_bound, upper_bound])
    

    sorted_ranges = sorted(sorted_ranges)
    i = 1
    while i < len(sorted_ranges):
        if sorted_ranges[i][0] >= sorted_ranges[i - 1][0] and sorted_ranges[i][0] <= sorted_ranges[i - 1][1]:
            if sorted_ranges[i][1] > sorted_ranges[i - 1][1]:
                sorted_ranges[i - 1][1] = sorted_ranges[i][1]
            sorted_ranges.pop(i)
            i -= 1
        i += 1
    for merged_range in sorted_ranges:
        upper_bound = merged_range[1]
        lower_bound = merged_range[0]
        sum += (upper_bound - lower_bound) + 1
    
    return sum

            


print(part_two())
