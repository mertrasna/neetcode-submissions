from typing import List

def read_integers() -> List[int]:
    user_input = input()
    parsed_list = user_input.split(",")
    for i in range(len(parsed_list)):
        parsed_list[i] = int(parsed_list[i])
    return parsed_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
