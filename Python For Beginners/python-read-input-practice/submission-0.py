def add_two_numbers() -> int:
    user_input = input()
    parsed_list = user_input.split(",")
    sum = 0
    for e in parsed_list:
        sum += int(e)
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
