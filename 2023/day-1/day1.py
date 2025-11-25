

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
                if (str.rindex(nums[key]) > max_index):
                    max_index = str.rindex(nums[key])
                    return_tuple[1] = key
            except ValueError: 
                print(end='')   
    return_tuple[0] = max_index
    return return_tuple

with open("list.txt", "r") as file:
    for str in file:
        str_tuple_tens = calculate_first_alphanum(str)
        str_tuple_ones = calculate_last_alphanum(str)
        tenths_place_num = 900000
        for c in range(len(str)):        
            char = str[c]
            if (char.isnumeric()):
                tenths_place_num = c
                break
        
        if (tenths_place_num == -1 or str_tuple_tens[0] < c):
            tenths_place = int(str_tuple_tens[1])
        else:
            tenths_place = int(char)

        ones_place_num = -1
        for c in range(len(str)):  
            char = str[len(str) - (c + 1)]
            if (char.isnumeric()):         
                ones_place_num = len(str) - (c + 1)
                break

        if (ones_place_num == -1 or str_tuple_ones[0] > ones_place_num):
            ones_place = int(str_tuple_ones[1])
        else:
            ones_place = int(char)

        print(int(tenths_place * 10 + ones_place))
        print(str)
        sum += int(tenths_place * 10 + ones_place)

print(sum)
