

sum = 0
ones_place = 0
tenths_place = 0
nums = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

def calculate_first_alphanum(str):
    min_index = 999
    return_tuple = [0, ""]
    for key in nums:
        try:
            if (str.index(nums[key]) < min_index):
                min_index = str.index(nums[key])
                return_tuple[1] = key
        except ValueError:
            print(end='')  
    return_tuple[0] = min_index
    return return_tuple

def calculate_last_alphanum(str):
    return_tuple = [0, ""]
    max_index = -1
    for key in nums:
            try:
                if (str.index(nums[key]) > max_index):
                    max_index = str.index(nums[key])
                    return_tuple[1] = key
            except ValueError: 
                print(end='')   
    return_tuple[0] = max_index
    return return_tuple

with open("list.txt", "r") as file:
    for str in file:
        for c in range(len(str)):
            char = str[c]
            if (char.isnumeric()):
                str_tuple = calculate_first_alphanum(str)
                if (str_tuple[0] < c):
                    tenths_place = int(str_tuple[1])
                else:
                    tenths_place = int(char)
                break
        for c in range(len(str)):
            char = str[len(str) - (c + 1)]
            if (char.isnumeric()):
                str_tuple = calculate_last_alphanum(str)
                if (str_tuple[0] > 0):
                    ones_place = int(str_tuple[1])
                else:
                    ones_place = int(char)
                break
        print(int(tenths_place * 10 + ones_place))
        sum += int(tenths_place * 10 + ones_place)

print(sum)
