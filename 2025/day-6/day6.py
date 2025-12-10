import re

with open("list.txt", "r") as file:
    parsed_input = file.readlines()
    parsed_input = [line.rstrip('\n') for line in parsed_input]
    space_indices = [0]
    for i in range(1, len(parsed_input[-1])):
        if parsed_input[-1][i] == '+' or parsed_input[-1][i] == '*':
            space_indices.append(i - 1)
    
    space_indices.append(len(parsed_input[-1]))
    formatted_input = []
    for row in parsed_input:
        arr = []
        start_idx = 0
        end_idx = 1
        while (end_idx < len(space_indices)):
            if (start_idx == 0):
                arr.append(row[space_indices[start_idx]:space_indices[end_idx]])
            else:
                arr.append(row[space_indices[start_idx] + 1:space_indices[end_idx]])
            start_idx += 1
            end_idx += 1
        formatted_input.append(arr)
        

def part_one():
    sum = 0
    for c in range(0, len(formatted_input[0])):
        equation = []
        for r in range(0, len(formatted_input)):
            equation.append(formatted_input[r][c])
        print(equation)
        operation = equation[-1]
        result = int(equation[0])
        for i in range(1, len(equation) - 1):
            if (operation == '*  '):
                result *= int(equation[i])
            elif (operation == '+  '):
                result += int(equation[i])
        sum += result  
    return sum

def part_two():
    sum = 0
    for c in range(0, len(formatted_input[0])):
        equation = []
        for r in range(0, len(formatted_input)):
            equation.append(formatted_input[r][c])
        operation = equation[-1]

        print(equation)
        MAX_DIGITS = len(str(max([int(equation[i]) for i in range(0, len(equation) - 1)])))
        formatted_equation = []
        for col in range(0, MAX_DIGITS):
            num = ""
            for row in range(0, len(equation) - 1):
                num += equation[row][col]
            formatted_equation.append(num)
        
        result = int(formatted_equation[0])
        for i in range(1, len(formatted_equation)):
            if (operation.find('*') != -1):
                result *= int(formatted_equation[i])
            elif (operation.find('+') != -1):
                result += int(formatted_equation[i])
        
        print(result)
        sum += result
    return sum

print(part_two())