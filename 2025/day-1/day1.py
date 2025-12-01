with open("list.txt", 'r') as file:
    rotation_list = [line.strip() for line in file]

location = 50
password = 0
for line in rotation_list:
    direction = 0
    if line[0] == "R":
        direction = 1
    elif line[0] == "L":
        direction = -1
    
    amt = int(line[1:])
    for i in range(amt):
        location += direction
        if location == 100:
            location = 0
        elif location == -1:
            location = 99
        
        if (location == 0):
            password += 1

    print(location)


print(password)
    