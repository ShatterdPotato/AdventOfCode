with open("list.txt", 'r') as file:
    banks = [line.strip() for line in file]

sum = 0
for bank in banks:
    char_list = list(bank)
    temp_list = list(bank)
    digit_list = []
    print(f"initial char list")
    while len(digit_list) < 12:     
        big_idx = temp_list.index(max(temp_list))
        print(f"BIG IS {temp_list[big_idx]}, idx {big_idx}")
        if len(char_list[char_list.index(temp_list[big_idx]):]) >= 12 - len(digit_list): 
            digit_list.append(char_list[big_idx])
            char_list = char_list[big_idx + 1:]
            temp_list = []
            for char in char_list:
                temp_list.append(char)
            print(f"new char list: {char_list}")
        else:
            print(f"popping {temp_list[big_idx]} because {len(char_list[big_idx:])} is less than {12 - len(digit_list)}  ({char_list[big_idx:]})")
            temp_list.pop(big_idx)
    num = "" 
    for digit in digit_list:
        num += digit
    sum += int(num)
    print(num)

print(sum)  




