

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
    min_index = len(str) - 1
    for key in nums:
        try:
            if (str.index(key) < min_index):
                min_index = str.index(key)
        except ValueError:
            print(f"{key} is not present in {str}")
    return min_index

def calculate_last_alphanum(str):
    max_index = 0
    try:
        for key in nums:
            if (str.index(key) > max_index):
                max_index = str.index(key)
    except ValueError:
         print(f"{key} is not present in {str}")
    return max_index

with open("list.txt", "r") as file:
    for str in file:
        ones_place_stridx = calculate_last_alphanum(str)
        tenths_place_stridx = calculate_first_alphanum(str)
        for c in range(len(str)):
            if (c.isnumeric()):
                tenths_place = int(c)
                break
        for c in range(str.__len__()):
            char = str[str.__len__() - (c + 1)]
            if (char.isnumeric()):
                ones_place = int(char)
                break
        
        
        sum += int(tenths_place * 10 + ones_place)

print(sum)
