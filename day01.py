def read_input_for_testing(filepath: str):
    file = open(filepath, "r")
    return file


def parse_input(data) -> list:
    line_list = [line.strip() for line in data.readlines()]
    return line_list


def get_calories_per_elf_list(calorie_list) -> [int]:
    sum_calorie_list = []
    tmp_calories = 0
    for line in calorie_list:
        if line != '':
            tmp_calories += int(line)
        else:
            sum_calorie_list.append(tmp_calories)
            tmp_calories = 0
    return sum_calorie_list


def part_one(calorie_list) -> int:
    return int(max(get_calories_per_elf_list(calorie_list)))


def part_two(calorie_list) -> int:
    sum_calorie_list = get_calories_per_elf_list(calorie_list)
    sum_calorie_list.sort()
    return int(sum(sum_calorie_list[-3:]))


if __name__ == '__main__':
    print(f"Answer 1 for day 1 is {part_one(parse_input(read_input_for_testing('inputs/input_01.txt')))}")
    print(f"Answer 2 for day 1 is {part_two(parse_input(read_input_for_testing('inputs/input_01.txt')))}")
